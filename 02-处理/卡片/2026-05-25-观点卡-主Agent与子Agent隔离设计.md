---
title: "主Agent与子Agent隔离设计"
card_type: 观点卡
layer: 处理
source: "[[2026-05-25-080-揭秘在Claude Code里WebSearch是如何搜索网页的.md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 卡片/观点
  - 素材/观点
related:
  - "[[上下文隔离：节省成本与注意力]]"
  - "[[攻击面隔离：防止提示词注入]]"
  - "[[WebSearch实际工作流程]]"
  - "[[子Agent是执行脏活的手脚]]"
---

# 主Agent与子Agent隔离设计

Claude Code的WebSearch采用“主Agent（Opus）规划 + 子Agent（Haiku）执行”的多层架构，这是一种精心设计的隔离策略。其核心设计哲学是：
> 使用昂贵的、强大的模型（Opus）作为主脑进行规划和总结，使用廉价、快速的模型（Haiku）作为“手脚”去执行具体的、可能含有不可信内容的脏活。所有潜在的脏活和不可信内容都隔离在子Agent里。

这种隔离主要服务于两个关键目标：
1.  [[上下文隔离：节省成本与注意力]]
2.  [[攻击面隔离：防止提示词注入]]

具体实现可参考[[WebSearch实际工作流程]]。隔离的子Agent使得系统能够安全地调用如`web_search`这类[[LLM中的工具类型]]中的服务器端工具。

> 来源：[[2026-05-25-080-揭秘在Claude Code里WebSearch是如何搜索网页的]]