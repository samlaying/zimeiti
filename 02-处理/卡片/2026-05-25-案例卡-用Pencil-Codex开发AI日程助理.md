---
title: "用Pencil+Codex开发AI日程助理"
card_type: 案例卡
layer: 处理
source: "[[2026-05-25-043-实战推荐！Pencil + Codex 实现 AI 日程助理 App.md]]"
date: 2026-05-25
tags:
  - 卡片/案例
  - 主题/AI工具
  - 主题/编程
  - 素材/案例
related:
  - "[[agents.md 项目规范文件]]"
  - "[[Build iOS App 插件]]"
  - "[[Codex 的 Sub-Agents 并行审查]]"
---

# 用Pencil+Codex开发AI日程助理

这是一个完整的 **AI 辅助 iOS App 开发实战案例**：使用 Pencil 和 Codex 从零构建一个 AI 日程助理。

**核心开发流程：**
1.  **创建项目与规范**：在 Xcode 中新建项目，并创建 [[agents.md 项目规范文件]] 详细定义需求和技术细节。
2.  **UI 实现**：提供 [[Pencil 设计稿 (.pen)]]，使用 Codex 的 [[Build iOS App 插件]] 先完成 UI 部分，确保可交互和系统权限接入。
3.  **后端接入**：提供 [[OpenAPI AI友好型文档]]，指令 Codex 接入后端 AI 解析服务。
4.  **审查与调试**：利用 [[Codex 的 Sub-Agents 并行审查]] 代码，并解决编译错误和权限问题。
5.  **功能迭代**：根据测试结果，逐步添加跳转、删除等细节功能。

**关键启示：** 清晰的规范文件 (`agents.md`)、结构化的设计稿和 API 文档，以及善用 Agent 的规划与审查能力，是高效完成项目的关键。
> 来源：2026-05-25-043-实战推荐！Pencil + Codex 实现 AI 日程助理 App.md