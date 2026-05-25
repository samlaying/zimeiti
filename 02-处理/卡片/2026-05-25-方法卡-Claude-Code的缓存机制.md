---
title: "Claude Code的缓存机制"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-116-解密Claude Code和Anthropic后端是如何通信.md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 卡片/方法
  - 素材/教程
related:
  - "[[理解Claude Code请求结构]]"
  - "[[Token消耗分析]]"
---

# Claude Code的缓存机制

## Claude Code的缓存机制

[[Claude Code]]通过巧妙的设计来优化Token成本和响应效率。

**核心机制**：
1.  **缓存切割点**：在请求的`Messages`字段中，**用户实际输入**（如“hello”）被标记为`cache control`（一小时过期），作为缓存分界点。**该点之前的所有注入内容**（Hooks、工具清单、MCP指南、Skills、Cloud.md）可以被缓存和复用。
2.  **Token消耗结构**：以“hello”为例，其Token消耗构成为：
    - `Input Token`（用户输入）：~6
    - `Cache Creation Input Token`（新写入缓存的内容）：~14000
    - `Cache Read Input Token`（从已有缓存读取的内容）：~16000
    - **总计**：~31000 Token
3.  **成本优化**：缓存读取（`Cache Read`）比正常输入便宜**90%**。因此，在连续对话中，大部分系统提示词和工具定义的Token成本通过缓存复用得以大幅降低，费用不会线性增长。

> 来源：[[2026-05-25-116-解密Claude Code和Anthropic后端是如何通信]]