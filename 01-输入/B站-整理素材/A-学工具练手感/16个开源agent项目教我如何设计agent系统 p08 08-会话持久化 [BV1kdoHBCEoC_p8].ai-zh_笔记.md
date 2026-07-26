---
category: A
source_type: opinion
ownership: external
knowledge_role: reference
mainline_candidate: pending
source_file: 16个开源agent项目教我如何设计agent系统 p08 08-会话持久化 [BV1kdoHBCEoC_p8].ai-zh.srt
status: reference
---

# 16个开源agent项目教我如何设计agent系统 p08 08-会话持久化

> 摘要：Agnes 分析失败，使用标题规则归档。

> ⚠️ 外部参考：这是收藏的视频内容，不代表本人经历、成果或能力证据。

## 关键要点


## 可能的参考价值
待人工确认。

## 原始字幕

今天讲绘画持久化这个话题乍看枯燥 但实际上是AI agent 工程里最能体现设计选择的地方 想象这个场景 你让agent帮你做一件很复杂的事 agent执行了两个小时 调用了几百次工具 中途进程崩了 你重启之后 agent能不能接着做 不同项目对这个问题的回答差异非常大 goose能精确恢复到崩溃前的每一条消息 Oh my open agent用摘要注入近似恢复 丢失一些细节 但能继续 Dr flow 默认压根不做持久化 但不影响它在web场景下好用 这些都是正确的设计 因为场景不同 这一讲我们拆解六个主要项目的持久化方案 理解每个选择背后的理由 最后给出什么场景下 你该参考谁 同样所有分析来自源码 不是主观猜测 ghost的持久化系统是这六个项目里最完整的 我们从最核心的数据结构开始 session结构体包含了一次AI对话的完整状态 身份信息id 工作目录命名LLM自动生成的名字 VS用户自己取的名字 分类七种绘画类型 成本追踪当前周期 token加跨压缩累计token 能力配置模型配置权限模式 关联recipe工作流线程id 这个设计告诉你 ghost的绘画不只是存了对话历史 它存了整个绘画的完整上下文 你用的是什么模型 在什么目录下工作 总共花了多少 token是否绑定了recipe工作流 恢复一个绘画 就是把所有这些状态都还原回来 绘画名称自动生成 很值得一提 积累三条用户消息后 goose调用LLM分析对话内容 生成描述性名称 这个名字存在数据库里 让用户从历史列表里能一眼认出是哪个 绘画会七种session type 乍看很多 但每种都有具体的来由 user是最常见的 用户通过CLI或桌面app发起的对话 scheduled是定时任务 自动触发关联 schedule id失败时可以重试 sub agent是orchestrate派发给此agent的任务 对用户隐藏 但父绘画需要知道子绘画的状态 HIEN是内部操作 比如上下文压缩时创建的临时绘画 完全不在UI里显示 terminal是终端集成 gateway是第三方通过HTTPAPI调用创建的绘画 ACP是ACP协议会话 这些类型影响的是展示和管理策略 而不是存储结构 list sessions默认只返回user和scheduled 不污染用户的历史列表 list all sessions可以查 全部用于调试和管理 这是个很典型的设计决策 在产品功能增加的过程中 不是每次加功能都创建一张新表 而是用枚举字段区分行为 V5版本才加入这个字段 之前所有绘画都是user类型 V9版本专门做了数据迁移 把历史数据里错分类的CP会画修正过来 goose的数据库schema已经迭代到V11 有人可能觉得这是技术债务 但实际上 这11个版本是goose功能眼镜的忠实记录 V1是建立了schema version表 本身为后续迁移做基础设施 VR加了user recipe values 支持recipe工作流 需要用户填写的参数 V3给messages加了metadata 存储消息的可见性等源信息 V4加了name和user set name是LLM自动命名功能上线的那一刻 V5加了session type是子agent功能上线的那一刻 V6加了model configure 让每个绘画可以绑定特定模型配置 V7给消息加了全局唯一message id 支持精确消息定位 截断ACP追踪 V8加了goose mode权限模式 变成了绘画级别可配置的设置 V9是一次纯数据迁移 修正历史数据的分类问题 V10加了threads和thread messages表 支持CP协议的多会化线程组织 V11加了provider inventory 用于统计模型使用情况 每次加字段都对应一个用户能感知到的功能 这就是为什么gust的schema迁移代码 写的这么认真 它是产品历史的一面镜子 迁移策略也值得学习 启动时检查schema version 如果低于当前版本 主版本应用迁移 用while事务保证迁移过程的原子性 旧数据库自动升级 用户无感知 在所有持久化方案里 有两种最具代表性的思路值得深入对比 goose的精确恢复 会话中断后重新打开时 从messages表加载完整的对话历史模型 看到的上下文与中段时完全一致 代价是高 token消耗一个200条消息的会话 恢复时所有200条都要放进上下文 ommy open agent的摘要注入 当上下文使用率超过90%时 先保存任务状态未完成的TODO列表 已完成的操作摘要 关键决策记录 然后调用open code的compact压缩历史 压缩后把保存的状态摘要注入新对话开头 摘要注入的优势是token效率高 长时间任务几小时 超过模型上下文限制也能继续进行 劣势是有信息损耗 摘要不是完整 历史细节 可能丢失任务状态的准确性依赖摘要的质量 这不是好坏之分 而是场景之分 goose面向桌面工具 用户会画不会超出上下文限制 精确性优先 Oh my open agent 面向超长任务 上下文会耗尽是正常情况 连续性优先 INNO的检查点容易被误解 我们来说清楚 INNO的checkpoint store持久化的是计算图的执行状态 而不是对话历史 它包含每个节点的输入输出值 序列化为字节 每个channel的当前状态 deck channel和praggo channel各有自己的状态结构 节点依赖技术 哪些节点还在等待输入被中断的节点和中断 原因用途是支持human in the loop 人在回路中断恢复图执行到某个节点时暂停 等待用户确认 比如agent要删除这个文件确认吗 用户确认后从该节点继续 而不是从头重跑整个图 I know 还支持一个有趣的功能 读取已有检查点 但写到不同的检查点 这叫分查场景 从历史状态开始走一条新路径 不修改原有记录 这在实验性AI工作流里很有用 如果从这个状态开始用不同的提示词 结果会是什么关键区别 INNO检查点解决的是从哪里恢复执行 Goose session 解决的是从哪里恢复对话 前者是工程框架层的概念 后者是产品层的概念 两者不可互换 也没有竞争关系 拿到clue和DEFLOW代表了两种不同的简化思路 值得放在一起看 Nanoche 单一SQLITE文件 所有群组共享一个数据库 sessions表 按group folder作为主键 记录每个群组当前的session id进程 重启后 通过group folder到session id的映射 找回每个群组正在进行的对话 上下文发给cloud agent SDK 回复消息 历史也存在SQL lit里 但主要用于日志和调试 不是用来完整恢复对话状态的 nano cloud的持久化目标是实用性 进程重启后 每个群组的agent知道自己在做什么 不要求完整历史重放 只要上下文能接续就行 Dear flow 默认不做自己的持久化 把状态管理外包给line graph Land graph server 托管会话状态可以配置memory saver内存或SQLIT Cia squlight 进程重启后恢复 dear flow自己只维护channel store JASON就是i am聊天到lang graph thread ed的映射 其余状态由LANGUA负责 dear flow之所以这么做 是因为它面向web服务场景服务器24X7 运行不像桌面app频繁启停 lg graph已经提供了完整的状态管理基础设施 重复造轮子没有意义 用户通过thread标识绘画 符合无状态服务设计 让我们把所有方案放在矩阵里 比较goose SQL lit ww 加精确恢复 加多会化并发加V11自动迁移 加token追踪指向桌面AI工具 HERMESSQLITFTS5加记忆层为主 加单会化 无版本管理 无token追踪 适合个人助手 重心在记忆 I know 用户实现checkpoints store 加节点及恢复加多图并发 无内置schema 无token追踪 适合AI工作流框架 Nanocho squlit 加session id映射恢复加单进程加手动try catch迁移 无token追踪 适合多租户 IM机器人deer flow lg graph托管可选 SQL light依赖land graph状态管理 适合web AI服务 o my open agent无存储加摘要注入单会话无schema 适合open code插件选型决策树 第一步 你有存储控制权吗 在plugin架构里没有 只能用摘要注入 第二步 你是桌面工具还是web服务 桌面工具有完整数据库控制权 用SQLIT精确回复 web服务可以外包给line graph和云存储 第三步 你是多租户还是单用户 多租户需要隔离 第四步 你需要会画内断点恢复还是跨天恢复图 执行中断恢复 由inno checkpoint跨天绘画恢复 用goose session 根据真实项目的经验 给出几个具体的引入建议 如果你在做桌面AI工具 想支持跨天恢复 参考goose的SQLIT方案 但不要一开始就上V11的全部功能 从最简单的schema开始 sessions表有eye created at working deer messages表有session I'd roll content time stamp 就已经能支持基本的绘画恢复 加入schema version表尾降来的字段扩展 预留迁移路径 如果你在做IM机器人 想支持群组隔离 nano cloud sessions表示最简单的起点两个字段 一条UPSERT进程 重启后查一下session ide就能恢复 不需要更复杂的结构 除非你遇到了具体的问题 如果你的agent的任务会超出上下文限制 参考ommy open agent的摘要注入模式 在上下文超过80%时 主动保存TODO状态 到临时文件调用压缩后注入摘要 这不需要数据库 只需要文件IO能力 一个普遍适用的警告 不要引入不需要的复杂度 如果你的用户不需要跨天恢复 比如每次对话是独立的任务 持久化会话状态只是存储开销和代码维护负担 先把功能做好再考虑持久化 总结一下今天的内容 绘画持久化没有赢单 每种方案都是对特定约束和需求的回应 ghost精确恢复方案的前提是 你有完整的数据库控制权 你的用户需要跨天接续工作 你愿意承担完整历史的token开销 Oh my open agent 摘要注入的前提是 你在别人的plugin架构里没有存储控制权 任务很长会超出上下文 连续性比完整性更重要 dear flow外包给lg graph的前提是你是web服务 line graph已经提供了状态管理 不需要重复造轮子 nano cloud群组及SQULITTER的前提是你是多租户 系统隔离适应需求 简单实用 比功能全面更重要 一诺图执行检查点的前提是你在做AI工作流 框架需要的是节点级别的中断恢复 而不是对话历史恢复 最重要的一句话 架构约束决定了方案的上限 在plugin架构里不可能做到精确恢复 在web服务里 本地SQL light不是最佳选择 先理解你的约束 再选择最适合约束的方案 而不是追求看起来最完整的方案 谢谢有问题可以直接提

## 标签
[]
