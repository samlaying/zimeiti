---
title: "CSS Transform控制导航菜单显隐"
note_type: 方法论
domain: 编程/技术
source: "[[2026-05-25-058-响应式导航栏教程HTML CSS JAVASCRIPT.md]]"
date: 2026-05-25
reusable: "适用于移动端侧边栏、模态框、下拉菜单等需要从屏幕外滑入/滑出的UI组件实现。"
tags:
  - 原子笔记
  - 类型/方法论
  - 领域/编程/技术
---

# CSS Transform控制导航菜单显隐

> 用`translateX`和过渡，实现平滑的滑入/滑出交互。

## 核心内容
移动端导航菜单通过CSS的`position: absolute`脱离文档流定位，初始状态使用`transform: translateX(100%)`将其移出可视区域实现隐藏。当需要显示时，通过JavaScript切换一个类（如`.nav-active`），将`transform`属性改为`translateX(0)`，使其滑入屏幕。配合`transition`属性可以实现平滑的滑动动画。

## 原文关键段落
> .nav-links { 
>     position: absolute; 
>     right: 0px; 
>     height: 92vh; 
>     top: 8vh; 
>     transform: translateX(100%); 
>     transition: transform 0.5s ease-in; 
> } 
> 
> .nav-active { 
>     transform: translateX(0%); 
> }

## 我的想法/延伸
<!-- 这是从"搬运"变成"原创"的分水岭。写下你的观点、联想、加工思路 -->


## 可复用场景
适用于移动端侧边栏、模态框、下拉菜单等需要从屏幕外滑入/滑出的UI组件实现。

> 来源：[[2026-05-25-058-响应式导航栏教程HTML CSS JAVASCRIPT.md]]