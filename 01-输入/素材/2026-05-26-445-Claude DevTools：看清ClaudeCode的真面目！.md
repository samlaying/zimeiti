---
title: "Claude DevTools：看清ClaudeCode的真面目！"
author: "ValleyAI"
source: https://www.bilibili.com/video/BV1iQZQBQEvf
date: 2026-05-26
tags:
  - bilibili
  - 笔记
  - AI开发工具
  - Claude Code
  - 调试工具
  - 开源
  - 效率提升
  - 前端工具
type: video-note
bvid: BV1iQZQBQEvf
duration: "3:21"
cover: "http://i0.hdslb.com/bfs/archive/09814a66dd65d318d10f482196aacb2ccd5eb9f4.jpg"
description: "用Claude Code写代码，却不知道它偷偷读了什么文件、改了什么代码、token花在哪？   Claude DevTools 是一个开源的可视化调试工具，不修改Claude Code本身，零配置即装即用：  🔍 上下文可视化 — token消耗7维度拆解，花哪了一目了然  📊 压缩可视化 — 上下文压缩前后对比，不再黑盒  🔔 自定义通知 — 敏感文件被访问立即提醒  🛠️ 工具调用检查器 — 每一步操作都有详细展开   GitHub：github.com/matt1398/claud e-devtools  完全本地运行，不上传任何数据，MIT开源   📌 ValleyAI — 硅谷+中"
---

# Claude DevTools：看清ClaudeCode的真面目！

