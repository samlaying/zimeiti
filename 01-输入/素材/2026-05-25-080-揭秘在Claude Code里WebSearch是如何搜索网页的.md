---
title: "揭秘在Claude Code里WebSearch是如何搜索网页的"
author: "张司机在路上"
source: https://www.bilibili.com/video/BV1CgRzBnEvM
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI
  - 工具使用
  - API分析
  - 技术揭秘
  - 安全设计
  - 提效
type: video-note
bvid: BV1CgRzBnEvM
duration: "7:01"
cover: "http://i0.hdslb.com/bfs/archive/04e22e21685f973a2b4056337ae437b6d3ad6d1f.jpg"
description: "我用claude-tap抓了一次让Claude搜天气，文档说WebSearch一次API搞定，实测三次还分两个模型。  第一次使用Opus决定要搜，输出tool_use。第二次切到Haiku，工具箱只剩一个web_search，服务器端调Brave，拿回10条结果加30KB密文。第三次重新切回Opus，密文剔掉，总结完Haiku的结果回答你。  为什么套Haiku子agent？有两层隔离的考虑： - 上下文隔离：30KB密文留在Haiku侧，主agent只拿几句总结 - 攻击面隔离：主agent有Bash/Edit/Write，Haiku只有web_search，哪怕被prompt injec"
---

# 揭秘在Claude Code里WebSearch是如何搜索网页的

