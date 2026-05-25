#!/usr/bin/env python3
"""
逐字稿原子化处理脚本 — 带状态管理 + 批量处理

用法:
    # 单篇处理
    python3 process-transcript.py <逐字稿路径>

    # 查看处理状态
    python3 process-transcript.py --status

    # 批量处理：所有未处理的（按文件名序号顺序）
    python3 process-transcript.py --batch

    # 批量处理：只跑 N 篇
    python3 process-transcript.py --batch 5

    # 从指定序号开始（含）
    python3 process-transcript.py --batch --from 100

    # 强制重新处理某篇（重置状态）
    python3 process-transcript.py "xxx.md" --force

    # 重置某篇状态为 pending（不处理，只改状态）
    python3 process-transcript.py --reset "xxx.md"

    # 重置全部状态
    python3 process-transcript.py --reset-all

状态文件: 02-处理/state.json
"""

import re
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests


# ── 配置 ────────────────────────────────────────────────────────

MIMO_API_KEY = "tp-czq97wj2vol05hpfipuico337yuvk7tbo8ikslu5yh8vjnlb"
MIMO_BASE_URL = "https://token-plan-cn.xiaomimimo.com/v1"
MIMO_MODEL = "mimo-v2.5-pro"

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent       # 自媒体/
TRANSCRIPT_DIR = VAULT_ROOT / "01-输入" / "素材"
CARD_DIR = VAULT_ROOT / "02-处理" / "卡片"
STATE_FILE = VAULT_ROOT / "02-处理" / "state.json"


# ── 系统提示词 ─────────────────────────────────────────────────

SYSTEM_PROMPT = """你是一个专业的内容分析师，擅长从逐字稿中提取原子化知识卡片。

你的任务：读取一篇逐字稿，提取出所有有价值的原子卡片，每张卡片用 Obsidian 双链格式输出。

## 卡片类型

| 类型 | 何时提取 | frontmatter card_type 值 |
|------|---------|-------------------------|
| 概念卡 | 核心术语、工具定义、技术概念 | `概念卡` |
| 方法卡 | 有明确操作步骤的流程 | `方法卡` |
| 观点卡 | 有传播价值的判断、洞察 | `观点卡` |
| 案例卡 | 完整的实践故事、用户案例 | `案例卡` |
| 金句卡 | 适合直接引用的高光表达 | `金句卡` |

## 输出格式

严格按以下 JSON 数组输出，不要输出其他内容：

```json
[
  {
    "card_type": "观点卡",
    "title": "卡片标题（简洁有力，15字以内）",
    "tags": ["主题/AI工具", "素材/观点"],
    "related": ["相关卡片名1", "相关卡片名2"],
    "content": "卡片正文，使用 Markdown 格式，正文中用 [[双向链接]] 标注相关内容"
  }
]
```

## 双链规则

1. 正文中提到其他卡片的概念时，用 `[[卡片名]]` 标注
2. content 末尾加一行：`> 来源：[[原始逐字稿文件名]]`
3. 相关但不同卡片之间用 `related` 字段互指
4. 同一主题的多张卡片应互相链接

## 标签规则

每张卡片必须包含：
- 一个卡片类型标签：`卡片/概念`、`卡片/方法`、`卡片/观点`、`卡片/案例`、`卡片/金句`
- 至少一个主题标签，从以下选择：
  - `主题/AI工具`、`主题/Skills`、`主题/编程`、`主题/产品经理`
  - `主题/设计`、`主题/PPT`、`主题/自媒体`、`主题/知识管理`
  - `主题/浏览器自动化`、`主题/视频`
- 可选的素材用途标签：`素材/观点`、`素材/教程`、`素材/热点`、`素材/金句`、`素材/案例`

## 提取原则

1. 一卡一主题，每张卡片只讲一个点
2. 自包含，卡片本身能独立理解
3. 提取有传播价值、可复用的内容，不要水字数
4. 一篇逐字稿通常提取 3-8 张卡片，质量优先
5. 金句要原汁原味，不要改写"""


