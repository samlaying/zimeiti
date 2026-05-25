---
title: "Paperclip Routines - 让“零人公司”每天自动干活"
author: "五里墩茶社"
source: https://www.bilibili.com/video/BV1KPDcBTEwc
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI
  - 自动化
  - 定时任务
  - 工具
  - 效率提升
type: video-note
bvid: BV1KPDcBTEwc
duration: "8:44"
cover: "http://i1.hdslb.com/bfs/archive/f58925fc26db9c039709f4614b359fadf57d1d84.jpg"
description: "一个key用全球大模型🔴 https://DMXAPI.cn 🚀 国内直连OpenAI、Claude、Gemini，💰￥1元起充！  - 加入我的知识星球：https://t.zsxq.com/W5Oj7  上期我们用 Paperclip 搭了一个 AI 公司，但每次都要手动唤醒 Agent。这期解决这个问题 —— 用 Routines 让 Agent 自动定时干活。每天自动 code review、每周自动出周报、GitHub push 自动跑测试，全程不用你操心。  Paperclip 系列第二期，从创建到配置到演示，完整流程。  项目地址：https://github.com/paper"
---

# Paperclip Routines - 让“零人公司”每天自动干活

> [五里墩茶社](https://space.bilibili.com/615957867) | [BV1KPDcBTEwc](https://www.bilibili.com/video/BV1KPDcBTEwc) | 时长 8:44

## 引言
- Paperclip 是一个用于构建AI公司的工具，在上期视频中，用户创建了具有CEO、CTO、CMO等角色的AI公司，能够自动执行任务。
- 但存在一个问题：每次任务执行都需要手动创建issue，这限制了自动化程度，无法实现定时或事件驱动的任务。

## 问题：手动触发的局限
- 手动创建issue导致任务需要人工干预，效率低下。
- 无法自动化常见场景，例如：
  - 让CTO每天早上9点自动进行code review。
  - 让CEO每周一自动出一份周报。
  - 当GitHub有新的Push时，自动触发测试。

## 解决方案：Paperclip Routines
- Routine 是 Paperclip 内置的定时任务系统，作为视频系列的第二期内容，专注于自动化任务管理。
- 它旨在解决手动触发问题，让AI公司能实现“零人公司”的自动运行。

## Routine 的工作原理
- Routine 是一个任务生成器，每次执行时会自动创建一个新的issue。
- 创建的issue会被分配给指定的agent（如CTO、CEO等）。
- 分配后，系统会立刻唤醒该agent来处理任务，无需手动介入。

## 具体应用场景和例子
- **定时任务示例**：
  - CTO 每天早上9点自动执行code review，通过Routine设置定时触发。
  - CEO 每周一自动出一份周报，Routine确保任务按计划执行。
- **事件触发任务示例**：
  - 当GitHub仓库有新的Push时，Routine自动创建issue并分配测试任务，触发自动化测试。
- 这些场景展示了Routine如何支持多样化自动化需求。

## 类比和理解
- Routine 可以理解为类似cron job的定时任务工具，但更集成于AI工作流。
- 与传统cron job不同，它创建的不是脚本，而是issue，并分配给AI agent处理，增强了任务的可管理性和自动化程度。

## 总结
核心要点：Paperclip Routines 是一个自动化任务系统，通过定时或事件触发自动创建issue并分配给AI agent，解决了手动干预的局限，让“零人公司”能每天自动干活，显著提升任务执行效率和自动化水平。

---

## 原始字幕

上期视频,我们用PaperClip搭了一个AI公司,有CEO,CTO,CMO,并且能够自动的帮助我执行任务。但有个问题,每次都要我手动创建issue,才能让agent干活。如果我想让CTO每天早上9点自动做一次code review,如果我想让CEO每周一自动出一份周报呢?或者如果GitHub有了新的Push就自动触发测试呢这就是RoutinePayPalClip内置的定时任务系统能够支持的场景大家好我是小木头这期是PayPalClip系列的第二期Routine是任务生成器每次Routine执行它会自动创建一个新的issue分配给指定的agent然后立刻唤醒那个agent来处理你可以把它理解成quangjob但创建的不是一个脚本之下