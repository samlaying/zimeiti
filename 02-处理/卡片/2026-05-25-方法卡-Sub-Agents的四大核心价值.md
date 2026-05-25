---
title: "Sub Agents的四大核心价值"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-182-跟着Claude Code官方文档学Claude（3）.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 素材/教程
related:
  - "[[Sub Agents（子代理）是什么]]"
---

# Sub Agents的四大核心价值

[[Sub Agents（子代理）是什么|Sub Agents]]提供了以下四大核心使用价值：

1.  **隔离高输出操作**：将刷屏任务（如跑测试、处理日志）委派给Sub Agent，保护主窗口上下文。
2.  **并行研究多个任务**：同时启动多个Sub Agent探索不同模块，互不干扰，可显著提升效率。
3.  **链式处理工作流**：支持链式调用，例如先让“code reviewer”找问题，再让“optimizer”修复，形成流水线作业。
4.  **条件控制与验证**：通过hooks进行细粒度验证，例如设置数据库Sub Agent仅允许SELECT操作，拦截所有写操作，增强安全性。

> 来源：[[2026-05-25-182-跟着Claude Code官方文档学Claude（3）.md]]