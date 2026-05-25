---
title: "Auto Mode Classifier"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-089-🧲 Claude Code 自动：长程任务的保障 Auto Mode.md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 主题/编程
  - 卡片/概念
related:
  - "[[Claude Code Auto Mode]]"
---

# Auto Mode Classifier

**Auto Mode Classifier（自动模式分类器）** 是 [[Claude Code Auto Mode]] 背后的核心安全机制。它运行在独立的服务器配置上，负责评估每个操作的安全性。

- **安全操作**：直接执行，日志显示 `allowed by auto mode classifier`。
- **危险操作**：会被拦截（`denied`），分类器会**主动中断任务**并询问用户下一步指示。

该分类器基于一套**可自定义的规则**运行，本地配置的规则会与线上的分类器互动，共同决定操作是否被允许。注意，运行分类器会产生**额外的Token消耗和费用**。

> 来源：2026-05-25-089-🧲 Claude Code 自动：长程任务的保障 Auto Mode.md