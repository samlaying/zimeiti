---
title: "CSS max-height平滑展开"
note_type: 方法论
domain: 编程/技术
source: "[[2026-05-25-062-[HTML+CSS] 悬停资料卡片.md]]"
date: 2026-05-25
reusable: "实现折叠菜单、详情展开、消息列表等收起/展开动画。"
tags:
  - 原子笔记
  - 类型/方法论
  - 领域/编程/技术
---

# CSS max-height平滑展开

> 无需JavaScript实现的纯CSS高度过渡动画技巧。

## 核心内容
实现内容从收起到平滑展开的动画，可以巧妙地过渡`max-height`属性。初始状态给元素设置一个足够小的`max-height`并配合`overflow: hidden`来隐藏内容。悬停时，将`max-height`过渡到一个足够大的值（如500px），内容便能平滑地展开显示出来。

## 原文关键段落
> .card {
>   max-height: 200px;
>   overflow: hidden;
>   transition: max-height 0.5s ease-out;
> }
> .card:hover {
>   max-height: 500px;
> }

## 我的想法/延伸
<!-- 这是从"搬运"变成"原创"的分水岭。写下你的观点、联想、加工思路 -->


## 可复用场景
实现折叠菜单、详情展开、消息列表等收起/展开动画。

> 来源：[[2026-05-25-062-[HTML+CSS] 悬停资料卡片.md]]