---
layer: 输入
input_type: 认知
type: 课程笔记
status: 定稿
source: "王建硕 · Claude Code Skills"
tags: [ClaudeCode, Skills, 视频剪辑, 自动化]
---
# 王建硕的 Claude Code Skills 详细笔记

## 一、背景与起源

### 起因
- 王建硕与任鑫在茶馆聊天，临时起意录制播客，约一个多小时
- 录完后重新激活了他多年的执念：**AI 自动剪辑视频**
- 五年前就开始没日没夜地写自动剪辑代码，效果一直不理想
- 这次有了 Claude Code，一个晚上就把视频剪辑的核心逻辑重写了一遍

### 重构经历
- 初始版本出现了「Skill 是新时代的函数」中提到的那种**代码崩坏感**——所有功能堆在一起，互相耦合
- 做了一轮重构：统一命名，拆分为 **15 个独立子 Skill** + 若干流水线 Skill
- 代码仓库：https://github.com/jianshuo/Claude-skills
 
---

## 二、Skill 系统基础知识

### 什么是 Skill
- 一个带 frontmatter 的 `SKILL.md` 文件 + 一组脚本
- 当用户的请求匹配 skill 描述里的触发词（如"翻译字幕"、"做封面"、"上传 YouTube"）时，Claude 会自动加载该 skill 并按流程执行

### SKILL.md 格式标准
- Anthropic 公开标准（2025 年 10 月发布）
- 2025 年 12 月被 OpenAI Codex 采纳
- 兼容平台：Claude Code、OpenAI Codex CLI、Cursor、Gemini CLI、Goose
- 第三方分发平台：ClawHub、SkillsMP（自动索引）

### 命名约定
- 所有 skill 以**动名词（V-ing）**开头
- 如 `transcribing-audio`、`dubbing-video`、`editing-multicam`
- 描述「正在做什么动作」，与 Claude 自动加载逻辑对齐
- 加 `wjs-` 前缀保持风格一致

### 设计哲学
> 一个 skill 想做的事情越少，它就越靠得住，也越容易跟别的 skill 接上。一个 skill 的名字，其实就是它对外的接口。

---

## 三、安装方式

### 方式一：从 ClawHub 装单个 skill
```bash
clawhub install wjs-transcribing-audio
```

### 方式二：作为 Claude Code marketplace
```bash
claude plugin marketplace add jianshuo/claude-skills
claude plugin install wjs-transcribing-audio
```

### 方式三：直接 clone 到 skills 目录
```bash
git clone https://github.com/jianshuo/claude-skills ~/.claude/skills/wjs
```

### 自动同步机制
- 通过 PostToolUse hook（`~/.claude/skills-publish-hook.sh`）自动 rsync 并推送到 GitHub
- 每次编辑 `wjs-*` skill，对应目录会自动同步

### 使用
- 自然语言触发：如「转写这个视频」、「做 SRT」
- 斜杠命令显式调用：如 `/wjs-transcribing-audio`
- 不需要重启 Claude Code，即时生效

---

## 四、15 个 Skill 详解（五组分类）

### 第一组：视频本地化——换一种语言（5 个）

这组构成一条完整的本地化流水线：**转写 → 翻译 → 配音 → 烧字幕**，每步独立可调用，也可通过编排器串联。

| # | Skill | 功能 | 输入 → 输出 |
|---|-------|------|------------|
| 1 | `wjs-transcribing-audio` | 音视频转字幕（原语言） | 视频/音频 → 同语言 SRT |
| 2 | `wjs-translating-subtitles` | 字幕翻译 + 标点重切 | A 语言 SRT → B 语言 SRT（或双语 SRT） |
| 3 | `wjs-dubbing-video` | 文本时间对齐 TTS 配音 | 视频 + 目标语 SRT → 配好音的视频 |
| 4 | `wjs-burning-subtitles` | 烧字幕 + 混音 + 最终合成 | 视频 + SRT + (可选)dub → 上传就绪 MP4 |
| 5 | `wjs-localizing-video` | 上面四步的总编排器 | 视频 + 目标语言 → 本地化视频 |

