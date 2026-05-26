---
title: "【保姆级教程】OpenClaw配置最强国产大模型Kimi K2.5 | Cloudflare云端部署版"
author: "五里墩茶社"
source: https://www.bilibili.com/video/BV1tdFGzYEbw
date: 2026-05-26
tags:
  - bilibili
  - 笔记
  - AI
  - 云计算
  - 模型部署
  - 配置教程
  - OpenClaw
  - Kimi K2.5
type: video-note
bvid: BV1tdFGzYEbw
duration: "10:40"
cover: "http://i2.hdslb.com/bfs/archive/43378546ee3520ff1543d31323228290e0578e81.jpg"
description: "一个key用全球大模型🔴 https://DMXAPI.cn 🚀 国内直连OpenAI、Claude、Gemini，💰￥1元起充！ 推荐一个目前全网价格最实惠的合租平台，ChatGPT，MidJourney，奈飞，迪士尼，苹果TV等热门软件应有尽有 - https://dub.sh/unibus ，首单9折优惠 - 优惠码 01Coder  - 加入我的知识星球：https://t.zsxq.com/W5Oj7  Kimi K2.5是月之暗面发布的最新开源大模型，能力全面而强大。本期视频将带大家手把手集成K2.5到Cloudflare云端部署的OpenClaw。  Moltworker Git"
---

# 【保姆级教程】OpenClaw配置最强国产大模型Kimi K2.5 | Cloudflare云端部署版

