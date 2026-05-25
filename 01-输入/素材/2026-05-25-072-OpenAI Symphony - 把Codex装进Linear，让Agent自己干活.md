---
title: "OpenAI Symphony - 把Codex装进Linear，让Agent自己干活"
author: "五里墩茶社"
source: https://www.bilibili.com/video/BV1Fg9bBmEaX
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI
  - 提效
  - 项目管理
  - 工具
  - 自动化
  - 编程
type: video-note
bvid: BV1Fg9bBmEaX
duration: "14:31"
cover: "http://i2.hdslb.com/bfs/archive/a59591bef4eac9dd227a46aab4fe14bf21fdcf22.jpg"
description: "一个key用全球大模型🔴 https://DMXAPI.cn 🚀 国内直连OpenAI、Claude、Gemini,💰￥1元起充!  加入我的知识星球:https://t.zsxq.com/W5Oj7  这一期我们实操 OpenAI 今天开源的 Symphony - 一个把 Linear 当成 control plane 的 Codex 编排框架。我会带你看清它跟 Codex CLI、Claude Code 这类 agent 的本质差别，然后现场给我的个人网站 verysmallwoods 派一张真的 issue，让 Symphony帮我调度Agent工作。  仓库地址:https://git"
---

# OpenAI Symphony - 把Codex装进Linear，让Agent自己干活

