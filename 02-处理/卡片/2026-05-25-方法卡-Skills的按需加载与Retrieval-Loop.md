---
title: "Skills的按需加载与Retrieval Loop"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-012-《浅入深出》Agent系列之十一：Skills原理解析.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/Skills
  - 主题/AI工具
  - 素材/教程
related:
  - "[[Skills内容结构]]"
  - "[[Skills的卸载策略]]"
---

# Skills的按需加载与Retrieval Loop

为解决上百个Skills全部注入导致的“上下文爆炸”问题，采用 **按需加载** 策略：

1.  **初始注入**：仅将所有Skills的[[Metadata]]（Name和Description）列表作为“目录”注入[[LLM]]上下文。
2.  **按需检索**：当[[LLM]]遇到具体问题时，根据目录的Description判断所需Skills，通过类似`retrieval`的函数从Skills库中查找对应的Markdown文件。
3.  **Retrieval Loop**：[[LLM]]加载第一个Skill后，会检查其是否足够或是否依赖其他Skills，若需要则继续检索，形成循环，直到获得足够的信息。

> 来源：2026-05-25-012-《浅入深出》Agent系列之十一：Skills原理解析.md