---
title: "OpenPoseEditor姿势控制"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-371-B站首推！2025最新版AIGC从入门到精通教程(Midjourney+StableDiffusion+ChatGPT).md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 素材/教程
  - 卡片/方法
related:
  - "[[ControlNet控制网辅助]]"
---

# OpenPoseEditor姿势控制

用于控制AI生成人物姿势的进阶方法。通过编辑骨骼图来自定义模特的展示姿态。

**核心工具**：`OpenPoseEditor` 插件。
**工作流程**：
1.  **提取姿势**：在[[ControlNet控制网辅助]]中，使用“OpenPose”预处理器提取原图的人物骨骼图。
2.  **编辑姿势**：将骨骼图发送至 `OpenPoseEditor` 插件，手动调整各个骨骼点（如手部、腿部）至目标姿势。
3.  **应用生成**：将编辑好的姿势图发回 ControlNet 进行生成。

**关键技巧**：当同时使用多个 ControlNet 单元（如 Canny 控制线稿+OpenPose 控制姿势）时，需通过调整**权重**来平衡两者的影响。
> 来源：2026-05-25-371-B站首推！2025最新版AIGC从入门到精通教程(Midjourney+StableDiffusion+ChatGPT).md