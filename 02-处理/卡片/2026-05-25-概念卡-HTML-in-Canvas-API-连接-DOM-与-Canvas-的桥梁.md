---
title: "HTML-in-Canvas API：连接 DOM 与 Canvas 的桥梁"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-018-使用 HTML-in-Canvas API 构建下一代用户界面.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/编程
  - 主题/浏览器自动化
  - 素材/概念
related:
  - "[[DOM 与 Canvas 的传统困境]]"
  - "[[API 的核心使用三阶段]]"
---

# HTML-in-Canvas API：连接 DOM 与 Canvas 的桥梁

HTML-in-Canvas API 是一项浏览器标准，允许将 DOM 元素直接绘制到 [[Canvas]]、WebGL 或 WebGPU 纹理中。
它的**核心作用**是作为一座桥梁，解决了传统开发中高性能图形与富功能 UI 之间的矛盾。
通过将 HTML 放在 `<canvas>` 标签内并更新元素变换，**内容不仅可交互，所有浏览器功能（如无障碍、翻译、页面内查找等）也能保持连接**，从而获得两全其美的效果。

> 来源：[[2026-05-25-018-使用 HTML-in-Canvas API 构建下一代用户界面.md]]