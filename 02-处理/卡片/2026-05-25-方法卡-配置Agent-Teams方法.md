---
title: "配置Agent Teams方法"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 素材/教程
related:
  - "[[Agent Teams并行通信机制]]"
  - "[[创建Agent Teams提示词]]"
---

# 配置Agent Teams方法

配置Agent Teams的步骤：
1. 打开本地配置文件 `Setting.json`。
2. 在 `env` JSON字段中添加配置字段，将相关值设置为1（如果默认为0则改为1）以开启Agent Teams。
3. 保存配置后，Claude Code即启用Agent Teams功能。
> 来源：[[2026-05-25-256-深入Claude Agent Teams：配置创建Sub Agent调用改代码，原理与实战一次讲透、Claude 教程、.md]]