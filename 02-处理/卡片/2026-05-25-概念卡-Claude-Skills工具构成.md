---
title: "Claude Skills工具构成"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-011-Claude skills｜30s从Excel到三层环形图.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 主题/Skills
  - 素材/教程
related:
  - "[[三层环形图生成步骤]]"
  - "[[Excel快速生成环形图案例]]"
---

# Claude Skills工具构成

**Claude Skills** 是一种自动化工具方案，用于实现特定任务。

其核心构成包含两部分：
1. 一个 `Skills.markdown` 文件，用于定义触发关键词和指令逻辑。
2. 一个通用的 `Python` 脚本，作为执行引擎。

**工作原理**：通过设定的触发词（如“[[三层环形图]]”）来激活，当用户提供相应输入（如Excel文件）时，会根据预设逻辑自动生成并执行一个定制化的Python脚本，从而完成复杂任务，如数据可视化。

> 来源：[[2026-05-25-011-Claude skills｜30s从Excel到三层环形图.md]]