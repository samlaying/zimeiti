---
title: "DOM与Canvas的桥梁API"
note_type: 观点
domain: 编程/技术
source: "[[2026-05-25-018-使用 HTML-in-Canvas API 构建下一代用户界面.md]]"
date: 2026-05-25
reusable: "用于阐述Web技术演进、前端图形化方案选择、UI框架设计理念的讨论。"
tags:
  - 原子笔记
  - 类型/观点
  - 领域/编程/技术
---

# DOM与Canvas的桥梁API

> 该API解决了高性能图形与富功能UI长期存在的根本矛盾。

## 核心内容
传统Web开发中，DOM拥有无障碍、翻译、页面查找等丰富的浏览器功能，而Canvas/WebGL/WebGPU则提供了高性能图形渲染能力，但两者结合困难。HTML-in-Canvas API的核心价值在于充当桥梁，允许将DOM元素直接绘制到Canvas或WebGPU纹理中，从而同时获得高性能渲染和完整的浏览器功能集成。

## 原文关键段落
> The HTML and Canvas API is the bridge that gives you the best of both worlds by letting you paint DOM elements into a canvas or web GPU texture.and the best part is that by putting the HTML inside the canvas tag and updating the transform the content not only remains interactable but all the browser features I mentioned stay hooked up too.

## 我的想法/延伸
<!-- 这是从"搬运"变成"原创"的分水岭。写下你的观点、联想、加工思路 -->


## 可复用场景
用于阐述Web技术演进、前端图形化方案选择、UI框架设计理念的讨论。

> 来源：[[2026-05-25-018-使用 HTML-in-Canvas API 构建下一代用户界面.md]]