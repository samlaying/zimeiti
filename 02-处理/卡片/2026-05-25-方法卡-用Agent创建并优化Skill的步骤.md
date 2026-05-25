---
title: "用Agent创建并优化Skill的步骤"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-135-手把手教你打造专属HTML SKILL！让AI完全懂你的设计风格.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/Skills
  - 素材/教程
related:
  - "[[创建专属HTML Skill的完整流程]]"
  - "[[迭代优化Skill的策略]]"
---

# 用Agent创建并优化Skill的步骤

以[[Workbody]]为例，创建并优化Skill的操作步骤：

1.  **创建**：在聊天窗口上传满意的HTML文件，并指示AI：“我想以后能做出类似的HTML，帮我创建一个Skill叫XX”。
2.  **调用**：AI会调用 `Skill Creator` 技能，自动生成模板HTML和Skill定义。
3.  **优化**：直接使用可能会出现问题（如显示不全）。此时将具体问题（如字体加载、布局错位）告知AI，并要求其优化Skill。解决一个问题后，明确指示AI更新Skill以避免复发。
4.  **迭代**：反复进行“测试 -> 反馈问题 -> AI优化”的循环，直到Skill稳定可靠。

> 来源：[[2026-05-25-135-手把手教你打造专属HTML SKILL！让AI完全懂你的设计风格]]