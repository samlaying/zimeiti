# AI Lifelog 项目方案：低资源每日截图工作日志

## 项目定位

做一个面向个人效率和作品集展示的桌面工具：自动、低打扰地记录我每天在电脑上做了什么，并在一天结束后生成一份 AI 工作日志。

它不是全量录屏工具，而是一个“轻量屏幕记忆 + AI 日报”工具：

- 自动截图记录工作上下文
- 自动识别应用、窗口标题、时间段和可能的任务
- 用 AI 生成每日总结、时间分布、关键成果和待办线索
- 本地优先存储，保护隐私
- UI 做成高颜值时间线，可作为项目展示

## 参考项目研究

### screenpipe

screenpipe 是最完整的开源屏幕记忆底座。它的核心思路是把屏幕、音频、本地存储和 AI 串起来，形成可搜索的个人记忆。它强调本地、私密、可扩展，并提供 MCP、REST API、插件系统。

值得借鉴：

- 不做简单定时全量录制，而是事件驱动采集
- 使用 OCR、accessibility tree、音频转录组合还原上下文
- 支持自然语言搜索和 AI agent
- 有明确的隐私权限和过滤机制

不建议照搬：

- 功能太重，资源占用目标是 0.5-3GB RAM，不适合作为轻量作品集 MVP
- 音频、MCP、插件系统可以作为未来扩展，不应放进第一版

### Dayflow

Dayflow 最接近目标产品：自动工作日志、本地优先、时间线、日报/周报、自然语言提问。它的关键亮点是从“窗口打开了什么”上升到“我实际完成了什么”。

值得借鉴：

- 每日 standup：昨天亮点、今天任务、阻碍
- 和工作日志对话
- 周复盘：专注模式、分类、应用使用、交互图
- 自动清理旧截图，控制磁盘
- 支持本地模型、Gemini、ChatGPT、Claude 等 AI provider

不建议照搬：

- 先不做完整 work journal chat
- 先不做复杂音频/会议分析
- 先聚焦一个好看的 daily timeline 和 AI summary

### Familiar

Familiar 的重点不是做完整产品，而是把屏幕观察结果变成 AI 可用的 markdown 上下文。它会截图、OCR、生成 markdown，并清理敏感信息。

值得借鉴：

- 截图只是中间产物，最终沉淀为结构化文本
- 图片可设置短期保留，文本长期保留
- 做敏感信息过滤，如 password、API key、credit card
- 输出成 markdown，很适合 Obsidian 和作品集展示

不建议照搬：

- 它更像 agent memory 层，不是完整的个人时间管理产品
- 作品集展示需要更强的可视化界面

### ActivityWatch

ActivityWatch 是成熟的自动时间追踪底座，记录活跃应用、窗口标题、浏览器标签、键鼠活动和 AFK 状态。它不 AI-first，但非常适合做低资源采集。

值得借鉴：

- active app + window title 比截图便宜很多
- AFK 检测可以避免记录无意义空闲时间
- watcher 架构清晰，可扩展不同数据源
- 用户拥有本地数据

不建议照搬：

- UI 和 AI 体验不够适合作品集展示
- 需要补上截图视觉证据和 AI 总结层

## 产品名称候选

- DayTrace
- FocusFrame
- TimeLens
- Recallite
- SnapLog
- ChronoFrame

推荐：TimeLens。含义清楚，适合展示“用 AI 透视一天”。

## MVP 功能范围

### 1. 自动低资源截图

第一版只做桌面端。

采集策略：

- 默认每 60 秒检查一次当前窗口
- 只有在以下情况截图：
  - 当前应用变化
  - 窗口标题变化
  - 用户从 AFK 返回
  - 距离上次有效截图超过 5 分钟
  - 手动点击“记录此刻”
- 对截图做 perceptual hash，重复度过高则丢弃
- 截图保存为 WebP 或 JPEG，宽度压缩到 1280px
- 同时生成 320px 缩略图用于时间线

资源目标：

- 常驻内存：低于 150MB
- 后台 CPU：空闲时低于 1%
- 每日存储：100-300MB
- 默认保留截图 7 天，长期保留 OCR/AI 摘要

### 2. 本地数据结构

使用 SQLite。

核心表：

- captures：截图事件
- sessions：连续工作片段
- summaries：AI 日报/周报
- app_rules：应用分类规则
- privacy_rules：隐私过滤规则

capture 字段：

- id
- timestamp
- app_name
- window_title
- image_path
- thumb_path
- phash
- ocr_text
- inferred_category
- inferred_task
- is_sensitive

session 字段：

- start_time
- end_time
- app_name
- category
- task_title
- capture_count
- representative_capture_id

### 3. AI 每日总结

AI 不要每张图实时分析，太耗资源也太贵。建议晚上统一批处理：

- 先按应用/窗口/相似截图聚类
- 每个 session 选 1-3 张代表截图
- OCR 文本 + 窗口标题 + 时间段输入给模型
- 输出 daily report

