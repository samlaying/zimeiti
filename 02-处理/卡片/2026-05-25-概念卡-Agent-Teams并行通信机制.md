---
title: "Agent Teams并行通信机制"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
related:
  - "[[Sub Agents串行通信限制]]"
  - "[[配置Agent Teams方法]]"
---

# Agent Teams并行通信机制

Agent Teams是一种AI工作流机制，通过主Agent（Team Leader）和多个子Agent并行通信来提高效率。与[[Sub Agents串行通信限制]]不同，子Agent之间可以相互通讯，并与主Agent通讯，实现并行工作，从而解决串行工作流的瓶颈。
> 来源：[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]