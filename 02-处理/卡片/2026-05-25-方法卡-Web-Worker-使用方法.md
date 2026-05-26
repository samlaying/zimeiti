---
title: "Web Worker 使用方法"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-363-一张图讲清前端架构.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/编程
  - 主题/浏览器自动化
  - 素材/教程
related:
  - "[[Web Worker 处理繁重计算]]"
  - "[[消息总线（Event Bus）模式]]"
---

# Web Worker 使用方法

使用 Web Worker 处理繁重任务，核心步骤如下：
1.  **创建 Worker**：`const worker = new Worker('worker.js');` 指定 Worker 代码文件。
2.  **建立双向通信**：
    - **主线程 → Worker**：使用 `worker.postMessage({type: 'task', data: videoData})` 发送任务数据。
    - **Worker → 主线程**：在 Worker 内部通过 `self.postMessage` 回传结果或进度。在主线程通过 `worker.onmessage` 监听并处理返回消息。
3.  **Worker 内部**：通过 `self.onmessage` 接收主线程消息，执行计算，再通过 `self.postMessage` 回传。

**关键**：主线程与 Worker 间只能通过消息通信，不能直接调用。

> 来源：[[2026-05-25-363-一张图讲清前端架构.md]]