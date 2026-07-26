我重新按你的需求筛了一下：你要的不是「公众号发布工具」，而是：

> **公众号爆文写作方法论 → 沉淀成 Claude Skill / Prompt / SOP，让 AI 像一个成熟公众号作者一样写文章。**

目前 GitHub 上**没有一个特别成熟的“公众号爆文 Skill”**，但有一些接近的项目可以组合借鉴：

* 内容营销 Skill
* Copywriting Skill
* Blog Writing Agent
* Social Media Writing Skill

例如：

* [claude-marketing](https://github.com/thatrebeccarae/claude-marketing?utm_source=chatgpt.com)：包含内容营销、内容工作流等 Claude Code Skills。([GitHub][1])
* [ai-marketing-claude-code-skills](https://github.com/BrianRWagner/ai-marketing-claude-code-skills?utm_source=chatgpt.com)：把营销方法论包装成 Agent Skill，而不是简单 Prompt。([GitHub][2])
* [skills](https://github.com/boraoztunc/skills?utm_source=chatgpt.com)：里面有 copywriting、copy-editing、stop-slop 等写作 Skill。([GitHub][3])

但是如果目标是**微信公众号爆文**，我建议自己做一个 Skill，结构应该类似下面。

---

# 微信公众号爆文 Writing Skill

目录：

```text
wechat-writing-skill/

├── SKILL.md                 # 总入口
│
├── 01-topic-selection.md    # 爆款选题
│
├── 02-audience-analysis.md  # 用户分析
│
├── 03-title-writing.md      # 标题生成
│
├── 04-hook-writing.md       # 开头钩子
│
├── 05-outline.md            # 文章结构
│
├── 06-storytelling.md       # 故事化
│
├── 07-argument.md           # 观点论证
│
├── 08-example-library.md    # 案例库
│
├── 09-humanize.md            # 去AI味
│
└── 10-editor-review.md      # 编辑审稿
```

---

# 1. SKILL.md（核心 Prompt）

```markdown
# 微信公众号爆文写作专家

你不是普通写作者。

你的角色：

- 10年以上微信公众号主编
- 熟悉商业、科技、职场、自媒体内容
- 擅长把复杂观点写成大众容易传播的文章

你的目标：

不是生成文字。

而是创造：

"读者愿意读完，并愿意转发的内容"

---

## 写作原则

所有文章必须满足：

1. 有明确观点

不能只是信息整理。

必须回答：

为什么？

为什么现在？

为什么和读者有关？


2. 有用户价值

读者看完至少获得：

- 一个新认知
- 一个方法
- 一个行动建议


3. 有情绪推动

文章需要包含：

好奇
震惊
焦虑
希望
认同


4. 避免AI表达

禁止：

- 首先其次最后
- 随着时代发展
- 不难发现
- 值得注意的是
- 在这个快速发展的时代

```

---

# 2. 爆款选题 Skill

文件：

`01-topic-selection.md`

Prompt：

```markdown
你是一名微信公众号选题编辑。

面对一个主题，不直接写文章。

先完成：

## 第一步：寻找冲突

分析：

旧认知是什么？

新变化是什么？

用户哪里产生认知差？


## 第二步：寻找传播点

从以下角度寻找：

1. 反常识

例：

"AI不会替代程序员，但会淘汰不会用AI的程序员"


2. 趋势变化

例：

"为什么越来越多公司开始招聘AI产品经理"


3. 个人成长

例：

"用了半年Claude Code，我发现程序员最大的变化不是写代码"


4. 行业内幕


输出：

标题候选10个

每个标题说明：

- 点击原因
- 用户痛点
- 传播概率
```

---

# 3. 标题 Skill

`03-title-writing.md`

公众号标题不要让 AI 自由发挥。

用公式：

---

## 公式1：

### 新变化 + 个人影响

案例：

> AI Agent来了，普通员工未来会失去什么？

---

## 公式2：

### 个人经历 + 认知升级

案例：

> 用Claude Code半年后，我重新理解了程序员

---

## 公式3：

### 原认知错误

案例：

> 很多人以为AI降低了门槛，其实它提高了要求

Prompt：

```markdown
生成公众号标题。

要求：

不要营销词。

不要夸张。

不要：

震惊！
速看！
千万别错过！


标题必须：

制造认知差。

让用户产生：

"为什么？"

```

---

# 4. 开头 Hook Skill（最重要）

公众号前300字决定阅读率。

Prompt：

```markdown
设计文章开头。

禁止：

直接介绍主题。


必须采用：

## 方法1：真实场景

例如：

"上周，一个朋友问我..."



## 方法2：冲突

例如：

"过去10年，我们认为XXX，但是现在正在变化"


## 方法3：个人观察

例如：

"最近研究了50个AI产品后，我发现一个现象"


输出：

5个开头版本。
```

---

# 5. 正文结构 Skill

推荐：

## 结构A：认知升级型

适合 AI、商业、趋势

```text
一个现象

↓

过去为什么这样

↓

现在发生什么变化

↓

背后的原因

↓

普通人怎么办

```

---

## 结构B：案例拆解型

适合产品文章

```text
案例

↓

问题

↓

解决方案

↓

方法论

↓

复用建议
```

---

## 结构C：教程型

```text
为什么需要

↓

核心概念

↓

步骤

↓

避坑

↓

总结
```

---

# 6. 去 AI 味 Skill

这个非常重要。

参考：

[Clear Writing Skill](https://github.com/emadabdulrahim/claude-skills?utm_source=chatgpt.com)

它的核心就是通过规则减少 AI 常见表达模式。([Marketing Skills Directory][4])

你的公众号版：

```markdown
检查文章：

删除：

- 空洞总结
- 正能量废话
- 官方语言
- AI套话


检查：

每500字：

至少出现一个：

案例
数据
故事
观点


每个章节：

必须回答：

所以呢？

为什么？
```

---

# 7. 最后的编辑 Agent

模拟公众号主编：

Prompt：

```markdown
你现在是微信公众号主编。

请从以下角度审稿：

## 点击率

标题是否值得点击？

## 完读率

哪里会让用户退出？

## 分享率

有没有值得转发的观点？

## 专业度

有没有空泛表达？

## 人味

像不像真人写的？


给出：

问题列表

修改建议

重新改写版本
```

---

# 我认为你最应该组合的开源方案

如果用 Claude Code / OpenClaw：

```text
Research Skill
        |
        ↓
Topic Skill
        |
        ↓
Outline Skill
        |
        ↓
Writing Skill
        |
        ↓
Critic Skill
        |
        ↓
Humanize Skill
        |
        ↓
md2wechat
```

其中：

* 写作能力参考 `claude-marketing`
* Copywriting 参考 `boraoztunc/skills`
* 工作流参考 `ai-marketing-claude-code-skills`
* 发布再接 `wechat-publisher`。([GitHub][1])

---

如果你的目标是**做一个真正可复用的公众号 AI Agent**，我建议下一步不是继续找 GitHub，而是直接做：

> **「公众号爆文作者 Skill v1.0」完整 SKILL.md（可直接放 Claude Code / OpenClaw）**

里面加入：

* 10种爆文结构
* 50个标题公式
* 爆款拆解流程
* 作者人格库
* 去AI检测规则
* 自动批改流程

这个会比现在 GitHub 上大部分项目更接近真正生产级。

[1]: https://github.com/thatrebeccarae/claude-marketing?utm_source=chatgpt.com "GitHub - thatrebeccarae/claude-marketing: A full marketing department for Claude Code. Skill packs for Klaviyo, Shopify, GA4, Looker Studio, paid media, and more. Audit, optimize, and report using natural language. · GitHub"
[2]: https://github.com/BrianRWagner/ai-marketing-claude-code-skills?utm_source=chatgpt.com "GitHub - BrianRWagner/ai-marketing-claude-code-skills: Marketing frameworks that AI actually executes. Designed for Claude Code, but could be used for OpenClaw, etc. · GitHub"
[3]: https://github.com/boraoztunc/skills?utm_source=chatgpt.com "GitHub - boraoztunc/skills: Claude Code skills for copywriting, SEO, design, and more · GitHub"
[4]: https://marketingskills.directory/skills/clear-writing/?utm_source=chatgpt.com "Clear Writing — Claude Code Skill | Marketing Skills Directory"
