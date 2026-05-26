---
title: "Stable Diffusion图生图局部重绘"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-371-B站首推！2025最新版AIGC从入门到精通教程(Midjourney+StableDiffusion+ChatGPT).md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 主题/电商
  - 素材/教程
  - 卡片/方法
related:
  - "[[segment anything插件]]"
  - "[[ControlNet控制网辅助]]"
---

# Stable Diffusion图生图局部重绘

一种用于AI换装换背景的核心方法，核心是“保留服装，重绘其余部分”。

**核心步骤**：
1.  **制作蒙版**：使用[[segment anything插件]]，通过点选黑点（保留区域，如服装）和红点（重绘区域，如背景、皮肤），自动生成黑白蒙版。
2.  **局部重绘设置**：在SD的“图生图”功能中，选择“局部重绘（上传蒙版）”模式。关键参数设置：
    - **重绘区域**：选择“非蒙版区域”。
    - **宽高**：必须与原图尺寸一致。
    - 迭代步数可调至30左右。
3.  **辅助控制**：为提升效果，需启用[[ControlNet控制网辅助]]，使用“Canny”等模型识别原图线稿，以更好地保留服装细节。
> 来源：2026-05-25-371-B站首推！2025最新版AIGC从入门到精通教程(Midjourney+StableDiffusion+ChatGPT).md