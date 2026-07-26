#!/usr/bin/env python3
"""Use Agnes AI to turn Bilibili SRT files into classified Obsidian notes."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "B站-收藏夹字幕"
TARGET = Path("/Users/sam/02-Obsidian/自媒体/01-输入/B站-整理素材")
AGNES_MD = Path("/Users/sam/lark/account/servers/RackNerd/new-api/providers/agnes/agnes.md")
LABELS = {"A": "A-学工具练手感", "B": "B-学产品备面试", "C": "C-学认知看趋势"}


def parse_srt(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if not line.strip() or line.strip().isdigit() or "-->" in line:
            continue
        line = re.sub(r"<[^>]+>", "", line).strip()
        if line and (not lines or (line != lines[-1] and line not in lines[-1] and lines[-1] not in line)):
            lines.append(line)
    return " ".join(lines)


def safe_filename(value: str) -> str:
    value = re.sub(r"[\\/:*?\"<>|\n\r]+", " ", value).strip()
    return value[:120].rstrip(" .") or "未命名"


def classify_title(title: str) -> str:
    """Deterministic fallback: operational A, product B, everything else C."""
    if re.search(r"产品经理|需求|竞品|PRD|UX|用户体验|面试|原型", title, re.I):
        return "B"
    if re.search(r"教程|实战|安装|部署|代码|编程|开发|Skill|Agent|Claude|Codex|Python|HTML|CSS|JS|React|Vue|剪辑|PPT|Word|Obsidian|飞书|Figma|Axure|自动化|建站|浏览器", title, re.I):
        return "A"
    return "C"


def load_agnes() -> tuple[str, str, str]:
    text = AGNES_MD.read_text(encoding="utf-8")
    key = re.search(r"API Key\s*\|\s*`?([^|`\s]+)", text)
    endpoint = re.search(r"上游端点\s*\|\s*`([^`]+)", text)
    model = re.search(r"`(agnes-[^`]+)`", text)
    if not (key and endpoint and model):
        raise RuntimeError(f"无法从 {AGNES_MD} 读取 Agnes 配置")
    return key.group(1), endpoint.group(1), model.group(1)


def ask_agnes(title: str, transcript: str, key: str, endpoint: str, model: str) -> dict:
    prompt = f"""你是 Obsidian 外部参考资料整理员。依据标题和字幕，严格只返回 JSON：
{{\"category\":\"A|B|C\",\"source_type\":\"tutorial|product|theory|trend|career|business|opinion\",\"summary\":\"一句话摘要\",\"tags\":[\"最多5个中文或英文标签\"],\"key_points\":[\"3-8条要点\"],\"possible_use\":\"它可能补充哪类项目/方法表达；不确定就写待确认\"}}
规则：A=工具与具体实操；B=产品、需求、UX、原型、面试；C=原理、趋势、行业、商业、职业经验和观点。必须选一个主分类。
重要：这是他人的视频收藏，不是用户亲自完成的项目。不得写成用户的经历、成果或能力证据；只描述视频讲了什么及可能的参考价值。
标题：{title}\n字幕：{transcript[:16000]}"""
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.1, "max_tokens": 1800}).encode()
    req = Request(endpoint, data=body, headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urlopen(req, timeout=45) as response:
        data = json.loads(response.read().decode())
    content = data["choices"][0]["message"]["content"]
    content = re.sub(r"^```json\s*|\s*```$", "", content.strip())
    result = json.loads(content)
    if result.get("category") not in LABELS:
        raise ValueError("Agnes 返回了无效 category")
    return result


def make_note(source: Path, result: dict, transcript: str) -> str:
    title = source.name.rsplit(" [BV", 1)[0]
    category = result["category"]
    tags = ", ".join(json.dumps(str(x), ensure_ascii=False) for x in result.get("tags", [])[:5])
    points = "\n".join(f"- {x}" for x in result.get("key_points", []))
    return f"---\ncategory: {category}\nsource_type: {result.get('source_type', 'opinion')}\nownership: external\nknowledge_role: reference\nmainline_candidate: pending\nsource_file: {source.name}\nstatus: reference\n---\n\n# {title}\n\n> 摘要：{result.get('summary', '')}\n\n> ⚠️ 外部参考：这是收藏的视频内容，不代表本人经历、成果或能力证据。\n\n## 关键要点\n{points}\n\n## 可能的参考价值\n{result.get('possible_use', '待确认：需要结合自己的项目判断是否能进入主线。')}\n\n## 原始字幕\n\n{transcript}\n\n## 标签\n[{tags}]\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--retries", type=int, default=2)
    args = parser.parse_args()
    files = sorted(SOURCE.glob("*.srt"))[: args.limit or None]
    if not files:
        print("没有找到字幕文件", file=sys.stderr)
        return 1
    key, endpoint, model = load_agnes()
    def process(source: Path):
        stem = source.stem
        bv = re.search(r"\[(BV[^]]+)\]", source.name)
        # Keep the language/part suffix so the same BV with multiple subtitle
        # variants never overwrites another source.
        output_name = safe_filename(f"{stem}_笔记") + ".md"
        fallback = classify_title(source.name)
        existing = list(TARGET.glob(f"*/{output_name}"))
        if existing and not args.force:
            return "skip", source, None, existing[0]
        transcript = parse_srt(source.read_text(encoding="utf-8", errors="replace"))
        error = None
        for attempt in range(args.retries + 1):
            try:
                result = ask_agnes(source.name, transcript, key, endpoint, model)
                break
            except Exception as exc:
                error = str(exc)
                if attempt < args.retries:
                    time.sleep(1.5 * (attempt + 1))
        else:
            result = {"category": fallback, "source_type": "opinion", "summary": "Agnes 分析失败，使用标题规则归档。", "tags": [], "key_points": [], "possible_use": "待人工确认。"}
        destination = TARGET / LABELS[result["category"]] / output_name
        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(make_note(source, result, transcript), encoding="utf-8")
        return ("fallback" if error else "done"), source, error, destination

    completed = skipped = failed = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [pool.submit(process, source) for source in files]
        for index, future in enumerate(as_completed(futures), 1):
            status, source, error, destination = future.result()
            if status == "skip":
                skipped += 1
            elif status == "fallback":
                failed += 1
                (ROOT / "organize_bilibili_failures.log").open("a", encoding="utf-8").write(f"{source.name}\t{error}\n")
            else:
                completed += 1
            print(f"[{index}/{len(files)}] {status} {source.name}", flush=True)
    print(f"完成：{completed}，跳过：{skipped}，标题兜底/失败：{failed}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
