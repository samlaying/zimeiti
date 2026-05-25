---
title: "解密Claude Code和Anthropic后端是如何通信"
author: "张司机在路上"
source: https://www.bilibili.com/video/BV1G2o5BqELx
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI
  - Claude Code
  - 工具
  - 通信
  - Token优化
  - 调试
type: video-note
bvid: BV1G2o5BqELx
duration: "9:22"
cover: "http://i1.hdslb.com/bfs/archive/6e17d94009cfffb7fdfd249b2af9ad5f372771cf.jpg"
description: "你在Claude Code里打一句hello，五个字。但实际发给API的请求里，塞了将近三万个token。  两万六千字符的系统提示词，十个工具定义，你的hello被包装成六个content block，五个是Claude Code注入的上下文，最后一个才是你的消息。  返回也不是一整坨JSON。是一串SSE事件流：message_start带token用量，content_block_delta逐块推送文字，message_delta告诉你为什么停下来。  分析使用的工具claude-trace可以一行命令拦截所有流量，退出后生成HTML文件，浏览器打开就能看。"
---

# 解密Claude Code和Anthropic后端是如何通信

> [张司机在路上](https://space.bilibili.com/7429895) | [BV1G2o5BqELx](https://www.bilibili.com/video/BV1G2o5BqELx) | 时长 9:22

## 引言
视频探讨了Claude Code（可能指Cloud Code）与Anthropic后端通信的细节，重点分析简单交互（如输入“hello”）为何消耗大量Token，并介绍工具监控和优化通信过程。

## 工具介绍
### CC History
- **功能**：对比任意两个Claude Code版本之间系统提示词和工具定义的变化。
- **用途**：解决行为不一致问题（如上周提示词有效，这周无效），帮助识别Anthropic的更新。
- **示例**：通过CC History网站查看历史变化。

### CloudTrace
- **作者**：Mario Zegner（Pi框架作者）。
- **功能**：拦截Claude Code与Anthropic服务器的所有API流量，记录并生成HTML文件用于分析。
- **优势**：实时监控通信内容，便于调试和优化。

## 请求结构详解
Claude Code发送给API的请求包含多个字段，按顺序解析如下：

### Messages字段
- **内容**：用户输入“hello”被包装成6个content block。
  1. **Hooks配置**：注入用户自定义的hooks（如superpowers hook），如果未使用则无。
  2. **延迟加载工具清单**：仅列出工具名称（如bash、edit等），避免完整定义占用Token；模型需要时通过Tool Search加载完整定义。
  3. **MCP服务器使用指南**：指导模型如何调用MCP工具（如Contact7文档的MCP）。
  4. **可用Skills列表**：包含所有技能（如simplify、review、生成PR等）。
  5. **Cloud.md文件内容**：项目指令、结构说明、写作规则等自定义配置。
  6. **用户实际输入**：即“hello”，并设置cache control为一小时过期，作为缓存切割点。
- **关键点**：前面5个block无缓存控制，用户输入是缓存复用的分界点，之前的上下文可缓存。

### System字段
- **结构**：数组形式，包含四个文本块：
  1. **计费头**：记录Claude Code版本号和入口类型。
  2. **身份定义**：一句话说明模型身份（如“You are Cloud Code Anthropic Official COI for Cloud”）。
  3. **行为准则**：核心规则，包括运行环境、任务执行方式、谨慎操作（如删除文件需确认）、工具使用建议（如避免用grep而用read）、语气风格（短句、无emoji）等。
  4. **记忆系统与环境信息**：详细说明记忆类型（如用户身份、反馈、不记忆内容）、记忆方法，以及环境信息（如Shield类型、工作目录）。
- **特点**：所有内容随每次对话发送，占用Token。

### Tools字段
- **定义**：Claude Code给模型定义的10个工具，例如：
  - `agent`：用于子任务派发。
  - `bash`：执行命令，说明超过1万字符，涵盖使用场景（如提交、PR创建）。
  - `edit`：修改文件。
  - `glob`：搜文件名。
  - `grep`：搜索文件内容。
  - `read`：读文件。
  - 其他工具如`schedule`、`tool_search`等。
- **细节**：每个工具带完整参数定义和使用说明，这些也计入Token。

### 其他字段
- **Thinking**：设置为Adaptive，模型自行决定是否启动深度推理。
- **Output Config**：包含Effort字段，设置为X-High（最高推理档位），提示词中的“UltraThink”即触发此设置。

## 响应结构详解
Claude Code的API返回使用SSE（Server-Sent Events）事件流，逐步推送数据：
- **事件顺序**：
  1. `Message Start`：返回消息基本信息（模型名称、ID、Token用量）。
  2. `Content Block Start`：开启文本块。
  3. `Ping`：心跳保持连接。
  4. `Content Block Delta`（多个）：模型实际输出的文字（如“hello”、“how can I help you today”），实现终端逐字打印效果。
  5. `Content Block Stop`：文本块结束。
  6. `Content Block Delta`带`stop_reason`为`end_turn`：模型主动结束回复。
  7. `Message Stop`：整个消息流结束。

## Token消耗分析
- **示例数据**：输入“hello”后，Message Start中的Usage字段显示：
  - **Input Token**：6（用户输入“hello”加格式标记）。
  - **Cache Creation Input Token**：14000（新写入缓存的内容，如部分系统提示词和工具定义，缓存有效期一小时）。
  - **Cache Read Input Token**：16000（从已有缓存读取的系统提示词和工具定义）。
  - **总计**：约31000 Token（6+14000+16000）。
- **缓存机制**：缓存读取比正常输入便宜90%，因此连续对话时费用不会线性增长，优化了Token成本。

## 实操步骤：使用CloudTrace
1. **替换命令**：将平时使用的Claude命令替换为`CloudTrace`。
2. **添加参数**：加`include all requests`参数以记录所有请求。
3. **正常使用**：在Claude Code中进行正常交互（如输入“hello”）。
4. **退出生成**：使用完成后退出，自动生成HTML文件。
5. **查看记录**：在浏览器中打开HTML文件，查看所有通信细节（请求和响应）。

## 总结
核心要点：Claude Code与Anthropic后端的通信涉及复杂的上下文注入（如系统提示词、工具定义、用户配置），导致简单交互消耗大量Token（接近3万）。通过工具CloudTrace可以监控和分析通信内容，帮助优化使用和调试。缓存机制能降低重复内容的成本，理解请求结构（Messages、System、Tools）和响应流程（SSE事件流）有助于更好地使用Claude Code并控制Token消耗。

---

## 原始字幕

你在Cloud Code里打了一句hello它回了一句有什么能帮你的一个词进去一句话出来但你有没有想过就这么一句话到底消耗了多少Token答案是接近3万个今天我们把这个请求拆开来看看这3万个Token到底购在哪里了我用的工具叫CloudTrace作者是Mario Zegner用过OpenCloud同学都应该知道OpenCloud底层Agent框架叫Pi就是他写的整个框架只有4个工具系统提示词不到1000个Token就能跑起一个完整的Coding Agent然后非常推荐大家去读下它的技术博客这期视频就是参考它的这一篇叫CC HistoryTracking Cloud Code System Prompt and Tool Changes文章它用Monkey Catch说了Monkey Patch截持了Cloud Code的命令行里的这个Fetch函数这样就能拦截Cloud Code的发给Anthrope服务器的所有请求和返回值基于这个研究它做了两个工具第一个叫CC History它是一个网站能对比任意两个Cloud Code版本之间系统提示词和工具定义的变化同样的提示词上周好好的这周就不听话了所以去CC history一查就知道 Anthropik改了什么第二个就是我们今天用的CloudTraceCC history它能告诉你改了什么那么CloudTrace它能告诉你现在发了什么它会拦截Cloud Code跟Anthropic服务器之间所有的API流量然后记录下来的生成一个StML文件留任器打开就能看用法很简单只要你把平时用的Cloud命令替换成CloudTrace然后后面加include all requests的参数记录所有的请求然后就开始这个Cloud了你正常用就行比如说helloOK你用完以后直接退出就行了它会生成这个HTML然后你看这就是Cloud Code和Anthropic服务器所有的通信的这个记录然后比如说我们要看的其实应该是这个Message对吧你看这就是你发的hello现在来看发给API的这个POST请求吧我把刚才HTML文件里的数据保存成了这个JSON文件我们按照字段出现的顺序从上往下看第一个字段是这个Messages对吧里面只有一条user消息你以为你发过去的是Hello这五个字母你打开一看你的消息被包装成六个content block前五个block全是Cloudcode注入的这个system reminder标签第一个一大坨就是你装在的这个hooks完整配置比如说我的我用的那个superpowers所以Cloudcode会有这个superpowers的hook如果你没用就不会有这个比如说你看到的这这个cshistory里面这部分就没有的OK这个就不是系统自带的注入了那么第二个是延迟加载的工具清单比如我看到cshistory你看这里会比较明显一点然后这个里面只列了这个工具名它没有完整的定义为什么要这样呢因为每个工具的完整定义可能有几千个字符那么全塞进去太账token了所以clark code只告诉模型你有这些工具可以用等模型真的需要这个工具了那么你再用这个Tool Search这个工具来加载完整的定义然后第三个是我的这个MCP服务器的使用指南告诉模型怎么调用我配置的MCP工具比如说唯一使用的就是这个Contact7文档的MCP平时有什么工具查不到怎么用了那么Clockode就会去Contact7的MCP查一下这个怎么用第四个是一大坨这里是我所有可用的Skills完整列表比如说我用CC History看的比较明显一点比如你看这里常用的simplify对吧我们写代码的时候经常用的然后还有比如说review这里生成一个pr都在这里了对吧然后我现在看第五个这个就是我的cloud.md文件你在项目里写的所有的指令然后项目结构说明写作的规则工具偏好cloudcode原封不动的都会塞进这段消息里面所以模型之所以会知道我的项目规范都是因为每次对话里都在这里带着的最后一个block才是我的hello你看只有这个block上面标注了这个cache control设立成了一小时过期前面那五个注入的block都没有标这意味着clock code把我的实际输入当做缓存的切割点你的输入之前的内容都可以被缓存复用你的输入本身每次都会重新发那我们做一个小小的总结那么clock code发出的请求里面第一个user数据块里面就包含了所有clock code自动注入的上下文关于用户的比如说hooks配置对吧然后这些延迟加载的工具清单mcp的配置然后所有可用的skills还有你自己定义的这些Cloud Code MD对吧最后是你的输入的这个提示词那我们接着往下面看System字段那么这个就是系统的提示词是Anthropic写的它会告诉模型你是谁你该怎么做它不是一整段文字而是一个数组比如说里面有四个文本块第一块很短是记费头它记录了你的Cloud Code版本号和入口的类型那么第二块只有一句话叫You are Cloud CodeAnthropic Official COI for Cloud这就是Cloud的身份定义然后第三块有一大坨我们切到CC history看你看这就是核心的这个规则里面它有好几个章节比如说这里的system它定义了运行的环境然后doing tasks它会告诉它怎么去做任务然后这里还有executing actions with care它规定了比如说哪些操作需要谨慎比如删文件force push这些需要给你确认然后比如说using your tools它规定了比如说grab就不用用batch里的grab了用read不要用cat然后这里tone和style是要求短句还有比如说不要用emoji我们继续往下看第四块它比第三块还要长比如里面看它这里面说了这个输出的格式用什么规则然后还有比如说绘画级别这个指引然后还有比如说自动记忆它就比如说规定了有哪种记忆类型比如user这是身份和偏好然后第二个是比如用户给它的反馈然后还有比如说什么不用记还有比如说怎么记你看这么大一段全是定义的记忆系统说明Cloud Code在这一块的内置功能已经很强大了再往下看还有当性的环境信息比如说你的Shield类型然后你的工作目录全在里面这四块加起来这么多提示词你说的每一句话这些提示词都会跟着一起发过去接下来我们总结一下请求里的第二部分系统提示词第一个是它的记废头第二个是Cloud Code的自己的身份说明第三个是它的行为准则怎么做事情的第四部分很大一部分是关于它是怎么处理这个记忆还有环境的这个说明接着我们看这个下面的tools字段Clark Code给模型定义了十个工具比如这个agent就是用来给subagent派发任务的然后我们往下看比如说还有这个bass命令光bass这一个命令的说明超过一万多个字符里面详细写了什么时候该用bass什么时候不该用然后比如说什么时候创建这个地的提交对吧然后还有比如说怎么去提交一个PR然后继续往下看还有比如说Edit的命令是修改文件的然后Global是搜文件名还有Grapple是搜索文件的内容然后比如说还有Read读文件还有比如说像什么ScheduleWayCup然后还有比如说什么ToolSearch你可能都没注意过每个工具它都带完整的参数定义和使用说明这些说明也是模型上下文的一部分也占Token最后两个小字段这里的Thinking设置成了Adaptive意思就是模型自己决定要不要启动深度推理然后有一个Output Config有个Efford字段这里是X-HighEfford控制的是模型的推理深度从Low一直到X-High一共无档X-High就是现在Clock Code的目前的默认值每次对话都是用的最高推理档位你在提示词里用UltraThink实际上就是触发这个X-HighOK 这里简单总结一下请求里的最后两个部分Tools是所有Clock Code自带的工具定义然后Thinking是否自定决定进行深度推理然后Effort是决定最高推理的档位OK请求我们介绍完了我们现在看看Cloud的返回它的API返回不是一整坨JSON而是一串叫SSE事件流的东西SSE全称ServerSend Events就是服务器一条一条的往客户团推数据我们顺序来过一遍第一个事件叫Message Start返回来消息的基本信息比如模型的名称ID还有Token的用量然后紧接着是Content Block Start它开启了一个文本块紧接的是一个ping就是心跳保持连接用的接下来是两个content block delta这就是模型实际输出的文字第一个delta是hello然后第二个是how can I help you today你在中端里看到的逐字打印的效果就是这些delta一个一个推过来的然后是content block stop这个文本快结束了然后content block delta带了一个stop reason叫end turn意思就是模型主动结束了回复最后一个messive stop这个整个消息流就结束了我们回头看看Message Start里面这个Usage字端这里是最值得细看的一块比如说Input Token是6所以你的hello加上格式标记一共就6个Token但是Cache Creation Input Token是14000这14000是什么是这次新写入缓存的内容你的部分的系统提示词和工具的定义被写进了一个小时有效的缓存力然后这里的Cache Read Input Token所以是16000这16000是从已有的缓存力读的所以上一次对话已经缓存了一部分系统提示词这一次直接复用了所以你觉得自己只发了5个字但实际上模型实际处理的上下文是6加14加16一共是31000个token好消息是缓存读取比正常输入便宜九成所以不是每次都从头赚钱这是为什么Cloud Code连续对话时费用不会线性增长OK所以这就是一句hello背后所有的全部真相Cloud Code给Anthropic后端服务器的所有通信内容它的请求还有它的回复都在这里了下次如果你觉得Cloud Code的行为奇怪或者token烧得特别快不要瞎猜了用Cloud Trace看一下它到底发了什么收了什么就都清楚了