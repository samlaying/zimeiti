---
title: "Knowledge Flywheel（知识飞轮）"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-346-深度解析：如何让 OpenClaw Multi-Agent 系统实现自我发现、自修复与持续进化？.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 主题/知识管理
  - 素材/观点
related:
  - "[[三步法实现多Agent系统自我进化]]"
  - "[[OA Dashboard系统监控]]"
---

# Knowledge Flywheel（知识飞轮）

**Knowledge Flywheel（知识飞轮）** 是衡量多智能体系统**知识沉淀与复用能力**的关键概念。它通过两个指标量化：
1. **知识检索次数**：任务执行中，agent调用memory search进行知识查询的频率。
2. **知识沉淀次数**：任务结束后，agent将本次经验写入memory的频率。

一个高效的知识飞轮能让系统从每次任务中学习，积累并复用知识，从而实现**持续进化**。当前许多系统此指标较低，是优化的重点方向。

> 来源：[[2026-05-25-346-深度解析：如何让 OpenClaw Multi-Agent 系统实现自我发现、自修复与持续进化？.md]]