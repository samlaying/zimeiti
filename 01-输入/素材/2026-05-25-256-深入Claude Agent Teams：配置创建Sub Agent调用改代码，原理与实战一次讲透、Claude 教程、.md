---
title: "深入Claude Agent Teams：配置/创建/Sub Agent调用/改代码，原理与实战一次讲透、Claude 教程、Claude原理"
author: "下班学AI"
source: https://www.bilibili.com/video/BV1MxDLBEE1f
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI
  - 工具
  - 提效
  - Claude
  - Agent
  - 教程
type: video-note
bvid: BV1MxDLBEE1f
duration: "6:56"
cover: "http://i0.hdslb.com/bfs/archive/fe65bd7f3d012ce5c425bb7e7e6bdbf946db9d57.jpg"
description: "标题： 深入Claude Agent Teams：配置/创建/Sub Agent调用/改代码，原理与实战一次讲透 简介： 👋 本期视频带你深入实战 Claude Agent Teams —— 从零配置到自动创建 Agent，再到调用 Sub Agent 协作修改代码，全程在线演示，同时拆解背后的运行原理。 🔥 你将看到： ⚙️ 配置与创建：手把手搭建 Claude Agent Teams 环境，自动生成 Agent 🤖 Sub Agent 调用：主 Agent 如何动态调用子 Agent 完成任务 💻 修改代码实战：真实场景演示 Sub Agent 修改代码文件并返回结果 🧠 原理拆解：Age"
---

# 深入Claude Agent Teams：配置/创建/Sub Agent调用/改代码，原理与实战一次讲透、Claude 教程、Claude原理