> [五里墩茶社](https://space.bilibili.com/615957867) | [BV1Fg9bBmEaX](https://www.bilibili.com/video/BV1Fg9bBmEaX) | 时长 14:31

## OpenAI Symphony 概述
### 定义和目的
OpenAI Symphony 是一个开源工具，旨在将项目工作转化为一组互相隔离的自制的任务执行，充当一个调度器，而非直接写代码的工具。它通过自动化任务分配和执行，让 Agent 自主处理项目管理，从而提升效率。

### 关键数字
- **15K**：Symphony 仓库在 GitHub 上的 Star 数已突破 15K。
- **500%**：OpenAI 内部团队使用 Symphony 后，PR（Pull Request）数量增长了 5 倍。
- **零**：在实操示例中，用户为自己的网站开发功能时，键盘输入次数为零，体现了高度自动化。

## 核心概念
### 隔离、自制、运行
Symphony 的核心设计基于三个关键词：**隔离**（每个任务在独立工作区运行）、**自制**（任务由 Agent 自主决策执行）、**运行**（通过调度器管理任务生命周期）。这使其区别于传统代码生成工具，专注于项目调度和自动化。

## 工作原理
### 轮询机制
- Symphony 默认每 30 秒轮询一次 Linear 看板，检查处于 `to do` 或 `in progress` 状态且没有未关闭 blocker 的 ticket。
- 每个 issue 拥有自己的专属工作区（workspace），避免任务冲突，且工作完成后保留以便后续复用。
- 失败后会采用指数退避机制，不会因单次失败彻底停止任务。

### 任务执行
- Symphony 负责调度任务，包括决定谁该运行、运行时长、超时处理和收尾工作。
- Agent 使用 OpenAI 的 Codex App Server 作为代码执行引擎，Symphony 本身不直接写代码或修改 Linear 状态，而是由 Agent 通过工具自主操作。

## 与现有工具对比
### 入口差异
- 传统工具如 Codex CLI 或 Claude Code 的入口是终端，用户需要直接交互（如输入指令、审查代码）。
- Symphony 将入口切换为 Linear 看板，用户只需在 Linear 上创建和管理 ticket，Agent 自动处理任务，实现从“盯着 Agent 写代码”到“管项目”的转变。

### 适用人群
- 非技术人员（如产品经理、设计师、运营）只要能在 Linear 上提 ticket，就能调度 Agent 工作，降低了项目管理的技术门槛。

## 开源和维护
- Symphony 不是产品，OpenAI 明确表示不会将其作为产品维护，仅作为开源参考实现展示 Codex App Server 接入 workflow 工具的潜力。
- 参考实现基于 Elixir 语言编写，提供了完善的文档以帮助用户快速上手。

## 安装和配置
### 依赖安装
1. 安装 Mise 管理工具（例如在 macOS 上使用 `brew install mise`）。
2. 克隆 Symphony 代码仓库：`git clone https://github.com/openai/symphony`。
3. 进入 Elixir 目录（如 `symphony/elixir`），运行安装命令（具体命令参考官方文档）。

### 配置 Linear
1. 在 Linear 上注册登录，创建一个项目并记录项目 ID（从项目 URL 中获取）。
2. 在 Linear 个人设置中，导航至“Security and Access”，创建一个 Personal API Key 并保存。

### 启动 Symphony
1. 在项目目录中，创建或配置 Workflow MD 文件（例如 `workflow.md`），设置以下参数：
   - `Project Slug`：填写 Linear 项目 ID。
   - `Hooks`：在 `AfterCreate` 部分配置 `git clone` 命令，指定要克隆的代码仓库 URL。
2. 设置环境变量 `LINEAR_API_KEY` 为之前创建的 API Key。
3. 使用命令启动 Symphony：`mise exec symphony -- workflow.md`（需添加 `--yes-i-know-what-i-am-doing` 标志以确认风险）。

## 实际示例
### Linear issue 处理
- **步骤**：
  1. 在 Linear 项目中创建一个 issue（例如将网站页角的 email 链接改为可点击），设置状态为 `to do` 和优先级为 `high`。
  2. Symphony 自动检测到新 issue，派发 Agent 处理。
  3. Agent 在独立工作区克隆代码仓库，执行修改（如添加 `mailto:` 协议），并更新 Linear issue（如添加工作计划、验收标准和 token 消耗统计）。
  4. 用户可在 Linear issue 中查看进度，并在 `Symphony/Workspaces` 目录下验证代码更改。
- **结果**：任务自动完成，用户无需手动编码，展示了 Symphony 的高效自动化能力。

## 总结
OpenAI Symphony 通过将项目管理入口从终端切换到 Linear 看板，实现了任务调度的自动化，让非技术人员也能驱动 Agent 工作。它基于隔离工作区和轮询机制，利用 Codex App Server 执行任务，显著提升了团队效率（如 PR 数量增长 500%）。尽管作为开源参考实现而非产品，Symphony 展示了 AI 驱动项目管理的潜力，用户可通过简单配置快速上手，让 Agent 自主处理项目任务。

---

## 原始字幕

大家好,我是小木头今天聊一个OpenAI刚开源的东西Symphony在开始前,我们先来看三个数字第一个数字,15KSymphony仓库开源到现在Github新星已经突破了15K第二个,500%OpenAI自己披露内部用上Symphony的团队落地的PR数量涨了5倍第三个数字零我接下来录屏里给我自己的网站做了一个小功能在这个功能开发中我自己敲键盘的次数是零这三个数字摆在一起基本就是OpenAI这次想讲的故事不是又造了一个写代码的Agent而是把管项目这件事重新设计了一遍留给Agent自己跑Symphony到底是什么呢咱们来到官方代码仓库官方的定义是把项目工作变成一组互相隔离的自制的任务执行注意三个词隔离自制运行这三个词决定了Symphony不是一个写代码的工具而是一个调度器它的工作方式是这样的你的linear看板上每一张ticketSymphony都会去看一眼处于to do或in progress状态又没有未关闭的blocker他就会派一个agent进去干这个agent跑在自己专属的workspace代码本体跑的是OpenAI的Codex App ServerSymphony自己只负责调度谁该跑,跑多久,超时怎么从事,跑完怎么收尾在官方代码仓库有这么一份文档spec这是Symphony的服务规范我读了一遍其中有几个关键点,咱们拎出来单独的聊一聊第一个是轮询也就是pulling轮询默认30秒一次linear看板上有新卡状态变了30秒内Symphony就会注意到每个issue有自己的工作区也就是workspace不会互相打架跑完一次还会保留下来下次同一个issue再跑可以接着用失败后会有指数退币重视不会一次失败就彻底挡平Symphony他自己不写ticket只读linear的状态要不要在linear上回复评论修改状态是agent自己用工具去做的那这跟我们已经在用的Codex CRI或Claw Code有什么不一样呢差别就一个谁是入口Codex CRIClaw Code这种入口是终端我打开它我跟他说帮我修改这个文件他写我审Symphony把入口换成了linear看板我只管在linear上提ticketagent自己去解我从盯着agent写代码变成管项目agent自己开工Symphony把入口换成了linear看板我只管在linear上提ticketagent自己去解我从盯着agent写代码变成管项目agent自己开工这一句听起来好像没什么但你想想这意味着什么不会写代码的人也能给项目派活产品经理设计师运营只要会在linear上提ticket他们就在调度agent最后还有一件事得说清楚Symphony不是产品OpenAI自己说不会把它当产品维护就是放传给大家看Codex App Server接workflow工具能跑成什么样在Symphony代码仓库还开源出来一个参考实现这个实现是基于Elexer写的这个选择还是令我蛮意外的至少我并不熟悉Elexer但这个参考实现还是提供了非常完善的文档帮助我快速的上手听了一番我的介绍恐怕还是蛮抽象的那咱们来实际的安装操作一下看看它的体验究竟是什么样的咱们根据Alexa的Reading文档来完成操作在这里有一个非常简明的安装配置手册也介绍了它是如何工作的它会轮选Linear去寻找可以适合自己的工作为每个issue创建工作区域启动Codex发送提示词给Codex推动Codex不断的工作直到issue成功被解决在这里面咱们就需要几样东西首先是代码仓库这是你要让Symphony工作的地方另一个就是Linear的API Key在目前的这个实现中用到了Linear作为一个任务的调度和管理的系统在此之前首先是需要完成一系列依赖的安装因为Alexa所以咱们需要用到一个叫Mise的管理工具在官方网站这里也有非常详细的安装方式根据不同的操作系统大家选择对应的安装方式完成安装比如在macOS咱们就用brew install mice接下来参考文档的后续步骤主一的运行可以通过Mice EXEC Alexa version来查看安装版本在克隆Symphony代码仓库在Alexa目录中运行如下一系列命令完成安装与配置最后这条命令MiceXEC BainSymphonyWorkflow.md就是运行Symphony的一条命令我们先来看看在我本地已经运行起来的这么一个Symphony环境配合Linear它是怎么工作的我在当前的终端已经运行了Symphony它监听的或对接的项目是Linear上的这个Very Small Oots项目它会每隔五秒钟刷新扫描一次它可以做的工作在Linear这一侧我创建了个项目叫Very Small Oots通过URL大家应该能看到770B618这个ID或者这个项目呢正是目前咱们在终端这里监听的项目它每隔五秒扫描一次当咱们期望通过Symphony来协调调度工作的执行我们通过issue来追踪那现在呢就来创建一个issue来看看效果当前管理的项目呢是我的这个官方网站我尝试让他帮我完成一个简单的工作吧在页角这里有一个email这是联系方式但是呢不能点击在网站上常见的电子邮件呈现方式呢是可以通过点击自动打开比如邮件的应用快速的来编写邮件那我期望在这里做一番改进我现在就回到linear期望更新一下在页角中的email让它可以点击我将它状态切换到to do有限期呢切换到high我可以将它只拍给我自己创建issue这个issue创建后我们赶紧回到终端这里很快通过扫描它发现到了这个新的issue目前处于to do状态这是它可以进行处理的那它现在就开始处理这个issue我们给它一些时间来完成操作我们回到linear点开这个issue能够看到这个issue底下呢已经做了许多的更新这个更新呢是一个codex的工作计划版包含了工作计划以及验收的标准最后呢是如何验证花了一些时间他完成了这个任务的执行那在这里呢有一个token的进与出的统计数据这个呢大概就反映了在这个任务执行中他的对话他的提示词究竟的开销是什么样的那我现在回到Linion这边来看看issue的更新情况那究竟这个是怎么工作的呢我们来看看在本地他得到了一些什么咱们现在回到另外一个终端在code目标下一个Symphony Workspaces这里面列出了所有issue对应的目录刚才工作的应该是8号实际上呢它就是将very small odds我这个个人的网站的项目克隆到了Workspaces底下在这里面它会做对应的代码修改如果需要呢我们可以来到这个目录手动的在这里运行个人的站点看看它的修改情况再验证是否修改是我们期望的目前这个issue的执行我们来看看最下方它的记录这里面就有一系列它的处理情况处理到最后它有一个confusion的信息点看起来在整个的执行中get的操作有一些问题我不确定是不是我本地的环境的配置或者当前的网络存在一些问题这个在视频后我回来检查一下看得出来它主要的改动就是添加了mail2这个前缀或者这个协议的标识符使得电子邮件可以点击那这当然是一个正确的改进或者修复这就是我们如何在本地运行Symphony并且基于Linear来做任务的协调本地的执行呢会用到Codex那大家可能好奇该怎么配置那我们现在快速的就过一遍安装与配置首先大家在Linear完成注册与登录在这里呢我已经创建了一个项目叫Bare Small OOT在项目这里大家可以点击加好创建个新的项目比如我取名Experiment这个项目会有一个ID当我们点击这个项目的时候在浏览器的地址栏就有这个ID这个ID是我们在后续配置中会用到的另一方面我们需要配置Linear的API Key在个人账号这里来到Settings应该有Security and Access这个菜单点击它在下方创建一个自己的personal API key在linear车的配置就完成了在咱们自己电脑上我们现在做一些配置安装配置过程呢我们参考Symphony中Elexa的文档接下来就是克隆Symphony这个代码仓库再来到SymphonyElexa目录我已经完成了克隆后续的命令我也已经都执行过了大家可以逐一的执行最后这条命令MessExecBainSymphony这个就是启动Symphony的命令我回到刚才运行的这个中段将它停掉可以来看看整个的命令的情况BainSymphony这表示运行Symphony但是需要给它一个workflow的MD文件这个文件在哪里呢我们马上介绍在文档中并没有添加我们后面提供的这个参数那如果大家在运行同样命令时出现错误呢它会有提示那么我遇到提示就是将这个选项添加上这表示我已经明白这个运行呢会存在风险它并没有通常需要的这种安全的防护这样呢就启动了在本地运行的Alexa实现也就是说运行了Symphony那在这里面会提供的Workflow MD文件是什么呢这就很关键了我们依然回到Alexa的文档这里要提供一个Workflow MD文件这个文件呢是你想要它工作的项目中配置的Workflow文件那我在这里提供的呢就是very smallwood项目下的Workflow.md在Alexa目录下会有Workflow MD文件这是一个类似于模板的文件我们可以打开看看它的内容在这里面包含了一系列我们可以配置的参数那作为初次使用或体验呢我们只需要关注两个参数就好一个是Project Slug一个呢是Hooks这里的getClone命令最方简单的介绍Project Slug配置为刚才我们在Linear App中创建的项目的ID也就是咱们刚才创建项目的URL中的这部分另一个呢就是Hooks这里的AfterCreate然后克隆一个目录这个目录呢就是大家的代码仓库的URL比如现在如果我想要他帮助我来做Sessionate这个项目的开发和管理呢我就将这个URL交给他他的工作原理是在每个Acho处理中会在Symphony Workspace克隆这个代码仓库完成必要的操作比如修改代码编译确保一些正常然后更新咱们在Linear上的issue现在我们就来看看我在这里命令中提供的Workflow MD文件来到本地的VS Code我打开的就是Workflow MD这个Workflow MD是我在Very Small Outs这个项目中复制粘贴后做的修改Project Slug设置为了这么一个字符串我是从Linear App中复制粘贴过来的另一个很重要的就是After Create这个后面get clone克隆的就是这么一个代码仓库在启动Symphony之前呢我们还需要配置linear的API-Key我现在在环境变量中已经配置了linear API-Key这个呢是在视频分享前我已经创建并且添加到这里的到此我们就已经完成了B2的准备工作通过MysExecSymphony命令启动它就好在这个命令中我们给到了这个workflow.md文件那现在大家就可以在自己的Linear项目中创建issue项目这里呢点击issues可以创建一个新的issue这也是在项目中的第一个可以根据自己的需要来决定将状态切换成什么比如切换到tudio表示这个issue呢已经可以开始工作了自己本地运行的Symphony的agent就会将这个issue取下来看看是否能做再根据需要将它切换到比如in progress状态进行工作并随时的在底下做更新做笔记好了这就是咱们今天分享的主要内容那大家觉得这套任务的调度编乏体验是否能够满足自己的工作和学习的需要呢大家是否已经开始使用Symphony也欢迎大家在评论区跟我们留言那今天的分享就到这里我们下次再见吧