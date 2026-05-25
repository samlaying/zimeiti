---
title: "Sub Agents（子代理）是什么"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-182-跟着Claude Code官方文档学Claude（3）.md]]"
date: 2026-05-25
tags:
  - 卡片/概念
  - 主题/AI工具
  - 素材/观点
related:
  - "[[Sub Agents的四大核心价值]]"
  - "[[Sub Agents与Agent Team的区别]]"
---

# Sub Agents（子代理）是什么

Sub Agents是Claude Code中的一项核心功能，本质上是“给你的AI助手再配一群专业的AI下属”。

- **核心思想**：[[用分工代替堆叠，用委派代替直接处理]]。
- **运作机制**：每个Sub Agent拥有**独立的上下文窗口**、系统提示词和工具权限，完成任务后只返回摘要，避免污染主窗口。
- **目的**：解决主[[上下文窗口]]稀缺资源被轻易填满的痛点，通过委派“脏活累活”来保护主资源，保持主上下文干净。
- **核心价值**：[[Sub Agents的四大核心价值]]。

> 来源：[[2026-05-25-182-跟着Claude Code官方文档学Claude（3）.md]]