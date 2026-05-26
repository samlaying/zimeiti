---
title: "Claude Agent Teams 并行通信原理"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 素材/教程
related:
  - "[[串行工作流是AI Agent效率瓶颈]]"
  - "[[Agent Teams 与 Sub Agents 区别]]"
---

# Claude Agent Teams 并行通信原理

**Agent Teams** 是 Claude 中实现并行工作的机制。其核心结构包括：
1. 一个**主Agent**（Team Leader）
2. 一个**共享的task list**
3. 多个**子Agent**

关键特性在于其**并行通信能力**：
- **子Agent之间**可以直接相互通信
- **子Agent与主Agent**之间也可以相互通信

这种多向通信网络使得多个子Agent能够同时处理不同的子任务，从而大幅提升整体工作效率。

> 来源：[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]