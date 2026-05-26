---
title: "Agent Teams 与 Sub Agents 区别"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 素材/教程
related:
  - "[[Claude Agent Teams 并行通信原理]]"
---

# Agent Teams 与 Sub Agents 区别

**Sub Agents** 与 **Agent Teams** 的根本区别在于**通信拓扑结构**：
- **Sub Agents**：采用**星型拓扑**。各个子Agent**只能与主Agent通信**，子Agent之间**无法直接通信**。
- **Agent Teams**：采用**网状拓扑**。子Agent之间**可以相互通信**，同时也与主Agent相互通信，实现了**真正的并行工作**。

理解这一区别是有效利用两者优化工作流的关键。

> 来源：[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]