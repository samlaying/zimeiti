---
title: "Karpathy的Obsidian RAG + Claude Code = 作弊代码"
author: "GoldenSpiderAI"
source: https://www.bilibili.com/video/BV1W1SSBzEaC
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI
  - 知识管理
  - Obsidian
  - Claude Code
  - RAG
type: video-note
bvid: BV1W1SSBzEaC
duration: "13:56"
cover: "http://i2.hdslb.com/bfs/archive/317c27ab9d65bae8413740fc8fd4d5cd68a6a70b.jpg"
description: "原视频链接： https://www.youtube.com/watch?v=OSZdFnQmgRw  原视频发布日期：2026年4月4日  视频名称： Karpathy的Obsidian RAG + Claude Code = 作弊代码  视频描述： Karpathy刚刚用Obsidian取代了RAG。  在本视频中，我将解析Karpathy的Obsidian知识库的工作原理，如何自己设置它，以及何时真正需要&quot;真正的&quot;RAG系统。  ⏰时间戳： 0:00 - 介绍 0:52 - Obsidian &quot;RAG&quot; 3:22 - 工作原理 6:30 - 设置方"
---

# Karpathy的Obsidian RAG + Claude Code = 作弊代码

> [GoldenSpiderAI](https://space.bilibili.com/3546838527380108) | [BV1W1SSBzEaC](https://www.bilibili.com/video/BV1W1SSBzEaC) | 时长 13:56

# Andrej Karpathy的Obsidian RAG系统笔记

## 一、系统概述与核心理念
- **核心思想**：使用Obsidian笔记软件构建一个轻量级、无向量数据库、无嵌入和复杂检索流程的“RAG”系统。
- **解决的问题**：允许大语言模型（LLM）处理大量文档、回答问题并收集准确信息，模拟传统RAG系统的功能。
- **主要优势**：
    - **轻量级且免费**：无需传统RAG的技术栈（如向量数据库、嵌入模型）。
    - **结构透明**：前端是Obsidian，用户可直接查看所有文档和Wiki内容，不像传统RAG是黑盒。
    - **完美中间方案**：适合个人开发者或小型团队处理中等规模文档。
- **工作流程**：
    1. **数据摄取**：将文章、论文、代码仓库等原始数据放入Obsidian vault的`raw`文件夹。
    2. **人工/LLM处理**：使用Claude Code等工具处理原始数据，生成结构化的Wiki文档。
    3. **查询与问答**：通过Claude Code针对生成的Wiki进行提问和探索。

## 二、核心文件结构
整个系统建立在一个层次清晰的Obsidian vault内：
- **Vault根目录**：在Obsidian中指定为整个知识库的根文件夹。
- **`raw`文件夹（原始数据区）**：
    - **作用**：暂存所有原始研究资料、文章、PDF等，作为Wiki生成的“暂存区”。
    - **内容**：主要为Markdown文件，可通过工具（如网页剪藏器）从网络导入。
- **`wiki`文件夹（知识Wiki区）**：
    - **作用**：存放最终生成的结构化、相互链接的Wiki文档。
    - **结构**：包含多个子文件夹，每个子文件夹对应一个主题Wiki（如`AI-agents`, `RAG-systems`）。
    - **`master-index.md`文件**：位于`wiki`文件夹内，是所有Wiki主题的**主索引列表**。
    - **每个Wiki文件夹内**：
        - 有一个**索引文件**（如`RAG-systems-index.md`），列出该主题下的所有文章。
        - 包含多篇相互链接的详细文章。

## 三、系统设置实操步骤
### 步骤1：安装与初始化
1.  **下载并安装Obsidian**：访问 [obsidian.md](https://obsidian.md)。
2.  **创建新Vault**：在本地选择一个文件夹作为Vault（可命名为`vault`）。

### 步骤2：初始化文件结构（使用Claude Code）
1.  在Vault目录下打开Claude Code。
2.  使用提示词让Claude Code创建`raw`和`wiki`文件夹，并说明其用途。
3.  创建`cloud.md`文件（详见下文）。

### 步骤3：配置`cloud.md`系统提示文件
- **作用**：这是整个系统的“大脑指令”，指导LLM（如Claude Code）如何理解、遍历和操作这个知识库。
- **内容应包含**：
    - 知识库的规则和结构说明。
    - 文件遍历逻辑（利用Wiki链接格式）。
    - Wiki文档的生成规范和链接格式。
- **获取方式**：UP主提供模板，可在其社区免费获取。

### 步骤4：配置数据摄入工具
1.  **安装Obsidian网页剪藏器**：
    - 访问 [obsidian.md/clipper](https://obsidian.md/clipper) 安装Chrome扩展。
    - **重要设置**：在扩展选项中，将“Note location”从默认的`clippings`改为`raw`，确保剪藏内容自动存入`raw`文件夹。
2.  **安装社区插件`Local Images Plus`**：
    - 在Obsidian设置中进入“社区插件” -> “浏览”。
    - 搜索并安装`Local Images Plus`，启用。
    - **作用**：确保剪藏的网页中的图片能下载到本地，并在Obsidian中正常显示。

### 步骤5：使用系统
- **手动摄取**：使用网页剪藏器浏览网页，一键将内容（含图片）保存至`raw`文件夹。
- **生成Wiki**：
    - 在Claude Code中，指示它基于`raw`文件夹中的资料或直接进行网络搜索，为特定主题（如“Claude Code Skills”）创建Wiki。
    - Claude Code会自动创建主题文件夹、索引文件和相互链接的文章，并更新`master-index.md`。
- **查询知识库**：
    - 在Vault中打开Claude Code，直接提问（如“解释RAG系统和这个Obsidian系统的区别”）。
    - Claude Code会依据`cloud.md`的指令，沿着`wiki` -> `master-index.md` -> 具体主题索引 -> 具体文章的路径进行高效检索和回答。

## 四、与传统RAG系统的对比
- **Obsidian RAG（本方案）**：
    - **优点**：设置简单、免费、透明可查、适合中小规模数据、维护成本低。
    - **缺点**：在处理海量文档（数百万级）时，检索效率和成本可能不如专业RAG系统。
    - **适用对象**：个人开发者、研究人员、小型团队、项目初期探索阶段。
- **传统/图RAG系统（如LightRAG）**：
    - **优点**：为大规模、超大规模文档检索优化，具备高级检索和图谱推理能力。
    - **缺点**：技术栈复杂、可能产生费用、过程不透明（黑盒）。
    - **适用对象**：需要处理企业级海量数据、对检索精度和复杂关系挖掘要求极高的场景。

## 五、核心要点总结
Andrej Karpathy提出的这套基于Obsidian的知识管理系统，巧妙地利用了文件系统的层次结构、Markdown的Wiki链接功能以及LLM（通过Claude Code）强大的文件理解和导航能力，模拟了RAG的核心检索增强生成效果。它摒弃了向量数据库等复杂组件，以近乎零成本的方式为个人和小团队提供了一个透明、易用且足够强大的知识库解决方案。其核心启示在于：对于大多数非海量数据的场景，从最简单的方案开始实验远比过早纠结于复杂技术选型更为高效。当现有方案确实无法满足规模需求时，再过渡到专业RAG系统也不迟。

---

## 原始字幕

Andre Carpathie just gave us the keys to his personal Obsidian RAG system.And I put RAG in air quotes because this Obsidian Power Knowledge Base has no vector database, no embeddings, and no complicated retrieval process. Yet, it solves the exact same problem that these more complicated RAG structures claim to do, which is allow our large language model to handle large amounts of documents and answer questions and gather accurate information about them. And the best part about this Obsidian-powered system is that it is very lightweight, it's essentially free, and it is the perfect middle ground for a solo operator or a small team. So today I'm going to show you how Carpathie's Obsidian knowledge system works, how to set it up yourself, and how it differs between traditional RAG systemsso you know if this is the right option for youso the process by which we are going to createthis obsidian powered knowledge systemwas laid out yesterdayin a pretty comprehensive twitter postby andre carpathynow the big takeaway from this postis that we are able to createlarge language model knowledge basesthat essentially act in the same wayas something like light rag or rag anythingor any other graph rag systemwith obsidianand we're able to do soin a rather simple mannerby just having a clever structureto our file systemand how we actually ingest dataand the end resultis that I am able to ingesta pretty significant amountof data and documentsinto my obsidian vaultand use cloud codeto ask questions about itto figure out connectionsbetween different thingsa.a. the exact same thingyou would dowith a traditional rag systembut with none of the overheadand a way simpler setupand as Andre lays outthe setup looks something like this first we have data ingestion we are bringing in articles we're bringing in papers we're bringing in repos from the internet or from wherever and we're bringing it into a raw directory inside of our obsidian vault this is essentially the staging area before it gets turned into a wiki we as the human being in this interaction are able to see all of this happening via obsidian obsidian for all intents and purposes is our front end here's where i can where all the documents are laid out here's where i can read all the wikis so it isn't sort of abstracted away in a black box like it isn't a rag system it's kind of hard even in a graph rag setup like light rag to actually go inside of here and really see everything i mean i can but as cool as this looks this isn't you know very efficient and from there you just do a q a via something like cloud code and like andre laid out here he expected that he would have to reach out for something like RAG, but the large language model has been pretty good about auto-maintaining index files and brief summary of all the documents it reads. And this is something we are going to be able to do too with a pretty simple cloud.md file, which I will be giving you. And you will be able to find that cloud.md as well as a written guide that comes with a bunch of prompts inside of my free Chase AI community. There will be a link to that in the description of this video. And speaking of Chase AI, and you knew this was coming, quick plug for my Cloud Code Masterclass. Just released this a couple of weeks ago,and it is the number one place to go from zero to AI dev especially if you do not come from a technical backgroundyou can find a link to this in the pinned comment so make sure to check this out if you're serious about learning this toolnow before we jump into the specifics of how to set up the subsidian system for yourselflet's go over the actual file structure because this is important to understand how data is coming into our vault and then getting turned into wikis. So the Obsidian vault is where everything lives. As you'll see, if you've never used it before, when you download Obsidian, you are going to designate a specific folder as the vault. In my case, it is quite literally called the vault. That's where everything in Obsidian lives. As a subfolder of the vault,we are going to have the raw folder the raw folder is where all of our research gets dumped anything we want to manually include in these wikis gets put this is essentially the staging folder so this is where all the raw data is going to be held this can be markdown files this can be pdfs and i'm going to show you how to use the obsidian clipper to essentially turn any web page into a markdown file that gets sent to the raw folder automatically we will have another subfolder that is the wiki所以我們要做,在大型語言,在我們上的網絡會是可以做的,是我們會看到它會有一個技巧,是我們會看到它在網絡的網絡,來自找它,我們會有一個網絡的網絡,在會發採訪,從那裡,它會發採取一個網絡,所以你看,我們有三個網絡網絡,一是AI agents,一是RAG systems,一是關於網絡網絡的網絡網絡, Now, in between the wiki folder and these sub wiki folders is the master index markdown. This is essentially just a list of all of the different wikis that have been created. Because the idea is when you, this is you, when you talk to Claude Code, all right, that's Claude Code over there, and say, hey, I want to learn more about AI agents. Can you ask, you know, I want to ask questions about my wiki. Well, what is it going to do? well it's going to go to the vault because you're probably already in there it's then going to go to the wiki folder it's going to go to the master index folder and say hey what wikis that we created oh he wants to know about rag systems okay goes down to rag and the wiki folders themselves have index files which break down all the additional content so what obsidian gives us and what this file structure gives us is a very clear path to find information even if we have a一整个人的图片and then from there you know I can click on it it takes me to the index of that specific wiki and then I can look at different stuff inside of there it's that simple and it's that simple for ai2 which is why we're able to use essentially just a markdown file structure to somewhat mimic a rag system so while that theory is cool now let's go into how to actually set this up for yourself first and foremost you're going to need to download obsidian you're just going to head to obsidian.md Go through the wizard, it's completely free and you're going to designate some folder as the vault Just create one, call it the vault Makes it easy for me and it'll probably work for you After we create the vault we now need to set up this file structure inside of it The easiest way to do that is with cloud code Simply open up cloud code in the vault So that's the directory I'm in and you're going to give it a prompt telling it to createrheit,是障ブ Solomon都属于Vault所以藉主是什么击开的角色让我把ンド惠等就感变出 gagstaging area for where all this information is going to get dumped until it gets turned into a wiki so just as needed now the next thing we want to do is create a cloud.md file personal assistant type projects things like this that are very markdown heavy cloud.mds are perfect for and this cloud.md file is breaking down the knowledge base rules as well as how to essentially traverse it so again that we aren't wasting tokens when we ask questions again i have this entire cloud.mdtemplate prompt you can use this claw.md file is also telling claw how to structure these markdown files so it's very easy to traverse files with this wiki links format now let's talk about how we can bring things into this raw folder how we can get data into our system in the first place well super easy way to do this is with the obsidian web clipper so i will put a link to this in the school or you can go to obsidian.md slash clipper and this is just a chrome extension which which makes it super easy to turn a web page into data, into a markdown file. Now the one issue with this Web Clipper is it's going to struggle with images. It's just not even going to bring them in. I'll have them as a link. But I want to be able to see the images from these documents I ingest inside of Obsidian. So what do we do? Well, we are going to use an Obsidian community skill or Obsidian community plugin to help with this. So one of the cool things about Obsidian is the community plugins. There's thousands of them. So if you're inside of Obsidian, I'm inside the desktop app right now.I come down here and I hit this little gear I'm gonna go to community plugins I'm gonna go to browseand then you're gonna search for local images plus you're going to download it install it and turn it on make sure it's enabled you can confirm it's enabled by heading to your community plugins tab and seeing this little tab turned on now if we use the obsidian web clipper and I can see that here is an extension you can see what happens it immediately pulls everything and if I hit add to obsidian I can see this entire article including the images now there is one thing we need to set up inside of the web clipper and that's making sure it actually pulls it into the raw folder automatically I don't want to have to manually do that you're just going to head to the options on your web clipper I just right clicked it and then over here on the left where it says defaultI created my own new template but you can stick on the default if you want.Where it says location and note location right here.You're going to want to change that from clippings to raw.And that will make sure when you use the web clipper it automatically goes into the raw folder.So now with the Obsidian web clipper extension and the images community pluginwe can now turn any web page on the internet into a markdown file that will be used for our wiki.这 primer 320我们可以做一个副锁文 voz说是让'm说让它们叫想这是本来的同时你 levant more入手法和拿换材ẫn给你 temporalled in via the WebFlipper, go conduct your own research and bring in the relevant RAW MD files to generate that wiki. So what is it going to do? It's going to go on the internet, use its standard web search, and it's going to create its own wiki about CloudCode skills. So what you see is that this RAW folder, this whole RAW pipeline, that's more for you. That's for when you mainly want to put in some information. Now, you can have CloudCode do that as well, but CloudCode is also smart enough to essentially take the research, figure out what's relevant itself, and just create the wiki directly. This raw folder is really for you, the human being, to have some level of organization. And here's what Cloud Code came back with. So it created the Cloud Code Skills wiki. We see here in the master index that it's referenced here. If I click on it, this then brings us to the index of Cloud Code Skills. And right now it has four articles. So here's the skills overview article. You can see it links to websites and it also links to different articles within our Obsidian Vault.so if I click on skill ecosystemhere's more stuffI click on top skillsright so on and so forththere's a very clear pathwayfrom one article to anotherand how these things relatewhich means when you askCloud code questionsabout these articlesin these subjectsit's easy and cheapfor it to answer questionsabout themwhich then brings usto the obvious questiondo we need rag at allyou know we look atsomething like thislightrag setupyou watch my last few videoswithlightrag and rag anythingand seeing how simpleto set up with Obsidian, you're probably like, well, why would I ever even bother with these more complicated setups at all? And the truth is, if you're a solo dev, a solo operator, or a small team that isn't dealing with thousands of documents, the answer probably is Obsidian makes more sense for you. It's lightweight, and you really don't need RAG. These large language models, these harnesses like Cloud Code are good enough for your use case. And we can sit here andweeds about the differences between the obsidian rag and true rag but the truth is the big thing is scale right are we trying to scale to millions of documents or are we not because at a certain scale it's going to be cheaper and faster to use a proper rag system no matter how good cloud code is at navigating this md file document network you've created but this isn't a question you necessarily need to have the exact answer to right away why wouldn't you just start with something likeObsidian and if it's clear your scale goes well beyond the bounds of what this thing can handle then just move into rag i think people get really caught up in like answering this question when it's like just try it out just experiment it's not costing you anything to use some sort of rag system rag system like obsidian and if it doesn't work it doesn't work fine then go to use light rag instead people want to sit here as they inevitably will in the comments and like argue this back and forth just try it i think the answer will be pretty clear at a certain point when you need to move to a true RAG system. But the nice thing with this is, is again, most people don't need a real RAG system. They just don't, right? Even if they're in a small business team situation. So having a proper, you know, orchestrated system like the Subsidia and Knowledge Base, I think is a huge boon to the majority of people. So I hope this breakdown was useful to you. Definitely check out Andre's post about this. He goes into a fair amount of detail. Make sure to check out the free Chase AI School. There's a link to that in the description that has all the promptsand a written breakdown of how to actually do thisif you got confused at any partand as always take a look at Chase AI Plusif you want to get your hands on that masterclassbesides that let me know what you thoughtand I'll see you around