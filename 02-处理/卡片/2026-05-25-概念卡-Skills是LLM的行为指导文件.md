---
title: "Skills是LLM的行为指导文件"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-012-《浅入深出》Agent系列之十一：Skills原理解析.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/Skills
  - 主题/AI工具
related:
  - "[[Skills内容结构]]"
  - "[[Skills作用]]"
  - "[[AgentOS与Skills类比]]"
---

# Skills是LLM的行为指导文件

在[[Agent]]系统中，**Skills** 是用于指导[[LLM]]（大型语言模型）行为的结构化文本文件，通常是Markdown格式。它本质上不是代码，而是一份描述“如何做某事”的指令清单。

*   **为什么是“Skills”而非“能力”？** 虽然“能力”是常见译法，但在大模型上下文中没有完美对应，因此直接沿用英文术语。
*   **核心目的**：固化[[LLM]]的思考与行动流程，避免其自由发挥导致错误，提升[[tool calling]]的准确性和效率。

> 来源：2026-05-25-012-《浅入深出》Agent系列之十一：Skills原理解析.md