> [ValleyAI](https://space.bilibili.com/479792004) | [BV1iQZQBQEvf](https://www.bilibili.com/video/BV1iQZQBQEvf) | 时长 3:21

## Claude DevTools 简介
### 工具概述
- **什么是Claude DevTools**：一个开源工具，专门用于增强Claude Code的调试体验，帮助开发者看清Claude Code背后的执行细节。
- **作用背景**：使用Claude Code时，最新版隐藏了大量执行细节（如文件读取和修改的模糊摘要），开发者难以理解上下文占用和子Agent执行情况。
- **核心设计理念**：不修改Claude Code本身，而是读取其已有的日志文件（位于Home目录下的.claude文件夹），实现零配置、无需API Key或登录，安装即可使用。
- **支持平台**：Mac、Windows和Linux，采用MIT开源协议。

## 核心功能详解
### 上下文可视化
- **功能描述**：将Claude Code每轮对话的Token使用量进行完整拆解，分为七个维度，清晰展示Token花费位置。
- **七个维度**：
  1. Claude.md配置文件
  2. 技能激活
  3. 文件引用
  4. 工具调用
  5. 扩展思考
  6. 团队协调
  7. 用户提示
- **价值**：帮助开发者理解上下文占用情况，优化Token使用效率。

### 压缩可视化
- **功能描述**：当Claude Code达到上下文限制时自动压缩内容，Claude DevTools检测每次压缩边界，量化压缩前后的Token变化。
- **作用**：展示上下文如何从填充到压缩再填充的完整过程，避免开发者对压缩内容一无所知。

### 自定义通知
- **功能描述**：允许用户设置规则，当Claude Code执行特定操作时立即提醒。
- **具体例子**：
  - 访问环境变量文件（如.env）。
  - 操作支付相关代码。
  - Token用量异常（如超过阈值）。
- **价值**：增强安全性，及时警报潜在风险。

### 工具调用检查器
- **功能描述**：为每个工具调用提供专门的查看器，确保开发者无需猜测Claude Code背后的行动。
- **查看器细节**：
  - **文件读取**：语法高亮和行号显示。
  - **代码编辑**：内联差异对比（类似Git diff）。
  - **命令执行**：完整输出展示。
  - **子Agent**：可展开的执行树结构。
- **实用示例**：当Claude Code调用子Agent套用五层时，可展开查看每层执行细节。

## 技术特点与安全设计
- **技术栈**：使用Electron + React + TypeScript开发，代码质量高。
- **安全设计**：完全在本地运行，不发送任何数据到外部服务器，确保隐私安全。
- **日志来源**：支持分析所有来源的日志，无论开发者是在终端、IDE还是其他工具中使用Claude Code。

## 与其他工具对比
- **主要区别**：与Conductor或CraftAgents等GUI包装工具不同，Claude DevTools不修改Claude Code的行为，而是专注于分析现有日志。
- **适用场景**：适合所有重度使用Claude Code的开发者，提供深度调试和可视化功能。

## 使用建议与项目状态
- **项目状态**：截至视频发布时，项目上线仅10天，已获得500多个GitHub star，增长迅速。
- **使用建议**：强烈建议Claude Code用户前往GitHub搜索“Claude-DivTools”试用，以提升调试效率和代码透明度。
- **实操步骤**：虽然字幕未详细列出步骤，但根据描述，大致步骤为：
  1. 访问GitHub项目页面（搜索Claude-DivTools）。
  2. 下载或克隆仓库。
  3. 安装并启动工具（无需额外配置，直接读取.claude日志文件）。
  4. 在Claude Code运行时，通过DevTools界面查看可视化信息。

## 总结
Claude DevTools是一个创新的开源调试工具，通过可视化Claude Code的Token使用、压缩过程、工具调用和自定义通知，解决了开发者在使用Claude Code时面临的细节不透明问题。它不修改原工具，安全本地运行，并提供多维度分析，帮助开发者优化工作流程、增强安全性和提升效率，特别适合重度Claude Code用户快速上手尝试。

---

## 原始字幕

大家好,欢迎来到Valley AI。今天给大家介绍一个让我眼前一亮的开源工具,Cloud DevTools。如果你用Cloud Code写代码,这个工具可能会彻底改变你的调试体验。用过Cloud Code的人都知道,最新版把很多执行细节藏起来了。你只能看到,读取了三个文件,编决了两个文件这种模糊的摘要,却不知道具体读了什么改了什么上下文填满了也不知道是什么占的子Agent套完了五层你根本看不到里面在干嘛Claude DevTools用了一个非常巧妙的方案他完全不修改Claude Code本身他只是读取Claude Code已有的绘画日志文件也就是你Home目录下的.claude文件夹零配置不需要API Key要登录,装上就能用。第一个杀手机功能是上下文可视化,它把Cloud Code每轮对话的Token使用量做了完整的拆解,分成七个维度,cluade.md配置文件,技能激活,文件引用,工具调用,扩展思考,团队协调,用户提示,你可以清楚地看到Token都花在了哪里。第二个功能是压缩可视化,当Cloud Code达到上下文限制时会自动压缩但你完全不知道压缩了什么Cloud DevTools会检测每次压缩边界量化压缩前后的Token变化让你看到上下文是怎么填充压缩再填充的完整过程。第三个功能是自定义通知。你可以试制规则,比如当Cloud Code访问了你的环境变量文件,操作了支付相关的代码,或者Token用量异常时,它会立即提醒你。这对安全性来说非常重要。第四个功能是工具跳用检查器每个工具跳用都有专门的查看器文件读取有语法高量和行号代码编辑有内联差异对比命令执行有完整输出子Agent有可展开的执行术再也不用猜Cloud Code背后到底做了什么技术上它用的是Electron加React加TypeScript代码质量很高安全设计也很严格完全在本地运行不发送任何数据到外部支持Mac Windows和LinuxMIT开源协议和其他Cloud Code的GUI包装工具比比如Conductor或CraftAgents最大的区别是它不修改Cloud Code的行为而且能分析所有来源的绘画不管你是在终端IDE还是其他工具里用的适合所有重度使用Cloud Code的开发者这个项目上线才10天就拿到了500多star增长非常快如果你在用Cloud Code强烈建议去GitHub上搜Cloud-DivTools试一试觉得有帮助的话点个赞关注Valley AI下期见