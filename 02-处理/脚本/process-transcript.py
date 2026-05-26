#!/usr/bin/env python3
"""
逐字稿 → 原子笔记 处理脚本

核心思路：一份20分钟的逐字稿里藏着5-8个独立的、可复用的"知识点"。
把它们从原始语境中抽离，变成独立的、打了标签的、可拼接的原子笔记。

用法:
    # 单篇处理
    python3 process-transcript.py <逐字稿路径>

    # 查看处理状态
    python3 process-transcript.py --status

    # 批量处理：所有未处理的
    python3 process-transcript.py --batch

    # 批量处理：只跑 N 篇
    python3 process-transcript.py --batch 5

    # 从指定序号开始（含）
    python3 process-transcript.py --batch --from 100

    # 强制重新处理某篇
    python3 process-transcript.py "xxx.md" --force

    # 重置某篇状态为 pending
    python3 process-transcript.py --reset "xxx.md"

    # 重置全部状态
    python3 process-transcript.py --reset-all

    # 更新选题池（从已处理的原子笔记中汇总）
    python3 process-transcript.py --update-pool

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
POOL_DIR = VAULT_ROOT / "02-处理" / "选题池"
STATE_FILE = VAULT_ROOT / "02-处理" / "state.json"

# 9大领域
DOMAINS = [
    "AI工具/Skills",
    "编程/技术",
    "产品经理",
    "设计/PPT",
    "自媒体运营",
    "知识管理",
    "浏览器自动化",
    "视频制作",
    "理财/成长",
]

# 笔记类型
NOTE_TYPES = ["方法论", "案例", "观点", "数据", "故事", "金句"]

# 4种内容变形
DEFORMATIONS = {
    "观点文": "一个反常识的观点 → 用案例/数据佐证 → 你的立场",
    "实操教程": "我遇到了什么问题 → 我怎么解决的（带截图） → 你可以直接抄的步骤",
    "信息差/对比测评": "N个同类东西的横向对比 → 我的推荐 → 适用场景",
    "复盘/思考": "我做了什么 → 结果是什么 → 我学到了什么",
}


# ── 系统提示词 ─────────────────────────────────────────────────

SYSTEM_PROMPT = """你是一个专业的内容拆解师，擅长从逐字稿中提取独立的、可复用的原子笔记。

你的任务：读一篇逐字稿，找出其中所有有价值的"知识点"，把它们从原始语境中抽离出来，变成独立的、打了标签的、可以和任何其他素材拼接的原子笔记。

## 核心原则

1. **独立性**：每条笔记脱离原文也能看懂，不依赖上下文
2. **可复用性**：标注这条笔记可以用在哪些场景
3. **观点沉淀**："我的想法"栏是从"搬运"变"原创"的分水岭

## 笔记类型

| 类型 | 何时提取 | 说明 |
|------|---------|------|
| 方法论 | 有明确操作步骤或框架 | 可直接指导行动 |
| 案例 | 完整的实践故事、真实案例 | 有细节、有结果 |
| 观点 | 有传播价值的判断、洞察 | 反常识或有深度 |
| 数据 | 具体的数字、比例、对比 | 有说服力的论据 |
| 故事 | 有情节的个人经历或见闻 | 有代入感 |
| 金句 | 适合直接引用的高光表达 | 原汁原味，不改写 |

## 领域分类（必须选一个）

- AI工具/Skills
- 编程/技术
- 产品经理
- 设计/PPT
- 自媒体运营
- 知识管理
- 浏览器自动化
- 视频制作
- 理财/成长

## 输出格式

严格按以下 JSON 数组输出，不要输出其他内容：

```json
[
  {
    "title": "原子笔记标题（简洁有力，15字以内）",
    "type": "方法论/案例/观点/数据/故事/金句",
    "domain": "从上面9个领域中选一个",
    "reusable": "具体说明这条笔记可以用在什么场景",
    "summary": "用自己的话写2-5句话概括核心内容",
    "quote": "直接摘录最有价值的1-2段原文（如果有的话，没有则留空）",
    "hook": "一句话说明这个点为什么值得记住"
  }
]
```

