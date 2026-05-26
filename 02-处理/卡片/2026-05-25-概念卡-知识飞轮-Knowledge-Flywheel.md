---
title: "知识飞轮（Knowledge Flywheel）"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-346-深度解析：如何让 OpenClaw Multi-Agent 系统实现自我发现、自修复与持续进化？.md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 主题/知识管理
  - 卡片/概念
related:
  - "[[定义量化指标（Metrics）]]"
  - "[[团队健康度（Team Health）]]"
---

# 知识飞轮（Knowledge Flywheel）

衡量多Agent系统知识沉淀与复用能力的指标，是系统持续学习和进化的关键。

通过两个子指标衡量：
1.  **知识检索次数**：Agent使用 `memory search` 的频率，代表知识复用。
2.  **经验写入次数**：Agent在任务结束后将本次经验写入 [[Memory]] 的频率，代表知识沉淀。

提升知识飞轮效率是推动系统自进化的下一步重点。

> 来源：2026-05-25-346-深度解析：如何让 OpenClaw Multi-Agent 系统实现自我发现、自修复与持续进化？.md