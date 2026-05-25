---
title: "为什么需要Sub Agents"
card_type: 观点卡
layer: 处理
source: "[[2026-05-25-182-跟着Claude Code官方文档学Claude（3）.md]]"
date: 2026-05-25
tags:
  - 卡片/观点
  - 主题/AI工具
  - 素材/观点
related:
  - "[[Sub Agents（子代理）是什么]]"
---

# 为什么需要Sub Agents

使用Claude Code的一个常见痛点是：**上下文窗口是稀缺资源**。

当执行跑测试、扫描代码库、处理日志等任务时，大量数据会迅速填满上下文窗口，导致Token耗尽，真正的需求反而无法塞入。而[[Sub Agents（子代理）是什么|Sub Agents]]通过**委派（delegate）** 任务来解决这个问题。

> 来源：[[2026-05-25-182-跟着Claude Code官方文档学Claude（3）.md]]