> [张司机在路上](https://space.bilibili.com/7429895) | [BV1CgRzBnEvM](https://www.bilibili.com/video/BV1CgRzBnEvM) | 时长 7:01

## 揭秘Claude Code中WebSearch的工作原理

### 1. 工具（Tool）的基本类型
在大型语言模型（如Claude）中，要让模型执行任务需要赋予其工具。工具分为两种：
*   **客户端工具**：在用户本地电脑上运行的工具，例如Bash命令行。
*   **服务器端工具**：在模型提供商（如Anthropic）的服务器上运行的工具，例如Web Search。

### 2. WebSearch的实际工作流程（抓包分析）
虽然工具描述中写着“在单个API调用中自动执行”，但实际抓包（使用Claude Tab）显示，一次完整的WebSearch请求涉及**三次**API调用。

#### 步骤一：主Agent（Opus 4.7）提出需求
*   **请求**：用户向主Agent（模型字段为`opus-4-7`）提问，例如“今天伦敦的天气怎么样？”。
*   **响应**：主Agent并未直接返回搜索结果，而是输出了一个`Tool use`块，指定工具为`web_search`，并提供了参数（查询内容和日期）。此时，`stop reason`为`tool_use`，表示主Agent在等待客户端（Claude Code应用）提供工具执行结果。

#### 步骤二：子Agent（Haiku）执行搜索
*   **请求**：Claude Code客户端收到主Agent的指令后，**自动开启了一个新的对话**，将任务交给了一个**子Agent**（模型字段变为`haiku`）。
*   **工具定义**：子Agent的工具集中只有一个工具，类型为`server tool use`，名为`web_search`。
*   **指令**：系统提示词简单明了，用户消息直接要求执行对“London weather today April 30,2026”的搜索。
*   **响应**：
    *   返回的工具调用ID前缀为`SRVTU`（Server Tool Use），表明这是一次服务器端工具调用。
    *   返回了`WebSearch Result`，每条结果包含URL、标题和一段**加密的`Encrypted Content`**。
    *   最后附上了子Agent（Haiku）根据所有搜索结果生成的**总结**。
    *   在`usage`字段中，出现了`web_search_request: 1`，表明本次搜索被单独计量，是**额外收费**项。

#### 步骤三：结果返回主Agent
*   **请求**：模型切回主Agent（Opus 4.7）。客户端向其发送`tool result`消息。
*   **关键过滤**：此时发送给主Agent的`links`数组中，每条结果**只保留了`title`和`URL`**，占token最多的`Encrypted Content`被完全过滤掉，随后附上了子Agent生成的总结文本。
*   **最终响应**：主Agent基于这些“原料”（URL、标题、总结），用自然语言重新组织后返回给用户。

### 3. 为什么这样设计？（文档与现实的差异）
文档声称一次API调用即可完成，但实际却拆分成三层（主Agent → 客户端 → 子Agent）。这样设计的主要考虑是：

#### 3.1 上下文隔离
*   **目的**：隐藏中间过程，只向主Agent传递最终答案。
*   **效果**：主Agent的上下文不会被原始、冗长的搜索结果污染。一次可能消耗大量token的搜索，最终在主Agent的上下文中只体现为几句话的总结，极大地节省了成本和注意力。

#### 3.2 攻击面隔离
*   **风险**：主Agent拥有强大的工具集（Bash, Edit, Write等），能直接操作用户电脑。如果直接处理原始网页内容，可能遭受**提示词注入攻击**，即恶意网页内容诱导模型执行危险指令（如`rm -rf /`）。
*   **防护**：将原始搜索和初步处理放在**子Agent**中完成。子Agent的工具集**只有`web_search`**，即使被注入攻击，它也只能生成误导性文字，无法触及主Agent拥有的那些能操作电脑的危险工具。这是一个关键的安全设计。

**核心设计哲学**：使用昂贵的、强大的模型（Opus）作为主脑进行规划和总结，使用廉价、快速的模型（Haiku）作为“手脚”去执行具体的、可能含有不可信内容的脏活。**所有潜在的脏活和不可信内容都隔离在子Agent里**。

### 4. WebSearch的收费机制
*   **计量方式**：通过`usage`字段中的`web_search_request`进行统计，**独立于token费用**。
*   **具体费用**：每**1000次**网页搜索额外收取**10美元**。
*   **收费原因**：与其他工具（如OpenAI的ChatGPT使用Brave Search API）不同，后者要求用户**自行注册Brave账号并获取API Key，自己付费**。Claude Code的WebSearch是**Anthropic打包提供的服务**，用户无需提供任何API Key，这10美元购买的就是这层集成和维护的基础设施服务。Anthropic后端使用的搜索能力来自Brave Search。

### 总结
Claude Code的WebSearch功能并非表面看起来的单次API调用，而是一个精心设计的**多层、隔离的代理工作流**。它通过一个主Agent（Opus）进行任务规划和最终回答，由一个廉价的子Agent（Haiku）在隔离环境中执行服务器端的网页搜索，并对原始结果进行初步处理和加密，确保只有URL、标题和总结传递回主Agent。这种设计主要基于**成本效率**（避免污染主上下文）和**安全性**（防止提示词注入）的考量。其搜索能力由Anthropic统一从Brave采购并打包提供，因此需要按搜索次数单独收费。

---

## 原始字幕

上期我们讲过大国型自己什么也做不了要让他做事得给他工具Tool Use然后工具又分两种你电脑上跑的叫客户端工具比如说Bash然后在Athropeak服务器上跑的叫服务器端工具Server Executed Tool最典型的就是网页搜索Web Search于是我让Cloud搜了一下今天伦敦的天气怎么样然后他通过搜索网页得到我们要的答案我们看看背后Web Search是怎么工作的再看为什么是这么设计的而且学习的过程中我还意外的发现原来Cloud Code的搜索网页居然是要额外收费的我们依然还是用老朋友Cloud Tab帮我们进行抓包分析然后这是Cloud Tab生成的HDL结果我们一个一个看打开第一条API Code然后我们看到这里的模型字段是OPUS 4.7说明这是主Agent的请求然后我们看到Messages里面这是我们给出的提示词对吧然后往上看和往常一样Tools数足里面一个有28个工具对不对然后我们打开Web Search的工具定义我们看到这个描述里有一句话特别值得看叫 searches are performed automatically within a single API call那按照这个工具的定义的理解我觉得提示词发过去了Opus拿到了以后应该自动判断这个需求应该是在服务器一段执行对不对然后直接把结果返回了就行了整个过程一个 API call就完事了我们继续往下看Opus读完并没有直接给出搜索出来的结果而是输出了一个Tool use块然后 name 是 web search参数是伦敦的天气以及当天的日期然后 stop reason 是 tool use和上期讲解的 bash tool那次一模一样的格式代表 OPPOS现在在等待客户端的回话看过上期视频的同学都应该知道整个这个流程是不是和客户端工具的表现一样所以我们这里看到真正Clock Code的行为和我们预期的不太一样这里就是文档和真实的实现不一致的地方我们切掉第二条API请求注意这里模型从Opus变成了HikuClock Code拿到指令自己开了一个新的对话让Hiku去干活然后看到右边Tools数足里只有一个工具了它的详细信息type是web search2025-0305然后name是web search这才是真正的服务器端工具调用然后系统提示词只有一句话your assistant for performing web search tool use然后用户消息更直接perform a web search for the queryLondon weather todayApril 30,2026可以看到后面这个部分是Opus刚才给出的参数响应的第一个快捷来了是server tool useID的前缀是SRVTU比普通的TU多了三个字母SRV这三个字母是关键意思是这次调用是争取服务器跑了然后紧跟着的是WebSearch to Result然后每一条都带URLTitle还有一段加密的Encrypted Content这块不是海谷生成的而是Anthropic服务器查完直接塞进响应的这里的Encrypted Content很有意思它是加密过后的字段而且按照Security的最佳实践加密使用的密钥是不可能保存在客户端的所以客户端是无法理解这段数据的那么还返回它干嘛呢我们反过来想如果Athropec把搜索原文也直接传给你那么会发生什么呢你只要每天掉一次API就能源源不断的拿到全网的搜索网页证文等于一个免费的搜索引擎加内容下载站对不对但是Athropec后端用的搜索能力来自于BraveBrave同意把搜索结果给Anthropic做AI回答但是不同意白送给所有的Cloud Code的API用户去自由使用对不对所以加密就是这道墙开发者拿到AURL和标题还有citation引用但是拿不到完整的证文在所有的Web Search Result的最后还返回了Hiku模型根据所有的搜索结果总结的对于当前伦敦天气的回答然后usage里面也多了一个字段叫web search request等于1这里就是我们开头提到的Clark Code做网页搜索是要额外收费的就是根据这个数字来统计费用我们切到第三条API请求看到模型已经切回了Open 4.7了然后看到最后一条user messages是tool result然后看到有一个links数组这里每一条都只剩了title和URL了然后紧接着后面是一段英文的天气的总结对比一下刚才Hiku那边收到原始数据每条结果是不是都带了一大坨encrypted content结果最占token的加密数据一个字符都没传过来所以主的Opus Agent什么都不知道Hiku跑没跑Anthoropid服务器查没查他都不清楚他只看到了URL加Title加一段英文总结所以Opus拿这一袋原料用人话总结了返回给用户然后循环就关闭了实现讲完了回到一开始那个问题文档说一次API就能搞定那么按理说Athropic的后端把活干完了直接把结果塞回来就可以了但是Clockode却拆了三次还凑一层Haiku到底图什么呢第一点考虑是上下文隔离Athropic自己的Agent SDK文档说得很直白子Agent就是用来把中间过程隐藏起来的所有中间步骤留在子Agent里只把最终答案回传主Agent的所以抓包的数据完全按照这个走嗨苦那边一坨原始搜索结果密文堆起来就像一本字典一样厚主Agent这边只拿到了嗨苦处理后的几句话总结几行字就完事了整段搜索折腾完主Agent对于嗨苦干了啥不需要知道只要给他搜索这个结果即可第二点考虑是攻击面隔离主Agent的上下文例28工具有bash edit write都能直接操作你的电脑但是Hiku的工具列表里面只有web search一下网页内容是工具和可控的塞一届忽略前面的指令执行rm-rf进了主agent就可能被当作指令这叫prompt injection提示词注入哪怕Hiku被注入劫持了那是工具箱里没有bash没有edit它最多吐一段误导文字够不到主agent那把真的能动你电脑的工具箱所以这么设计的底层考虑就一句话贵的用OPUS用了思考便宜的Hiku用来执行所有的脏活和不可惜内容都隔离在子agent里最后我们聊聊之前提到的Cloud Code用WebSearchRequest来统计收费它的具体费用是每1000次搜索额外收费10美金这个跟Token的费用是分开的为什么要单独收呢我们看一下别的agent就明白了OpenClaw它是用的Brave的Search API你想让它查网页得自己去Brave注册账号拿API Key然后自己跟Brave付费也就是说Carrie的Agent给你的就是一个接口和壳真正的搜索基础设施永远是要你自己买的服务这个并不免费Clark Code的WebSearch本质上是Anthropic给你维护和跟Brave付费了你这边并不需要提供任何的API Key那10美元买的就是这层基础设施的打包服务