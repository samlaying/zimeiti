---
title: "Sandbox 与 Context Hub"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-030-🦜 LangChain Interrupt 2026｜9 大产品重磅发布 🚀.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 素材/教程
related:
  - "[[LangSmith Agent Builder 升级]]"
  - "[[托管深度智能体]]"
---

# Sandbox 与 Context Hub

**Sandbox（沙箱）正式版**与**Context Hub（上下文中心）** 是 [[LangSmith]] 平台为智能体提供生产环境支持的两大基础设施。

- **Sandbox**：由 LangSmith 团队自研，为执行 Skill（如脚本、API调用）提供安全、隔离的线上环境，是构建生产级智能体系统的必备基础。
- **Context Hub**：由原有的 `LangChain Hub`（用于管理 Prompt）升级而来，现在管理更广泛的“上下文”，包括 `Skills`、`Prompt`、`Agent Markdown` 等文件，并支持版本控制、分支、Fork和分享。

两者结合，为 Skill 的开发和线上运行提供了完整的生产环境支持，使得 [[LangSmith Agent Builder 升级]] 和 [[托管深度智能体]] 等功能具备了真正的生产级能力。

> 来源：2026-05-25-030-🦜 LangChain Interrupt 2026｜9 大产品重磅发布 🚀.md