> [下班学AI](https://space.bilibili.com/3546599351388553) | [BV1MxDLBEE1f](https://www.bilibili.com/video/BV1MxDLBEE1f) | 时长 6:56

## 引言：为什么需要Agent Teams
在AI Agent时代，同一个Agent需要处理搜索资料、编码、查资料等多项任务，导致串行工作流。这种串行方式混乱且速度慢。Agent Teams通过并行工作来提高效率，解决这一问题。

## Agent Teams工作原理
### 基本结构
- 参考官网图，Agent Teams包括一个主Agent（man agent）和一个共享的task list。
- 下面有多个子Agent，这些子Agent之间可以相互通信，也可以与主Agent通信。

### 与Sub Agents的区别
- **Sub Agents**：各个子Agent只能与主Agent通信，相互之间不能通信。
- **Agent Teams**：子Agent之间可以相互并行通信，同时也与主Agent相互通信，实现并行工作，提高效率。

## 配置Agent Teams
### 配置步骤
1. 打开本地配置文件 `Setting.json`。
2. 在 `env` JSON字段中添加配置字段，以开启Agent Teams。例如，将相关值设置为1（如果默认为0则改为1）。
3. 保存配置后，Claude Code即启用Agent Teams功能。

## 实战：创建和运行Agent Teams
### 创建提示词
- 编写一个提示词，用于创建Agent Teams。示例提示词要求创建两个Agent：一个前端架构师和一个UI设计师。
- 运行后，系统自动分屏显示主Agent（Team Leader）和两个子Agent。

### 运行示例
- 本地已有一个自定义Agent，用于女性化配色方案。网站代码有四个功能区，初始以蓝色为主。
- 使用提示词创建Agent Teams后，子Agent开始工作。前端工程师Agent可能报错（如400错误），通过切换模型解决（例如，通过 `Model` 参数切换到可用模型）。
- UI设计师Agent分析问题，前端工程师Agent接收需求并开发。
- 结果：网站颜色从蓝色变为女性化配色。

### 结合自定义Agent
- 自定义Agent可以封装业务逻辑，例如女性化配色方案。在Agent Teams中，可以结合自定义Sub Agent和系统自动创建的Team Agent使用。
- 建议：将工作中常用的业务封装成自定义Agent，灵活用于Sub Agent或Agent Teams。

## 总结核心要点
Agent Teams通过并行通讯机制（子Agent之间以及与主Agent之间）显著提高AI工作效率，解决串行工作流的瓶颈。配置简单，只需在 `Setting.json` 中设置相关字段。实战中可结合自定义Agent，灵活处理复杂任务，如前端和UI设计。理解Sub Agents和Agent Teams的区别（通讯方式不同）是关键，建议用户充分利用Agent Teams并行优势优化工作流。

---

## 原始字幕

你的AI还在做完一个再做一个太慢了我们今天分享一下Cloud的Agent Teams然后这是官网我们一起来看一下这是Agent Teams的一个价格图我们昨天分享了Sub AgentsAgent Teams可以通过这个在Sets.json文件中我们通过这个page来开启我们为什么需要Agent Teams在当Agent时代我们同一个Agent我们就要搜索资料又要coding同时做很多工作它都是一个串行的工作流既要搜索又要写代码还得查资料它很混乱然后速度慢是一个串行的工作我们讲一下Agent Teams的一个工作原理我们参考一下官网的这张图右边的然后是一个man agent然后它有一个共享的task list下面有很多子agent我们看一下这个子agent是可以相互通讯的managent可以跟我们各个agent之间也是可以通讯的这就是跟我们subagent的一个区别我们subagent各个agent之间是不可以通讯的只是每一个subagent跟我们的主agent是可以通讯的也就是说在agent teams里面各个agent是可以相互并行通信的,他们跟主agent也是可以相互通信的这就是他的一个真正的一个原理然后通过一个并行的一个工作来提高我们的一个效率我们刚才讲了ageteams的一个工作原理下面我们来讲一下怎么来配置Aged Teams我们只要在我们的一个Setting.json文件中我们把这个配置给它写进去就OK了我们打开我们自己的一个配置文件找到Setting.json我们打开然后我们在这个env这个json中我们配置上这个字段然后就代表我们的cloud code已经开启了agent teams本地如果没有这个配置我们自己加进去如果有可能这里是0把它改成1就开启了agent teams现在我们以一个实战的案例来演示一下我们怎么创建我们的agent teams我本地已经有了一个agent昨天创建的subagent我们打开看一下这个agent它只有一个作用就是女性化配色方案我本地还有一份代码是一个网站我们看一下是一个网站的一个简单代码它有四个功能区然后是蓝色为主我们现在来创建我们自己的agent teams我这里写了一个提示词复制一下提示词的作用就是创建一个agent的teams然后创建两个agent一个前单架构师还有一个UI创建好了它自动给我分屏好 我们来看一下这边是一个前单工程师然后这边是一个UI然后这是Team Leader然后现在他们都暂停工作了前段工程师这里报错报了一个400应该是他的一个模型不对模型的Token我用完了我们给他切换一个模型现在切换到了前段工程师我们给他切换一个模型这个Agent我们通过Model给它切换到了我们这个模型然后我们切换到我们的设计师这里设计师这里我这里创建了两个agent然后一个前段工程师这是系统自动创建的设计师也是系统自己创建的刚才我们在这里是不是自定义了一个agent如果不会自定义agent可以去看我上一期视频我们这个agent的名字叫这个复制使用自定义agent自定义agent已经创建好了名字叫我们把指令告诉他让他去用我们自己已经创建好的Agent稍等一下UI设计师已经分析出来了问题然后前单工程师这里也收到了需求然后他开始开发了好我们看一下现在我们的这个Agent Teams都已经工作完了我们来看一下它工作后的一个结果然后还是这个我们打开现在是不是变了现在是一个偏女性的一个颜色刚才这是刚刚开始一个蓝色我们把它改成一个偏女性的一个颜色我们看到我们这个agentteams里面它是一个team leader左边是一个自定义的一个subagent然后右边是不是这个team它自动创建了一个agent这样就结合了我们我们自己创建subagent跟team agent一个结合我们可以把自己工作中所要用的一些业务封装成自己的agent我们不管用subagent还是team agent我们都可以来联合使用大家一定要知道这个subagent跟agentteams他们之间的一个区别大家有任何问题可以评论去留言