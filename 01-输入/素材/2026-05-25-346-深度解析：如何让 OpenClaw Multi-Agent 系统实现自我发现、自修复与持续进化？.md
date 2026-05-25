---
title: "深度解析：如何让 OpenClaw Multi-Agent 系统实现自我发现、自修复与持续进化？"
author: "amy师婧"
source: https://www.bilibili.com/video/BV1jNwQzZEHt
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI
  - Multi-Agent系统
  - 自动化运维
  - 数据监控
  - 系统进化
  - 工具开发
type: video-note
bvid: BV1jNwQzZEHt
duration: "14:00"
cover: "http://i2.hdslb.com/bfs/archive/0fb6029810c9c5b882079b4ae1338890cbc7a1fb.jpg"
description: "为什么你的 AI Agent 总是反馈“任务已完成”，结果却是你一直要追着问和提意见？ 在多智能体（Multi-Agent）系统的实际落地中，最难的不是让它跑起来，而是如何跨越“完成”与“预期结果”之间的鸿沟。  本期视频我将深度分享过去一周的实战发现：如何通过 OA（Operation Analytics）运营分析指标看板，赋予 Agent 系统自我观测与自我进化的能力。不再需要你盯着日志找 Bug，让系统自己发现问题、修复问题！   🚀 核心 Insight： 为什么 Agent 无法主动发现错误？（指标、基准线与流水线的缺失）  📊 OA Dashboard 深度拆解： * Cron 可"
---

# 深度解析：如何让 OpenClaw Multi-Agent 系统实现自我发现、自修复与持续进化？

