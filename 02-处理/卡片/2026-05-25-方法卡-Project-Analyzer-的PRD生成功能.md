---
title: "Project Analyzer 的PRD生成功能"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-372-别再手撸PRD了？我做了一个逆向工程Skill.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 主题/产品经理
related:
  - "[[Project Analyzer 逆向分析Skill]]"
  - "[[Project Analyzer 的两步使用法]]"
---

# Project Analyzer 的PRD生成功能

`Project Analyzer` [[Skill]] 的核心输出是一份结构化的PRD文档，包含**14个主要章节**，如产品定位、用户故事、[[Agent故事]]、[[Agent流程]]和提示词设计策略等。

此外，它还具备强大的提示词拆解分析能力：
1.  自动提取项目中的所有提示词，并存放在特定文件夹（如`AR Analyze`）。
2.  生成一个提示词索引文件（`index`）。
3.  对每个提示词提供详细分析，包括**文档位置、中文翻译、参数解析及相关代码片段**。

> 来源：2026-05-25-372-别再手撸PRD了？我做了一个逆向工程Skill.md