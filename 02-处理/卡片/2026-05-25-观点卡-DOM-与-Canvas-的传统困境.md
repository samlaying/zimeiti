---
title: "DOM 与 Canvas 的传统困境"
card_type: 观点卡
layer: 处理
source: "[[2026-05-25-018-使用 HTML-in-Canvas API 构建下一代用户界面.md]]"
date: 2026-05-25
tags:
  - 卡片/观点
  - 主题/编程
  - 素材/观点
related:
  - "[[HTML-in-Canvas API：连接 DOM 与 Canvas 的桥梁]]"
---

# DOM 与 Canvas 的传统困境

传统 Web 开发中，DOM 和 Canvas 各有优势，但存在难以调和的困境：
1.  **DOM 优势**：提供开箱即用的出色 UI、文本布局解决方案，并与浏览器功能深度集成（文本选择、无障碍、翻译、深色模式等）。
2.  **Canvas 优势**：提供底层访问能力，支持高性能的 2D/3D 图形渲染，是游戏和复杂应用的理想选择。
3.  **困境**：在 Canvas 中渲染 UI 时，需要自行处理文本布局等逻辑，且**所有 DOM 附带的浏览器功能会完全失效**。
[[HTML-in-Canvas API：连接 DOM 与 Canvas 的桥梁]] 的诞生正是为了解决这一根本矛盾。

> 来源：[[2026-05-25-018-使用 HTML-in-Canvas API 构建下一代用户界面.md]]