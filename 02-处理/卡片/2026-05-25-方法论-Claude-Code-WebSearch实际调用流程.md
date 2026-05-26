---
title: "Claude Code WebSearch实际调用流程"
note_type: 方法论
domain: AI工具/Skills
source: "[[2026-05-25-080-揭秘在Claude Code里WebSearch是如何搜索网页的.md]]"
date: 2026-05-25
reusable: "可用于技术分析、拆解AI产品架构、向他人解释Claude Code的工作原理。"
tags:
  - 原子笔记
  - 类型/方法论
  - 领域/AI工具/Skills
---

# Claude Code WebSearch实际调用流程

> 文档说一次，实际三次，表里不一的背后是精密的架构设计。

## 核心内容
文档描述WebSearch是单次API调用，但实际抓包发现是三次调用。首先主Agent（Opus）接收用户问题后输出工具调用指令；然后客户端开启新对话，让子Agent（Haiku）执行真正的网页搜索并返回加密结果和总结；最后将处理后的摘要（URL、标题、总结）返回给主Agent，由其组织最终回答。

## 原文关键段落
> 抓包（使用Claude Tab）显示，一次完整的WebSearch请求涉及**三次**API调用。

## 我的想法/延伸
<!-- 这是从"搬运"变成"原创"的分水岭。写下你的观点、联想、加工思路 -->


## 可复用场景
可用于技术分析、拆解AI产品架构、向他人解释Claude Code的工作原理。

> 来源：[[2026-05-25-080-揭秘在Claude Code里WebSearch是如何搜索网页的.md]]