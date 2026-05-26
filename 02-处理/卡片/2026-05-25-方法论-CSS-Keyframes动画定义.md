---
title: "CSS Keyframes动画定义"
note_type: 方法论
domain: 编程/技术
source: "[[2026-05-25-058-响应式导航栏教程HTML CSS JAVASCRIPT.md]]"
date: 2026-05-25
reusable: "适用于定义任何复杂的、多步骤的CSS动画序列，如淡入、滑动、旋转、缩放等组合效果。"
tags:
  - 原子笔记
  - 类型/方法论
  - 领域/编程/技术
---

# CSS Keyframes动画定义

> `@keyframes`是定义复杂动画的基石。

## 核心内容
使用`@keyframes`规则定义动画序列。本例中定义了`navLinkFade`动画，它让元素从`opacity: 0`（完全透明）且`transform: translateX(50px)`（向右偏移50像素）的状态，变化到`opacity: 1`（完全不透明）且`transform: translateX(0px)`（原始位置）的状态，从而实现了淡入并向左滑动的效果。

## 原文关键段落
> @keyframes navLinkFade {
>     from {
>         opacity: 0;
>         transform: translateX(50px);
>     }
>     to {
>         opacity: 1;
>         transform: translateX(0px);
>     }
> }

## 我的想法/延伸
<!-- 这是从"搬运"变成"原创"的分水岭。写下你的观点、联想、加工思路 -->


## 可复用场景
适用于定义任何复杂的、多步骤的CSS动画序列，如淡入、滑动、旋转、缩放等组合效果。

> 来源：[[2026-05-25-058-响应式导航栏教程HTML CSS JAVASCRIPT.md]]