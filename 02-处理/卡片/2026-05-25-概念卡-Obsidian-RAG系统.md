---
title: "Obsidian RAG系统"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-309-Karpathy的Obsidian RAG + Claude Code = 作弊代码.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 主题/知识管理
related:
  - "[[传统RAG系统]]"
  - "[[云指令文件cloud.md]]"
  - "[[文件结构设计]]"
---

# Obsidian RAG系统

Karpathy提出的基于[[Obsidian]]和[[Claude Code]]的轻量级知识管理系统。它不使用向量数据库或嵌入模型，而是通过巧妙的文件结构（如`raw`和`wiki`文件夹）和Markdown的[[Wiki链接]]功能，结合LLM的文件导航能力，模拟传统[[传统RAG系统]]的检索增强生成功能。

**核心优势**：轻量、免费、结构透明、适合个人或小团队处理中等规模文档。

> 来源：[[2026-05-25-309-Karpathy的Obsidian RAG + Claude Code = 作弊代码.md]]