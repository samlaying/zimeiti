---
title: "CubeSandbox案例"
card_type: 案例卡
layer: 处理
source: "[[2026-05-25-128-AI Agent的沙箱是什么？它和Docker容器虚拟机有什么区别.md]]"
date: 2026-05-25
tags:
  - 卡片/案例
  - 主题/AI工具
  - 主题/编程
  - 素材/案例
related:
  - "[[MicroVM是安全与性能的平衡点]]"
  - "[[CubeSandbox的架构与核心优化]]"
---

# CubeSandbox案例

**CubeSandbox**是腾讯云开源的一个高性能云沙箱方案，专为AI Agent设计。

- **定位**：可理解为给AI Agent用的云沙箱底座，负责沙箱的创建、隔离和回收。
- **优势**：对比同类方案E2B，其**开源产品化做得更好，搭建成本更低**。
- **应用**：已被原爆的在线编程和MiniMax的Agent强化学习训练采用。

它通过[[MicroVM是安全与性能的平衡点]]作为底层技术，并运用了快照克隆、写时复制等[[CubeSandbox的架构与核心优化]]技术，实现了毫秒级沙箱启动。

> 来源：2026-05-25-128-AI Agent的沙箱是什么？它和Docker容器虚拟机有什么区别.md