> [五里墩茶社](https://space.bilibili.com/615957867) | [BV1tdFGzYEbw](https://www.bilibili.com/video/BV1tdFGzYEbw) | 时长 10:40

## 视频概述
本视频为保姆级教程，详细讲解如何在Cloudflare云端部署OpenClaw并集成国产开源大模型Kimi K2.5。通过使用OpenRouter和Cloudflare AI Gateway，实现灵活的模型切换和管理，适合希望在云端使用多种大模型的用户。

## Kimi K2.5模型介绍
- **发布者**：月之暗面。
- **类型**：最新开源多模态大模型。
- **特性**：用于驱动Agent Swarm，支持大规模并发任务执行。
- **集成方式**：在OpenClaw生态中，可通过服务厂商（如OpenRouter）提供支持。

## 部署准备
- **工具**：Cloudflare ModeWorker项目（UP主分叉版本，支持OpenRouter）。
- **前提**：需拥有Cloudflare账户，并安装Rancher或类似客户端用于部署。
- **关键组件**：Cloudflare Worker、AI Gateway、R2存储。

## 配置步骤
### 1. 配置API Keys和Secrets
- **Anthropic API Key**：作为备选方案，可设置无效值（如随便填写），仅在AI Gateway故障时使用。
- **OpenRouter API Key**：
  - 通过OpenRouter获取API Key。
  - 在Cloudflare Worker中创建Secret：命名为`OpenRouter API Key`，填入Key值。
- **AI Gateway Base URL**：
  - 格式：`https://gateway.ai.cloudflare.com/v1/{AccountID}/{GatewayID}/openrouter`
  - 获取Account ID：在Cloudflare Dashboard的Account Home菜单中复制。
  - 创建Gateway ID：在Cloudflare Dashboard的Compute and AI -> AI Gateway中创建新Gateway（如命名Modboard）。
- **AI Gateway API Key**：
  - 在AI Gateway页面右侧点击Create，生成API Token（如命名openclone）。
  - 复制Token并在Worker中创建Secret：`AI Gateway API Key`。
- **GateToken**：
  - 使用OpenSSL随机生成字符串：`openssl rand -hex 32`。
  - 创建Secret：`GaveToken`，填入生成的字符串。
- **其他Secrets**：
  - `Team Domain`和`AUD`：参考上一期视频获取配置值，用于Worker访问控制。

### 2. 部署Worker
- 在终端登录Cloudflare（如使用Rancher）。
- 运行`npm run deploy`进行部署。
- 部署完成后，获得Worker的访问URL（如`WorkerStepURL`）。

### 3. 配置R2存储
- **用途**：保存OpenClaw数据，包括配置、设备配对和聊天历史。
- **步骤**：
  - 在Cloudflare Dashboard中，进入R2存储（已自动创建Bucket，如Modbot Data）。
  - 点击Manage -> Create API Token，选择Object Read and Write权限，应用到该Bucket。
  - 获取并配置Secrets：
    - `Access Key ID`：从API Token创建结果中复制。
    - `Secret Access Key`：同上。
    - `CF Account ID`：使用之前获取的Account ID。
- 重新部署Worker以应用R2配置。

### 4. 访问和配对设备
- **首次访问**：
  - 访问Worker URL，输入email获取验证码完成验证。
  - 可能出现“invalid token”错误，在URL后添加`?token={GateToken}`（GateToken为之前生成的字符串）。
- **设备配对**：
  - 加载设备列表，点击Approve或Approve All完成配对。
  - 后续访问无需重复操作。
- **验证运行**：
  - 访问URL，右上角显示“Health OK”表示OpenClaw运行正常。
  - 测试提问（如“What's a model in use?”），响应应显示为OpenRouter提供的Kimi K2.5模型。

## 测试和验证
- **模型集成**：通过OpenRouter调用Kimi K2.5，端到端通信正常。
- **数据存储**：R2存储会加载历史聊天记录（如有）。
- **AI Gateway监控**：
  - 在Cloudflare Dashboard的AI Gateway -> Logs中查看所有模型调用日志。
  - 提供统计和跟踪功能，便于了解使用情况。

## 优势和建议
- **灵活性**：支持切换OpenRouter上的多种模型（如Kimi K2.5），可在部署中调整硬编码模型。
- **可靠性**：AI Gateway作为中间层，提供故障转移（如Anthropic API Key备选）。
- **便利性**：R2存储简化数据管理，AI Gateway增强监控能力。
- **建议**：快速尝试，有问题在评论区留言。

## 总结核心要点
本视频完整演示了在Cloudflare云端部署OpenClaw并集成国产大模型Kimi K2.5的全过程，通过OpenRouter和AI Gateway实现模型的灵活切换与管理。教程涵盖了从配置API密钥、部署Worker到设置R2存储和设备配对的所有步骤，强调了AI Gateway在监控和统计方面的优势。用户可根据指南轻松完成部署，在云端高效使用多种大模型。

---

## 原始字幕

大家好,我是小木头在过去两期视频,我们介绍了如何在Cloudflare云端部署OpenCloud在视频分享后,有朋友也问到在云端是否只能使用Astropic所提供的Cloud模型当然不是的,在目前这套部署方案下市场上主流的模型供应商都能够支持本期视频我们就以最新发布的国产开源道模型KIMI 2.5为例我们看看如何在Cloudflare云端将这款大模型集成到OpenCloud那现在咱们就开始吧首先咱们对KIMI 2.5模型做一番简单的介绍这是月之暗面发布的最新款开源多模台大模型它也用来驱动了Agent Swarm这个新的特性关于Agent Swarm感兴趣的朋友可以来了解一下这是一个用于驱动大规模并发任务执行的执行方式当然了这并不是我们今天分享的主要话题那咱们还是回到OpenCloud的集成在生态中目前已经有许多的服务厂商提供了2.5模型的支持比如OpenRouter我们今天的分享就借OpenRouter的2.5模型在过去视频分享中咱们用到了Cloudflare所提供的ModeWorker这个代码仓库或项目这个项目默认当然支持的是Anthoropic模型实际上它也支持到了OpenAI从文档中可以看到可以通过OpenAI API Key这个Secret来配置对应的密钥从而使用OpenAI的模型在今天分享中我会用到我分岔出来的这个ModeWorker这个项目在其中做了一些小小的代码改动从而实现了对OpenRouter支持我不确定在原始的代码仓库中是否已经支持了OpenRouter如果已经支持了欢迎朋友也在评论区告诉我一声现在我就以分叉出来的项目为例也是如何做OpenRouter的支持在文档这里我做了简压的描述可以用到OpenRouter API Key这个Secret来指定API Key另一方面可以通过AI Gateway API KeyAI Gateway BaseURL这两个Secret如果要用这两个密钥我们需要使用Cloud Flare的AI Gateway这个服务在演示中我们就用这套方案那现在我们就操作起来在终端这里我已经完成了Rangular登录那直接我们就开始今天的配置首先咱们还是需要配置一个Anthropic API Key这个是在目前这个工具和项目部署中它会用到的当然当我们配置了AI Gateway相关的API Key和Base URLAnthropic API Key并不会被用到它只有在AI Gateway不工作的时候作为一个备选方案会用到因此我们首先来设置Anthropic API Key可以随便给它一个无销的值吧我们可以验证一下在后面的应用中他应该能够正常工作现在他会来创建一个新的Worker叫MotibotSandbox好了接下来我们要做的是首先配置这个AIGave API Key这里要配置的就是大家会用到的OpenRouter的API Key我去创建一个创建完成接下来我们配置AI gateway base URL当我们配置OpenRouter时需要使用目前我所复制的这个URL以OpenRouter结尾那中间会需要用的AccountID和GatewayID这两个值都从Cloudflare dashboard获取比如现在来到Cloudflare dashboard在Account Home这里小点点这里有一个菜单Copy Account ID我们复制它粘贴进刚才的URL接下来回到Dashboard在Compute and AI这里选择AI Gateway可以创建一个新的Gateway给它一个ID这个ID就会用到我们所配置的Base URL我已经创建了一个Modboard咱们就继续用它那现在就可以配置好这么个URL我们将其配置到这个secret大家注意的是如果你的AI gateway已经启用了authentication那在这里呢还要创建一个auth token我们来设置它一下token从哪里获得呢回到dashboard在这个AI gateway点击在右侧点击create创建一个token给它写个名字比如openclone点击Crate API Token复制这个API Token粘贴回控制台这样呢咱们就配置好了AI gateway相关的密钥接下来还要配置一系列的Secret比如GaveToken我们复制这一段粘贴过来通过OpenSSL随机的生成一个字符串这个串呢用来作为token好了我们尝试部署在部署中同样咱们要启动docker我使用的客户端呢是Rancher大家可以根据自己的偏好来选择现在咱们运行npm run deploy完成部署部署完成我们回到文档这里参考一下接下来还要配置两个secrets一个是Team Domain另一个是AUD这两个Secrets的配置在上一期的分享中我们也介绍到了可以回看上一期视频来了解如何获取这两个值我们快速的配置一下配置完毕现在可以部署不过我们暂时并不部署完成下一步的配置这一步就是R2R2 Pocket用于保存MultiBot也就是OpenClaw的数据包括了配置配对的设备以及聊天的历史等等我个人觉得这个呢还是很方便的一个存储的机制同样这部分的配置呢在上一期的分享中也有介绍那现在我们快速的就配置一下第一个是配置Access Key ID我们简单介绍一下在刚才的配置后其实呢已经创建了一个R2Bucket名字就叫Modbot Data我们只需要在右侧在Account Details这里点击Manage创建一个API token选择Create User API Token写个名字比如OpenFlow选择Object Read and Write应用到指定的Bucket我们选择Modible Data这正是刚才在部署中已经创建的点击Create User API Token这里会给到我们一系列的值比如Access Key ID这是我们第一个需要的第二个是Secret Access KeySecret Access Key同样复制它粘贴进来最后呢是CF Account ID这个在刚才配置Base URL的时候已经介绍了如何获取到这个Account ID我们粘贴进来现在呢就完成了又一波的配置我们来部署一下部署完成我们现在呢就点击这里给到我们的Worker staff这个URL在初次访问这个URL的时候呢大家应该会看到类似的界面我们需要输入自己的email获取一个code完成验证在完成了验证后大家可能会得到一个invalet token的错误那么我们初次访问的时候呢需要在这个URL后面加上问号token等于提供的值是我们在最开始配置的时候生成的那一长串token因此大家需要回到最初的配置这里获取这个值复值粘贴进来接下来获取会看到目前这一个输出表示我们需要完成配对初次配对以后呢后续就不再需要操作了我们来访问一下这个URL它会加载设备这里会列出目前等待配对的设备可以选择Approve或在右上角点击Approve All一次性完成多个配对完成配对后就可以开始使用在云端运行的OpenClaw现在我们如果再次访问刚才复制的这个WorkerStepURL就能够看到右上角HealthOK表示呢这个ClawBot也就是OpenClaw运行正常了打个招呼吧Hi端到端的通信一切正常这里呢加载了一些文字大家不要惊奇这个呢是因为我的R2Pocket在过去已经有过聊天历史的存储因此呢它有所加载如果我提问What's a model in use大家可以看到这里他说是OpenRider所提供的Kimi K2.5这样呢咱们就完成了端到端的集成在结束本期视频分享前我们回到Cloudflare dashboard来到AI gateway在刚才创建的这个AI gateway底下点击Logs大家能看到所有的模型调用的情况这也是使用AI gateway一大好处我们可以做很好的统计跟踪了解非常详细的模型的使用情况那感兴趣的朋友可以赶紧来尝试一下OpenRouter提供了许许多多模型的支持在目前我所分享的分叉的这个Modeworker代码仓库中硬编码的Kimi2.5这款模型大家可以在部署中自行的调整期望使用的open router的模型这样呢我们就可以非常灵活的切换模型在云端使用openclone好了那今天的分享就先到这里吧大家在配置和运行中有任何问题呢也欢迎在评论区给我们留言那今天的分享就先到这里感谢大家收看咱们下次视频分享再见同学们拜拜