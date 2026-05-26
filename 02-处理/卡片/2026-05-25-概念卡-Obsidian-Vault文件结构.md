---
title: "Obsidian Vault文件结构"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-309-Karpathy的Obsidian RAG + Claude Code = 作弊代码.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 主题/知识管理
  - 素材/教程
related:
  - "[[Obsidian RAG系统核心思想]]"
  - "[[Obsidian RAG工作流程]]"
---

# Obsidian Vault文件结构

系统建立在层次清晰的Obsidian Vault内：
- **Vault根目录**：整个知识库的根文件夹。
- **`raw`文件夹**：暂存原始研究资料（如Markdown文件、PDF），作为Wiki生成的“暂存区”。
- **`wiki`文件夹**：存放结构化Wiki文档，包含主题子文件夹（如`AI-agents`、`RAG-systems`）。
- **`master-index.md`文件**：位于`wiki`文件夹内，是所有Wiki主题的主索引列表。
- 每个Wiki文件夹内有索引文件和相互链接的文章。
> 来源：[[2026-05-25-309-Karpathy的Obsidian RAG + Claude Code = 作弊代码.md]]