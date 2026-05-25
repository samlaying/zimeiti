---
title: "OpenAPI AI友好型文档"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-043-实战推荐！Pencil + Codex 实现 AI 日程助理 App.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 主题/编程
  - 素材/教程
related:
  - "[[agents.md 项目规范文件]]"
---

# OpenAPI AI友好型文档

OpenAPI 文档是一种 **AI 友好型的接口文档格式**，常见为 `openapi.yaml` 或 `openapi.json` 文件。

**与普通API文档的区别：**
- **普通文档**：通常是网页或 Markdown 格式，主要供人类阅读。
- **OpenAPI文档**：结构化的 JSON/YAML 格式，方便 AI 编程工具 (如 [[agents.md 项目规范文件]] 中提及的 Codex) 直接解析和读取，以实现后端 API 接入。

**内容要素：** 定义 API 的名称、版本、访问路径、请求参数以及返回的 JSON 数据结构。提供此文档能让 AI 更准确、高效地生成或接入后端代码。
> 来源：2026-05-25-043-实战推荐！Pencil + Codex 实现 AI 日程助理 App.md