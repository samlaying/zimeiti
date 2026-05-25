---
title: "Codex CLI：Rust系统工程"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-186-编程智能体开发必读？Codex与Claude Code全面剖析.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/编程
  - 素材/教程
related:
  - "[[沙箱 vs. 审批：两种AI编程智能体哲学]]"
  - "[[Claude Code：TypeScript产品路线]]"
  - "[[工具哲学：少而精 vs. 多而专]]"
---

# Codex CLI：Rust系统工程

**OpenAI Codex CLI** 是AI编程智能体的“系统工程”路线代表，其技术选型如下：
- **语言**：Rust。
- **结构**：一个包含81个Crate的庞大单体仓库（monorepo），模块划分清晰（CLI、TUI、核心组件、沙箱环境等），编译器强制执行模块边界。
- **分发**：编译为**静态链接的原生二进制文件**。NPM包仅为平台检测的“包装器”。
- **API**：使用 OpenAI Responses API，支持 SSE 和 WebSocket（有连接池和预热）。

其核心安全支柱是 [[安全基石：内核沙箱 vs. 模型审查|内核级沙箱]]，工具设计则贯彻了 [[工具哲学：少而精 vs. 多而专|“少而精”]] 的哲学。

> 来源：2026-05-25-186-编程智能体开发必读？Codex与Claude Code全面剖析.md