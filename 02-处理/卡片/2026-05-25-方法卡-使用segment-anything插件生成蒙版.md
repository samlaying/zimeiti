---
title: "使用segment anything插件生成蒙版"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-371-B站首推！2025最新版AIGC从入门到精通教程(Midjourney+StableDiffusion+ChatGPT).md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 方法卡
  - 主题/AI工具
  - 主题/电商设计
  - 素材/教程
related:
  - "[[AIGC电商模特换装工作流]]"
  - "[[图生图局部重绘换装法]]"
---

# 使用segment anything插件生成蒙版

在[[Stable Diffusion]]中，利用`segment anything`插件替代PS手动操作，自动生成用于局部重绘的蒙版：
1. **插件安装**：将插件地址复制到SD的“扩展”->“从网址安装”中，安装后重启SD。
2. **模型下载**：下载插件所需的SAM模型，并放入`\extensions\sd-webui-segment-anything\models\sam`目录，然后在插件界面刷新模型列表。
3. **生成蒙版**：
   - 上传原图（模特图）。
   - **标记区域**：
     - **左键单击（黑点）**：标记需要**保留**的区域（如服装）。
     - **右键单击（红点）**：标记需要**重绘**的区域（如背景、皮肤）。
   - 点击“生成模板”，系统会生成黑底白图的蒙版（白色区域即保留区域）。
   - 从多个预览图中选择效果最佳的一张，保存到本地。

> 来源：[[2026-05-25-371-B站首推！2025最新版AIGC从入门到精通教程(Midjourney+StableDiffusion+ChatGPT).md]]