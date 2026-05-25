---
title: "CubeSandbox的架构与核心优化"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-128-AI Agent的沙箱是什么？它和Docker容器虚拟机有什么区别.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 主题/编程
  - 素材/教程
related:
  - "[[CubeSandbox案例]]"
  - "[[MicroVM是安全与性能的平衡点]]"
---

# CubeSandbox的架构与核心优化

CubeSandbox通过精巧的架构设计和关键技术优化实现高性能：

### 架构
- **控制面**：包含Cube API和CubeMaster，负责管理和调度。
- **工作节点 (Node)**：裸金属服务器，包含CubeLater组件，负责实际创建和运行沙箱。
- **请求流程**：API -> CubeMaster -> CubeLater -> KVM创建MicroVM。

### 核心优化技术
1.  **快照克隆**：提前制作并保存一个完整的MicroVM**模板快照**，后续请求直接从快照**克隆**，省去初始化时间，启动压至**几十毫秒**。
2.  **写时复制 (Copy-on-Write)**：所有沙箱初始共享同一份底层内存/磁盘页面，仅在**真正写入时**才复制，将单个沙箱内存开销控制在**几MB**。
3.  **API屏蔽细节**：对外提供简单API，Agent无需关心底层实现。

这套方案是实现[[MicroVM是安全与性能的平衡点]]落地的重要实践。

> 来源：2026-05-25-128-AI Agent的沙箱是什么？它和Docker容器虚拟机有什么区别.md