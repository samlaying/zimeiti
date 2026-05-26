---
title: "第一时间速测，国产模型开启Agent Teams（Claude Code的Agent蜂群模式）"
author: "小天fotos"
source: https://www.bilibili.com/video/BV1EKFEzwEiP
date: 2026-05-26
tags:
  - bilibili
  - 笔记
  - AI
  - Agent Teams
  - 模型测试
  - 国产模型
  - 效率提升
type: video-note
bvid: BV1EKFEzwEiP
duration: "2:07"
cover: "http://i2.hdslb.com/bfs/archive/56a150de7c24151dddedad5dc64fbebc4ba50765.jpg"
description: "GLM4.7,Kimi K2.5 Minimax M2.1都成功开启Agent Teams 看来用量最足的GLM要被薅秃了  Qwen3 Coder Next Q4和 GLM 4.7 Flash Q4 可能因为配置问题 暂时测试失败无法开启蜂群，回头研究下看看能解决不"
---
/
# 第一时间速测，国产模型开启Agent Teams（Claude Code的Agent蜂群模式）

> [小天fotos](https://space.bilibili.com/28554995) | [BV1EKFEzwEiP](https://www.bilibili.com/video/BV1EKFEzwEiP) | 时长 2:07

## 引言
本笔记基于UP主小天fotos的视频“第一时间速测，国产模型开启Agent Teams（Claude Code的Agent蜂群模式）”，总结了对国产模型Agent Teams功能的测试情况。Agent Teams类似于Claude Code的蜂群模式，可同时启动多个代理执行任务，测试旨在验证国产模型的兼容性和效果。

## 设置与启动步骤
### 前置条件
- **升级模型版本**：确保使用的模型升级到最新版本，这是支持Agent Teams功能的基础。
- **配置Settings.json文件**：在Cloud目录中的Settings.json文件中，将相关设置项（如标志位）设为1，以启用Agent Teams功能。字幕中具体指“设成1”，可能是一个启用开关。

### 具体操作流程
1. **准备环境**：确认模型已更新，并定位到Cloud目录。
2. **编辑配置文件**：打开或创建Settings.json文件，将指定字段设置为1（具体字段需根据模型文档，但视频中未详细说明）。
3. **启动测试**：启动模型并输入统一提示词（prompt），以创建Agent Teams。提示词示例为：“创建一个Agent Teams调查一个人调查本地代码一个调查PR还有一个调查其他的repo”，这指示代理同时处理多个任务。
4. **观察启动过程**：在运行中观察代理是否成功启动，视频显示启动后会出现多个代理实例（如“启动了两个了三个”），每个代理可能负责不同任务。

## 测试模型与结果
### 成功启动的模型
- **GLM4.7**：成功启动Agent Teams。测试中直接使用提示词后，代理快速启动并显示多个实例（如“启动了两个了三个”），表明功能运行正常。
- **Kimi K2.5**：成功启动，但启动过程较慢（字幕提到“KIMI是不是用的人多是不是好慢”）。最终也支持Agent Teams，启动后代理聪明地执行任务。
- **minimax M2.1**：成功启动，但过程中遇到问题。首次启动时出错（字幕：“出错了他现在启动的是task”），第二次重试后成功（“这次好了有时候会出错”）。测试显示代理先搜索项目、克隆本地，然后启动任务，需注意错误处理。

### 失败或未成功的案例
- **GLM4.7flash**：测试失败，未成功启动Agent Teams。UP主提到“我也试了一下也不行”，但未详细演示，计划后续测试。
- **本地部署的小模型**：目前实验未成功，UP主表示“目前我还没有实验成功”，暗示可能需要更多配置或模型能力不足。

### 关键数据与观察
- **版本要求**：所有测试均基于最新版本模型，强调更新的重要性。
- **启动行为**：代理启动时显示为独立实例，如GLM4.7测试中“启动了两个了三个”，Kimi K2.5和minimax M2.1也类似。
- **错误与重试**：minimax M2.1测试中出错后通过重试成功，提示在实操中可能需要耐心和调试。

## 总结
核心要点：国产模型GLM4.7、Kimi K2.5和minimax M2.1已初步支持Agent Teams功能（类似Claude Code的蜂群模式），通过升级版本和正确配置Settings.json文件即可启动。测试中模型能同时处理多个任务（如调查本地代码、PR和其他repo），但启动速度和稳定性因模型而异，GLM4.7flash和本地小模型暂不支持。建议用户及时更新模型，并在遇到错误时尝试重试。UP主计划进一步测试GPTOSS等其他模型，以扩展兼容性范围。

---

## 原始字幕

朋友们我给你们速度测试一下Cloud的最新的这Cloud Code最新支持的这个Agent Teams我们看一下版本是最新要升到最新的版本你的这个Cloud目录里的Settings.json看到没有这个要设成1好吧我们来启动我先测第一个GRM4.7我的prompt就是创建一个Agent Teams调查一个人调查本地代码一个调查PR还有一个调查其他的repo好吧我们来看一下效果它能不能启动看看到没有这就是启动的特点现在启动了两个了三个看到没有每一个是不同的我们再回到主的好吧这是质朴的grm4.7我们现在在启动一个KIMI还是同样的promptKIMI是不是用的人多是不是好慢搜一下它试啥再去启动也挺聪明的看KIMI K2.5也可以了也是支持的好我们关了我们继续来测我们现在测的是minimax m2.1还是同样的prompt他先搜索了一下找到了我的项目我在克隆道本地了这不遵循指令吗好了他现在准备开始启动了出错了他现在启动的是task我们再给他一次机会他这次直接启动看看是不是这次好了有时候会出错好minimax也是成功通过我们现在有coding plan的这三个主流的模型一个是GLM4.7Kimi K2.5minimax M2.1都是能启动这个agent teams但是本地部署的小模型目前我还没有实验成功刚才那个GLM4.7flash我也试了一下也不行我就不给大家演示了这个我后面再测一下明天再试试什么GPTOSS之类的好了谢谢大家