## 提取原则

1. 一篇20分钟的逐字稿通常藏着5-8个独立知识点
2. 质量优先，宁可少提取也不要凑数
3. 金句必须原汁原味，不要改写
4. summary 要用自己的话概括，不要直接复制原文
5. reusable 要具体，写清楚可以用在什么内容里
6. hook 是一句话记忆锚点，方便后续检索时快速判断是否相关"""


# ── 状态管理 ─────────────────────────────────────────────────

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding='utf-8'))
    return {"files": {}, "updated_at": None}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = datetime.now().isoformat()
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')


def scan_transcripts():
    files = sorted(TRANSCRIPT_DIR.glob("2026-*.md"))
    def sort_key(f):
        m = re.search(r'-(\d+)-', f.name)
        return int(m.group(1)) if m else 99999
    return sorted(files, key=sort_key)


def sync_state(state):
    existing = set(state["files"].keys())
    transcripts = scan_transcripts()
    added = 0
    for f in transcripts:
        if f.name not in existing:
            state["files"][f.name] = {
                "status": "pending",
                "notes_count": 0,
                "processed_at": None,
                "error": None,
            }
            added += 1
    return added


def extract_index(filename):
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
    user_msg = f"""请分析以下逐字稿，提取原子笔记。

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


def parse_notes_from_reply(reply):
    """从 LLM 回复中解析 JSON，多层容错"""
    # 提取 json 代码块
    m = re.search(r'```json\s*(.*?)\s*```', reply, re.DOTALL)
    if m:
        raw = m.group(1)
    else:
        m2 = re.search(r'(\[\s*\{.*\}\s*\])', reply, re.DOTALL)
        raw = m2.group(1) if m2 else reply

    raw = raw.strip()
    raw = re.sub(r',\s*([\]}])', r'\1', raw)

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # 逐行修复
    lines = raw.split('\n')
    fixed_lines = [line.strip() for line in lines if line.strip()]
    fixed = ' '.join(fixed_lines)
    try:
        return json.loads(fixed)
    except json.JSONDecodeError:
        pass

    # 暴力提取每个 { ... } 块
    notes = []
    for m in re.finditer(r'\{[^{}]*\}', raw, re.DOTALL):
        try:
            note = json.loads(m.group(0))
            if 'title' in note and 'type' in note:
                notes.append(note)
        except json.JSONDecodeError:
            block = m.group(0)
            block = re.sub(r',\s*}', '}', block)
            block = block.replace('\n', '\\n')
            try:
                note = json.loads(block)
                if 'title' in note and 'type' in note:
                    notes.append(note)
            except json.JSONDecodeError:
                continue

    if notes:
        return notes

    raise json.JSONDecodeError("无法从回复中解析出有效笔记", raw, 0)


def build_note_md(note, source_fm, source_filename):
    """构建原子笔记的 Markdown 内容"""
    title = note['title']
    note_type = note.get('type', '观点')
    domain = note.get('domain', '未分类')
    reusable = note.get('reusable', '')
    summary = note.get('summary', '')
    quote = note.get('quote', '')
    hook = note.get('hook', '')

    # frontmatter
    lines = [
        '---',
        f'title: "{title}"',
        f'note_type: {note_type}',
        f'domain: {domain}',
        f'source: "[[{source_filename}]]"',
        f'date: {source_fm.get("date", datetime.now().strftime("%Y-%m-%d"))}',
        f'reusable: "{reusable}"',
        'tags:',
        f'  - 原子笔记',
        f'  - 类型/{note_type}',
        f'  - 领域/{domain}',
        '---',
    ]

    # 正文
    body = [
        f'# {title}',
        '',
        f'> {hook}' if hook else '',
        '',
        '## 核心内容',
        summary,
    ]

    if quote:
        body.extend([
            '',
            '## 原文关键段落',
            '> ' + quote.replace('\n', '\n> '),
        ])

    body.extend([
        '',
        '## 我的想法/延伸',
        '<!-- 这是从"搬运"变成"原创"的分水岭。写下你的观点、联想、加工思路 -->',
        '',
        '',
        '## 可复用场景',
        reusable,
        '',
        f'> 来源：[[{source_filename}]]',
    ])

    return '\n'.join(lines) + '\n\n' + '\n'.join(body)


