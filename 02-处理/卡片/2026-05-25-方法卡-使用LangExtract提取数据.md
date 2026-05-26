---
title: "使用LangExtract提取数据"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-302-LangExtract-小而美的结构化数据提取工具.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 素材/教程
related:
  - "[[LangExtract：结构化数据提取工具]]"
  - "[[中文合同信息提取案例]]"
---

# 使用LangExtract提取数据

使用[[LangExtract：结构化数据提取工具]]提取结构化数据的步骤：
1. 定义提取任务：明确需要提取的字段，并提供示例（Few-shot prompting）。
2. 配置大模型：使用默认Gemini或通过Factory模式配置其他模型（如DeepSeek）。
3. 准备输入文本：将非结构化文本转换为纯文本（如Markdown转TXT）。
4. 执行提取：调用extract函数，获取JSON结果和HTML可视化。
> 来源：[[2026-05-25-302-LangExtract-小而美的结构化数据提取工具.md]]