# ── 状态管理 ─────────────────────────────────────────────────

def load_state():
    """加载状态文件，不存在则初始化"""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding='utf-8'))
    return {"files": {}, "updated_at": None}


def save_state(state):
    """保存状态文件"""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = datetime.now().isoformat()
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')


def scan_transcripts():
    """扫描素材目录，按文件名中的序号排序返回"""
    files = sorted(TRANSCRIPT_DIR.glob("2026-*.md"))
    # 按文件名中的数字序号排序
    def sort_key(f):
        m = re.search(r'-(\d+)-', f.name)
        return int(m.group(1)) if m else 99999
    return sorted(files, key=sort_key)


def sync_state(state):
    """把新出现的逐字稿加入状态，返回新增数量"""
    existing = set(state["files"].keys())
    transcripts = scan_transcripts()
    added = 0
    for f in transcripts:
        if f.name not in existing:
            state["files"][f.name] = {
                "status": "pending",
                "cards_count": 0,
                "processed_at": None,
                "error": None,
            }
            added += 1
    return added


def extract_index(filename):
    """从文件名提取序号"""
    m = re.search(r'-(\d+)-', filename)
    return int(m.group(1)) if m else 0


# ── 核心处理 ─────────────────────────────────────────────────

def parse_frontmatter(content):
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return {}, content
    fm_text = match.group(1)
    body = content[match.end():]
    fm = {}
    current_key = None
    current_list = None
    for line in fm_text.split('\n'):
        line = line.rstrip()
        if line.startswith('  - '):
            if current_list is not None:
                current_list.append(line[4:].strip())
        elif ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val == '':
                current_key = key
                current_list = []
                fm[key] = current_list
            else:
                fm[key] = val.strip('"').strip("'")
                current_key = None
                current_list = None
    return fm, body


