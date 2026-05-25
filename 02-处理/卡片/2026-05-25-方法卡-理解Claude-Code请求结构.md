---
title: "理解Claude Code请求结构"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-116-解密Claude Code和Anthropic后端是如何通信.md]]"
date: 2026-05-25
tags:
  - 主题/AI工具
  - 卡片/方法
  - 素材/教程
related:
  - "[[Token消耗分析]]"
  - "[[缓存机制]]"
---

# 理解Claude Code请求结构

## Claude Code请求结构分析

[[Claude Code]]发送给API的POST请求包含多个字段，按顺序解析如下：

### 1. Messages字段
一条用户消息被包装成**6个content block**：
- **Block 1: Hooks配置**：注入用户自定义的hooks（如superpowers hook）。
- **Block 2: 延迟加载工具清单**：仅列出工具名称，模型需要时通过`Tool Search`加载完整定义，以节省Token。
- **Block 3: MCP服务器使用指南**：指导模型如何调用用户配置的MCP工具。
- **Block 4: 可用Skills列表**：包含所有可用技能（如simplify, review）。
- **Block 5: Cloud.md文件内容**：项目自定义配置（指令、结构、规则）。
- **Block 6: 用户实际输入**：如“hello”，并设置`cache control`为一小时过期，作为**缓存切割点**。

### 2. System字段
数组形式，包含四个文本块：
- **计费头**：记录版本号和入口类型。
- **身份定义**：模型身份说明。
- **行为准则**：核心规则（运行环境、任务方式、操作谨慎性、工具使用建议、语气风格）。
- **记忆系统与环境信息**：详细说明记忆类型、方法及环境信息（如工作目录）。

### 3. Tools字段
定义了10个内置工具（如`bash`, `edit`, `read`），每个工具都带有完整的参数定义和使用说明，这些也计入Token消耗。

### 4. 其他字段
- **Thinking**：设置为`Adaptive`，由模型自行决定是否启动深度推理。
- **Output Config**：`Effort`字段设置为`X-High`，即最高推理档位（`UltraThink`触发此设置）。

> 来源：[[2026-05-25-116-解密Claude Code和Anthropic后端是如何通信]]