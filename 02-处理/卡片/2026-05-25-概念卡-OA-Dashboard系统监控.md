---
title: "OA Dashboard系统监控"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-346-深度解析：如何让 OpenClaw Multi-Agent 系统实现自我发现、自修复与持续进化？.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 素材/教程
related:
  - "[[三步法实现多Agent系统自我进化]]"
  - "[[Crown Job可靠性]]"
  - "[[Knowledge Flywheel（知识飞轮）]]"
---

# OA Dashboard系统监控

**OA Dashboard（Operational Analytics and Dashboard）** 是实现多智能体系统**可观测性**的监控面板，实时展示系统健康状态。其核心监控指标包括：
- **[[Crown Job可靠性]]**：衡量系统主动性。
- **自我修复率（Fix Rate）**：衡量系统自动发现问题并修复的能力。
- **Team Health（团队健康度）**：关注agent的memory使用和上下文管理效率。
- **[[Knowledge Flywheel（知识飞轮）]]**：衡量知识积累与复用。
- **Prompt Size by Agent**：监控加载文件大小，识别可优化为Skill的流程。

Dashboard数据波动会自动触发系统的自我检测与修复闭环。

> 来源：[[2026-05-25-346-深度解析：如何让 OpenClaw Multi-Agent 系统实现自我发现、自修复与持续进化？.md]]