日报结构：

- 今日概览
- 时间分布
- 主要完成事项
- 注意力漂移
- 高频上下文
- 明日建议
- 可复制到 Obsidian 的 markdown

模型策略：

- 默认：OpenAI-compatible API
- 隐私模式：Ollama 本地模型
- 演示模式：内置 mock 数据，不需要真实截屏

### 4. 高颜值 UI

作品集展示重点是第一屏和时间线。

核心页面：

- Dashboard：今日总览
- Timeline：截图时间线
- Report：AI 日报
- Search：自然语言搜索
- Privacy：隐私规则

视觉方向：

- 深浅色双主题
- 类 Linear / Raycast / Arc 风格
- 左侧紧凑导航，右侧主内容
- 时间线用横向时间轴 + 截图卡片
- 每个 session 显示 app icon、任务标题、时长、代表截图
- AI 日报做成漂亮的 editorial report，而不是普通文本框

关键展示动效：

- 截图卡片 hover 放大
- 时间线滚动吸附
- AI 总结生成时 skeleton shimmer
- 今日时间分布使用环形图或 stacked bar

## 技术栈建议

### 推荐方案：Tauri + React + Rust

原因：

- 比 Electron 更轻，内存占用更适合“不要占太大内存”
- Rust 适合做后台采集、压缩、SQLite
- React 适合快速做高颜值作品集 UI
- 跨平台潜力好

建议技术：

- Tauri 2
- React + TypeScript
- Tailwind CSS
- shadcn/ui 或 Radix UI
- SQLite
- Rust screenshots crate / platform API
- image crate 做压缩
- fast_image_resize
- ocr 可先用系统 OCR 或后置服务

### 替代方案：SwiftUI macOS only

如果第一版只做 Mac，SwiftUI 会更原生、更省资源。但跨平台和 Web 展示成本更高。

## 低资源关键设计

### 不做全量录屏

全量录屏会导致：

- 存储爆炸
- CPU/GPU 占用持续偏高
- AI 分析成本不可控
- 隐私压力大

应采用“事件触发 + 稀疏截图 + 文本长期保存”。

### 图片短期保存，文本长期保存

推荐保留策略：

- 原图：7 天
- 缩略图：30 天
- OCR 文本：永久
- AI 摘要：永久

这样既能展示视觉时间线，又不会让磁盘无限膨胀。

### 先 metadata，后 AI

后台常驻只做便宜操作：

- 当前 app
- 当前 window title
- AFK 状态
- 截图去重
- 图片压缩

AI 分析只在：

- 用户手动点击
- 每日固定时间
- 电脑空闲时

## 隐私设计

必须做，因为截图工具天然敏感。

第一版要有：

- 暂停记录按钮
- 隐私应用黑名单，如 1Password、银行、微信、邮箱
- 窗口标题关键词过滤
- 敏感截图自动打码或不保存
- 本地数据目录可清理
- AI 发送前预览

作品集展示时可以强调：

- Local-first
- User-owned data
- Screenshot retention policy
- Sensitive app filtering
- Optional local model

## 项目展示卖点

一句话：

> TimeLens is a lightweight AI work journal that turns sparse screenshots into a beautiful daily timeline and private productivity report.

中文：

> TimeLens 是一个轻量 AI 工作日志工具，通过低频、去重、隐私友好的截图采样，把一天的电脑活动整理成漂亮的时间线和日报。

作品集亮点：

- 系统级桌面采集
- 低资源后台设计
- 图像去重和存储压缩
- 本地 SQLite 数据建模
- AI 批处理总结
- 隐私过滤机制
- 高颜值数据可视化 UI

## 开发路线

### Week 1：可运行采集器

- Tauri 项目初始化
- 后台定时检测当前应用和窗口标题
- 截图保存到本地目录
- SQLite 记录 capture
- UI 显示今日截图列表

### Week 2：低资源优化

- perceptual hash 去重
- 图片压缩和缩略图
- AFK 检测
- 应用黑名单
- 自动清理旧截图

### Week 3：AI 日报

- session 聚类
- 代表截图选择
- OCR 文本提取
- AI summary prompt
- 导出 markdown

### Week 4：作品集打磨

- Dashboard
- Timeline
- Report 页面
- 示例数据演示模式
- README、架构图、demo 视频

## MVP 不做什么

第一版先不做：

- 24 小时音频录制
- 实时视频回放
- 多设备同步
- 团队管理
- 完整 MCP server
- Agent 自动操作电脑
- 浏览器插件

这些都很酷，但会让项目变重。

## 推荐最终形态

做成一个轻量、漂亮、可演示的 Mac/Windows 桌面 app：

- 后台只做低频截图和 metadata 采集
- 白天几乎不打扰
- 晚上生成 AI 日报
- 每天有一条漂亮的“我今天做了什么”时间线
- 可导出到 Obsidian

这个方向比单纯复刻 screenpipe 更适合个人项目展示，因为它有明确边界、工程亮点和视觉亮点。
