---
title: "卸载 OpenClaw！拥抱NanoClaw"
author: "Terminator-AI"
source: https://www.bilibili.com/video/BV1F6fYB3Eix
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI
  - 工具对比
  - 效率
  - 个人助理
  - 代码优化
type: video-note
bvid: BV1F6fYB3Eix
duration: "3:13"
cover: "http://i1.hdslb.com/bfs/archive/843986dedcbb19d5fc0afde929e3933ac63582da.jpg"
description: "AI 大神 Karpathy 最近公开表示，NanoClaw 的配置方式让他大开眼界。 我也去体验一下NanoClaw，只有一个结论：卸载 OpenClaw，拥抱NanoClaw ！ OpenClaw就不用吐槽了，软件质量跟屎一样，每天都能遇到不同的Bug。"
---

# 卸载 OpenClaw！拥抱NanoClaw

> [Terminator-AI](https://space.bilibili.com/328381287) | [BV1F6fYB3Eix](https://www.bilibili.com/video/BV1F6fYB3Eix) | 时长 3:13

## 引言
AI领域知名专家Karpathy公开推荐NanoClaw，并表示其配置方式令人印象深刻。UP主Terminator-AI体验后得出明确结论：应卸载OpenClaw，全面拥抱NanoClaw。

## OpenClaw的主要问题
- **软件质量差**：每天都会遇到不同的bug，甚至连一个简单的定时任务都可能报错。
- **系统过于沉重**：包含超过52个模块、45个依赖项；为适配15个不同的渠道商设计了复杂的抽象层。
- **进程臃肿**：所有功能都挤在一个共享内存的Node进程中，加入了大量无用功能。
- **资源浪费**：占用无谓的硬盘空间，并急速消耗token和内存资源。

## NanoClaw的核心优势
### 轻量级与简洁性
- 核心代码量极少，仅约2000行。
- 采用单个进程，仅包含少数几个核心文件。
- **彻底无配置文件概念**：所有定制化需求均通过“Skills（技能）”系统完成。

### 安装与配置步骤（实操指南）
1. **基本安装**：只需执行三句话即可搭建一个私人助理。
   - 运行 `setupCloud Code` 命令。
   - 该命令会自动处理一切，包括：依赖安装、身份验证、容器设置和服务配置。
   - 整个安装过程无需手动编写任何配置文件。
2. **以接入Telegram为例的定制步骤**：
   - 在控制台输入 `AD Telegram` 命令。
   - 接下来，AI会自动完成以下操作：
     1. 读取对应的Skill文档。
     2. 自动安装相关依赖包。
     3. 自行修改源代码，添加Telegram的消息处理逻辑。
     4. 自动配置好Bot Token。
     5. 甚至帮你完成联通性测试。

### 高度灵活的定制能力
- 支持完全自由的定制：用户可以直接用自然语言向Cloud Code下达指令，例如：
  - 想修改触发词
  - 想添加问候语
  - 想定期存储摘要
  - 直接说出需求即可实现。

### 优越的安全性
- 与底层Docker容器进行隔离，天然具备操作系统级别的安全隔离。
- 这一特性省去了OpenClaw常见的安全问题（如“月全”问题）。

### 先进的Agent Swarms支持
- NanoClaw是首个支持“Agent Swarms（智能体群）”的AI助手。
- 其创始人Gabriel Cohen提出了三个颠覆性开发理念：
  1. **“不重复造轮子”原则已过时**：AI在修改共享函数时往往不考虑下游连锁反应，因此适度的代码重复反而成了最简单有效的物理隔离手段。
  2. **严格的文件行数限制已过时**：与其让AI在多个文件间反复横跳，不如让它在一个稍长的文件里完成整件事。
  3. **代码无需经得起时间考验**：只需满足当前需求即可，因为六个月后更强大的下一代模型会直接帮你将整个系统重写一遍。

## 总结
NanoClaw并非一个包罗万象的臃肿框架，而是追求极致的简洁与高性能。它通过极简的架构、无配置的设计、强大的Skills定制系统以及先进的Agent Swarms理念，让用户能够轻松打造属于自己的数字化助手。这标志着属于个人AI的黄金时代正式开启。

---

## 原始字幕

卸载OpenCloud拥抱NanoCloudAI大神Karpathy最近公开表示NanoCloud的配置方式让它大开眼界我也去体验了一下只有一个结论卸载OpenCloud拥抱NanoCloudAI大神Karpathy最近公开表示NanoCloud的配置方式让它大开眼界我也去体验了一下NanoCloud只有一个结论卸载OpenCloud拥抱NanoCloudOpenCloud就不用吐槽了软件质量跟屎一样每天都能遇到不同的bug甚至连一个简单的定时任务都能报错OpenCloud真的太重了它有超过52个模块45个依赖项为了适配15个不同的渠道商设计了厚厚的抽象层最后所有的东西都挤在一个共享内存的Node进程里里面加了一堆永远用不到的功能占用无谓的硬盘空间急速消耗token和内存NanoCloud的做法完全不一样它的核心只有大约2000行代码只有一个进程少数几个核心文件安装也是简单到不能再简单只用三句话就可以搭建一个私人助理然后运行到setupCloud Code会处理一切依赖安装身份验证容器设置服务配置整个安装过程不需要你写一行配置因为它根本没有配置文件这个概念所有的定制化需求全部通过Skills技能来完成以接入Telegram为例在OpenCloud里你需要去后台开启开关填入参数但在NanoCall里你只需要在控制台输入AD Telegram接下来AI会自动读取Skill文档自己安装依赖包自己修改原码加上Telegram的消息处理逻辑自己配好Bot Token甚至帮你跑完联通性测试NanoCore支持完全自由的定制直接用大白话告诉Cloud Code你的需求想改触发词想加问候语想定期存摘要直接下达指令它的安全性也更好和底层Docker容器进行隔离天然具备操作系统级别的隔离杀箱完全省去了OpenClaw月全的问题更重要的是NanoClaw是首个支持Agent Swarms智能体积群的AI助手NanoClaw创始人Gabriel Cohen提出了三个颠覆性理念第一Jerry不重复造轮子的原则过时了AI修改共享函数时不会考虑下游连锁反应适度的代码重复反而成了最简单有效的物理隔离第二严格的文件行数限制过时了与其让AI在多个文件间反复横跳不如让它在一个稍长的文件里把整件事干完第三代码不需要经得起时间的考验只要满足当下需求即可六个月后更强大的下一代模型会直接帮你把整个系统重写一遍整体来讲NanoClock不是一个企图包罗万象的臃肿框架它追求极简与性能相信你能通过它轻松打造数字化助手属于个人AI的黄金时代现在才正式刚刚开场