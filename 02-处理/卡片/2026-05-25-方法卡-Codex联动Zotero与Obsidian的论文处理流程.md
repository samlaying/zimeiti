---
title: "Codex联动Zotero与Obsidian的论文处理流程"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-124-Codex、Obsidian、Zotero联动的论文库工作流.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/编程
related:
  - "[[三工具论文工作流角色分工]]"
  - "[[Frogmatter笔记属性]]"
  - "[[DataView插件]]"
  - "[[处理单篇论文的实践案例]]"
---

# Codex联动Zotero与Obsidian的论文处理流程

这是一个从文献处理到智能检索的自动化全流程，核心依赖Codex专用[[Skills]]：
### 1. 准备工作
- **下载Skills**：从Github获取两个关键文件夹：
  - **Zotero Analytical Workflow Skills**：包含三个子Skill，协调自动化处理。
  - **Research for Literature Retrieval Skills**：辅助文献检索。
- **设置Obsidian**：
  - 创建机器人（如“ResearchBot”）。
  - 建立两个核心目录：存放论文的库、存放模板的目录。
  - **准备模板**：重点设置[[Frogmatter笔记属性]]区，字段越详细，后续检索越方便。
### 2. 处理论文
- **在Zotero中组织文献**：按主题创建文件夹（如“机器学习卡牌决策”），存放PDF。
- **在Codex中处理**：加载Skills后，通过自然语言指令操作：
  - **处理单篇**：“精读，所以Tail中的，[论文名称]”。
  - **批量处理**：“处理Zotero中的[文件夹名]中的所有论文”。
  - Codex会自动调用`Zotero Collection Manager`、`Zotero Data Fetcher`和`Zotero Analytical Writer`完成处理，并将笔记存入Obsidian目录。
### 3. 检索与应用
- **在Obsidian中**：安装并启用[[DataView插件]]，它能自动提取所有笔记的[[Frogmatter笔记属性]]，生成动态索引页。
- **在Codex中**：打开Obsidian的论文库文件夹，通过对话进行自然语言查询，例如“针对卡牌类游戏的机器学习方法有哪些？”，Codex会基于论文库给出总结。
> 来源：2026-05-25-124-Codex、Obsidian、Zotero联动的论文库工作流.md