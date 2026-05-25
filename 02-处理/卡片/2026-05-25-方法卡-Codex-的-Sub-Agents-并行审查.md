---
title: "Codex 的 Sub-Agents 并行审查"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-043-实战推荐！Pencil + Codex 实现 AI 日程助理 App.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 素材/教程
---

# Codex 的 Sub-Agents 并行审查

在 Codex 中，可以启用 **Sub-Agents** (子智能体) 功能来并行审查代码，提高效率并避免上下文污染。

**工作流程：**
1.  主线程 (主 Agent) 将审查任务 (如“审查后端 API 接入部分”、“检查本地持久化逻辑”) 分配给多个 Sub-Agents。
2.  每个 Sub-Agent 在独立的上下文中并行执行审查任务。
3.  审查结果返回主线程，主线程综合结果或下达进一步指令。

**优势：**
- **上下文隔离**：各 Sub-Agent 的对话历史互不干扰，避免信息混乱。
- **并行处理**：多个任务同时进行，缩短审查时间。
- **灵活配置**：可以为不同 Sub-Agent 选择不同的模型 (如 GPT-5.4 mini)。
> 来源：2026-05-25-043-实战推荐！Pencil + Codex 实现 AI 日程助理 App.md