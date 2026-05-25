---
title: "Reference（参考资料）与Script（脚本）"
card_type: 概念卡
layer: 处理
source: "[[2026-05-25-127-7分钟速通Agent Skills是什么？跟MCPWorkflowCommandPrompt有什么关系？.md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 主题/Skills
  - 主题/编程
  - 卡片/概念
related:
  - "[[System Prompt（系统提示词）]]"
  - "[[Skill（智能体技能）]]"
---

# Reference（参考资料）与Script（脚本）

## Reference（参考资料）
存放被拆分出的详细资料文件。模型有需要时，AI客户端可通过系统命令（如`cat`）按需读取这些文件供其参考，实现**渐进式披露**，进一步节省Token。

## Script（脚本）
存放可执行的代码脚本（如Python脚本）。通过 [[System Prompt（系统提示词）]] 指定触发条件，AI客户端便能执行本地脚本，实现生成PDF等扩展功能，突破纯文本聊天限制。

> 来源：[[2026-05-25-127-7分钟速通Agent Skills是什么？跟MCPWorkflowCommandPrompt有什么关系？.md]]