---
title: "NanoClaw飞书集成手把手教程 - Andrej都觉得有趣的轻量级安全优先AI助手"
author: "五里墩茶社"
source: https://www.bilibili.com/video/BV1fufxBEE2q
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI
  - 工具
  - 集成
  - 教程
  - 安全
type: video-note
bvid: BV1fufxBEE2q
duration: "12:34"
cover: "http://i2.hdslb.com/bfs/archive/e18e80ac66e2ed55573ad8d050855c9817a5ed63.jpg"
description: "一个key用全球大模型🔴 https://DMXAPI.cn 🚀 国内直连OpenAI、Claude、Gemini，💰￥1元起充！ 推荐一个目前全网价格最实惠的合租平台，ChatGPT，MidJourney，奈飞，迪士尼，苹果TV等热门软件应有尽有 - https://dub.sh/unibus ，首单9折优惠 - 优惠码 01Coder  - 加入我的知识星球：https://t.zsxq.com/W5Oj7  我也算是 Nanoclaw 早期体验者了，2月5日我做了视频分享，记得当时的🌟还是徘徊在6k左右。感兴趣的朋友👇视频。 https://www.bilibili.com/video/"
---

# NanoClaw飞书集成手把手教程 - Andrej都觉得有趣的轻量级安全优先AI助手

> [五里墩茶社](https://space.bilibili.com/615957867) | [BV1fufxBEE2q](https://www.bilibili.com/video/BV1fufxBEE2q) | 时长 12:34

## NanoClaw飞书集成手把手教程

### 引言
- 视频主题：分享NanoClaw飞书集成的教程，帮助用户轻松完成集成。
- 背景：UP主五里墩茶社曾于2月5日发布视频介绍NanoClaw本地安装与配置，本期是续集，聚焦飞书集成。
- NanoClaw在AI圈内因大神Andrej的推文而受到关注，被描述为一款轻量级安全优先的AI助手。

### NanoClaw概述
#### 什么是NanoClaw
- 一款小巧但安全优先的AI助手，提供完全不同的安装、配置和使用体验。
- 最近在AI圈内活跃起来，主要由于Andrej的推文将其带火。

#### NanoClaw的特点
- **代码体量小**：小到能够装进自己的脑子里，也能轻松被AI智能体理解。
  - 好处：易于审计和理解，从而保证安全可靠的服务。例如，对比几十万或上百万行代码的智能体，NanoClaw更易掌控。
- **默认容器化运行**：实现更好的隔离，让用户在本地运行时更放心。
- **独特的配置方式**：不使用config文件配置，而是用Skills修改代码本身。
  - 在运行过程中，NanoClaw会实时修改代码，实现自我进化。
  - 这与OpenClaw等工具的设计哲学不同，OpenClaw依赖配置文件配置所有重要组件。

#### 与OpenClaw的区别
- OpenClaw：运行环境中有配置文件，配置重要元素。
- NanoClaw：设计哲学完全不同，强调通过代码修改实现进化，而非静态配置。

### NanoClaw的安装与配置
#### 安装步骤（从零开始）
1. **克隆代码仓库**：使用Git客户端克隆NanoClaw的代码仓库。
2. **使用CodeCode命令行工具**：通过CodeCode命令行工具完成安装。
   - NanoClaw已创建一系列可直接使用的命令，其中`Setup`命令用于初始安装与配置。
3. **运行Setup命令**：执行`Setup`命令来完成最初的安装与配置过程。

#### 注意事项
- 安装过程非常有趣且简单，视频中会从零开始演示。
- 此前视频中集成的是WhatsApp，本期聚焦飞书集成。

### 集成飞书教程
#### 背景
- 主要话题：如何在NanoClaw中集成飞书。
- 基于之前视频的基础，继续学习飞书集成。

#### 实操步骤（基于字幕开头部分）
1. **准备环境**：确保已克隆NanoClaw代码仓库。
2. **启动安装**：通过Cloud启动命令（字幕不完整，可能指使用CodeCode工具启动）。
   - 具体细节：跟随视频手把手教程完成飞书集成。

#### 建议
- 视频是一套完整教程，跟随步骤应能轻松完成集成。
- 注意NanoClaw的配置方式独特，需理解Skills修改代码的机制。

### 总结核心要点
NanoClaw是一款创新性的轻量级AI助手，以其小代码体量、容器化安全隔离和独特的Skills配置方式（通过代码修改而非config文件实现自我进化）在AI圈内受到关注，特别是经Andrej推文带火后。本视频提供了从零开始的飞书集成手把手教程，包括克隆仓库、使用CodeCode工具和Setup命令的安装步骤，强调安全优先的设计哲学，帮助用户轻松实现集成并理解其与OpenClaw等工具的差异。

---

## 原始字幕

大家好,我是小木头本期视频我会分享一款最近默默活起来的AI助手NanoClaw我们的主题是飞速的集成本期视频会是一套手把手教程跟着我一起应该能够帮助大家轻松的完成NanoClaw飞速集成那现在就开始今天的分享吧实际上在2月5日我就发布了一期视频介绍了NanoClaw本地的安装与配置这是一款小巧但安全优先的AI助手给到了用户完全不同的安装配置以及使用的体验为什么它最近会在AI圈内慢慢活了起来呢最近AI圈内大神Anderle发表了一篇推文其中提到了这款非常有趣的AI助手NanoClaw这也意外的将其带火在Android的推文中提到了一些NanoClaw所特有的特点首先它的代码体量小小到能够装进自己的脑子里也能轻松的被AI智能体理解这样最大的好处是一审计可控也更安全设想一下有几十万上百万行代码的一个智能体你是否能够轻易的阅读理解它呢在没有阅读和理解之前你怎么能保证这个智能体能够安全可靠的为你服务呢另一方面NanoClaw它默认容器化运行实现了更好的隔离相较而言在本地运行时让用户也更放心最后就是非常敬艳的配置方式在NanoClaw的哲学当中它并不是使用config文件配置而是用Skills来修改代码本身这也是在上一期视频分享中我提到的看起来在配置运行中NanoClaw会实时的修改代码随时的让自己放生进化如果用过OpenClaw的朋友应该了解在OpenClaw的运行环境中有这么一套配置文件配置着其中所有重要的组件元素因此可以看得出来NanoClaw是有完全不同的设计哲学的本期视频分享的主要话题是如何在NanoClaw集成飞书不过NanoClaw的安装与配置过程非常有趣也很简单我们还是从零开始完成一套NanoCode的安装配置以及废数的集成在2月5号那期的视频中我们集成的是WhatsAppNanoCode的安装过程非常的有趣通过Git客户代码仓库然后使用CodeCode命令行工具完成安装在CodeCodeNanoCode已经创建了一系列可以直接使用的命令其中Setup就是帮助我们完成最初的安装与配置的那现在我们就来看看该怎么做在这里我已经克隆了NanoCloud代码仓库现在要做的呢就是通过Cloud启动命令