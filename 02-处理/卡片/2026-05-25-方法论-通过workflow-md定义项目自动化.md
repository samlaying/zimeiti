---
title: "通过workflow.md定义项目自动化"
note_type: 方法论
domain: 编程/技术
source: "[[2026-05-25-072-OpenAI Symphony - 把Codex装进Linear，让Agent自己干活.md]]"
date: 2026-05-25
reusable: "适用于介绍如何通过声明式配置文件（如YAML、Markdown）来定义和启动一个复杂的自动化流程，是DevOps、自动化工具配置的常见模式。"
tags:
  - 原子笔记
  - 类型/方法论
  - 领域/编程/技术
---

# 通过workflow.md定义项目自动化

> 一个Markdown文件，定义了项目ID和初始化代码仓库的钩子，就能驱动AI全自动工作。

## 核心内容
启动Symphony需要配置一个workflow.md文件，其中关键参数包括‘Project Slug’（Linear项目ID）和‘Hooks’（如在任务创建后执行‘git clone’命令来初始化代码工作区）。这个文件将Symphony指向具体的项目仓库和管理看板，实现了工具的项目适配。

## 我的想法/延伸
<!-- 这是从"搬运"变成"原创"的分水岭。写下你的观点、联想、加工思路 -->


## 可复用场景
适用于介绍如何通过声明式配置文件（如YAML、Markdown）来定义和启动一个复杂的自动化流程，是DevOps、自动化工具配置的常见模式。

> 来源：[[2026-05-25-072-OpenAI Symphony - 把Codex装进Linear，让Agent自己干活.md]]