**技术细节：**
- **转写**：中文走豆包（Volcano）ASR，其他语言走 OpenAI Whisper word-level timestamps + 自行重组 cue
- **翻译**：所有 cue 按标点切分，保证每条字幕在句号/问号/感叹号处结束，避免句子被切到一半
- **配音**：按 voice ID 路由——中文走豆包 TTS，其他语言走 edge-tts neural；默认单说话人，可选多说话人多音色
- **烧字幕**：一次 ffmpeg 编码同时完成——烧字幕（libass）、混入 dub 音轨、原音降低作底噪。**不走级联**，避免多次重编码掉画质。Homebrew ffmpeg 不带 libass 时自动下载 evermeet 静态构建
- **编排器**：当用户说「完整本地化」时使用，单步需求直接调用上面四个之一

**使用场景举例：** 把一段中文播客变成带西语字幕甚至西语配音的视频。

---

### 第二组：长视频变短视频（3 个）

| # | Skill | 功能 | 输入 → 输出 |
|---|-------|------|------------|
| 6 | `wjs-segmenting-video` | 长视频按话题切片 + 裁剪 | 长视频 + SRT → 3–6 个独立短片 + 各自 SRT |
| 7 | `wjs-overlaying-video` | 后期：封面/字幕/动画/CTA | 短片 + SRT → 带后期的成片 |
| 8 | `wjs-reframing-video` | 横竖屏互转 + 说话人跟踪裁切 | 16:9 ↔ 9:16，4:3 ↔ 3:4 |

**技术细节：**
- **切片**：5 步流水线——① Agent 读 SRT 决定话题边界 → ② Stream-copy 切原视频（不重编码）→ ③ gpt-image-2 生成封面（标题烤进图里）→ ④ 封面作 1.5 秒 title card 拼到 clip 前面 → ⑤ libass 烧字幕。只做切+裁，后期交给下游
- **后期**：基于 **HyperFrames**（HTML/CSS 视频合成框架），一次最终编码里渲染所有元素，不做级联。包括：AI 生成封面首帧、HTML/CSS kinetic captions（逐词高亮、自定义字体）按 SRT 同步、hook moment 动画、章节 chip/片尾 CTA/lower-thirds
- **横竖屏互转**：裁切而非缩放或加黑边。用 **MediaPipe FaceLandmarker + 嘴部张合度方差**找真正在说话的人（不是最大或最 confident 的脸）。段落间硬切，不做 smooth pan。输出 `.crop.json` 记录裁切计划，原片不动

---

### 第三组：多机位剪辑（2 个）

这是王建硕五年前就开始做的执念，最终用 Claude Code 一个晚上实现的效果超越了之前几个月手写的结果。

| # | Skill | 功能 | 输入 → 输出 |
|---|-------|------|------------|
| 9 | `wjs-syncing-multicam` | 多机位音频互相关对齐 | N 个机位 → 每个机位一份 `.sync.json` |
| 10 | `wjs-editing-multicam` | 多机位自动剪辑（音量切机位） | 同步过的 N 个机位 → 单条 MP4 |

**技术细节：**
- **对齐关键设计——sidecar over re-encode**：不生成 `_synced.MOV`，只输出 `.sync.json` 元数据文件。原片永不被改写/复制/重编码。理由：75 分钟 3 机位 4K 拍摄 = 60+ GB，重编码会让磁盘翻倍且画质下降
- 下游用 `ffmpeg -itsoffset` 在消费侧应用偏移
- **自动剪辑**：决策完全由**每秒音频能量**驱动——哪个机位的麦最响就切到哪个。硬切（无 crossfade）+ 可选画中画小窗。音频取自被选中机位的麦，不做多麦克风 mix。不做人脸/取景识别

---

### 第四组：发布与分发（3 个）

