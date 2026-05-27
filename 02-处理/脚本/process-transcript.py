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

    # 分析素材库领域分布
    python3 process-transcript.py --analyze-materials

    # 让素材长成"选题胚胎"（默认优先读卡片，卡片为空时读原始素材）
    python3 process-transcript.py --incubate 10

    # 直接从原始素材孵化，并生成发布草稿骨架
    python3 process-transcript.py --incubate 10 --incubate-source raw --draft

状态文件: 02-处理/state.json
"""

import re
import sys
import json
import time
import hashlib
import argparse
import urllib.error
import urllib.request
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    requests = None


# ── 配置 ────────────────────────────────────────────────────────

MIMO_API_KEY = "tp-czq97wj2vol05hpfipuico337yuvk7tbo8ikslu5yh8vjnlb"
MIMO_BASE_URL = "https://token-plan-cn.xiaomimimo.com/v1"
MIMO_MODEL = "mimo-v2.5-pro"

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent       # 自媒体/
TRANSCRIPT_DIR = VAULT_ROOT / "01-输入" / "素材"
CARD_DIR = VAULT_ROOT / "02-处理" / "卡片"
POOL_DIR = VAULT_ROOT / "02-处理" / "选题池"
EMBRYO_DIR = VAULT_ROOT / "02-处理" / "选题胚胎"
MATERIAL_REPORT = VAULT_ROOT / "02-处理" / "素材分析.md"
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

# 2026 内容增长信号：用于把"素材摘要"加工成更像可发表内容的选题胚胎。
# 这些不是硬编码结论，而是给模型的编辑约束：少做工具搬运，多做观点、证据和人味。
CONTENT_SIGNALS = [
    "用户越来越排斥没有人味、未标注、缺少证据的 AI 生成内容；AI 应该做后台编辑部，不应该替代前台人格。",
    "短视频和图文开头都要前置价值：3 秒内给冲突、结果、反常识问题或强视觉变化。",
    "工具教程必须升级成场景教程：谁遇到什么痛点，用这个方法节省了什么，踩坑是什么。",
    "爆款素材通常同时具备：强痛点、新鲜观点、可演示结果、可信证据、可收藏模板。",
    "长尾流量越来越依赖结构化、可引用、可检索的内容：标题、关键词、清单和原始证据要清楚。",
]

# 标题级领域归类规则。比用 frontmatter 的 bilibili/笔记 标签更准。
DOMAIN_RULES = [
    ("AI编程/Vibe Coding/开发实战", r"vibe|vibecoding|coding|codex|claude\s*code|opencode|cursor|lovable|trae|代码|编程|开发|前端|后端|web3|ios|python|react|html|css|javascript|github|git|code review|登录|数据库|小程序|网站|网页"),
    ("Agent/Skills/MCP/OpenClaw", r"agent|智能体|skills?|skill|openclaw|claw|clawdbot|mcp|tool use|multi-agent|多agent|多智能体|hermes|symphony|qoder|memory|记忆|context|上下文|agent teams"),
    ("设计/UI/PPT/文档/可视化", r"设计|ui|ux|figma|ppt|幻灯片|海报|审美|动效|组件|material|hig|word|docx|排版|图标|配色|原型|流程图|excalidraw|图表|canva|affinity|pencil|stitch|画布|交互|导航|毛玻璃|时间轴"),
    ("视频/剪辑/生图/多模态创作", r"视频|剪辑|字幕|口播|短剧|生图|图片|seedance|veo|remotion|tts|asr|b站|抖音|小红书|youtube|vlog|影视|成片|播客|nano|banana|gpt image|image2|即梦|midjourney|stable"),
    ("产品经理/职场/商业/个人IP", r"产品经理|产品|pm|prd|需求|roadmap|面试|职场|汇报|一人公司|创业|商业|个人ip|公众号|自媒体|老板|跳槽|简历|试用期|性格|相亲|信任|协作|项目"),
    ("知识管理/Obsidian/信息整理", r"obsidian|笔记|知识库|信息|收藏|notebooklm|youmind|memos|zotero|大纲|整理|阅读|研报|复习|学习材料|文件夹|论文"),
    ("自动化/RPA/n8n/飞书/工作流", r"自动化|rpa|n8n|工作流|部署|cloudflare|docker|服务器|浏览器自动化|api|cli|飞书|微信|qq|tasker|macrodroid|make|监控|上传|采集|爬虫|scrapling|coze"),
    ("AI模型/行业观察/基础教程", r"模型|openai|anthropic|gemini|kimi|deepseek|glm|minimax|qwen|claude opus|gpt|ai时代|焦虑|底层|原理|教程|入门|趋势|geo|langchain|rag|向量|多模态|提示词"),
]


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


def clean_text(text):
    """压缩空白，保留中文内容可读性。"""
    return re.sub(r'\s+', ' ', text or '').strip()


def get_title_from_file(filepath):
    content = filepath.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(content)
    return fm.get('title', filepath.stem), fm, body


def classify_domain(title, body=''):
    """按标题为主、正文为辅做主领域归类。"""
    haystack = f"{title}\n{clean_text(body[:1000])}".lower()
    best_domain = "其他/泛主题"
    best_score = 0
    for domain, pattern in DOMAIN_RULES:
        matches = re.findall(pattern, haystack, flags=re.IGNORECASE)
        score = len(matches)
        if score > best_score:
            best_score = score
            best_domain = domain
    return best_domain


def canonical_domain(domain, fallback="其他/泛主题"):
    names = [name for name, _ in DOMAIN_RULES] + ["其他/泛主题"]
    if domain in names:
        return domain
    guessed = classify_domain(domain or "", "")
    return guessed if guessed != "其他/泛主题" else fallback


def infer_audience(title, domain):
    """用轻量规则给选题胚胎补一个默认读者。"""
    text = title.lower()
    if re.search(r"产品经理|pm|prd|需求|roadmap|面试", text):
        return "产品经理/想转 AI 产品的人"
    if re.search(r"设计|ui|figma|ppt|审美|原型", text):
        return "设计师/需要做视觉表达的知识工作者"
    if re.search(r"剪辑|视频|b站|抖音|小红书|口播|自媒体", text):
        return "自媒体创作者/视频创作者"
    if re.search(r"代码|编程|开发|前端|后端|github|codex|cursor", text):
        return "独立开发者/AI 编程学习者"
    if re.search(r"obsidian|笔记|知识库|notebooklm|信息", text):
        return "知识管理重度用户/内容创作者"
    if "Agent" in domain or "Skills" in domain:
        return "AI 工具玩家/想把工作流产品化的人"
    return "想用 AI 放大生产力的普通创作者"


def local_material_score(title, domain, body=''):
    """不调用模型的粗评分，方便筛选值得孵化的素材。"""
    text = f"{title}\n{body[:1500]}"
    score = 0
    reasons = []
    if re.search(r"保姆级|手把手|实战|教程|从0|零基础|完整|一键|模板|开源", text, re.IGNORECASE):
        score += 2
        reasons.append("可教程化")
    if re.search(r"最强|爆火|神器|彻底|全网|重磅|颠覆|改变|封神|上限", text, re.IGNORECASE):
        score += 1
        reasons.append("标题冲突强")
    if re.search(r"复盘|踩坑|经验|失败|死了|总结|真实|实测", text, re.IGNORECASE):
        score += 2
        reasons.append("可信度/人味强")
    if re.search(r"产品经理|设计|剪辑|自媒体|Obsidian|Claude Code|Codex|OpenClaw|Skills|PPT", text, re.IGNORECASE):
        score += 1
        reasons.append("垂直受众明确")
    if domain != "其他/泛主题":
        score += 1
        reasons.append("领域清晰")
    return min(score, 10), reasons


def extract_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        return [tags]
    return tags if isinstance(tags, list) else []


def call_mimo_chat(system_prompt, user_msg, temperature=0.3, max_tokens=8000):
    headers = {
        "Authorization": f"Bearer {MIMO_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MIMO_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_msg},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    url = f"{MIMO_BASE_URL}/chat/completions"
    if requests:
        resp = requests.post(url, headers=headers, json=payload, timeout=120)
        resp.raise_for_status()
        data = resp.json()
    else:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="ignore")
            raise RuntimeError(f"HTTP {e.code}: {detail[:500]}") from e
    return data["choices"][0]["message"]["content"]


def call_mimo(title, body, source_filename):
    user_msg = f"""请分析以下逐字稿，提取原子笔记。