def safe_filename(title):
    s = re.sub(r'[^\w一-鿿\-]', '-', title)
    s = re.sub(r'-+', '-', s).strip('-')
    return s[:60]


def process_one(filepath, out_dir, dry_run=False, force=False, max_retries=2):
    """处理单篇逐字稿，返回 (success, notes_count, error_msg)"""
    state = load_state()
    fname = filepath.name

    # 检查状态
    entry = state["files"].get(fname)
    if entry and entry["status"] == "done" and not force:
        return True, entry["notes_count"], "already_done"

    # 标记 processing
    state["files"][fname] = {
        "status": "processing",
        "notes_count": 0,
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
    reply = ""
    for attempt in range(max_retries + 1):
        try:
            reply = call_mimo(title, body, source_filename)
            notes = parse_notes_from_reply(reply)

            if dry_run:
                print(f"      ✓ 提取到 {len(notes)} 条原子笔记 (dry-run)")
                for n in notes:
                    print(f"        - [{n.get('type','?')}] {n.get('title','?')} ({n.get('domain','?')})")
                state["files"][fname]["status"] = "pending"
                save_state(state)
                return True, len(notes), None

            written = 0
            for note in notes:
                note_title = note.get('title', '无标题')
                note_type = note.get('type', '观点')
                safe = safe_filename(note_title)
                filename = f"{date}-{note_type}-{safe}.md"
                out_path = out_dir / filename
                md = build_note_md(note, fm, source_filename)
                out_path.write_text(md, encoding='utf-8')
                written += 1

            # 标记 done
            state["files"][fname] = {
                "status": "done",
                "notes_count": written,
                "processed_at": datetime.now().isoformat(),
                "error": None,
            }
            save_state(state)
            print(f"      ✓ {written} 条原子笔记 → {out_dir.name}/")
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
        "notes_count": 0,
        "processed_at": None,
        "error": last_error,
    }
    save_state(state)
    return False, 0, last_error


# ── 选题池更新 ─────────────────────────────────────────────────

def update_topic_pool():
    """从已处理的原子笔记中汇总选题池"""
    POOL_DIR.mkdir(parents=True, exist_ok=True)

    # 扫描所有原子笔记
    notes_by_domain = {d: [] for d in DOMAINS}
    notes_by_domain["未分类"] = []

    for note_file in sorted(CARD_DIR.glob("*.md")):
        if note_file.name.startswith("_"):
            continue
        content = note_file.read_text(encoding='utf-8')
        fm, _ = parse_frontmatter(content)
        domain = fm.get('domain', '未分类')
        note_type = fm.get('note_type', '')
        title = fm.get('title', note_file.stem)
        reusable = fm.get('reusable', '')
        source = fm.get('source', '')

        if domain not in notes_by_domain:
            notes_by_domain[domain] = []

        notes_by_domain[domain].append({
            "title": title,
            "type": note_type,
            "reusable": reusable,
            "source": source,
            "file": note_file.name,
        })

    # 按领域生成选题池文件
    total = 0
    for domain, notes in notes_by_domain.items():
        if not notes:
            continue

        safe_domain = domain.replace('/', '-')
        pool_file = POOL_DIR / f"{safe_domain}.md"

        lines = [
            f'# {domain} - 选题池',
            '',
            f'> 自动生成于 {datetime.now().strftime("%Y-%m-%d %H:%M")}',
            f'> 共 {len(notes)} 条原子笔记',
            '',
            '## 原子笔记索引',
            '',
        ]

        # 按类型分组
        by_type = {}
        for n in notes:
            t = n["type"] or "未分类"
            by_type.setdefault(t, []).append(n)

        for note_type in NOTE_TYPES:
            type_notes = by_type.get(note_type, [])
            if not type_notes:
                continue
            lines.append(f'### {note_type}')
            lines.append('')
            for n in type_notes:
                lines.append(f'- [ ] **{n["title"]}** — {n["reusable"]}')
                lines.append(f'      来源: {n["source"]}')
            lines.append('')

        lines.extend([
            '## 4种内容变形思路',
            '',
        ])
        for deform, desc in DEFORMATIONS.items():
            lines.append(f'### {deform}')
            lines.append(f'> {desc}')
            lines.append('')
            lines.append('<!-- 从上面的原子笔记中挑选组合，构思具体选题 -->')
            lines.append('')

        pool_file.write_text('\n'.join(lines), encoding='utf-8')
        total += 1
        print(f"  {domain}: {len(notes)} 条笔记")

    print(f"\n已更新 {total} 个领域的选题池 → {POOL_DIR}")


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

    total_notes = sum(v.get("notes_count", v.get("cards_count", 0)) for v in files.values())

    print(f"┌─────────────────────────────────────┐")
    print(f"│  逐字稿 → 原子笔记 处理状态          │")
    print(f"├─────────────────────────────────────┤")
    print(f"│  总计:   {total:>4} 篇                   │")
    print(f"│  已完成: {done:>4} 篇  ({total_notes} 条笔记)     │")
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
            count = entry.get("notes_count", entry.get("cards_count", 0))
            print(f"    [{idx:03d}] {count}条笔记  {fname[:50]}")


