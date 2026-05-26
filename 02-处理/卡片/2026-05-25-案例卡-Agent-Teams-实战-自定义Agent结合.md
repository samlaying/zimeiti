---
title: "Agent Teams 实战：自定义Agent结合"
card_type: 案例卡
layer: 处理
source: "[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]"
date: 2026-05-25
tags:
  - 卡片/案例
  - 主题/AI工具
  - 素材/案例
related:
  - "[[Claude Agent Teams 并行通信原理]]"
  - "[[Agent Teams 配置方法]]"
---

# Agent Teams 实战：自定义Agent结合

实战演示了如何创建并运行 [[Claude Agent Teams]]，并**结合自定义Agent**处理复杂任务。

**案例任务**：将网站默认的蓝色配色方案改为女性化配色。
**操作流程**：
1.  **创建Teams**：通过提示词创建一个Agent Teams，系统自动生成 Team Leader、前端工程师Agent和UI设计师Agent。
2.  **结合自定义Agent**：将已有的封装了“女性化配色方案”业务逻辑的**自定义Sub Agent**，指令给Teams中的Agent使用。
3.  **并行协作**：UI设计师Agent分析问题并提出需求，前端工程师Agent接收需求并执行代码修改。两者并行工作。
4.  **结果**：成功将网站配色从蓝色改为女性化配色方案。

**启示**：可以将常用业务封装成自定义Agent，无论是用于 [[Sub Agents]] 还是 Agent Teams，都能灵活组合，提升开发效率。

> 来源：[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]