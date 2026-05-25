---
title: "WebSearch收费机制对比"
card_type: 案例卡
layer: 处理
source: "[[2026-05-25-080-揭秘在Claude Code里WebSearch是如何搜索网页的.md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 主题/产品经理
  - 卡片/案例
  - 素材/案例
related:
  - "[[WebSearch实际工作流程]]"
  - "[[主Agent与子Agent隔离设计]]"
---

# WebSearch收费机制对比

Claude Code的WebSearch功能需要**按搜索次数单独收费**（每1000次10美元），其计量字段为`web_search_request`。这与Token费用分开计算。

**收费原因与商业模式**：
*   **其他平台（如OpenAI的ChatGPT）**：通常要求用户**自行注册第三方搜索服务（如Brave Search）的账号，获取API Key，并自己支付费用**。平台提供的是一个调用接口。
*   **Claude Code**：由Anthropic**统一采购并打包**了搜索服务（实际使用Brave Search能力）。用户无需提供任何API Key，支付的10美元购买的是**Anthropic提供的集成、维护、安全隔离（如通过[[主Agent与子Agent隔离设计]]实现）和基础设施服务**。

这体现了不同的产品策略：一个是“用我的工具，请自付原料”；另一个是“用我的一体化服务，我收服务费”。具体的[[WebSearch实际工作流程]]支撑了这种服务模式。

> 来源：[[2026-05-25-080-揭秘在Claude Code里WebSearch是如何搜索网页的]]