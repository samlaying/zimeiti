---
title: "文件编辑：apply_patch vs. file_edit"
card_type: 案例卡
layer: 处理
source: "[[2026-05-25-186-编程智能体开发必读？Codex与Claude Code全面剖析.md]]"
date: 2026-05-25
tags:
  - 卡片/案例
  - 主题/编程
  - 素材/案例
related:
  - "[[工具哲学：少而精 vs. 多而专]]"
  - "[[文件搜索：自带rg vs. 指导用rg]]"
---

# 文件编辑：apply_patch vs. file_edit

两者文件编辑工具均为自研，实现策略不同：
- [[Codex CLI]] 的 **`apply_patch`**：
  - 纯Rust实现，非标准unified diff。
  - 核心是 **4G模糊匹配算法**（精确匹配、忽略尾部空白、忽略首尾空白、Unicode标点归一化）来定位代码。
  - 一次调用可**同时修改、创建、删除多个文件**，且是**事务性**的。
- [[Claude Code]] 的 **`file_edit`**：
  - 纯TypeScript实现，底层是JavaScript的`String.replace`和`replaceAll`。
  - 增加了**智能引号归一化**（单引号、直引号匹配）、编码检测和换行符保留。
  - 设计哲学：**一次调用只改一个文件的一个位置**，简单、可靠、安全。

> 来源：2026-05-25-186-编程智能体开发必读？Codex与Claude Code全面剖析.md