---
title: "WebSearch实际工作流程"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-080-揭秘在Claude Code里WebSearch是如何搜索网页的.md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 卡片/方法
  - 素材/教程
related:
  - "[[主Agent与子Agent隔离设计]]"
  - "[[WebSearch收费机制]]"
  - "[[LLM中的工具类型]]"
---

# WebSearch实际工作流程

Claude Code的WebSearch功能并非一次API调用完成，而是涉及三次调用的多层流程：

1.  **主Agent（Opus）提出需求**：用户提问后，主Agent（如Opus 4.7）不直接搜索，而是输出一个`Tool use`指令块，指定调用`web_search`工具及参数，`stop reason`为`tool_use`，等待客户端提供结果。
2.  **子Agent（Haiku）执行搜索**：客户端自动开启新对话，将任务交给**子Agent**（如Haiku模型）。子Agent的工具集仅有`web_search`（一种`server tool use`）。它调用后，服务端返回包含URL、标题和**加密内容**（`Encrypted Content`）的搜索结果，以及子Agent基于结果生成的**总结**。此过程单独计量（`web_search_request`）。
3.  **结果返回主Agent**：客户端将处理后的`tool result`（仅包含URL、标题和子Agent的总结）发送回主Agent。主Agent基于此用自然语言生成最终答案。

这种设计的核心目的是实现[[主Agent与子Agent隔离设计]]，并涉及[[WebSearch收费机制]]。背后的[[LLM中的工具类型]]（服务器端工具）在第二步被实际调用。

> 来源：[[2026-05-25-080-揭秘在Claude Code里WebSearch是如何搜索网页的]]