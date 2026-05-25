---
title: "LangSmith Engine：自闭环智能体运维"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-030-🦜 LangChain Interrupt 2026｜9 大产品重磅发布 🚀.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 素材/教程
related:
  - "[[SmithDB：智能体专属数据库]]"
  - "[[LLM 网关统一模型管理]]"
  - "[[LangSmith Agent Builder 升级]]"
---

# LangSmith Engine：自闭环智能体运维

**LangSmith Engine** 是 [[LangSmith]] 平台的核心分析引擎，它整合了原有的 `Tracing`（追踪）、`Evaluation`（评估评测）和 `OpenSuite`（开源套件）能力。

其核心升级在于能够绑定用户的线上代码仓库，直接对代码进行分析，**诊断问题并自动提交修复的PR**。修复后，还会自动进行**评估**，判断修复效果，并建议是否需要进一步迭代。

结合 LangSmith 的生产监控能力，它实现了**7x24小时**的自动问题发现、诊断和修复，相当于一个强大的“后台守护伙伴”，自动进行代码维护和生产监控。

> 来源：2026-05-25-030-🦜 LangChain Interrupt 2026｜9 大产品重磅发布 🚀.md