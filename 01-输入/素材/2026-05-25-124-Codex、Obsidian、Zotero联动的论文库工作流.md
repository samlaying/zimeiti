---
title: "Codex、Obsidian、Zotero联动的论文库工作流"
author: "原来是大如呀"
source: https://www.bilibili.com/video/BV17FD1BmE2t
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI工具
  - 论文管理
  - 科研提效
  - Obsidian
  - Zotero
  - Codex
type: video-note
bvid: BV17FD1BmE2t
duration: "8:33"
cover: "http://i1.hdslb.com/bfs/archive/219fba0a68b0768dfe1897b33d47efd9ec2ef4eb.jpg"
description: ""
---

# Codex、Obsidian、Zotero联动的论文库工作流

> [原来是大如呀](https://space.bilibili.com/631486754) | [BV17FD1BmE2t](https://www.bilibili.com/video/BV17FD1BmE2t) | 时长 8:33

## 引言
视频介绍了如何使用Codex、Obsidian和Zotero联动构建论文管理和检索系统。该系统通过三个工具分工合作，实现高效的论文处理和信息检索，适用于科研工作者进行文献管理和智能查询。

## 工具角色分工
- **Zotero**：负责管理文献和PDF文件，提供文献组织和存储功能，便于按主题分文件夹管理。
- **Codex**：负责调用GPT进行总结和管理，处理论文内容，支持单篇或批量处理，并可用于对话式查询。
- **Obsidian**：负责保存笔记和进行后续检索，利用DataView插件提取笔记属性，生成索引页。

## 详细工作流程

### 第一步：下载Skills和准备Obsidian
1. **下载Skills**：
   - 从Github下载两个Skills文件夹：
     - **Zotero Analytical Workflow Skills**：包含三个子Skill，用于自动化处理论文。
     - **Research for Literature Retrieval Skills**：辅助文献检索，具体用途在流程中涉及。
   - 这些Skills是Codex工作流的核心，需确保下载完整。

2. **设置Obsidian**：
   - 在Obsidian中新建一个Bot，例如命名为“ResearchBot”。
   - 创建目录结构：
     - 一个目录用于存放所有论文（位置重要，需正确设置以便后续访问）。
     - 另一个目录用于存放论文框架模板（可自定义，针对研究方向）。
   - **准备模板**：使用自定义模板，重点设置**Frogmatter**笔记属性区。
     - Frogmatter用于填写检索字段（如标题、作者、关键词、摘要等），字段越详细，后续DataView检索越方便。
     - 模板内容应根据研究领域调整，例如卡牌游戏或机器学习相关字段。

### 第二步：处理论文
1. **使用Zotero管理论文**：
   - 在Zotero中按主题分文件夹组织论文，例如创建“机器学习卡牌决策”文件夹。
   - 论文需以PDF形式存储在Zotero中，便于后续抓取。

2. **使用Codex处理论文**：
   - 打开Codex，加载Zotero Analytical Workflow Skills。
   - **Skills说明**：
     - **Zotero Collection Manager**：负责调度整个工作流，协调其他Skill。
     - **Zotero Data Fetcher**：抓取每篇论文的元数据（如标题、作者、摘要）。
     - **Zotero Analytical Writer**：负责论文的处理部分，生成结构化笔记。
   - **实操步骤**：
     - 处理单篇论文：在Codex中输入“精读，所以Tail中的，[论文名称]”，例如“Towards sample efficient deep reinforcement learning in collectible card games”。Codex会自动处理并生成笔记。
     - 处理整个文件夹：在Codex中输入“处理Zotero中的机器学习卡牌决策中的所有论文”。Codex会按工作流批量处理文件夹内所有论文。
     - 处理完成后，论文笔记自动保存到Obsidian的对应目录中，Frogmatter属性已填充。

### 第三步：检索与应用
1. **安装DataView插件**：
   - 在Obsidian中安装DataView插件（社区插件）。
   - 如果未安装，需关闭第三方安全模式，打开社区插件市场搜索“DataView”并安装。
   - 安装后确保插件处于启用状态。

2. **使用DataView检索**：
   - DataView插件自动提取每篇论文笔记前的Frogmatter属性。
   - 基于这些属性生成索引页（如动态列表），便于快速浏览和检索论文。

3. **在Codex中查询**：
   - 在Codex中打开Obsidian的论文库文件夹。
   - 直接与Codex对话，提出自然语言问题，例如“针对卡牌类游戏的机器学习方法有哪些？”。
   - Codex基于已处理的论文库，利用GPT进行总结，给出准确结论和检索结果。

## 示例与效果
- **处理示例**：处理论文“Towards sample efficient deep reinforcement learning in collectible card games”后，Obsidian中自动生成带Frogmatter属性的笔记。
- **查询示例**：询问卡牌游戏机器学习方法时，Codex返回基于论文库的详细总结，内容准确。
- **效率提升**：整个流程实现自动化，减少手动整理时间，增强检索能力。

## 总结
这个工作流通过Codex、Obsidian和Zotero的联动，实现了从文献管理、论文处理到智能检索的全流程自动化。关键步骤包括下载专用Skills、设置Obsidian目录和模板、使用Codex处理论文、以及利用DataView插件进行检索。最终，用户可以通过自然语言查询快速获取论文库中的信息，大幅提升科研效率，适用于需要高效管理大量学术文献的研究者。

---

## 原始字幕

大家好,这期视频我想分享一下我现在是怎么用Codex,Obsidian和Zotero进行我自己的论文管理和检索系统的。现在界面上可以看到就是最后搭建出来的一个结果我们可以跟现有的论文库通过Codex对话来得到一些结论和总结在这套流程里面主要是用到三个工具分别负责不同的事情Zotero负责管理文献和PDF,Codex负责调用GPT和总结管理,Obsidian则主要是负责保存笔记和进行后面的检索。整个流程我主要是分路成三个步骤来讲解。第一步要先下载好我在Github上传的这两个Skills一个是这个Dotelian Analytical Workflow Skills一个是Research for Literature Retrieval这个Skills等一下我会讲到这两个Skills具体是如何用的接下来要做好准备的是打开Obsidian在里面新建一个关于论文的Bot可以大家自由创建一下我这里又创建的名字叫做ResearchBot了这个目录里面是这个目录的位置比较重要因为它有关系到我们下面一部论文库的位置在这里面要一个是放所有的论文一个是放我们后面处理的时候需要用到的一个论文框架这里大家可以自由替换成自己研究方向所针对性的框架内容这个模板中最重要的一个部分就是模板前面的这个笔记属性区也就是Frogmatter用来写一些适合检索的字段写的越详细就会越方便我们后面用DataView进行检索准备好论文准备好模板之后下一步就是处理论文我一般习惯在Zotero里面把论文按照主题分好文件夹分文件夹进行处理然后在Codex这边就要用到了我们刚刚说的其中一个Skills文件夹就是这个Zotero Analytical Workflows这个里面有三个Skill一个是Zotero Collection Manager负责对整个Skill进行调度第二个是Zotero Data Fetcher这主要是负责抓取每一篇论文的原数据然后是Zotero Analytical Writer则是主要负责论文的处理部分具体的使用我在这个文件夹中给大家演示一下如果我们要经读The Taro里面的某一篇论文我们就可以直接在Codex中说,精读,所以Tail中的,比如说这篇,Towards sample efficient deep reinforcement learning in collectible card games我们就直接把这个名字复制下来然后跟他说视频里放Codex思考过程有点长所以都剪辑掉了好的,现在我们就是可以看到他已经处理好单篇的论文了。如果我们想要处理Zotero里面某一个文件夹中的所有论文也可以直接跟他说处理Zotero中的机器学习卡牌决策中的所有论文这样Codex就会按照我们整个工作流的流程来进行处理了好的,现在我们就可以看到论文已经被处理好了现在打开Obsidian就可以看到这几篇论文已经被整理在了这个里面把所有的论文都处理好了之后下一步就是在Obsidian里面做检索这里需要确认在我们的Obsidian里面安装了一个叫DataView的插件如果没有安装这个插件的话就要关闭第三方安全模式然后打开社区浏览社区插件市场浏览安装保证你的这个DataView是一个打开的状态它的作用主要是提取每篇论文笔记前面的这个属性属性界面的属性它的作用主要是提取每篇论文前面这个笔记属性的部分然后自动生成锁引页以上的部分都完成之后我们就可以在Codex里面打开这个论文库的文件夹和Codex进行对话了比如我们可以问他针对卡牌类游戏的机器学习方法有哪些?好的,现在就是Codex已经基于他的回答逻辑给出了我结论。内容也基本都很准确。好的整个论文库的搭建就是这样了祝希望这个视频可以帮助到大家祝大家科研胜利