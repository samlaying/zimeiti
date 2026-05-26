---
title: "ControlNet控制网辅助"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-371-B站首推！2025最新版AIGC从入门到精通教程(Midjourney+StableDiffusion+ChatGPT).md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 素材/教程
  - 卡片/概念
related:
  - "[[Stable Diffusion图生图局部重绘]]"
  - "[[OpenPoseEditor姿势控制]]"
---

# ControlNet控制网辅助

Stable Diffusion的一个强大插件，用于通过外部参考图（如线稿、姿势图）精确控制AI图像的生成，极大提升可控性。

在[[Stable Diffusion图生图局部重绘]]流程中，常使用“Canny”模型来识别原图线稿，以更好地保留服装等细节。在[[OpenPoseEditor姿势控制]]流程中，则使用“OpenPose”模型来控制生成人物的姿势。

**使用要点**：需启用“完美像素”，并根据任务选择合适的预处理器和模型。多个控制单元间可通过调整权重来平衡影响力。
> 来源：2026-05-25-371-B站首推！2025最新版AIGC从入门到精通教程(Midjourney+StableDiffusion+ChatGPT).md