原始文件名：{source_filename}
标题：{title}

--- 逐字稿正文 ---
{body}
--- 正文结束 ---
"""
    return call_mimo_chat(SYSTEM_PROMPT, user_msg, temperature=0.3, max_tokens=8000)


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


# ── 素材分析与孵化 ─────────────────────────────────────────────

def analyze_materials():
    """扫描原始素材，生成领域分布报告。"""
    files = scan_transcripts()
    by_domain = {}
    tag_counts = {}
    scored = []

    for f in files:
        title, fm, body = get_title_from_file(f)
        domain = classify_domain(title, body)
        score, reasons = local_material_score(title, domain, body)
        by_domain.setdefault(domain, []).append((title, f.name, score, reasons))
        scored.append((score, title, domain, f.name, reasons))
        for tag in extract_tags(fm):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    lines = [
        "# 素材领域分析",
        "",
        f"> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"> 扫描素材：{len(files)} 篇",
        "",
        "## 领域分布",
        "",
        "| 领域 | 数量 | 适合长出的内容 |",
        "|---|---:|---|",
    ]

    growth_map = {
        "AI编程/Vibe Coding/开发实战": "实测教程、失败复盘、工具横评、普通人上手路线",
        "Agent/Skills/MCP/OpenClaw": "架构拆解、工作流案例、未来趋势判断、系统提示词分析",
        "设计/UI/PPT/文档/可视化": "高级感改造、模板、审美训练、AI 设计工作流",
        "视频/剪辑/生图/多模态创作": "AI 视频流程、自动剪辑、脚本模板、工具链复盘",
        "产品经理/职场/商业/个人IP": "AI 产品经理、职场提效、面试、个人品牌观点文",
        "知识管理/Obsidian/信息整理": "第二大脑、素材库、自动写作系统、笔记工作流",
        "AI模型/行业观察/基础教程": "模型更新解读、趋势判断、反常识观点、基础科普",
        "自动化/RPA/n8n/飞书/工作流": "一人公司、自动化运营、无人后台任务、低成本部署",
        "其他/泛主题": "观点文、人物/商业案例、跨领域联想",
    }

    for domain, items in sorted(by_domain.items(), key=lambda x: len(x[1]), reverse=True):
        lines.append(f"| {domain} | {len(items)} | {growth_map.get(domain, '选题组合、观点加工')} |")

    lines.extend([
        "",
        "## 最值得优先孵化的素材",
        "",
    ])
    for score, title, domain, fname, reasons in sorted(scored, reverse=True)[:40]:
        reason_text = "、".join(reasons) if reasons else "待人工判断"
        lines.append(f"- **{score}/10** `{domain}` [[{fname}]]")
        lines.append(f"  - {title}")
        lines.append(f"  - 理由：{reason_text}")

    lines.extend([
        "",
        "## 高频标签",
        "",
    ])
    for tag, count in sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:60]:
        lines.append(f"- `{tag}`：{count}")

    lines.extend([
        "",
        "## 孵化原则",
        "",
        "1. 不把素材直接洗成文章，先补上你的判断、实测、反常识和场景。",
        "2. 工具素材优先改造成场景素材：谁卡住了、用什么方法、节省什么、踩了什么坑。",
        "3. 每个选题胚胎必须至少带 3 个钩子、1 个观点、1 个证据缺口、1 个可演示结果。",
        "4. AI 做后台编辑部，人做前台人格；最终发布前必须写入你的立场和经验。",
    ])

    MATERIAL_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"已生成素材分析: {MATERIAL_REPORT}")


INCUBATION_PROMPT = """你是一个自媒体总编辑，负责把原始素材孵化成可发表、有新鲜观点、可能爆款的选题胚胎。

