---
title: "Claude Code重磅更新！新增TASKS功能，彻底告别死循环，效率起飞！"
author: ""
source: https://www.bilibili.com/video/BV17WzMB7Egn
date: 2026-05-26
tags:
  - bilibili
  - 笔记
  - AI编程
  - 效率提升
  - Claude Code
  - 任务管理
  - 工具更新
  - 项目管理
type: video-note
bvid: BV17WzMB7Egn
duration: "0:00"
cover: ""
description: ""
---

# Claude Code重磅更新！新增TASKS功能，彻底告别死循环，效率起飞！

> [](https://space.bilibili.com/) | [BV17WzMB7Egn](https://www.bilibili.com/video/BV17WzMB7Egn) | 时长 0:00

## Claude Code TASKS功能详解

### 背景与问题
- **Opus 4.5升级**：Claude Code的底层模型Opus 4.5更擅长自主运行较长时间，使得原有TODO功能对小任务变得不必要。
- **TODO功能的局限性**：
  - 所有数据存储在内存中，关闭会话后TODO列表丢失。
  - 子代理（sub-agents）无法访问主代理的TODO列表，导致跨会话和多代理协调困难。
  - 无法定义任务依赖关系，例如“任务C必须在任务A和任务B完成后才能开始”。

### TASKS功能介绍
- **核心目标**：解决大型项目中的任务管理、依赖定义和跨会话协作问题。
- **关键特性**：
  - **任务依赖支持**：通过元数据定义任务间关系，如“任务D依赖任务C，任务E不依赖”，模拟实际项目工作流程。
  - **跨会话与子代理协作**：多个Claude Code会话或子代理可共享同一任务列表；一个会话的更新会实时广播到所有相关会话，实现并行化工作。
  - **持久化与共享**：通过环境变量设置任务列表ID，确保会话关闭后任务状态不丢失，并能跨实例协调。

### 工作原理与使用方式
- **环境变量配置**：
  - 设置环境变量`claud_code_task_list_id`为任意名称（例如`groceries`）。
  - 启动Claude Code，所有使用相同ID的会话将共享同一任务列表。
  - 适用于CLI模式（claude -p）和Agent SDK。
- **操作示例**：
  1. 定义项目需求。
  2. 让Claude将需求分解为多个任务，并明确任务依赖关系。
  3. 启动多个子代理，每个处理任务树中的独立分支。
  4. 子代理在各自上下文窗口中工作，但通过共享任务列表同步进度。

### 使用场景与工作流程
- **适用场景**：
  - 小任务（如重构函数或修复bug）：无需TASKS功能，Claude可自主处理。
  - 大型项目（如构建完整功能、大规模重构、创建测试套件）：TASKS功能可显著提升效率。
- **推荐工作流程**：
  - 使用TASKS定义项目任务和依赖。
  - 结合Git WorkTree进行分支隔离和自动PR创建（可与Ralph Wiggum插件互补）。
  - 通过并行子代理加速开发，避免重复工作或冲突。

### 与现有工具对比
- **Ralph Wiggum插件**：
  - 通过停止钩子（stop hook）强制Claude循环直到任务完成，但本质是单任务循环hack。
  - 不支持多任务、依赖管理或跨会话协调。
- **TASKS功能优势**：
  - 官方集成，原生支持多任务、依赖定义和跨代理协作。
  - 将“持续工作直到完成”的理念架构化，支持更复杂的项目管理。

### 优缺点与反馈
- **优点**：
  - 核心功能扎实，解决了自主AI编程中的关键协调问题。
  - 支持并行化，提升大型项目效率。
- **缺点与改进建议**：
  - **文档不足**：当前文档稀疏，需完善。
  - **缺乏界面**：建议开发仪表板（dashboard）以可视化任务进度和依赖。
  - **配置不便**：环境变量设置略显笨拙，希望未来添加斜杠命令（如`/tasks share groceries`）简化协作。

### 总结
核心要点：Claude Code的TASKS功能通过支持任务依赖定义、跨会话和子代理的实时协作，彻底解决了大型项目中AI编程的协调问题。它将AI从单一助手升级为可管理的团队，代表了AI编码工具向项目管理集成的趋势，显著提升了自主工作的效率和可靠性。

---

## 原始字幕

字幕志愿者 李宗盛 here's the deal as opus 4.5 got better at running autonomously for longer periods anthropic noticed something interesting the total right tool became kind of unnecessary for smaller tasks claude already knew what it needed to do it didn't need a checklist for simple stuff but for bigger projects for stuff that spans multiple sessions or involves multiple sub-agentsTODOS were completely uselessthink about itwith TODOSeverything lived in memoryif you closed your sessionyour TODO list was goneif you spun up a sub-agentit had no idea what the main agent was working onif you tried to coordinate workacross multiple Claude code sessionsyou were basically yelling into the voidtasks fix all of thatnow我要拼 Christopher目的能力一要放心該慶野一切出 różnych代表我會有這就著牌ALG的這 fünf7來 McKinke include подар我給你你的發還沒必要今天的呢 details因為提出還是因為只要消失拼 handler相對統 by todas全部都是一座列TASK A, TASK B, TASK C但真正的事啊但真正的事啊甚至TASK C不能始終TASK A和TASK Bhat Sometimes Task C can't start until Task A and Task B are done Sometimes Task D depends on Task C but Task E doesn't Tasks let you define these relationships in the metadata which mirrors how actual projects work Third and this is the big one Tasks enable collaboration across sessions and subagentsWhen you spin up multiple subagents or run multiple Cloud Code sessions, they can all work on the same task list.When one session updates a task, that change is broadcasted to all other sessions working on the same list.This is huge for parallelization.You can have one subagent working on the auth system, another on the database schema, and a third on the tests.They all see the same task list.they all know what's been completed and what's still pendingno more duplicate workno more agents stepping on each other's toesnow here's where it gets interestingremember my video on the ralph wiggum loopthat plugin where you trap claude code in a loopuntil it actually finishes the jobwelltasks are essentially the official versionof what ralph was trying to do but is built directly into Claude code let me explain Ralph Wiggum uses a stop hook to intercept Claude's exit attempts every time Claude tries to stop the hook blocks the exit and re-injects the original prompt it keeps going until the task is actually complete the problem was Ralph was essentially a hack a clever hack but still a hack它 didn't have any concept of multiple tasks, dependencies, or coordination. Tasks take that same philosophy of keep going until it's actually done and integrate it properly into Claude Code's architecture. Instead of one task in a loop, you can have 10 tasks with complex dependencies. Instead of one session banging its head against a problem, you can have multiple sessions and sub-agents dividing and conquering. And the best part? You can control this with an environment variable. If you want multiple sessions to collaborate on the same task list,you just set claud underscore code underscore task underscore list underscore id equals whatever name you want and then start claudall sessions using that same id will see and update the same tasksthis also works with claud-p for the cli mode and with the agent sdkso if you're building automation on top of claud codeyou can coordinate work across multiple instancesnow let me talk about when you'd actually use thisfor small tasksyou probably don't need tasks at allif you're just asking Claude to refactor a functionor fix a bugjust ask itClaude's smart enough now to handle thatwithout needing a task management systembut for bigger projectslike building a full feature across multiple files or doing a large refactor or creating a test suite. That's where tasks shine. Here's my workflow. I'll define my project requirements, ask Claude to break it down into tasks with proper dependencies, then spin up multiple subagents to work on independent branches of the task tree. Each subagent works in its own context window, but they're all seeing the same task list.就到 ensuring工作是這樣成為更新设裁因但是基本菜息類似被詞嘉藉操與 язы方的成问WorkTrees, and TaskDependencies on top of the Ralph loop. But now, Tasks handle a lot of that natively. You still might want Ralphie for the GitWorkTree isolation and automatic PR creation, but the CoreTaskCoordination? That's built in now. I do have a couple of nitpicks, though. First, the documentation is pretty sparse right now. The Cloud Code team announced TasksOnX,但未必有太多的 documentation yet我必要合作用的方式我可以合作用的方式和一些试图希望可以加上 proper doc soon第二我希望有一个实用的 interface现在你能看到他们在游戏然后你能看到他们的方式你能看到他们的方式但一 proper dashboard showing task progress和 dependencies也很棒 maybe someone in the community will build that third the fact that you need to set an environment variable to share tasks across sessions is a bit clunky I'd prefer if there was a slash command or a config option for this something like slash tasks share groceries to start collaborating on a task list called groceries but these are minor complaints the core functionality is solid and it's exactly what power users have been asking for. If you've been using the Ralph Wiggum plugin or Ralphie for autonomous loops, tasks won't completely replace those. Ralph is still useful for that single-minded don't-stop-until-it's-done behavior. But for coordinating work across multiple agents and sessions, tasks are the proper solution now.I think this is the directionAI coding tools should be goingWe're moving from AI as a helperto AI as a teamAnd when you have a teamyou need proper project managementTasks are Claude Code's answer to thatOverall, it's pretty cool