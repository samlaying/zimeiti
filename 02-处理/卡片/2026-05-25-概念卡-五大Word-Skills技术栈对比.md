---
title: "五大Word Skills技术栈对比"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-126-谁是最强 Word Skills？claude-docx、minimax-docx、pyword、OfficeCLI 实.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 主题/Skills
  - 素材/教程
related:
  - "[[Word Skills效果排名与选择策略]]"
  - "[[OfficeCLI命令行工具的速度优势]]"
---

# 五大Word Skills技术栈对比

本次评测涉及五种操作Word文档的AI“技能”(Skills)，其底层技术栈和工作原理各不相同：
- **Claude-docx & Claude文档助手**：基于[[Node.js]]环境，调用`docx`库生成文档。AI生成脚本，再由Node运行。
- **minimax-docx**：基于[[C#]]和[[Open XML SDK]]。AI生成C#脚本，需创建项目编译后运行，环境配置较复杂，但功能强大。
- **Pyword (自研)**：基于[[Python]]脚本。AI生成并执行Python代码创建文档，基础功能实现快。
- **[[OfficeCLI]]**：一个开源的命令行工具，内置了多种文档操作的预集成命令，通过调用命令来修改文档，运行速度快。

> 来源：[[2026-05-25-126-谁是最强 Word Skills？claude-docx、minimax-docx、pyword、OfficeCLI 实.md]]