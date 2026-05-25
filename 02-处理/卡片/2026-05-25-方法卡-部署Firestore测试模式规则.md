---
title: "部署Firestore测试模式规则"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-156-【Claude 教学】Claude大师课：掌握 AI 驱动开发【上集】.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 主题/编程
related:
  - "[[斜杠命令初始化Firebase]]"
  - "[[Firebase核心服务]]"
---

# 部署Firestore测试模式规则

配置Firestore测试模式安全规则的步骤：
1. 在初始化过程中，当提示部署Firestore安全规则时，选择**保持在测试模式**。
2. 测试模式规则允许读写访问数据，但仅限于指定日期（例如未来30天）。
3. 使用Firebase工具（通过npx命令）部署规则，完成数据库创建。
> 来源：[[2026-05-25-156-【Claude 教学】Claude大师课：掌握 AI 驱动开发【上集】]]