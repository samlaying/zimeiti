---
title: "Obsidian RAG设置实操"
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
  - "[[Obsidian Vault文件结构]]"
  - "[[Obsidian RAG工作流程]]"
---

# Obsidian RAG设置实操

**设置步骤**：
1. **安装Obsidian**：从obsidian.md下载，创建新Vault。
2. **初始化文件结构**：使用[[Claude Code]]在Vault中创建`raw`和`wiki`文件夹，并配置`cloud.md`系统提示文件（指导LLM如何遍历知识库）。
3. **配置数据摄入工具**：安装Obsidian网页剪藏器（设置Note location为`raw`）和社区插件`Local Images Plus`（确保图片本地保存）。
4. **使用系统**：手动剪藏网页到`raw`，用[[Claude Code]]生成Wiki和查询。
> 来源：[[2026-05-25-309-Karpathy的Obsidian RAG + Claude Code = 作弊代码.md]]