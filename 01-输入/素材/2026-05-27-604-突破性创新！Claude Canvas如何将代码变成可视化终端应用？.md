---
title: "突破性创新！Claude Canvas如何将代码变成可视化终端应用？"
author: "4zapi"
source: https://www.bilibili.com/video/BV12K6DBQEeh
date: 2026-05-27
tags:
  - bilibili
  - 笔记
  - AI
  - 终端工具
  - Claude Code
  - 效率提升
  - 可视化
type: video-note
bvid: BV12K6DBQEeh
duration: "8:24"
cover: "http://i0.hdslb.com/bfs/archive/19d78fa8498c1a2a31bdd619f1b1d44e758091e2.jpg"
description: ""
---

# 突破性创新！Claude Canvas如何将代码变成可视化终端应用？

> [4zapi](https://space.bilibili.com/3546872771774829) | [BV12K6DBQEeh](https://www.bilibili.com/video/BV12K6DBQEeh) | 时长 8:24

## Claude Canvas概述
- Claude Code 是一个强大的 AI 编程代理，运行在终端中，能够处理复杂任务并主动升级开发工作流。
- 新一代框架如 Ralph Loops 的持久执行模型和 AutoCode 的自主规范驱动子代理，进一步增强了 Claude Code 的能力。
- Claude Canvas 是一个 TUI（终端用户界面）工具包，为 Claude Code 提供专用显示，相当于 AI 代理的“外部监视器”。
- 它能在终端内生成丰富的交互式界面，用于处理电子邮件、日历管理、航班预订等任务，提升用户体验和效率。

## 核心功能
- **可视化终端界面**：Claude Canvas 能够在终端中绘制交互式界面，使复杂信息（如邮件字段、日历日程、航班详情）更直观。
- **双向通信**：界面与 Claude Code 之间支持实时双向数据交互，允许用户直接操作界面（如点击确认）并将结果反馈给 AI。
- **键盘与鼠标支持**：用户可以通过键盘导航或鼠标点击进行交互，模拟传统图形界面体验。

## 使用场景与例子
### 电子邮件起草
- **问题**：在对话模式下撰写邮件不够直观，缺乏传统邮件客户端的字段显示。
- **解决方案**：Claude Canvas 可生成邮件编辑界面，可视化显示发件人、收件人、抄送、密送、主题和消息内容。
- **具体例子**：用户要求 Claude 起草给联合创始人 Mark 的邮件，Canvas 生成界面后，用户可以实时编辑并迭代内容；还能添加其他收件人（如 Jason）以优化邮件。
- **优势**：提供熟悉的邮件布局，提升撰写效率和准确性。

### 会议预订
- **问题**：当使用工具（如 Google Calendar）查看多人可用时间时，对话式解释难以跟踪。
- **解决方案**：Claude Canvas 提供可视化场景，直观显示人们的可用时间段。
- **具体例子**：用户需要与两人安排会议，Canvas 以图形化方式展示日历，并允许用户选择时间；点击后确认预订，信息双向同步到 Claude Code 和日历工具。
- **优势**：简化复杂日程安排，减少认知负担。

### 航班预订
- **问题**：航班预订涉及大量信息（如座位图、选项比较），在对话中不易管理。
- **解决方案**：Claude Canvas 创建航班信息界面，可视化显示座位图、航班详情和比较视图。
- **具体例子**：用户查询去丹佛的航班选项，Canvas 展示座位图和关键信息（如价格、时间），并支持对比不同航班选项；用户可关闭界面以完成操作。
- **优势**：将复杂数据转化为直观视觉展示，辅助决策。

## 安装与设置步骤
1. **前提条件**：确保 Claude Code 已在终端中运行（需在 macOS 系统上）。
2. **安装插件**：
   - 在 Claude Code 中使用命令 `/plugin marketplace` 添加 Claude Canvas 插件。
   - 安装选项：可选择用户范围（仅当前用户）或工作空间范围（所有协作者）；建议从用户范围开始。
3. **验证安装**：安装完成后，Claude Canvas 会出现在已安装插件列表中。
4. **配置终端**：Claude Canvas 利用 Tmux 和 macOS 原生终端窗口/窗格 API 进行界面渲染。
5. **扩展支持**：存在一个 Fork 仓库可用于其他终端（如 iTerm2 和 Apple Terminal），但可能有限制。
   - 注意：当前版本仅适用于 macOS，不支持 Windows，且远程或可移植性较差。

## 局限性与注意事项
- **系统限制**：Claude Canvas 依赖 macOS 的原生终端 API，因此仅限于 macOS 用户；Windows 系统不支持。
- **可移植性**：在远程环境或非 macOS 设备上可能无法正常工作，限制了便携性。
- **格式化问题**：在某些终端（如非 macOS 终端）中，界面渲染可能不够完美（如日历显示偏移），需优化格式设置。
- **依赖项**：必须保持 Claude Code 在终端中激活，并确保所有相关技能（如 Tmux 集成）已安装。

## 总结
Claude Canvas 是一个突破性工具，通过将 Claude Code 的功能扩展为交互式终端可视化界面，显著提升了 AI 编程代理在非编码任务（如邮件处理、日程管理、旅行预订）中的效率和用户体验。它利用 TUI 技术在终端内模拟图形界面，支持实时编辑和双向通信，但目前仅适用于 macOS 系统。安装过程简单，只需通过插件市场添加即可；整体而言，这个工具代表了 AI 代理向更直观、高效工作流进化的重要一步。

---

## 原始字幕

AutoCode is already one of the most powerful AI coding agents that's out there, living inside your terminal handling insane levels of complexity and actively upgrading your entire development workflow. But lately, a new generation of frameworks have emerged that supercharge it even further. From Ralph Loops' persistent execution model to AutoCode's autonomous spec-driven subagents, AutoCode just keeps evolving. and today I want to showcase the next big upgrade. This is where I would like to introduce Quad Canvas. This is a Tui toolkit that gives Quad Code its own dedicated display, essentially an external monitor for your AI agent. It spawns rich interactive terminal interfaces for things like emails, calendars, flight bookings, and so much more, all directly within your terminal. Let's take a look at this demo.so a lot of people are discovering clawed code right now and they're using it for things other than coding and i'm also using clawed code as like a personal agent and to help me run my business draft an email to my co-founder mark uh saying that i'm really excited to see him when he comes to the bay area at the end of january so i was using clawed code to draft emails and i didn't like the experience of working on emails in a conversation so i thought what if clawed had its own monitor. What would that mean? So I created a skill called Claude Canvas that lets Claude spawn new panes where it can draw interactive interfaces. And this is just a simple example. Like when I'm writing emails to people, I like to see from to CC, BCC subject, and the message. Oh, Jason's coming as well. Be sure to include him in the email. So this helps me iterate in the way that I like. And so yeah, this is how I like to compose emails with Claude.it research that any of the people, あと、再度 Impf解釈予告达他的考慮。 łat bipartisan um with oursee to chea this week to talk to them about an upcoming project let's find a time they're both you know,別 Bess wasanother use case that I hadwhich was like booking a meeting with someoneand I have tools that give CloudCode accessto Google Calendarbut when it explainedmutual availability in the conversationit was kind of hard to keep track ofso this is CloudCanvaswith a specific scenario forvisualizing when people might be availableand CloudCodeit really embraces the terminal so all this is rendering in the terminal and you can use your keyboard to find a time or you can click and it's going to give me a second to confirm itand it's confirmed and that information is communicating two way with GLOT so it can come back and forth and let's see one more I need to book a flight to Denver this week what are some options. One more use case I had was my dream is that one of these agents will book travel for me. That just seems like the obvious low-hanging fruit or first use case for agents. But, you know, there's a lot of information when you're booking a flight. So this is a scenario in Cloud Canvas for showing flight information. And it's pretty basic, but, you know, it shows the seat map and all the little pieces of information I might care about. And then, you know, if I want to compare different flight options, it sort of visualizes it all in this contract way and I can close it.所以,那是我的第一次的 scenarios在 Cloud Canvas我會開放開的方式是一個鍵的鍵你會想試謝謝謝謝謝謝 David 為了其實在做這個鍵開放開我會把他的資料放開但要開始你會有幾個要求你會要有關的你會有關的用到來玩的 skills而是Tmux的Canvases在因為因為這個所以你會有這些 installed你必须要保持有 Cloud Code充滞在标策上的标策所以你能用它但是有趣的事情你能用这个Fork repo有人能用到另一种项目的ClaudCanvas但是这一种用 iTerm2和AppleTerminalwell. With this, you have it so that it is definitely only for macOS-specific users, but it uses a native terminal window and a pane API. It is also going to be having you auto-position canvases automatically. It has a smoother UX with this, but it is something that won't work for Windows, which is the only downside. And it won't work remotely and less portable in this particular use case.只要重新加坛,如果您不存在的 Cloud Code,我会在这里留下,因为您会需要这个开始了但是,你会有 Cloud Code开放在你的 Terminal你可以做这个,你可以在旁边You can then go ahead and install this plugin,by using the slash plugin marketplace commandto add the cloud canvas to your cloud code afterwards you'll see that it has been addedand now what you got to do is install the canvas plugin and you can use the following command to do that as well you have the option to install it for your own users scope or for all the collaborators of your workspace i'm going to be doing it for my scope and then once it has been installed we can大家只是教音っていう,還能夠 FOA,你開ora一點不是我在 ignoredWhat would evolved那個人不要最有意思しか muy開始先生,沒想到我想яться kier上有個功能發放著個這個是按燃完回那就,我們改善文这种最为 let you Juice HerALook it's going to be本当 in x'on the new eineke Powelli可以写淡一办情 ia分享或是在某台上 экails or it could be something where you're tracking a to-do list but you're going to have a better experience essentially with whatever sort of tasks that you're working with cloud code here is an email draft that it had created and you can see that you can visualize this directly within cloud code and you can make changes directly live in preview with this canvasso this is just another view this is just a calendar app that was fully visualized within our cloud code session not an app that it created but thanks to tmux it was able to visualize all of the dates now it looks a little off because i don't have it properly formatted but you can see that you get a good idea of what you can do with this canvas you can visualize things you can write up emails and even have it work on flight details and sinceI believe my output isn't properly structured whereas on macOS you get a better generationwith team tyma and you can see that a flight booking terminal looks absolutely amazingin this case on a macOS device if you liked this video and would love to support the channelyou can consider donating to my channel through the Super Thanks option below or you can consider joining our private discord where you can access multiple subscriptions to different ai tools for free on a monthly basis plus daily ai news and exclusive content plus a lot more but that's basically guys for today's video on cloud canvas this is just a small toolkit that you can easily get started with that will definitely elevate your cloud code experience these frameworks i'm showcasing nowadays are definitely things that you should take a look at because it truly enhances your overall development workflow a lot better so i'll leave all these links in the descriptioni'll see you guys really shortly