| # | Skill | 功能 | 输入 → 输出 |
|---|-------|------|------------|
| 11 | `wjs-uploading-video` | 批量上传 YouTube | MP4 + UPLOAD_META.md → YouTube |
| 12 | `wjs-publishing-wechat` | 写/润色/发微信公众号 | 草稿文本 → HTML + 题图 + 解释图 + 上传草稿 |
| 13 | `wjs-promoting-skills` | 每日自动推广 skill | wjs-* skills → X tweet + outbox drafts |

**技术细节：**
- **YouTube 上传**：读 `UPLOAD_META.md` 获取 title/description/tags；支持 SOCKS/HTTP 代理，直接走 `requests` 做 resumable upload（绕开 `google-api-python-client` 的 `MediaFileUpload` 在代理下卡死的问题）。不支持微信视频号（无公开 API）/抖音/小红书/B站
- **公众号**：轻润色不重写，保留作者语气和节奏，只改错字、调段落、抚平拗口句子。自动生成标题候选、摘要、可粘贴到 mp.weixin.qq.com 的 HTML，通过 `md2wechat` 上传草稿
- **推广**：X 真发，Reddit/HN/Discord 只起草不自动发（不冒封号风险）。Idempotent + 节流：同一 skill 7 天内不重复推，每天最多 1 条 X。角度轮换：痛点→设计决策→串联工作流→最近更新，四个维度循环

---

### 第五组：非视频类（2 个）

| # | Skill | 功能 | 输入 → 输出 |
|---|-------|------|------------|
| 14 | `wjs-auditing-project` | 项目状态体检 | "看看哪里出问题了" → 分组 checklist |
| 15 | `wjs-eating-and-growing` | 5 步反思框架 | 吃亏的经历 → 堑+自动输出+旧参数+新参数+替代动作 |

**技术细节：**
- **项目体检**：硬性两阶段——先 read-only 巡检给出分组 checklist，用户确认后才动手。覆盖：未合并分支、停滞 PR、失败 GitHub Actions、过期 build、TODOS.md/ROADMAP 漂移、未发布 commit、日志 error。了解 Cathier iOS app 工作流（Xcode + fastlane + @claude PR auto-merge）
- **吃一堑长一智**：底层 L1/L2/L3 三层框架——L1（不知道）→ L2（知道但临场来不及）→ L3（本能赢了）。目标永远是 L3。一步一问不可跳，五步：①说清"堑"→②抓住自动输出→③挖旧参数→④定新参数→⑤给替代动作

---

## 五、额外配套 Skills

除核心 15 个外，README 还记录了以下辅助 skills：

| Skill | 功能 |
|-------|------|
| `wjs-picking-comments` | 抓取上一篇公众号精选留言 Top 5，生成 HTML footer 追加到新文章 |
| `wjs-converting-text-to-video` | 公众号文章 → 1080×1920 竖屏 30-90 秒解说短视频（TTS + 水彩背景 + GSAP 动画） |
| `wjs-tweeting-from-articles` | 从公众号文章萃取每日 X tweet，三条候选供挑选后真发 |
| `wjs-teaching-english` | 英语单词 → HLS "超剪"课程（word + IPA + 中文解释 + 真实视频片段） |
| `wangjianshuo-perspective` | 切换到王建硕视角写作与思考 |

---

## 六、核心设计理念总结

1. **单一职责**：每个 skill 只做一件事，做好做透
2. **动名词命名**：名字即接口，描述动作而非状态
3. **Sidecar over re-encode**：尽量不动原始素材，元数据文件记录处理计划
4. **不走级联**：最终合成一次编码完成，避免多次重编码掉画质
5. **可组合**：独立 skill 可单独调用，也可通过编排器串联成完整流水线
6. **触发词驱动**：自然语言匹配即可激活，无需记住命令

---

## 七、实际使用场景

王建硕描述的实际工作流（播客那次）：

> "把这个录音转成字幕 → 切成四条短视频 → 第二条横转竖 → 给它们加封面和字幕 → 把讲 AI 教育那段配上西语 → 全部传到 YouTube。"

视频比较大，烧制约 5 小时，睡醒就做好了。