def call_mimo(title, body, source_filename):
    user_msg = f"""请分析以下逐字稿，提取原子卡片。

原始文件名：{source_filename}
标题：{title}

--- 逐字稿正文 ---
{body}
--- 正文结束 ---
"""
    headers = {
        "Authorization": f"Bearer {MIMO_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MIMO_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ],
        "temperature": 0.3,
        "max_tokens": 8000,
    }
    resp = requests.post(
        f"{MIMO_BASE_URL}/chat/completions",
        headers=headers,
        json=payload,
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def parse_cards_from_reply(reply):
    """从 LLM 回复中解析 JSON，多层容错"""
    # 第1步：提取 json 代码块
    m = re.search(r'```json\s*(.*?)\s*```', reply, re.DOTALL)
    if m:
        raw = m.group(1)
    else:
        # 找最外层的 [ ... ]
        m2 = re.search(r'(\[\s*\{.*\}\s*\])', reply, re.DOTALL)
        raw = m2.group(1) if m2 else reply

    # 第2步：清理常见问题
    raw = raw.strip()
    # 去掉尾部多余逗号
    raw = re.sub(r',\s*([\]}])', r'\1', raw)
    # 修复未转义的换行（在字符串值内）
    # 先尝试直接解析
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # 第3步：逐行修复——把裸换行替换成 \n
    lines = raw.split('\n')
    fixed_lines = []
    in_string = False
    for line in lines:
        stripped = line.strip()
        # 跳过明显不是 JSON 的行（比如 LLM 的解释文字）
        if not stripped:
            continue
        fixed_lines.append(stripped)
    fixed = ' '.join(fixed_lines)
    try:
        return json.loads(fixed)
    except json.JSONDecodeError:
        pass

    # 第4步：暴力提取每个 { ... } 块
    cards = []
    for m in re.finditer(r'\{[^{}]*\}', raw, re.DOTALL):
        try:
            card = json.loads(m.group(0))
            if 'title' in card and 'card_type' in card:
                cards.append(card)
        except json.JSONDecodeError:
            # 尝试修复这个块
            block = m.group(0)
            block = re.sub(r',\s*}', '}', block)
            block = block.replace('\n', '\\n')
            try:
                card = json.loads(block)
                if 'title' in card and 'card_type' in card:
                    cards.append(card)
            except json.JSONDecodeError:
                continue

    if cards:
        return cards

    # 全部失败，抛出异常让上层处理
    raise json.JSONDecodeError("无法从回复中解析出有效卡片", raw, 0)


def build_card_md(card, source_fm, source_filename):
    date = source_fm.get('date', datetime.now().strftime('%Y-%m-%d'))
    title = card['title']
    card_type = card['card_type']
    tags = card.get('tags', [])
    related = card.get('related', [])
    content = card['content']

    type_tag_map = {
        '概念卡': '卡片/概念', '方法卡': '卡片/方法',
        '观点卡': '卡片/观点', '案例卡': '卡片/案例', '金句卡': '卡片/金句',
    }
    expected = type_tag_map.get(card_type, '卡片/概念')
    if expected not in tags:
        tags.insert(0, expected)

    fm_lines = [
        '---',
        f'title: "{title}"',
        f'card_type: {card_type}',
        'layer: 处理',
        f'source: "[[{source_filename}]]"',
        f'date: {date}',
        'tags:',
    ]
    for t in tags:
        fm_lines.append(f'  - {t}')
    if related:
        fm_lines.append('related:')
        for r in related:
            fm_lines.append(f'  - "[[{r}]]"')
    fm_lines.append('---')
    return '\n'.join(fm_lines) + f"\n\n# {title}\n\n{content}"


def safe_filename(title):
    s = re.sub(r'[^\w一-鿿\-]', '-', title)
    s = re.sub(r'-+', '-', s).strip('-')
    return s[:60]


def process_one(filepath, out_dir, dry_run=False, force=False, max_retries=2):
    """处理单篇逐字稿，返回 (success, cards_count, error_msg)"""
    state = load_state()
    fname = filepath.name

    # 检查状态
    entry = state["files"].get(fname)
    if entry and entry["status"] == "done" and not force:
        return True, entry["cards_count"], "already_done"

    # 标记 processing
    state["files"][fname] = {
        "status": "processing",
        "cards_count": 0,
        "processed_at": None,
        "error": None,
    }
    save_state(state)

    content = filepath.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(content)
    title = fm.get('title', filepath.stem)
    source_filename = filepath.name
    date = fm.get('date', datetime.now().strftime('%Y-%m-%d'))
    idx = extract_index(fname)

    print(f"\n[{idx:03d}] {title}")
    print(f"      正文 {len(body)} 字符 → 调用 MiMo...")

    last_error = None
    for attempt in range(max_retries + 1):
        try:
            reply = call_mimo(title, body, source_filename)
            cards = parse_cards_from_reply(reply)

            if dry_run:
                print(f"      ✓ 提取到 {len(cards)} 张卡片 (dry-run)")
                state["files"][fname]["status"] = "pending"
                save_state(state)
                return True, len(cards), None

            written = 0
            for card in cards:
                card_type = card.get('card_type', '未知')
                card_title = card.get('title', '无标题')
                safe = safe_filename(card_title)
                filename = f"{date}-{card_type}-{safe}.md"
                out_path = out_dir / filename
                md = build_card_md(card, fm, source_filename)
                out_path.write_text(md, encoding='utf-8')
                written += 1

            # 标记 done
            state["files"][fname] = {
                "status": "done",
                "cards_count": written,
                "processed_at": datetime.now().isoformat(),
                "error": None,
            }
            save_state(state)
            print(f"      ✓ {written} 张卡片 → {out_dir.name}/")
            return True, written, None

        except Exception as e:
            last_error = str(e)[:200]
            if attempt < max_retries:
                print(f"      ⚠ 第{attempt+1}次失败，重试中... ({e})")
                time.sleep(2)
            else:
                print(f"      ✗ 失败({max_retries+1}次): {e}")

    # 保存原始回复供调试
    debug_dir = out_dir / "_debug"
    debug_dir.mkdir(exist_ok=True)
    debug_path = debug_dir / f"{idx:03d}-raw-reply.txt"
    try:
        debug_path.write_text(reply, encoding='utf-8')
        print(f"      原始回复已保存: {debug_path.name}")
    except Exception:
        pass

    state["files"][fname] = {
        "status": "error",
        "cards_count": 0,
        "processed_at": None,
        "error": last_error,
    }
    save_state(state)
    return False, 0, last_error


# ── 状态展示 ─────────────────────────────────────────────────

def show_status():
    state = load_state()
    added = sync_state(state)
    if added:
        save_state(state)

    files = state["files"]
    total = len(files)
    done = sum(1 for v in files.values() if v["status"] == "done")
    pending = sum(1 for v in files.values() if v["status"] == "pending")
    error = sum(1 for v in files.values() if v["status"] == "error")
    processing = sum(1 for v in files.values() if v["status"] == "processing")

    total_cards = sum(v["cards_count"] for v in files.values())

    print(f"┌─────────────────────────────────────┐")
    print(f"│  逐字稿处理状态                      │")
    print(f"├─────────────────────────────────────┤")
    print(f"│  总计:   {total:>4} 篇                   │")
    print(f"│  已完成: {done:>4} 篇  ({total_cards} 张卡片)     │")
    print(f"│  待处理: {pending:>4} 篇                   │")
    print(f"│  失败:   {error:>4} 篇                   │")
    if processing:
        print(f"│  处理中: {processing:>4} 篇                   │")
    print(f"└─────────────────────────────────────┘")

    if added:
        print(f"\n  新发现 {added} 篇逐字稿，已加入队列")

    # 显示失败的
    errors = [(k, v) for k, v in files.items() if v["status"] == "error"]
    if errors:
        print(f"\n  失败列表:")
        for fname, entry in errors:
            idx = extract_index(fname)
            print(f"    [{idx:03d}] {entry['error'][:60]}")

    # 显示最近完成的
    recent = [(k, v) for k, v in files.items() if v["status"] == "done"]
    recent.sort(key=lambda x: x[1].get("processed_at", ""), reverse=True)
    if recent[:5]:
        print(f"\n  最近完成:")
        for fname, entry in recent[:5]:
            idx = extract_index(fname)
            print(f"    [{idx:03d}] {entry['cards_count']}张卡片  {fname[:50]}")


# ── 主入口 ─────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='逐字稿原子化处理（带状态管理）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --status                          查看状态
  %(prog)s --batch                           批量处理所有 pending
  %(prog)s --batch 10                        只处理 10 篇
  %(prog)s --batch --from 50                 从第 50 篇开始
  %(prog)s --batch --from 50 --to 100        处理 50~100
  %(prog)s "01-输入/素材/xxx.md"             单篇处理
  %(prog)s "01-输入/素材/xxx.md" --force     强制重新处理
  %(prog)s --reset "xxx.md"                  重置单篇状态
  %(prog)s --reset-all                       重置全部状态
        """,
    )
    parser.add_argument('file', nargs='?', help='逐字稿文件路径')
    parser.add_argument('--status', action='store_true', help='显示处理状态')
    parser.add_argument('--batch', nargs='?', const=-1, type=int, help='批量处理（可指定数量）')
    parser.add_argument('--from', dest='from_idx', type=int, help='从指定序号开始（含）')
    parser.add_argument('--to', dest='to_idx', type=int, help='到指定序号为止（含）')
    parser.add_argument('--force', action='store_true', help='强制重新处理')
    parser.add_argument('--dry-run', action='store_true', help='只预览不写文件')
    parser.add_argument('--out', default=None, help='输出目录')
    parser.add_argument('--reset', nargs='?', const='', help='重置指定文件状态为 pending')
    parser.add_argument('--reset-all', action='store_true', help='重置全部状态为 pending')
    parser.add_argument('--delay', type=float, default=2.0, help='批量处理间隔秒数（默认2）')
    args = parser.parse_args()

    # 输出目录
    if args.out:
        out_dir = Path(args.out)
    else:
        out_dir = CARD_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    # ── 状态查看 ──
    if args.status:
        show_status()
        return

    # ── 重置全部 ──
    if args.reset_all:
        state = load_state()
        for fname in state["files"]:
            state["files"][fname]["status"] = "pending"
            state["files"][fname]["error"] = None
            state["files"][fname]["processed_at"] = None
        save_state(state)
        print(f"已重置 {len(state['files'])} 篇状态为 pending")
        return

    # ── 重置单篇 ──
    if args.reset is not None:
        state = load_state()
        if args.reset:
            # 重置指定文件
            target = args.reset
            matched = [k for k in state["files"] if target in k]
            if not matched:
                print(f"未找到匹配: {target}")
                return
            for fname in matched:
                state["files"][fname]["status"] = "pending"
                state["files"][fname]["error"] = None
                print(f"已重置: {fname}")
        save_state(state)
        return

    # ── 批量处理 ──
    if args.batch is not None:
        state = load_state()
        sync_state(state)
        save_state(state)

        # 按序号排序，筛选 pending
        all_files = sorted(
            state["files"].items(),
            key=lambda x: extract_index(x[0]),
        )

        # 筛选范围
        candidates = []
        for fname, entry in all_files:
            idx = extract_index(fname)

            # 范围过滤
            if args.from_idx and idx < args.from_idx:
                continue
            if args.to_idx and idx > args.to_idx:
                continue

            # 只处理 pending 或 error
            if entry["status"] in ("pending", "error"):
                candidates.append((fname, idx))

        # 限制数量
        limit = args.batch if args.batch > 0 else len(candidates)
        candidates = candidates[:limit]

        if not candidates:
            print("没有待处理的逐字稿")
            show_status()
            return

        print(f"批量处理: {len(candidates)} 篇")
        print(f"范围: [{candidates[0][1]:03d}] ~ [{candidates[-1][1]:03d}]")
        print(f"输出: {out_dir}")
        if args.dry_run:
            print(f"模式: dry-run（不写文件）")
        print(f"延迟: {args.delay}s/篇")
        print(f"按 Ctrl+C 可随时中断，已处理的会保留状态\n")

        success = 0
        fail = 0
        total_cards = 0

        for i, (fname, idx) in enumerate(candidates, 1):
            filepath = TRANSCRIPT_DIR / fname
            if not filepath.exists():
                print(f"[{idx:03d}] 文件不存在，跳过")
                fail += 1
                continue

            ok, count, err = process_one(filepath, out_dir, dry_run=args.dry_run)
            if ok:
                success += 1
                total_cards += count
            else:
                fail += 1

            # 间隔（最后一篇不等）
            if i < len(candidates) and not args.dry_run:
                time.sleep(args.delay)

        print(f"\n{'='*40}")
        print(f"批量处理完成:")
        print(f"  成功: {success} 篇")
        print(f"  失败: {fail} 篇")
        print(f"  卡片: {total_cards} 张")
        return

    # ── 单篇处理 ──
    if not args.file:
        parser.print_help()
        return

    filepath = Path(args.file)
    if not filepath.exists():
        # 尝试在素材目录中查找
        candidate = TRANSCRIPT_DIR / args.file
        if candidate.exists():
            filepath = candidate
        else:
            # 模糊匹配
            matches = list(TRANSCRIPT_DIR.glob(f"*{args.file}*"))
            if len(matches) == 1:
                filepath = matches[0]
            elif len(matches) > 1:
                print(f"匹配到多篇:")
                for m in matches:
                    print(f"  {m.name}")
                return
            else:
                print(f"文件不存在: {args.file}")
                return

    state = load_state()
    sync_state(state)
    save_state(state)

    ok, count, err = process_one(filepath, out_dir, dry_run=args.dry_run, force=args.force)
    if err == "already_done":
        print(f"已处理过（{count}张卡片），使用 --force 重新处理")


if __name__ == '__main__':
    main()
