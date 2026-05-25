---
title: "AI智能体循环：状态机 vs. Generator"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-186-编程智能体开发必读？Codex与Claude Code全面剖析.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 素材/教程
related:
  - "[[Codex CLI：Rust系统工程]]"
  - "[[Claude Code：TypeScript产品路线]]"
---

# AI智能体循环：状态机 vs. Generator

[[Codex CLI]] 和 [[Claude Code]] 的Agent Loop（智能体循环）本质相同，但实现迥异：
- **Codex CLI：基于“轮次”(Turn)的状态机**
  - 每轮有明确的 **Turn Context**（包含模型、沙箱策略等）。
  - 流式返回时即开始执行工具，使用读写锁控制并发。**关键：所有工具执行结果在流结束时统一发出**，轮次边界是同步点。
- **Claude Code：基于Generator的异步流式循环**
  - 核心是异步Generator函数，通过`Yield`产出事件，循环更流畅。
  - 同样在流式传输期间执行工具。**关键：可以在其他工具执行时通过`yield`发出已完成的结果**，同步粒度更细，无硬性轮次边界。

> 来源：2026-05-25-186-编程智能体开发必读？Codex与Claude Code全面剖析.md