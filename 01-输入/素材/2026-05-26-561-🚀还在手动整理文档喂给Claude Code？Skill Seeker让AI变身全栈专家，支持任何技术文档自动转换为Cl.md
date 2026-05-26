---
title: "🚀还在手动整理文档喂给Claude Code？Skill Seeker让AI变身全栈专家，支持任何技术文档自动转换为Claude Skills！开发效率倍增！"
author: "AI超元域"
source: https://www.bilibili.com/video/BV1R2sZzYE5T
date: 2026-05-26
tags:
  - bilibili
  - 笔记
  - AI
  - 提效工具
  - Claude Skills
  - 文档自动化
  - 开源
  - 编程助手
type: video-note
bvid: BV1R2sZzYE5T
duration: "11:07"
cover: "http://i0.hdslb.com/bfs/archive/65f1d2185498e2367cd34eebece18ff45f0af65a.jpg"
description: "🚀程序员福音！学习新框架从此不用看文档？Skill Seeker让Claude成为你的技术导师，CrewAI、AutoGen、LangGraph随便上，自动生成完整项目代码，告别学习曲线陡峭的噩梦    🚀🚀🚀视频简介： 📦完整教程！Skill Seekers从入门到精通：安装配置+CrewAI实战+Claude AI测试+Claude Code集成，10分钟让Claude精通任何技术栈，附GitHub源码+使用技巧+常见问题解答 本期视频将为大家深度解析Anthropic最新发布的Agent Skills功能，并重点演示开源神器Skill Seekers的实战应用！💪 ✨ 核心亮点： - 5"
---

# 🚀还在手动整理文档喂给Claude Code？Skill Seeker让AI变身全栈专家，支持任何技术文档自动转换为Claude Skills！开发效率倍增！

