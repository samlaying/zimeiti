---
title: "BrowserHannis"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-007-AI 操控浏览器，最省 token 的一条路.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 主题/浏览器自动化
related:
  - "[[AI浏览器操控四路径对比]]"
  - "[[BrowserHannis工作原理]]"
  - "[[BrowserHannis实操步骤]]"
---

# BrowserHannis

**BrowserHannis** 是一个由 [[BrowserUse]] 团队开发的、专为 AI Agent 设计的浏览器操控工具仓库。其核心特点是**代码量极小**（约600-800行Python）且**Token消耗极低**。

- **实现方式**：通过WebSocket直接控制Chrome内核，使用原生CDP（Chrome DevTools Protocol）。
- **市场反馈**：在GitHub上线15天即获得9400个Star。
- **核心理念**：与为人类设计的工具不同，它是为 AI “量身定做”的，将判断力从框架转移到了模型本身。

> 来源：2026-05-25-007-AI 操控浏览器，最省 token 的一条路.md