---
title: "BrowserHannis的CDP直连架构"
note_type: 方法论
domain: 浏览器自动化
source: "[[2026-05-25-007-AI 操控浏览器，最省 token 的一条路.md]]"
date: 2026-05-25
reusable: "可用于技术解析、原理解释或评估工具优劣时，说明其核心工作原理与优势。"
tags:
  - 原子笔记
  - 类型/方法论
  - 领域/浏览器自动化
---

# BrowserHannis的CDP直连架构

> 省去重新登录，直接在你的浏览器里工作，这就是CDP直连的魔力。

## 核心内容
BrowserHannis的工作原理是通过CLI发送指令给守护进程（Demon），再由守护进程通过Chrome DevTools Protocol（CDP）的WebSocket直接控制浏览器内核。这种架构使其能够直接连接用户正在使用的浏览器，从而复用已有的Cookie和登录状态，极大提升了实用性和效率。

## 原文关键段落
> Guardcode通过Cli把指令发送给了Demon然后Demon再通过CDP的WebSocket然后直接来控制我们的Chrome...它能连接你正在用的浏览器你的cookie登录状态就是你登录了抖音其他的一些登录状态都是完全可以服用

## 我的想法/延伸
<!-- 这是从"搬运"变成"原创"的分水岭。写下你的观点、联想、加工思路 -->


## 可复用场景
可用于技术解析、原理解释或评估工具优劣时，说明其核心工作原理与优势。

> 来源：[[2026-05-25-007-AI 操控浏览器，最省 token 的一条路.md]]