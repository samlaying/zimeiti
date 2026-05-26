---
title: "【CC4Research】我用claude code 10分钟做了个research！！！"
author: "宝宝粒的技术分享"
source: https://www.bilibili.com/video/BV1jJzSBcEah
date: 2026-05-26
tags:
  - bilibili
  - 笔记
  - AI
  - 提效
  - 学术研究
  - 工具配置
  - Claude Code
  - Python管理
type: video-note
bvid: BV1jJzSBcEah
duration: "7:22"
cover: "http://i2.hdslb.com/bfs/archive/19c3d398b2b805b4bf2b0f296e11a0fa1c345417.jpg"
description: "配置github和arxiv mcp，用Claude Code给你做research！！！  相关链接： https://github.com/blazickjp/arxiv-mcp-server https://github.com/anthropics/claude-plugins-official"
---

# 【CC4Research】我用claude code 10分钟做了个research！！！

> [宝宝粒的技术分享](https://space.bilibili.com/2266269) | [BV1jJzSBcEah](https://www.bilibili.com/video/BV1jJzSBcEah) | 时长 7:22

## 视频概览与核心功能
- **视频主题**：演示如何通过配置Claude Code，利用MCP（模型上下文协议）扩展其能力，在10分钟内完成一个简单的学术研究（Research）。
- **核心功能展示**：
    - 让Claude Code **总结论文**。
    - 基于总结内容，让Claude Code **在GitHub上搜索相关报告/代码库**。
    - **生成一个研究项目**（例如视频中提到的“火影忍者首饰识别”项目的前期研究）。
- **状态说明**：演示中的项目（如火影忍者识别）目前仅完成了研究（Research）部分，项目已生成并准备好了相关文件（如README），但代码和数据尚未完全就绪，不能直接运行。

## 实操步骤：配置 Claude Code 以集成 GitHub
1.  **开启插件**：
    - 打开 Claude Code，进入插件（Plugin）管理界面。
    - 搜索并安装 **“Github”** 插件。注意：不要使用网上过时的MCP安装方法，应直接使用此插件。
2.  **获取 GitHub Personal Access Token**：
    - 登录 GitHub，进入 `Settings` -> `Developer settings` -> `Personal access tokens` -> `Tokens (classic)`。
    - 生成一个新 Token，为所有仓库授予权限。
    - **复制**生成的 Token。
3.  **在 Claude Code 中配置 Token**：
    - 在 Claude Code 的插件设置中，找到 Github 插件的配置项（可能在“catch”或类似选项中）。
    - 将复制的 GitHub Token **粘贴**到对应的配置字段中。
4.  **验证连接**：
    - 配置完成后，在 Claude Code 中使用斜杠命令 `/MCP`。
    - 如果配置成功，会看到 Github MCP 已 **“connect”（连接）**。
    - 连接成功后，即可通过 Claude Code 搜索和访问 GitHub 上的仓库（Report）。

## 实操步骤：配置 Claude Code 以集成 XV（学术论文工具）
1.  **安装 UV**：
    - `UV` 是一个 **Python 的包管理工具**。如果系统中未安装，需要先安装它。建议运行相关命令以确保依赖下载完整。
2.  **配置 MCP Server**：
    - 在用户的 `~/.config/claude-code/` 目录下，找到 `mcp.json` 或类似配置文件。
    - **重要限制**：配置的MCP工具（如XV）**仅对配置文件所在目录下的项目生效**。如果终端工作目录不在该配置目录下，则无法使用XV的MCP工具。
    - 参考示例，将XV的MCP服务器配置段添加到配置文件中。
3.  **重启并验证**：
    - 重新启动 Claude Code。
    - 再次使用 `/MCP` 命令，应能看到 XV MCP 已连接。XV **无需登录或API Key**，可直接使用。

## 关键配置与注意事项
- **默认搜索限制**：Claude Code 的默认 Web Search 无法有效爬取 GitHub 项目内容，因此必须通过配置 **Github MCP** 来解决此问题。
- **MCP配置作用域**：配置的MCP工具（如XV）是基于目录的。确保在正确的项目目录下运行Claude Code才能调用相关工具。
- **Token消耗**：使用MCP进行大量论文搜索或分析时，会消耗较多Token。但工具本身通常有限制（例如默认的 `maxresults=15`），不会无限制地返回所有结果，这有助于控制消耗。
- **工具扩展性**：配置MCP是扩展Claude Code能力（如连接Github、访问学术工具XV）的关键方式，使其从一个聊天机器人转变为一个具备外部工具操作能力的自动化研究助手。

## 总结
本视频的核心是演示如何通过**配置MCP（模型上下文协议）**，将 **Claude Code** 与 **GitHub** 及 **XV（学术论文工具）** 连接起来，从而赋予AI代码助手进行**自动化文献检索、总结和项目生成**的能力。关键步骤包括安装相应插件/工具、获取并配置访问凭证（如GitHub Token），并注意MCP配置的**目录作用域限制**。通过这种配置，可以实现一个高效、自动化的研究工作流。

---

## 原始字幕

没问题的话我们就到这我们今天的主题这个我们要把这个XV和这个GitHub配好配好了能做什么事情你们可以看到这里我做了一个research下了一点paper让他做了一些总结让他基于基于总结的东西又去GitHub搜了一些report生成了这么一个项目这个项目之前讲的火影忍者首饰识别这么一个项目这里都是这他做的research现在能跑起来吗还没呢对你是没数据但整个Appline能运行起来吗还没跑呢OK对大体是这个样子对项目这是相关的引诱这是有引诱吗真来讲的还真这是我的项目他都帮我引诱都准备好了OK好然后开始配我们首先我开这首先我们到这个Cloud Code里面去把plugin打开这个应该可以了你们在操作吗我有点忘了但是你们可以直接把plugin打开打开了以后你可以在这里搜索Github因为我这边装了所以这里不显示了应该在Github搜好装好这是一个XV这是一个plugin的装的形式你不要去看网上任何就装Github MCP的形式这个形式已经逐渐被这个Cloud Code给淘汰掉了现在去装感觉会有点问题好装好了以后我们再去Github账号训settingssettings下面去获取personal key在这developer settings在这里用第二个就行创建一个给到所有的权限然后这个key复制下来复制下来以后就比较麻烦的是我们要到这里来点克劳德这里有个plugins找到这个catchcatch这边是我想想getup不知道为啥有两个反正找一个最新的这个好像是介绍对这里原来的它是一个bash的写法但是因为PowerShare运行bash的命令会有点问题直接把这个key贴到这里来OK贴好了以后这边你在一个斜杠MCP就可以看到它这边会有connect连接成功这个时候你就可以通过Talad Code去搜索Github的report了这是Github的配置然后3是这里因为它稍等一下默认WebSearch是不搜搜不了Github的搜不了它能搜到它爬取不了项目很多网站它可以搜到他让你点开但是他爬取不了任何东西OK所以加这个就可以对Oxv是这个这个就是搜索论文下载论文大体是这样这些东西我尝试了一下都有点问题但是先做这步先让你的中端能够跑这个命令有人不知道UV吗这话Tarita应该不知道我跟路易斯应该知道不觉得应该是在说我没有我只是在确认一下那时和那时知不知道那你直接问我知不知道不就行了吗给你面子吗知道知道OK但我电脑没拙UV是Python的一个管理工具管理器我知道但我电脑没拙对你如果要让那个MCP跑起来的话你最好就是运行一遍让他自己下载一些依赖下载好能够记起来就可以了OK接下来以后你可以参照这个这个东西这个命令我这边已经配好了在这里到你的用户user下找到这个点json找到你这个项目的路径他这边我不知道为什么好像改过几次了这边只能配置目录下的mcp也就是说说如果配在这里如果我的中端不在这个目录下它就没有XV的这个MCP的工具OK记录了以后你找到这里的这一段贴到这个MCP的Server里面再重新启动一下在结构MCP的时候就可以看到它连接了因为XV它是不用登录的也不用任何Token不用任何API Key它就直接可以支持你去做一些API的操作对就演示一下大家想看什么东西我后面让它总结保存成markdown的文件这样的topic会不会太大这个paper数量特别多的话会很靠token吗还是还好他不会全量去分析我的经验他不会全量去分析有的错评你给他说的很细可能还好有的说的很粗他虽然不会全量但不知道他会说多少对他应该会有限制的这是借口的限制就比如说maxresult15这可能不是借口这可能是他默认的我这边有个请求但是请求没有指定数量这边他调用MCP工具填参数的时候这边会给个默认的对应该是这个逻辑OK那么还好