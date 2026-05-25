---
title: "[开源免费]无需API KEY即可让龙虾接入nano banana！大学生的我搓了个这样的项目。"
author: "WJZ_P"
source: https://www.bilibili.com/video/BV1fNXTB2EAn
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI绘画
  - 自动化工具
  - 开源项目
  - 浏览器自动化
  - 提效工具
type: video-note
bvid: BV1fNXTB2EAn
duration: "2:11"
cover: "http://i0.hdslb.com/bfs/archive/f272d4d8696959fc0eb7496408f0f58ea34b9d8a.jpg"
description: "项目地址：https://github.com/WJZ-P/gemini-skill BGM：《HOME》 BV1e54y1z7XM  这是一个基于浏览器自动化的Gemini MCP &amp; Skill项目，能让你的AI无需API KEY，只需要一个Gemini账号就可以画图啦~  “爱在黑夜尾声 笼着微弱光芒埋入枯叶中， 愈是接近黎明愈加心痛。”"
---

# [开源免费]无需API KEY即可让龙虾接入nano banana！大学生的我搓了个这样的项目。

> [WJZ_P](https://space.bilibili.com/39684091) | [BV1fNXTB2EAn](https://www.bilibili.com/video/BV1fNXTB2EAn) | 时长 2:11

## 项目概述
- **UP主**: WJZ_P，此前开发过云顶自动刷宝典项目。
- **项目目的**: 开源免费项目，让AI（如龙虾）通过QQ机器人接入GMI网页版画图功能，无需API KEY。
- **功能亮点**: 支持传入参考图生成图片，使用GMI网页版，完全免费且无限画图（需Pro版账号）。
- **项目主页**: GitHub项目，鼓励用户多多star支持开源。

## 安装与使用
### 环境要求
- 必须拥有GMI账号（推荐Pro版，画图无数量限制）。
- 运行环境需支持浏览器，如Edge或Chrome。

### 第一次使用步骤
1. 首次使用时，在浏览器右上角手动登录GMI网页版。
2. 后续使用无需重复登录，项目会自动处理。

### 配置AI的方法
#### 1. 接入OpenClaw
- 安装项目后，让OpenClaw读取GMI-Skill（通常它会自动识别）。
- 直接让AI生成图片即可。
- 注意：OpenClaw原生不支持AMD；若需使用，需安装MakePorter库并注册本项目。

#### 2. 接入GGMD的AI
- 手动配置AMD（具体步骤参考项目文档）。

## 技术原理
- **核心机制**: 项目在本地上模拟人手操作浏览器，自动向GMI网页版发送消息、保存图片，并将图片返回给AI，再由AI发回用户。
- **示例**: 开头的两个表情包就是通过这种方式生成的。

## 技术细节
- **技术栈选择**: 使用JavaScript（JS）和Puppeteer库；也可用Python的Playwright，但UP主更熟悉JS，因此优先选择。
- **选择浏览器自动化的原因**: 
  - 基于浏览器自动化比基于API更简单，UP主无法实现API方式。
  - 缺点：内存占用较高，对无浏览器环境不友好。
- **反爬措施**: 
  - 启动浏览器时设置特定反爬参数。
  - 所有调用使用CDP协议，避免使用element click等易被检测的操作，以规避爬虫限制。

## 总结
这个开源项目通过浏览器自动化技术，使AI能够免费接入GMI网页版画图功能，无需API KEY，特别适合需要AI绘画但不想支付API费用的用户。项目基于JavaScript和Puppeteer实现，注重反爬措施，并支持OpenClaw和GGMD两种AI配置方式。UP主鼓励用户通过star支持开源发展，项目的核心在于简化流程、提升效率，让大学生或爱好者也能轻松实现AI画图集成。

---

## 原始字幕

大家好,就上次云顶自动刷宝典项目后,我又带来了新活,直接向图,我的龙虾接了QQ机器人,配合本项目就可以让他画图。这里是两个使用事例,这些传入参考图,当然不但也可以,使用的是GMI网页版画图,是完全不需要APIT的。这里是GitHub项目主页,一直在简介,希望大家多多stuff。下面给大家简单讲一下使用方法首先必须有一个GMI的账号我自己的是Pro版画图无数量限界另外你的环境必须支持浏览器EdgeChrome都可以第一次使用时需要你右上角手动登录一次后续就不用了接着第一如果你是接着OpenClaw在安装好本项目后直接让它读GMI-Skill一般它自己就误了直接让它生涂即可项目中同时提供了MMP方法但是OpenClaw原生是不支持AMD的当然想用的话让它装一个MakePorter库接着让它注册本项目。第二,如果是使用GGMD的AI,如图手动配置一下AMD就可以了。接下来给大家讲解一下核心的技术原理。这个项目本地上是代替人手去给JMI发送消息并保存图片,返回给AI,再由AI把图片发回给用户。这里的两次对话就是开头的两个表情包出处。我们把要求给AIAI发给GMI的时候还会自动认识Prompt非常不错那么为什么要基于浏览器而不是基于ADI的方式去做呢非常简单因为我做不出来基于浏览器自动化会简单很多但内存酱油也会变高并且对无浏览器的环境不友好技术上方面我更熟悉JS因此选择了POPT用Python的PlayWrite也是可以的为了尽可能规避散爬减色我启动浏览器的时候写了特定的反爬参数并且所有的调用都是走的CP不使用类似element click的操作项目介绍就到这里了希望大家多多star让我们下一个项目再见