---
title: "Claude Code：TypeScript产品路线"
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
  - "[[Codex CLI：Rust系统工程]]"
  - "[[工具哲学：少而精 vs. 多而专]]"
---

# Claude Code：TypeScript产品路线

**Anthropic Claude Code** 是AI编程智能体的“产品与应用”路线代表，其技术选型如下：
- **语言**：TypeScript。
- **结构**：单体包结构，拥有自定义的、基于 React 和 React Ink 的终端渲染器（非原版Ink）。
- **分发**：推荐使用**原生二进制安装，支持自动更新**。
- **API**：使用 Anthropic Messages API，仅支持 SSE。但拥有完善的**prompt缓存机制**（分静态/动态部分）以节省成本。

其核心安全支柱是 [[安全基石：内核沙箱 vs. 模型审查|大模型分类器+审批流程]]，工具生态则体现了 [[工具哲学：少而精 vs. 多而专|“多而专”]] 的设计。

> 来源：2026-05-25-186-编程智能体开发必读？Codex与Claude Code全面剖析.md