> [amy师婧](https://space.bilibili.com/3494362975570156) | [BV1jNwQzZEHt](https://www.bilibili.com/video/BV1jNwQzZEHt) | 时长 14:00

## 引言
视频主题是探讨如何让OpenClaw Multi-Agent系统实现自我发现、自修复与持续进化，使多智能体系统更接近全自动。UP主分享了过去一周的实践发现，包括问题洞察、解决方案、前后对比结果，并介绍了构建的CLI工具以便一键使用。

## 问题识别
- **核心问题**：agent的完成并不等于用户想要的结果。agent可能报告任务完成，但实际内容无效或不符合预期。
- **具体例子**：在daily digest（每日报告）中，agent汇报了任务状态，但关键内容（如share的learning）被阻塞，无法提供有意义的信息，导致结果无用。
- **影响**：agent对任务范围（scope）的定义与用户预期存在巨大差距，这限制了系统的自主性和可靠性。

## 洞察与发现
- **agent的任务定义差距**：agent在理解任务目标时，其定义与用户期望不一致，导致输出不符合需求。
- **agent的自我检测能力不足**：agent擅长解决问题（当被指出问题时能快速响应），但无法自行检测问题。需要外部锚点（anchor）和基准线（baseline）来判断任务对错。
  - **锚点（anchor）**：agent依赖于什么来知道任务是否正确。
  - **基准线（baseline）**：用于判断什么是问题的标准。
- **根本原因**：用户未给agent定义指标、基准线和闭环流水线，导致agent无法识别问题、不知道何时修复。

## 解决方案
基于洞察，提出了三步法解决方案，使系统能够自我发现、自修复和持续进化：

### 1. 定义指标（Metrics）
- **操作**：将用户对多agent系统最关心的方面量化，定义为具体指标。
- **目的**：为agent提供锚点，使其知道需要监控和优化什么。
- **示例指标**：Crown Job可靠性、Team Health、Knowledge Flywheel等（后续详细说明）。

### 2. 建立基准线（Baseline）
- **操作**：利用OpenClaw优秀的logging system回填历史数据，建立基准线。
- **目的**：提供比较基准，任何数据波动都能触发问题检测。
- **关键点**：OpenClaw的logging系统使数据回填变得容易，从第一天使用起所有指标数据都可被提取。

### 3. 建立闭环流水线（Closed-loop Pipeline）
- **操作**：构建自动检测、采集、修复和验证的闭环，实现零人工干预。
- **目的**：使系统能自动处理问题，形成持续改进的循环。
- **流程**：自动检测问题 → 采集数据 → 修复问题 → 验证结果。

## 实现与监控
通过创建OA Dashboard（Operational Analytics and Dashboard）来监控系统状态，并应用解决方案。

### OA Dashboard的目标指标
1. **Crown Job的可靠性**：
   - 定义：agent能否定时触发任务，并按时完成符合期望的结果。
   - 数据示例：从三月份开始，crown job success rate从50%提升至100%（通过自我修复机制波动后恢复）。
   - 重要性：决定系统的主动性，是全自动系统的基础。

2. **系统的自我修复能力**：
   - 定义：fix rate，即系统自动发现并修复问题的比例。
   - 数据示例：过去无机制时fix率为0；上线闭环后，每天fix率提升，如COO自动发起问题并被fixer自动修复。
   - 机制：通过COO（Chief Operating Officer agent）检测问题，fixer crown job自动修复。

3. **Team Health（团队健康度）**：
   - 定义：关注每个agent的memory使用情况和bootstrap文件大小（影响token使用量）。
   - 关键指标：memory alignment gap，即active session与memory记录的匹配度。
   - 数据示例：三月份前gap较大（许多agent不写memory）；上线机制后gap减小，近期几乎完美对齐。
   - 目的：确保agent高效管理上下文，优化资源使用。

4. **Knowledge Flywheel（知识飞轮）**：
   - 定义：衡量agent的知识沉淀和复用能力。
   - 指标：memory search使用次数（知识检索）和任务结束后经验写入次数（知识沉淀）。
   - 当前状态：使用率和写入率较低，是下一步优化重点。
   - 重要性：促进系统持续学习和进化。

5. **其他指标**：满意度、自我学习进展；prompt size by agent（监控每个agent的加载文件大小，识别可优化为skill的流程）。

### Dashboard的实现实例
- **实时监控**：dashboard实时更新，数据波动自动触发检测和修复。
- **数据追踪**：通过OpenClaw的tracing机制，可追踪每个指标背后的workflow，如agent、prompt、存储路径等，确保数据准确性和可追溯性。
- **自动修复**：若数据drift（偏差），系统自动检测并在下一个fixer任务中修复；超时问题也能被识别以优化稳定性。

## 工具与实操
### CLI工具介绍
- **名称**：OACLI（可从GitHub获取）。
- **功能**：将整个解决方案封装为一键式CLI工具，让agent直接使用。
- **作用**：简化设置过程，快速实现自我进化机制。

### 实操步骤
1. **自动检测OpenClaw安装**：确保环境就绪。
2. **识别agent**：扫描并识别系统中的所有agent。
3. **运行logging system**：自动建立pipeline和database，回填历史数据。
4. **建立metrics**：定义并监控指标。
5. **启动dashboard**：一键生成OA Dashboard，实时监控系统状态。
6. **支持自定义**：内置两个指标（Daily Crown Job Reliability和Team Healthy），也允许用户自定义指标以适应不同使用场景。

## 总结
核心要点是：通过定义量化指标、建立基准线和闭环流水线，可以使多agent系统实现自我发现、自修复与持续进化。OA Dashboard提供实时监控，CLI工具简化了实施过程，使系统从被动响应转向主动优化，大幅提升可靠性和自主性。

---

## 原始字幕

好今天我们继续往深挖我一直在思考就是说在多个agent这个系统里面它这个系统本身不是agent能力是系统本身可以怎么来变成一个自我发现自我修复以及自我进化和improve的这么一个机制那么它整个agent多agent这个系统就更像全自动的这个系统再迈上一步那今天这一期我就来跟大家分享在过去这一周我的一些发现包含了问题是什么我们的insight是什么解决方案是什么给大家呈现before and after这个对比结果以及最后会分享我把我整个这个solution build成了一个CLI所以你可以让你的agent一键去使用这个CLI以及解决方案好话不多说我们直接开始我在整个我跑了一段时间的这个多个agent之后呢我就会发现有一个典型的问题也就是agent的完成并不等于我们想要的结果举个例子我有一个crown job来去帮我定时去做daily的这个digest也就是每天给我做一个日报昨天完成了什么blocker是什么然后需要哪些是需要我的我的approve或者是attention那在这个里面我可以给大家看一下我3月1号我收到的就是之前包括之前收到的一个daily digest他首先汇报了这几个agent都在做什么事情然后其次呢在最重要的share的learning这里面他说他所有的内容都被这个execute approval这个给log住了所以他没办法取到新的数据然后同时所有的这些guidance他也没办法check因为都被block但是呢他又告诉我说这个事情他完成所以对我们来讲他这个完成所以对我们来讲他这个完成完全不是我们想要的结果他只是说这个定点我做了这个事情但是我们想要的是说有一些很有效很有意义的内容但是并没有那我就会发现说Agent对于Task的这个scope这个范围的定义和我们预期的其实是很不一样并且有一个巨大的gap这是第一个insights第二个insights呢我发现agent很擅长解决问题当我每次我说你这里没有做他马上说好 I'm on it然后就开始去解决但是他不知道他没办法自己去检测出来这个问题我当时我就很奇怪我说我在所有的agent里面也都写了在memory里面写了为什么这个还需要我一遍一遍的在跟他说然后我就会发现有一个核心的问题是说他其实不知道什么是问题比如说我一旦给他指出了我说这怎么会是这样他说哦呀这个是不make sense我需要这样解决但是我如果不说他认为这个是没有问题的所以在整个过程中我们会发现说agent他其实是需要一个anchor和一个baselineanchor就是说锚点他需要依赖什么东西来知道他自己做的这个事情到底是对还是错Base line是什么那来判断到底什么是问题这样的insights我就继续往下挖为什么他看不见问题就是发现说我没有给他定义定指标定义说什么是问题所以他不知道看谁我没有一个基准线所以他不知道好是什么然后我没有一个流水线所以他就是发现了他也没办法fix或者说他也不知道什么时候该fix是不是他的任务所以基于这三点我就发现发现我们其实只需要帮他建立一个定义清楚然后建立一个基线然后把这个loop这个流水线给它定义好那它support就是可以自己完成那知道这三点之后呢其实我们就要解决就比较容易了首先第一个定义指标或者定义metrics我把我对整个多agent这个系统里面我最在意的事情我把它量化下来把它定义成metrics那这样它就至少有一个anchor知道说我需要去看什么第二就是说给它建立一个baseline这一点我要归功于给那个opencloud有很大的creditopencloud呢当我第一天使用的时候它其实整个的这个logging system做得非常好所以我一旦把matrix定好之后我其实就可以去backfill它所有的data和pipeline就可以把所有的matrix从我第一天使用到现在的所有的matrix就可以曝出来所以把这个一旦建立起来之后就可以给它一个很明确的一个指标只要你今天的数据比昨天有波动比那个basedline有波动这就是一个问题那它就可以trigger一个它自我检测和自我修复的这么一个loop第三步呢我就是把所有的这些把它做成一个闭环它可以自动的检测自动的采集自动的检测以及自动的修复最后自动的验证那整个这里面零我的概念所以有了这三步suppose这个数据或者说这个系统应该它就可以自动转起来那我们话不多说我们看一下它到底有没有转起来好这个就是我现在的一个OA dashboard也是我针对这个去做的整个这个系统首先第一个呢就是什么叫OA就Operational Analytics and Dashboard就是整个的运营指标那我在这里面我有几个目标我非常的关注第一个目标是说它这个crown job这个是决定这个agent能不能主动开始一个任务那这个crown job的这个reliability到底好不好就是说它能不能定时的trigger定时的完成并且完成的这个东西是不是我想要的那在因为我们刚才讲了就是open cloud它logging system做得非常好所以我把这个pipeline一run之后我就可以看到整个time series我是从其实应该是从一月份开始我已经开始在使用Crown Job我大概是从三月份开始用那我的所有的数据你们可以看在刚开始的时候它其实只有两个Crown Job非常少但是它的Success Rate只有50%什么意思就是说它就像任意义B一样今天运行成功了明天运行没成功完全不可控那这个如果你把它认为是一个全自主的系统全自主的系统的话这是完全不可依赖的那3月1号3月7号开始我就开始去开发这个事情3月8号上线7个crown job大家可以看我的success rate从50%一路上标到80%100%然后昨天前天还是失败了一些但是它马上又自我修复然后今天100%这是第一个这是决定了CRAM的这个主动性那第二个我特别关注的就是说这个系统到底有没有自我修复那在这里面它其实你看我主要关注的是这个Fixit他有没有百分百的fix了所有的issue而这个问题是哪里来呢我们看一下今天的问题有四个是我发起的一个是COO自己发起的然后呢fixer就是另外一个crown job就会自动的去fix那对于昨天来说有五个是系统自动发现有COO自动detect有COO driftdetect这是两个不同的任务在监测不同的方向还有我给他使用的时候我提的一些feedback然后他也都他昨天加今天他都fix所以这个大家就可以看到从过去我没有这个机制的时候呢他只会去发现一些问题比如说在Trump Review里面发现一些问题他的fix是零他不会自动自己去主动去fix但是当我上线了之后他逐渐的开始每天都在引茂提升好那第三个也是我非常关注的就是Teen的Healthing因为我们现在有七个Agent那到底每一个agent我关注的是什么呢他有没有很好地把他的memory选好然后第二呢就是他boostrap那些file的大小也就是说那个大小决定了你token的使用的量有多大所以比如说中间这条线就是黄线和蓝线它应该是supposed to align蓝线呢是代表那一天的那个agent有memory黄线呢是代表那天的那个agent有active的sessionsupposedly我有active session就是应该有memory但其实你发现没有在我三月份之前这两个的gap很大就是很多是完全不写memory的但是有了这个job你看我这两个时间的这个gap是越来越小到最后这几天都可以是非常perfect aligned那还有一个chart是非常重要也是promptsize by agent大家都知道每一个agent在opencloth里面它有agent,memory,so,user,tools,还有heartbit这都是他每一次load的时候还没有进行开始一个conversation的时候这些都会被加载进来那这个snapshot会帮我一目了然的去了解清楚现在谁现在质量最大我需要去受伸而每一个这个gap都会是这个一个agent的意识那CEO就会去检测我到底哪些过程或流程可以从我的agent这个文件系统里面把它变成skill所以我就不用加载这么多那最后呢第四个也是我非常非常关注的是knowledge flywheel我这里有两个metrics第一个metrics在他每一个agent在使用的时候他到底有用了多少次的memory search因为search的背后其实就是knowledge的沉淀然后第二个呢就是after每一次在每一次他的任务结束之后他会不会写他这次学到的经验所以这两部分就可以组成整个knowledge的flywheel那现在看起来其实还是使用率是非常低也写的率也是非常低所以这个会是我下一步的重点的研究方向那最后这两个呢就是我的满意度和我的自我的学习等等所以整个这个dashboard就来能够一目了然的告诉我今天的这个机器多Aden这个系统到底让的怎么样而这个整个这个dashboard也是实时的但凡发生一点变化它都会直接变化我在这里面加了一个小小的metric代表说这个data的source是从哪里来的这个metric是怎么来定义的它的purpose到底是什么所以呢大家只能看到有了它和没有它在最近这一个礼拜你看作为演化的程度是完全不一样那同时呢其实我每一个gy就每一个go的这个背后我在这里面加了一个mechanism所以它背后它这个workflow到底是怎么来运作的这样这个也是归功于open cloud里面它本身这个tracing这个机制所以我就可以知道它从哪个agent用了什么样的crop写了什么样的crim存到哪个betabase里面最后通过什么方式去把这个match计算出来就一目了然所以你看我这个数据都是今天13月16号12点半的时候run出来的所以我就知道这个数据现在是准的然后如果说它有一个数据dry off它就会自动会在这个下面detect出来并且下一个fixer就会定时的再去fix然后呢他也会能知道说我每一个这个span里面有多少个span然后花了多少时间如果这个超时太严重的话那有可能会影响整个稳定性所以他也可以帮助这整个系统来自动的反映出来我的问题到底是什么是超时了还是没有被推搁还是什么其他的原因所以这个就是我这次我觉得当我运行了一周因为我没有提前来share就是我不知道好不好用当我运行了一周之后我自我认为觉得它已经在朝自我进化这个方向去发展了并且是一个很好的artifice所以我share出来同时我知道整个这个setup其实就比较困难所以好消息就是我把整个这个solution把它build成了一个CLI你可以到我的GitHub上里面的CLI里面叫OACLI你就可以从这里面让你的agent直接当作来使用一键它也可以有我这个dashboard整个这个里面其实在做几件事情第一个自动去检测你open cloud是不是有安装第二个识别你的agent第三去跑你所有的logging system把pipeline database都帮你建好metrics然后第四个就是帮你把这个dashboard给你sold起来你就可以一键能知道你现在的系统到底运行怎么样那在这个CLI里面我有两个build in的metrics一个是这个Daily的Crunch of Reliability还有一个是Team的Healthy因为这个我知道是Building的就是每一个Agent都会有这样的一个问题每一个我们的使用都会有这样的问题同时它也支持你自己去定义你因为我们每人使用的方法不一样所以你定义你自己的Go然后用它来去帮你去实现对于这个Go的监控和让这个Agent自动来进行系统自动来进行礼貌OK那今天就分享到这希望今天对于多Agent系统的自我进化自我improve的这个学习和这个实践能够对你给你带来一点点启发那我们下次再见拜拜