> [AI超元域](https://space.bilibili.com/3493277319825652) | [BV1R2sZzYE5T](https://www.bilibili.com/video/BV1R2sZzYE5T) | 时长 11:07

## 介绍Agent Skills和Skill Seeker
- Anthropic最近发布的新功能**Agent Skills**被认为是AI定制化领域的重大突破，它允许Claude加载自定义指令、脚本和资源，使AI在特定任务上表现更出色。
- **与MCP功能对比**：Agent Skills更高效，仅需一个Markdown文件，加载30-50token的描述；MCP需要多个组件架构，预先加载数千token，复杂度更高。
- **Skill Seeker**是一款开源自动化工具，专门用于将任何文档网站、PDF文件或技术文档转换为Claude AI的技能包（Skills），解决手动创建Skills耗时（需阅读和总结文档）的痛点。
- **关键优势**：使用Skill Seeker可在几分钟到十几分钟内自动完成整个过程，降低学习任何开源项目的成本至为零，实现开发效率倍增。
- **示例应用**：使用Skill Seeker创建了代码审查Skill（由Codex CLI审查代码后由Claude优化）和Anulogen框架生成智能体代码的Skill。

## Skill Seeker的核心优势
- **智能爬虫引擎**：支持任何文档网站结构，自动识别页面结构，智能过滤无关内容，使用自定义选择器，适用于99%的文档网站。
- **AI深度增强**：使用Claude AI将基础内容转为专业指南，提取最佳代码实例，生成快速参考指南和使用场景，支持本地或API两种方式。
- **智能缓存系统**：一次创建后可随时重建，支持快速迭代。
- **智能内容分类**：自动识别和组织文档内容，创建清晰的结构。
- **代码语言检测**：自动识别编程语言，添加语法高亮标志。
- **一键打包部署**：自动生成Claude和Claude Code可用的ZIP技能包，具备完整目录结构，即装即用，5-10秒内完成打包。

## 工作流程
1. **智能爬取阶段**：使用高级网页爬虫自动访问文档网站的所有页面，通过智能算法识别主要内容区域，提取纯净的文档内容。
2. **智能分类阶段**：对提取的内容进行深度分析，将文档自动分类到不同的主题类别中，形成清晰结构。
3. **AI深度增强阶段**：Claude AI深度分析文档内容，识别最佳实践，提取关键代码实例，生成使用场景说明，并创建全面的Skill文件。
4. **自动打包部署阶段**：将所有内容按照Claude Skill的标准进行打包，生成可直接上传到Claude的ZIP文件。

## 使用演示与实操步骤
### 准备工作与安装
- **步骤1：克隆项目**：打开终端命令行（Windows用户打开CMD），使用命令 `git clone <Skill Seeker项目地址>` 将项目克隆到本地。
- **步骤2：进入项目路径**：使用命令 `cd <项目路径>` 进入Skill Seeker目录。
- **步骤3：执行安装命令**：运行官方提供的安装命令（如 `pip install -r requirements.txt` 或类似），按照提示完成安装。

### 在Claude Code中生成Skills
- **步骤1：打开Claude Code**：启动Claude Code工具。
- **步骤2：输入自然语言描述**：在Claude Code中直接输入自然语言指令，加上文档网站链接。示例：“生成CrewAI Skill https://docs.crewai.com”（支持中文描述）。
- **步骤3：自动执行任务**：Claude Code会分解任务为子任务（如创建配置文件、评估页面数量、抓取文档、打包成ZIP文件），全自动完成。整个过程约需7-8分钟。
- **步骤4：保存生成文件**：任务完成后，Skill ZIP文件会自动保存在指定路径下。

### 上传和安装Skill到Claude
- **在Claude AI网页版使用**：进入Skills页面，点击上传，选择生成的ZIP文件，上传成功后即可在对话框中调用该Skill。
- **在Claude Code中安装**：
  1. 新开终端，使用命令在Claude Code的用户级Skills文件夹下创建子文件夹（如 `mkdir -p ~/.claude/skills/CrewAI`）。
  2. 找到Skill Seeker生成的Skill文件路径，使用命令 `cp -r <生成的Skill文件夹内容> ~/.claude/skills/CrewAI/` 拷贝文件。
  3. 重启Claude Code，使用 `/CrewAI` 命令即可调用Skill。

## 示例与效果
- **示例项目**：使用Skill Seeker为开源智能体框架**CrewAI**创建Skill。
- **效果测试**：
  - 在Claude AI中：上传Skill后，自动生成基于CrewAI的智能体系统代码，提供完整项目文件、使用说明（如设置API key、启动命令）。
  - 在Claude Code中：安装Skill后，输入 `/CrewAI` 命令，自动生成可运行的CrewAI项目代码，包括agents定义、配置文件和说明文档。
- **关键成果**：无需手动阅读官方文档，Skill Seeker自动将文档转换为高质量Skills，实现代码全自动生成，节省大量学习时间。

## 总结
Skill Seeker通过自动化工具链（智能爬虫、AI增强、一键打包）将任何技术文档转换为Claude Skills，彻底解决手动创建Skills的耗时问题。实操演示显示，它能快速生成可直接在Claude AI和Code中使用的Skills，使开发者无需深入学习开源项目文档即可生成完整代码，大幅提升开发效率和学习效率，是AI编程辅助领域的创新工具。

---

## 原始字幕

Athropec最近密集发布新功能尤其是前几天发布的Agent Skills还有Cloud CodeWeb对于AI Coding的场景这些功能非常有帮助尤其是Agent Skills功能被普遍认为是AI定制化领域的一次重大突破因为Skills功能允许Cloud加载自定义的指令脚本和资源使其在特定任务上表现更加出色相比以前Athropec发布的MCP功能因为MCP会预先加载数千token来描述所有可能的能力而Skills只需要加载30到50token的描述仅在需要特定功能时才拉取完整的信息所以在理论上Agent Skills是具有无限容量的相比MCP Agent Skills只需要一个Markdown文件再配合其他科选的资源而MCP它需要多个组件架构所以它的复杂度远比Agent Skills要复杂非常多所以Agent Skills发布之后备受好评大家都在创建自己的Skills像平时我们使用Cloud的自带的Skills Creator这个Skill来创建我们自己的Skills的时候效果并不是非常好创建出来的Skills可能达不到我们的要求所以本期视频将为大家演示一款开源的Skills生成项目Skill Seeker它是一款强大的自动化工具专门用于将任何文档网站或者PDF文件转为Cloud AI的技能报它解决了一个关键痛点那就是手动创建CloudSkill需要花费比较长的时间用于阅读文档和总结文档而使用这个工具就可以在几分钟到十几分钟内自动完成整个过程所以有了这个工具我们学习任何开源项目的成本都降为了零而且我使用这个工具创建了一个能够将Cloud Code写出的代码由Codex CLI进行代码审查然后再由Cloud Code根据Codex CLI的审查结果对代码进行优化的Skill并且我还使用这个工具创建了一个支持用微软的Anulogen框架来生成智能体代码的一个Skill像这样我们就可以在Cloud Code中输入需求然后由Cloud Code为我们自动调用Anulogen框架为我们生成智能体代码好 本期视频将为大家想显示Skill Seeker这个开源工具的使用方式并且测试使用这个项目来生成Skills的效果在演示之前我们先看一下Skill Seeker它的概念以及优势它是一个强大的自动化工具专门用于将任何文档网站转为Cloud AI可用的技能包它通过智能爬虫AI增强和自动打包三大核心技术无需我们阅读和手动整理文档即可全自动创建高质量的Cloud Skills像这样我们就可以大幅度节省时间并且实现高质量的输出而且适用于任何文档网站支持所有主流的编程语言我们还可以将PDF转为Skills好下面我们看一下它的核心优势首先它是通过爬虫引擎提取网页内容它支持任何文档网站结构能够自动识别页面结构智能过滤无关内容支持自定义选择器适用于99%的文档网站它使用Cloud AI将基础内容转为专业机指南能够提取最佳代码实力生成快速参考指南添加使用场景还包含本地或API两种使用方式还有就是它的智能缓存系统Hatch一次随时能够充建支持快速迭代它还具备智能内容分类能够自动识别和组织文道内容创建清晰的结构它还具备代码语言检测能够自动识别编程语言添加语法高量标志最后就是一键打包部署能够自动生成Cloud和Cloud Code可用的ZIP技能包具备完整的目录结构集传集用5到10秒即可完成它的详细工作流程分为四个阶段第一阶段就是智能爬取使用高级网页爬虫自动访问文档网站的所有页面通过智能算法识别主要内容区域从而实现提取纯净的文档第二阶段就是智能分类对提取的内容进行深度分析将文档自动分类到不同的主题类别中第三阶段就是AI深度增强Cloud AI会深度分析提取的文档内容识别最佳实践提取关键代码实例生成使用场景说明并创建全面的Skill文件第四阶段就是自动打包部署将所有内容按照CloudSkill的技能标准进行打包最后生成可以直接上传到Cloud的Zip文件所以使用这个工具我们就可以将任何开源项目或者框架打包成Skills好下面为大家详细演示和测试SkillSeeker它的使用方式并且我们使用它来结合实际的开源项目来创建Skills想使用这个项目非常简单我们只需要按照官方给出的命令去执行就可以首先我们需要将这个项目克隆到我们本地我们直接打开中端命令行Windows用户打开SAMD用getclone命令将这个项目克隆到我们本地我这里已经克隆完成然后我们用cd命令进入到这个项目的路径然后我们再执行这条命令我们直接执行这条命令就可以然后按照它的提示一步一步去操作好我这里已经安装完成安装完成之后我们就可以在Cloud Code中直接使用自然语言再加上指定的文档网站的链接就可以让它自动为我们来生成Skills好下面我们可以找一个开源的智能体框架CrewAI然后我们找到它的文档网站在Cloud Code中使用Skills Seeker根据CrewAI的文档创建Skills下面我们回到中端命令行我们打开Cloud Code中使用Skill Seeker根据Crew AI的文档创建Skill下面我们回到中端命理行我们打开Cloud Code在Cloud Code中我们直接输入自然语言描述再加上刚才的链接我输入的是生成Crew AI Skill像这个自然语言描述大家也可以直接用中文去描述然后我们直接运行可以看到这里他开始抓取Crew AI官方文档的这些内容在这里可以看到它将我们的任务分解成了四个子任务第一个子任务就是创建配置文件第二个子任务就是评估页面数量第三个子任务就是抓取CrewAI的文档第四个子任务就是打包成ZIP文件这样这样的话这四个子任务就会由它全自动去完成可以看到这里它自动打开了一个中端我们这里允许它执行这个中端执行的任务就是抓取这些文档然后这里他又先开了一个中端我们直接允许他执行然后这里他又开启了另一个中端我们让他执行好再等待了大概七八分钟左右这些任务已经完成他已经将CrewAI这个智能体框架创建成了Skill并且将创建好的Skill打包成了ZIP文件放在了这个路径下好下面我们可以进入Cloud AI的网页版在Skills这里我们点击上传然后找到它创建的Crew AI这个ZIP文件点击上传这里提示上传成功这里就显示了Crew AI这个Skill然后我们测试一下这个Skill的效果好进入到这个默认的对话框我们直接运行它默认的提示次看一下它能否生成Crew AI的这些项目代码好这里它提示它将使用Crew AI创建一个AI Research的智能系统好在等待了几分钟之后这里他使用CrewAI为我们成功创建了一个智能体而且这里还显示了这个智能体的demo而且这里还给出了具体的使用方式包括进入到项目路径安装所需的依赖设置API key然后启动这个智能体他这里给出了非常完整的说明文档像这样我们就成功实现了使用SkillSeeker根据CrewAI的官方文档全自动为我们生成了CrewAI skill好刚才我们测试的是在Cloud AI中来使用的Crew AI Scale下面我们还可以将Crew AI Scale直接安装到Cloud Code中这样的话我们就可以直接在Cloud Code中来使用Crew AI为我们生成智能体代码想在Cloud Code中使用这个Skill也非常简单我们可以新开一个终端命令行然后用这条命令我们在Cloud Code的用户级命令中的Skills文件夹下创建一个Crew AI文件夹我们直接运行就可以下一步我们需要找到Skill Seeker为我们创建的Crew AI Skills文件夹下创建一个CrewAI文件夹我们直接运行就可以下一步我们需要找到Skills Seeker为我们创建的CrewAI Skill的项目路径也就是在这个路径下然后我们就可以用CP命令将文件夹里的所有内容都拷贝到刚才我们创建的这个文件夹里然后我们直接执行这条命令就可以然后我们可以重新打开一下Cloud Code然后我们将它列出来所有的Skills好这里他列出了所有的skill包括我们刚才创建的CrewAI而且我们还可以在VSCode中使用Cloud Code的扩展插件来测试好下面我们就可以再输入框输入斜杠再输入CrewAI再运行我们就可以在Cloud Code中让他使用CrewAI skill为我们创建基于CrewAI的智能体育项目他这里给出了几个案例然后这里我们可以让他来创建一个新的CrewAI的智能体育项目我们这里直接入E让它创建新的Crew AI项目这里它提示它将创建一个新的Crew AI项目好这里提示这个项目已经创建成功这里列出了项目的文件结构并且给出了我们具体的使用方式包括设置API key还有启动项目下面我们可以看一下它为我们创建的项目这里是完整的Crew AI的这些项目文件然后我们再看一下这些agents这里是它创建的这些agents而且这里都加入了详细的注释然后这个文件我们就可以设置我们的API key而且这里还给出了欧拉玛的设置方式这里就是这个项目的说明文档包括创建虚拟环境安装这些依赖设置API key还有项目的结构像这样我们就做到了完全不需要我们自己去阅读CrewAI的官方文档然后只需要用Skill Seeker根据CrewAI的官方文档来生成Skill然后我们就可以在Cloud Code中调用这个Skill为我们全自动生成基于CrewAI框架的多智能体系统像以前我们需要阅读CrewAI的官方文道熟悉CrewAI的这些代码以及使用方式然后我们才能使用CrewAI创建我们自己的AI智能体但现在有了Skill Seeker我们只需要用Skill Seeker来生成对应的Skill然后我们上传到Cloud AI或者安装到Cloud Code里我们就可以使用这个Skill为我们生成完整可用的项目代码针对任何开源项目我们都可以使用Skill Seeker根据官方文档为我们生成对应的Skill像这样就能大大节省我们的学习时间从而大幅度提升我们的工作效率本期视频所用到的代码和指令我都会放在视频下方的描述栏或者评论区如果你在视频下方无法找到的话也可以通过我的博客去查找本期视频做对应的笔记好 本期视频就做到这里欢迎大家点赞关注和转发谢谢大家观看