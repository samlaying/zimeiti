---
title: "突破上限！Claude Code 自带无限记忆，彻底解决 AI 遗忘难题！"
author: ""
source: https://www.bilibili.com/video/BV1voFazeES7
date: 2026-05-26
tags:
  - bilibili
  - 笔记
  - AI编程
  - Claude Code
  - 记忆增强
  - 开发者工具
  - 效率提升
type: video-note
bvid: BV1voFazeES7
duration: "0:00"
cover: ""
description: ""
---

# 突破上限！Claude Code 自带无限记忆，彻底解决 AI 遗忘难题！

> [](https://space.bilibili.com/) | [BV1voFazeES7](https://www.bilibili.com/video/BV1voFazeES7) | 时长 0:00

## 笔记正文

### 一、 核心问题：AI的“遗忘”难题
1.  **根本限制**：当前Anthropic的Claude模型缺乏跨会话的真正持久记忆。
2.  **原因**：
    *   **无状态设计**：会话在设计上是无状态的。
    *   **有限的上下文窗口**：与Gemini等模型相比，上下文窗口较小。
3.  **后果**：
    *   当一次对话或编码会话结束时，模型下次启动通常会从头开始。
    *   Claude会**遗忘**你的项目上下文、决策历史和过往工作。
    *   这迫使用户每次都需要重新构建上下文，效率低下。

### 二、 解决方案：CloudMem 工具
CloudMem 是一个工具，旨在将Claude Code转变为一个真正能记住项目历史的工具。

#### 1. 工作原理
*   **自动捕获**：当会话结束时，它不会遗忘一切，而是自动捕获Claude的工具使用、决策和观察结果。
*   **压缩存储**：将这些信息压缩后，存储到一个**本地数据库**中（该数据库支持向量搜索）。
*   **上下文注入**：在未来的新会话中，它可以将相关的上下文**重新注入**，从而使Claude真正“记住”你的项目。
*   **自然语言检索**：允许你通过 `MemSearch` 和 **MCP工具**，使用自然语言搜索过去的工作。

#### 2. 核心优势
*   **开源且自动化**：一旦安装，它会在后台自动运行。
*   **减少冗余，提升质量**：使模型能将token预算用于创建深思熟虑、可投产的UI，而不是浪费在重建上下文上。
*   **赋能决策**：帮助团队在“因缺乏数据而行动过慢”和“因盲目开发而行动过快”之间找到平衡点。

### 三、 功能演示与效果对比
UP主使用一个详细的“仪表盘”提示词，分别测试了**有无CloudMem**两种情况。

#### 1. 无CloudMem（无状态会话）
*   能够生成一个功能性的仪表盘。
*   **缺点**：
    *   遗漏了许多项目特定的细节。
    *   存在一些错误（如滚动时出现重复的通用模式）。
    *   需要更多迭代才能与提示词中描述的“编辑、高端产品设计”对齐。
    *   输出未能体现提示词要求的交互和签名特性。

#### 2. 有CloudMem（启用记忆）
*   **优点**：
    *   记住了之前的决策、工具使用和过往会话的上下文。
    *   生成了一个更干净、更精确的仪表盘，**遵循了设计约束**。
    *   成功添加了提示词要求的所有必要功能和微妙的组件交互。
    *   **效果**：显著提高了输出质量，节省了时间。

### 四、 安装与配置步骤
1.  **前提准备**：确保拥有API密钥。
2.  **安装CloudMem**：
    *   使用 `cloud` 命令启动Claude Code。
    *   输入 `/plugin` 命令。
    *   使用键盘箭头键导航到市场（marketplace）。
    *   点击Enter添加新市场。
    *   复制CloudMem的仓库路径（来自文档或仓库），粘贴到添加市场的部分并按Enter。这会克隆仓库。
    *   在市场中找到CloudMem，按Enter浏览插件，然后进行安装。
3.  **激活使用**：
    *   安装完成后，**关闭并重启Claude Code**。
    *   重启后，CloudMem将在你的Claude会话中工作，提供跨会话的持久记忆。
    *   安装后会运行`funnet`，并可通过Web UI管理会话和记忆。

### 五、 高级用法与提示
1.  **命令与功能**：
    *   可以使用命令**手动注入自己的记忆**到会话中（**需谨慎**：注入错误记忆可能干扰未来生成）。
    *   对于**生产环境构建**，考虑在某些情况下关闭CloudMem。
    *   CloudMem能捕获Claude的所有工具操作（读、写、编辑、bash、glob等）。
    *   可使用斜杠命令检索和注入新记忆。
    *   **新功能**：可使用子代理执行计划，以及结合文档发现创建实施计划。
2.  **增强搜索**：
    *   **强烈建议**使用MCP工具，以获得更好的项目历史记忆搜索。设置方法参考描述区链接。
3.  **实际应用示例**：
    *   UP主要求创建一个落地页，并**注入了以往落地页的设计参考库**到CloudMem中。
    *   Claude因此记住了对输出风格的偏好，避免了生成常见的、泛用的“紫色AI-SaaS风格”页面。
    *   **节省了95%的token**，并且Claude能进行比常规多20倍的工具调用，从而输出符合要求的精美设计。

### 六、 核心要点总结
CloudMem通过自动捕获、压缩存储并智能注入跨会话的上下文记忆，从根本上解决了Claude Code的“遗忘”难题。它将无状态的AI交互转变为有记忆的连续协作，使开发者无需重复说明上下文，从而大幅节省token、减少迭代次数、提升生成结果的质量和准确性，真正让AI成为理解并延续项目历史的“记忆型”编程伙伴。其开源、自动化的特性以及与MCP等工具的集成，进一步增强了其在复杂开发场景下的实用价值。

---

## 原始字幕

One of the biggest limitations of Anthropixy Cloud models today is the lack of true persistent memory across sessions and this is due to sessions being stateless by design as well as them having a small context window in comparison to other models like Gemini. When a chat or coding session ends the model usually starts fresh the next time. This is where Cloud forgets your project context, decisions, and past work. That means you're forced to可以道개�warium一起充电 ,充满花篺,你的讯息是在这些讯息的问题上的问题但是有一个解决的解决它叫 CloudMem CloudMem turns CloudCode into a tool that actually remembers your project history across sessions所以你不能够解决 context every single time Instead of forgetting everything when a session ends CloudMem automatically captures what CloudMem does with tool usage, decisions, and observations, then compresses that information and stores it into a local database with Vector Search. It can inject relevant context back into future sessions, so Cloud truly remembers your project. On top of that, it lets you search your past work using natural language through Memsearch and MCP tools. And the best part is that it's open source and runs automatically in the background once you install it.to test the impact of persistent memory, I used the same detailed dashboard prompt twice, once with Claude in a stateless session and once with Claude mem enabled, and there's definitely a drastic impact in terms of the differentiation.Without Claude mem, Claude was able to produce this functional dashboard, but missed a lot of project specific details.There's a couple of errors already showcasing when I'm scrolling through this dashboard repeated generic patterns and required more iterations to actually align with the editorial the high-end product design that was described in this prompt wasn't outputted with this generation. Whereas if I'm to compare it with the CloudMEM generation it remembered previous decisions the tool usage as well as the context from prior sessions whicha cleaner more precise dashboard that followed the design constraints and you can see that there's subtle interactions with each component the signature feature exactly that was intended from the prompt that was actually sent in now i'm not saying that it is perfect because you can see that this generation over here with the chart doesn't look as great but in terms of adding all of the required features i had asked for was added with this generation with cloud met theThe difference clearly shows how persistent memory directly improves output quality which reduces redundancyas well as allows the model to focus its token budget on creating thoughtful production ready UIrather than just reconstructing context.Shipping features is easy.Shipping the right feature is what actually moves the needle.Most teams either move too slow because they lack the dataor move too fast because they're building things users never touch.覺得有很多的不成ы需要 paid你呈們確保你的 Remote consol vous substitution使用 logo.js精工adone.jsSql Lite更a開始AS糜備轉不用 the cloud command once you have it running use the slash plugin command and then what you want to do is head over to the marketplace by using the arrow key on your keyboard and you're going to go ahead and add a new marketplace and that is by clicking enter this is where you're going to need to go back into the repo or this dock essentially what you want to do is just copy this last section of the creator as well as the repository name and then what you want to do is just simply go ahead and paste this in into the add marketplace section and click Enter this will clone the repo then you will see within the marketplace section the New Cloudmem marketplace and you want to click on enter you want to browse the plugin and you want to go ahead and install Cloudmem if you haven't already after installing it's recommended thatyou close cloud code and then you can restart it back up and you should have cloud mem now workingwithin your cloud sessions where you're going to be able to have persistent memory across all ofyour sessions now this is going to be a huge feature that will help you in so many ways you can see right now that funnet is actually running which is also going to let you view this with thewebviewerui which is where it's going to prompt open this ui for you to actually manage yourSession as well as have it so that you can interact with your memory. Now there's a lot of different commands that you can use with CloudMem like injecting your own memory directly within all of your sessions which is something that you need to be really careful about because if you inject incorrect memory it could be interfering with future generations and sessions which is why it's recommended that if you're working with the production build you might want to consider thatyou should turn off cloud mem in certain cases but now that cloud mem is enabled you have a full cycle where you can now use this memory feature that persistent memory where it's going to be able to read all of your files write them it can edit use bash glob rep all other cloud tools and it is going to capture all that with this persistent memory locally and you're going to be able to even retrieve context with the slash commands they even have it so that you can pull and even inject new memory and right now you can see that there's two new uh commands that you will see the cloud mem do which is where you can execute a plan using subagents for implementation which is a pretty cool new feature and then creating an implementation plan with the documentation discovery so two of these features can go hand to hand so you can see right here that i had requested to create a landing page and it is going to use the plan tool with the mem feature and you can see that it is using multiple tools to help me execute this task right away also an fyi if you use mcp tools you're going to be able to get better memory search with your project history and you can easily enable this with the link in the description below which showcases how you can set this up but you can see that it has created multiple phases as to how it is actually going to create this so let's go aheadand have it work upon creating this landing page for usand here we gonow i want to give you guys some context as to why i created a landing pagewhat does that actually do with persistent memorywell the thing is that i actually went ahead and injecteda lot of my previous catalogs of landing pagesand i had it reference all of those landing pagesbecause i was going to have it remember my context that i had with previous generationsso I didn't have to re-explain what sort of output I was looking forbecause clearly if you are to request any AI model to generate a landing pageit is going to generate that typical purple AI-sass landing pagethat you don't want to seein this case it saves up 95% of the tokenseach time that you start a sessionthere's far more tool calls to get the best generations outputtedand with memory preservedyou can have it so that Cloud can make 20 times more tool calls with CloudMem enabled which is whyI get these beautiful generations out of it and I kid you not this is another landing page that I had generated with the same prompt and in this case it was able to use the catalog of typographyUI elements that had saved through other generations that I had injected into CloudMem and you can see它做了一件事的效果在这个兴趣的运动是在一只照片的一只照片如果您喜欢这个视频是在咕噩咕噩您可以用到你的运动在咕噩咕噩的程度上这是一个非常有趣的有很多更多的你只会会明白它的确性能力使用它更多而是你能用到你的运动和使用它们的运动使用它们的运动我会留下所有的运动在这里的运动你能不能再开始如果您已经不已请你去看