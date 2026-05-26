---
title: "Obsidian RAG工作流程"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-309-Karpathy的Obsidian RAG + Claude Code = 作弊代码.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 主题/知识管理
  - 素材/教程
related:
  - "[[Obsidian RAG系统核心思想]]"
  - "[[Obsidian Vault文件结构]]"
  - "[[Obsidian RAG设置实操]]"
---

# Obsidian RAG工作流程

**工作流程**分为三步：
1. **数据摄取**：将文章、论文等原始数据放入Obsidian Vault的`raw`文件夹。
2. **人工/LLM处理**：使用[[Claude Code]]处理原始数据，生成结构化的Wiki文档到`wiki`文件夹。
3. **查询与问答**：通过[[Claude Code]]针对生成的Wiki进行提问，模拟RAG检索。
> 来源：[[2026-05-25-309-Karpathy的Obsidian RAG + Claude Code = 作弊代码.md]]