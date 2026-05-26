---
title: "纯色背景用box-shadow实现凹角"
note_type: 方法论
domain: 编程/技术
source: "[[2026-05-25-063-CSS 内凹边框：四种切角实现方式.md]]"
date: 2026-05-25
reusable: "适用于需要实现纯色卡片、按钮等元素的内凹角效果，特别是在需要高浏览器兼容性的项目中。"
tags:
  - 原子笔记
  - 类型/方法论
  - 领域/编程/技术
---

# 纯色背景用box-shadow实现凹角

> 经典且兼容性极佳（IE9+）的纯色凹角实现方案。

## 核心内容
通过一个伪元素配合巨大的无模糊box-shadow来实现。将伪元素定位在目标角落，尺寸设为凹角大小，只圆化指向内部的一个角，然后为其设置一个颜色与父容器背景色相同、扩展值等于其边长的box-shadow。这个阴影会覆盖伪元素周围区域，从而“画”出凹角曲线。

## 原文关键段落
> A single pseudo element paired with one absolutely massive box shadow... a box shadow with no blur just spread painted in the parents exact background color and the moment that line lands the cutout appears because the shadow paints the parents color over everything around the pseudo's curve leaving just that curve untouched.

## 我的想法/延伸
<!-- 这是从"搬运"变成"原创"的分水岭。写下你的观点、联想、加工思路 -->


## 可复用场景
适用于需要实现纯色卡片、按钮等元素的内凹角效果，特别是在需要高浏览器兼容性的项目中。

> 来源：[[2026-05-25-063-CSS 内凹边框：四种切角实现方式.md]]