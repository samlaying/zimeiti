---
title: "设置Obsidian RAG系统"
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
  - "[[Obsidian RAG系统]]"
  - "[[数据摄入工具配置]]"
  - "[[生成与查询Wiki]]"
---

# 设置Obsidian RAG系统

搭建Karpathy式Obsidian知识管理系统的主要步骤：
1.  **初始化**：下载并安装[[Obsidian]]，创建一个新的Vault文件夹。
2.  **创建文件结构**：在Vault目录下使用[[Claude Code]]，通过提示词创建`raw`（原始数据暂存区）和`wiki`（结构化知识区）文件夹，以及`master-index.md`主索引文件。
3.  **配置系统指令**：创建并配置`cloud.md`文件，明确知识库规则和操作逻辑。
4.  **配置数据摄入工具**：安装Obsidian网页剪藏器并设置其存入`raw`文件夹；安装`Local Images Plus`社区插件以正确显示图片。

> 来源：[[2026-05-25-309-Karpathy的Obsidian RAG + Claude Code = 作弊代码.md]]