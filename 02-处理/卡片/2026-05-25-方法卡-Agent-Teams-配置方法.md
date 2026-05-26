---
title: "Agent Teams 配置方法"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 素材/教程
related:
  - "[[Claude Agent Teams 并行通信原理]]"
---

# Agent Teams 配置方法

启用 [[Claude Agent Teams]] 功能的配置步骤如下：
1.  找到并打开本地配置文件 `Setting.json`。
2.  在该文件的 `env` JSON字段中，添加或修改相关配置项。
3.  将该配置项的值设置为 `1`（如果默认是 `0` 则改为 `1`）。
4.  保存文件，即完成配置，Claude Code 便会启用 Agent Teams 功能。

整个过程在 `Setting.json` 中完成，操作简单。

> 来源：[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]