---
category: A
source_type: opinion
ownership: external
knowledge_role: reference
mainline_candidate: pending
source_file: 16个开源agent项目教我如何设计agent系统 p18 18-流式输出与事件系统 [BV1kdoHBCEoC_p18].ai-zh.srt
status: reference
---

# 16个开源agent项目教我如何设计agent系统 p18 18-流式输出与事件系统

> 摘要：Agnes 分析失败，使用标题规则归档。

> ⚠️ 外部参考：这是收藏的视频内容，不代表本人经历、成果或能力证据。

## 关键要点


## 可能的参考价值
待人工确认。

## 原始字幕

我问你一个问题 你让AI agent帮你重构一段代码 他工作了20秒 你面前什么都没有 你怎么知道它还在运行 而不是卡死了 这不是小问题 用户信任感很大程度上来自于可见性 我能看到他在做什么 今天我们讨论的是AI agent如何把自己的思考过程 实时传递给用户 这个问题涉及两个层面 第一是LLM的token流式输出边生成边显示 第二是工具调用事件 agent正在做什么的可见性 我们会看goose ino hermes open code4个项目 他们的解法截然不同 在进入各项目之前 先澄清一件事 刘氏这个词有三种含义 经常被混用 最底层是token级别 刘氏LLM每生成一个token就立刻推送 用户看到文字 一个字一个字出现 所有现代agent都支持ANTHROPIC和OpenAI的API原声 提供S1接口 中间层是工具事件流逝 agent调用工具时正在执行read file这条信息 实时显示工具可能跑几秒甚至几十秒 没有这个信息 用户只能盯着空白界面等待这一层的实现 差异最大 有的项目做了 有的根本没有 最顶层是系统事件流逝 上下文压缩发生了模式 切换了MCP服务器 有通知这些agent的内部状态变化也纳入事件流 这是goose独有的设计 记住这三层 它们是我们理解各项目设计差异的坐标系 goose是我们研究的项目里 事件系统最完整的核心是这个枚举message变体 包含一切LLM生成的文字工具 请求工具结果 History replaced 在上下文压缩发生时通知前端刷新历史显示 Macbook notificant 把MCP服务器的progress通知透传给前端 reply函数返回的不是一个结果 而是一个异步流 调用方通过next await逐个接收事件 整个A证执行过程在流中展开 这三个变体背后的设计意图是 前端永远不需要轮询所有信息 主动推送 goose同时服务两类用户 用命令行的工程师和用桌面app的普通用户 两者消费同一个agent 但方式不同 CLI直接消费agent event流打印到终端 简单直接零延迟 桌面app通过HTTP连接到goose server 用SSE长链接订阅 中间有一层session event bus 这个设计解决了一个真实问题 桌面app的WEBSOCKET可能断联 网络抖动 页面刷新断联重连时 客户端发送last event id header Session event bus 从缓冲区重放断点后的事件一个不漏 同一个agent实现两种消费方式 这是解耦的价值 未来加一个vs code插件 只需要实现一个新的消费者 i know的流式处理和前面说的都不一样 他不是agent到用户 而是图执行引擎中节点与节点之间的数据流 为什么需要四种模式 因为不同组件天然适合不同模式 chat model天然流失输出 它实现string方法 two note天然同步执行 它实现invoke方法 框架在节点边界自动转换 当需要把流转成普通值时 框架调用注册的CONCAT函数 这个注册机制是类型安全的关键框架 知道怎么合并你的自定义类型 这里要强调一点 一诺的流逝是管道层 goose的流逝是呈线层 两者解决不同问题 可以同时存在于一个系统中 hermes agent对工具调用可见性的解法极简单有效 这个代码块就是它的核心 实现一行打印语句加一个竖线符号 这个竖线是unicode box drawing 字符 视觉上清晰区分agent文字输出和工具执行 用户一眼就知道哦 agent现在在读文件 现在在写文件 现在在运行测试 为什么不是所有agent都做这个 第一需要世界模型里区分LLM 文字输出和工具开始没有这个区分 技术上无法实现 第二也是最重要的 这需要主动去做 默认情况下开发者倾向于工具执行完再显示 因为这样最简单 而mix还有一个细节 每30秒向gateway发送still running通知 这解决了what's app等渠道 有消息超时限制的痛点 让平台知道连接没死 只是工具在跑 open code在流失事件之外加了一层持久化保障 bus事件总线负责实时性双轨 pos up设计很有意思 一个word card接收所有事件 WEBSOCKET客户端订阅这个一个typed 按事件类型分桶权限服务 只订阅permission相关的先发wildcard 保全局顺序再发typed支持精确过滤 snapshot机制负责可恢复性 每次AI开始执行工具 调用前记录当前文件状态 工具执行完用户发现不对 想回滚一行代码 回到执行前 关键点快照 不是git commit 不污染项目历史七天后自动清理它 利用git内部对象存储静默运行 刘氏解决我现在在做什么 snapshot解决 我做错了怎么回去 这是两个维度的用户安全感 不把四个项目放在一起 三个维度的差异很清晰 世界流的目的 goose用来解耦CLI和桌面app INNO是组件间的数据管道 HERMES追求工具执行的用户体验 open code是全系统神经系统工具调用可见性 HERMES最直接一个符号加工具名 用户一眼就知道在干什么 goose通过agent event推给前端 前端自己决定怎么渲染INO和open code的可见性 由框架使用者的应用层决定断联恢复 goose有512个事件重放缓冲 支持last event id Open code 有snapshot文件及回复 HERMES和INAL不支持 因为面向不同场景 三个可以借鉴的方向 第一HERMES的工具进度显示成本极低 值得所有做终端agent的项目采纳 第2open code的snapshot机制 对于会修改文件的agent回滚能力 是用户安全感的基础 第3goose的session event bus 一旦想支持多个前端 这个解耦层是必要的 流式输出与事件系统 背后是三个根本性的架构决策 第一个决策事件的力度 token集 工具集 系统集选哪些力度越细 用户感知越完整 实现代价越高 goose全做了HERMES 重点做了工具齐INNO是框架 不做沉线层的选择 第二个决策 消费者解偶 生产事件的agent与消费事件的前端怎么隔离 解耦越彻底 新增前端越容易 但架构复杂度也越高 goose用agent event加session event bus两层open coat 用全系统bus hermes直接打印 最简单 但也最难扩展 第三个决策 流式vs持久化 只做流式 还是刘氏加快照 open code的snapshot是后者的最好示范 但需要get环境作为前提 没有最优解 rust桌面工具构组件框架 Python CLI typescript函数式应用 每个项目在自己的约束下 做出了不同的合理选择 理解这些约束比记住哪种方案更好重要得多的 最后给大家一个快速决策表 简单CLI单前端无断联需求 直接用HERMES的打印模式零架构开销 桌面应用需要token及实时展示 选goose的agent event加session event bus 它有完整的token及事件力度和断线重连机制 多前端同时连接web CLIIDEE插件都需要看到同一个agent的进度 选open code的bus 总线模式 新增前端零成本构组件框架 需要在节点间做类型安全的流式传输 选EO的stream reader泛型需要文件及状态回滚 也就是用户发现agent改错了 要恢复 选open code的snapshot加bus事件双保险 高可用生产环境网络不稳定 选goose的last event id加512事件缓冲工具 执行进度可见性 让用户知道agents在做什么 而不只是等待选HERMES的竖线工具 进度指示器或者goose的工具及事件

## 标签
[]
