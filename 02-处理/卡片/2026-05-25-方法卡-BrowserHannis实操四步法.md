---
title: "BrowserHannis实操四步法"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-007-AI 操控浏览器，最省 token 的一条路.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 主题/浏览器自动化
  - 素材/教程
related:
  - "[[BrowserHannis]]"
  - "[[Token消耗对比]]"
---

# BrowserHannis实操四步法

使用 [[BrowserHannis]] 进行浏览器操控（例如，让GMI生图）的基本步骤：

1.  **安装**：安装 Git、Chrome 和 UV Tools（使用 `UV Tools Install` 命令）。
2.  **连接 Chrome**：需要打开 Chrome 的远程调试功能，以便 BrowserHannis 通过 WebSocket 连接。**优势**：能连接用户正在使用的浏览器，复用现有的cookie和登录状态。
3.  **执行任务**：通过控制端（如CC）操控浏览器执行具体操作（例如，调用订阅版GMI/Gemini进行图片生成）。
4.  **封装技能**：将成功的操作流程封装成可复用的技能，便于未来调用。

> 来源：2026-05-25-007-AI 操控浏览器，最省 token 的一条路.md