---
title: "CloudTrace工具"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-116-解密Claude Code和Anthropic后端是如何通信.md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 卡片/概念
  - 素材/工具
related:
  - "[[CC History工具]]"
  - "[[Claude Code请求结构]]"
---

# CloudTrace工具

## CloudTrace

**定义**：一个由Mario Zegner（Pi框架作者）开发的命令行工具，用于拦截[[Claude Code]]与Anthropic服务器之间的所有API流量，记录请求与响应，并生成一个可分析的HTML报告文件。

**核心功能**：
- **流量拦截**：通过拦截[[Claude Code]]的Fetch函数来捕获所有通信内容。
- **报告生成**：将拦截到的完整通信记录（请求与响应）保存为HTML文件，便于在浏览器中查看和分析。

**使用方法**：
1. 将`claude`命令替换为`cloudtrace`。
2. 添加`include all requests`参数以记录所有请求。
3. 正常进行对话交互。
4. 退出后自动生成HTML分析报告。

> 来源：[[2026-05-25-116-解密Claude Code和Anthropic后端是如何通信]]