你不是洗稿助手。你的目标是帮作者从素材里长出"血肉"：
- 补出读者痛点
- 提出新鲜观点
- 设计开头钩子
- 找到需要补证据/实测的位置
- 给出适合不同平台的发布形态

必须遵守：
1. 不要虚构已发生的数据、报告、亲身经历；没有证据就写到 evidence_to_add。
2. 不要只写工具介绍，要把工具放进具体人群和具体任务。
3. 每个选题必须有人味：作者应该补哪段个人判断、踩坑或实测。
4. 标题和钩子要有冲突，但不要标题党到承诺无法兑现。
5. 输出严格是 JSON 对象，不要输出 Markdown 代码块。

JSON 字段：
{
  "title": "选题胚胎标题",
  "domain": "领域",
  "audience": "目标读者",
  "pain": "读者痛点",
  "fresh_angle": "新鲜观点/反常识角度",
  "core_pov": "作者可以站住的核心立场",
  "hooks": ["3-5个开头钩子"],
  "evidence_to_add": ["还需要补的证据/实测/截图/案例"],
  "demo_or_result": "最适合展示的结果画面或成果",
  "outline": ["发布内容结构，5-7步"],
  "platform_versions": {
    "小红书": "标题/图文角度",
    "B站": "视频标题/脚本角度",
    "公众号": "长文角度"
  },
  "draft_skeleton": "如果要求生成草稿，用 600-1000 字给出可继续改写的草稿骨架；否则给简短骨架",
  "publishability_score": 1,
  "score_reason": "为什么给这个分数",
  "risk": "可能翻车/同质化/证据不足的地方",
  "next_action": "作者下一步最该补什么"
}
"""


def parse_json_object(reply):
    raw = reply.strip()
    m = re.search(r'```json\s*(.*?)\s*```', raw, re.DOTALL)
    if m:
        raw = m.group(1).strip()
    else:
        m = re.search(r'(\{.*\})', raw, re.DOTALL)
        if m:
            raw = m.group(1).strip()
    raw = re.sub(r',\s*([\]}])', r'\1', raw)
    return json.loads(raw)


def material_payload(filepath, source_kind):
    title, fm, body = get_title_from_file(filepath)
    domain = fm.get("domain") or classify_domain(title, body)
    audience = infer_audience(title, domain)
    score, reasons = local_material_score(title, domain, body)

    if source_kind == "card":
        excerpt = body[:3500]
    else:
        # 优先保留视频笔记摘要，原始字幕只截一段，避免把模型带成逐字稿复述。
        body_without_subtitle = body.split("## 原始字幕")[0]
        excerpt = body_without_subtitle[:3500] if body_without_subtitle.strip() else body[:3500]

    return {
        "source_file": filepath.name,
        "title": title,
        "domain": domain,
        "audience": audience,
        "local_score": score,
        "score_reasons": reasons,
        "tags": extract_tags(fm),
        "date": fm.get("date", datetime.now().strftime("%Y-%m-%d")),
        "excerpt": clean_text(excerpt),
    }


def call_incubator(payload, draft=False):
    user_msg = {
        "content_signals": CONTENT_SIGNALS,
        "draft_required": draft,
        "material": payload,
        "editorial_goal": "把这条素材加工成可发表选题，不做搬运；优先生成有判断、有证据缺口、有钩子的内容胚胎。",
    }
    reply = call_mimo_chat(
        INCUBATION_PROMPT,
        json.dumps(user_msg, ensure_ascii=False, indent=2),
        temperature=0.45,
        max_tokens=6000,
    )
    return parse_json_object(reply)


def build_embryo_md(embryo, payload):
    hooks = embryo.get("hooks", [])
    evidence = embryo.get("evidence_to_add", [])
    outline = embryo.get("outline", [])
    platforms = embryo.get("platform_versions", {})
    score = embryo.get("publishability_score", "")
    domain = canonical_domain(embryo.get("domain", ""), payload["domain"])

    lines = [
        "---",
        f'title: "{embryo.get("title", payload["title"])}"',
        "type: 选题胚胎",
        f'domain: "{domain}"',
        f'audience: "{embryo.get("audience", payload["audience"])}"',
        f'source: "[[{payload["source_file"]}]]"',
        f'publishability_score: {score}',
        f'created: {datetime.now().strftime("%Y-%m-%d %H:%M")}',
        "status: incubated",
        "tags:",
        "  - 选题胚胎",
        f'  - 领域/{domain}',
        "---",
        "",
        f"# {embryo.get('title', payload['title'])}",
        "",
        f"> 来源：[[{payload['source_file']}]]",
        "",
        "## 读者与痛点",
        f"- 目标读者：{embryo.get('audience', payload['audience'])}",
        f"- 痛点：{embryo.get('pain', '')}",
        "",
        "## 新鲜观点",
        embryo.get("fresh_angle", ""),
        "",
        "## 核心立场",
        embryo.get("core_pov", ""),
        "",
        "## 钩子",
    ]
    for hook in hooks:
        lines.append(f"- {hook}")

    lines.extend(["", "## 还需要补的证据/实测"])
    for item in evidence:
        lines.append(f"- [ ] {item}")

    lines.extend([
        "",
        "## 最适合展示的结果",
        embryo.get("demo_or_result", ""),
        "",
        "## 内容结构",
    ])
    for i, item in enumerate(outline, 1):
        lines.append(f"{i}. {item}")

    lines.extend(["", "## 平台版本"])
    for platform, version in platforms.items():
        lines.append(f"- **{platform}**：{version}")

    lines.extend([
        "",
        "## 草稿骨架",
        embryo.get("draft_skeleton", ""),
        "",
        "## 爆款评分",
        f"- 分数：{score}",
        f"- 理由：{embryo.get('score_reason', '')}",
        f"- 风险：{embryo.get('risk', '')}",
        f"- 下一步：{embryo.get('next_action', '')}",
        "",
        "## 原素材摘录",
        payload.get("excerpt", "")[:1200],
    ])
    return "\n".join(lines) + "\n"


def select_incubation_sources(source, limit, from_idx=None, to_idx=None):
    if source == "auto":
        card_files = sorted([f for f in CARD_DIR.glob("*.md") if not f.name.startswith("_")])
        source = "cards" if card_files else "raw"

    if source == "cards":
        files = sorted([f for f in CARD_DIR.glob("*.md") if not f.name.startswith("_")])
        kind = "card"
    else:
        files = scan_transcripts()
        kind = "raw"

    selected = []
    for f in files:
        idx = extract_index(f.name)
        if from_idx and idx and idx < from_idx:
            continue
        if to_idx and idx and idx > to_idx:
            continue
        selected.append(f)

    # 原始素材默认按本地评分优先，卡片保持文件顺序。
    if kind == "raw":
        ranked = []
        for f in selected:
            title, _, body = get_title_from_file(f)
            domain = classify_domain(title, body)
            score, _ = local_material_score(title, domain, body)
            ranked.append((score, f))
        selected = [f for _, f in sorted(ranked, key=lambda x: x[0], reverse=True)]

    if limit and limit > 0:
        selected = selected[:limit]
    return kind, selected


def incubate_topics(limit=-1, source="auto", draft=False, force=False, from_idx=None, to_idx=None, dry_run=False):
    EMBRYO_DIR.mkdir(parents=True, exist_ok=True)
    kind, files = select_incubation_sources(source, limit, from_idx, to_idx)
    if not files:
        print("没有可孵化的素材")
        return

    print(f"孵化来源: {kind}")
    print(f"孵化数量: {len(files)}")
    print(f"输出目录: {EMBRYO_DIR}")
    if draft:
        print("模式: 生成草稿骨架")
    if dry_run:
        print("模式: dry-run（不调用模型，不写文件）")

    success = 0
    fail = 0
    for i, f in enumerate(files, 1):
        payload = material_payload(f, kind)
        source_hash = hashlib.md5(f.name.encode("utf-8")).hexdigest()[:8]
        safe = safe_filename(payload["title"])
        out_path = EMBRYO_DIR / f"{payload['date']}-选题胚胎-{safe}-{source_hash}.md"

        print(f"\n[{i}/{len(files)}] {payload['title']}")
        print(f"      领域: {payload['domain']}｜本地评分: {payload['local_score']}/10")

        if out_path.exists() and not force:
            print(f"      已存在，跳过: {out_path.name}")
            continue

        if dry_run:
            print(f"      目标读者: {payload['audience']}")
            print(f"      理由: {'、'.join(payload['score_reasons'])}")
            continue

        try:
            embryo = call_incubator(payload, draft=draft)
            md = build_embryo_md(embryo, payload)
            out_path.write_text(md, encoding="utf-8")
            print(f"      ✓ {out_path.name}")
            success += 1
        except Exception as e:
            print(f"      ✗ 失败: {e}")
            fail += 1

        if i < len(files) and not dry_run:
            time.sleep(1.5)

    print(f"\n孵化完成: 成功 {success}，失败 {fail}")


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
  %(prog)s --analyze-materials               分析素材领域分布
  %(prog)s --incubate 10                     生成10条选题胚胎
  %(prog)s --incubate 10 --draft             生成选题胚胎，并带发布草稿骨架
  %(prog)s --incubate-source raw --incubate 5 从原始素材孵化5条
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
    parser.add_argument('--analyze-materials', action='store_true', help='分析原始素材的领域分布')
    parser.add_argument('--incubate', nargs='?', const=-1, type=int, help='生成选题胚胎（可指定数量）')
    parser.add_argument('--incubate-source', choices=['auto', 'raw', 'cards'], default='auto', help='孵化来源：auto/cards/raw（默认auto）')
    parser.add_argument('--draft', action='store_true', help='孵化时生成更完整的发布草稿骨架')
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

    # ── 素材分析 ──
    if args.analyze_materials:
        analyze_materials()
        return

    # ── 选题孵化 ──
    if args.incubate is not None:
        incubate_topics(
            limit=args.incubate,
            source=args.incubate_source,
            draft=args.draft,
            force=args.force,
            from_idx=args.from_idx,
            to_idx=args.to_idx,
            dry_run=args.dry_run,
        )
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
