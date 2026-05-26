---
title: "LangExtract核心工作流程"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-302-LangExtract-小而美的结构化数据提取工具.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 主题/编程
related:
  - "[[LangExtract]]"
  - "[[LangExtract模型配置技巧]]"
---

# LangExtract核心工作流程

**LangExtract 的核心工作流程**：
1.  **输入准备**：提供需要处理的非结构化文本。
2.  **定义任务**：通过**提示词**和**示例**，明确需要提取的信息结构（类、属性、默认值）。
3.  **配置模型**：初始化并配置一个大模型（如 [[Gemini]]、OpenAI 或兼容 API 的模型）。
4.  **执行提取**：调用 `extract(text, prompt, examples, model)` 函数。
5.  **技术实现**：内部会对输入文本进行**分片**，然后在每个分片内进行**多轮、多线程**的文本查找和信息提取。

> 来源：[[2026-05-25-302-LangExtract-小而美的结构化数据提取工具.md]]