# ── 主入口 ─────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='逐字稿 → 原子笔记 处理脚本',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --status                          查看状态
  %(prog)s --batch                           批量处理所有 pending
  %(prog)s --batch 10                        只处理 10 篇
  %(prog)s --batch --from 50                 从第 50 篇开始
  %(prog)s "01-输入/素材/xxx.md"             单篇处理
  %(prog)s "01-输入/素材/xxx.md" --force     强制重新处理
  %(prog)s --update-pool                     更新选题池
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
    parser.add_argument('--update-pool', action='store_true', help='更新选题池')
    args = parser.parse_args()

    # 输出目录
    if args.out:
        out_dir = Path(args.out)
    else:
        out_dir = CARD_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    # ── 选题池更新 ──
    if args.update_pool:
        update_topic_pool()
        return

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

        all_files = sorted(
            state["files"].items(),
            key=lambda x: extract_index(x[0]),
        )

        candidates = []
        for fname, entry in all_files:
            idx = extract_index(fname)
            if args.from_idx and idx < args.from_idx:
                continue
            if args.to_idx and idx > args.to_idx:
                continue
            if entry["status"] in ("pending", "error"):
                candidates.append((fname, idx))

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
        total_notes = 0

        for i, (fname, idx) in enumerate(candidates, 1):
            filepath = TRANSCRIPT_DIR / fname
            if not filepath.exists():
                print(f"[{idx:03d}] 文件不存在，跳过")
                fail += 1
                continue

            ok, count, err = process_one(filepath, out_dir, dry_run=args.dry_run)
            if ok:
                success += 1
                total_notes += count
            else:
                fail += 1

            if i < len(candidates) and not args.dry_run:
                time.sleep(args.delay)

        print(f"\n{'='*40}")
        print(f"批量处理完成:")
        print(f"  成功: {success} 篇")
        print(f"  失败: {fail} 篇")
        print(f"  原子笔记: {total_notes} 条")

        # 自动更新选题池
        if not args.dry_run and total_notes > 0:
            print(f"\n自动更新选题池...")
            update_topic_pool()
        return

    # ── 单篇处理 ──
    if not args.file:
        parser.print_help()
        return

    filepath = Path(args.file)
    if not filepath.exists():
        candidate = TRANSCRIPT_DIR / args.file
        if candidate.exists():
            filepath = candidate
        else:
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
        print(f"已处理过（{count}条笔记），使用 --force 重新处理")


if __name__ == '__main__':
    main()
