---
title: "Hermes Agent安全测试结果"
card_type: 案例卡
layer: 处理
source: "[[2026-05-25-258-🦞完美取代OpenClaw：Hermes Agent自主进化+安全防御+无缝迁移！GitHub登顶第一的AI智能体深度实.md]]"
date: 2026-05-25
tags:
  - 卡片/案例
  - 主题/AI工具
  - 素材/案例
related:
  - "[[Hermes安全防御需额外加固]]"
  - "[[Hermes Agent本地演化复利系统]]"
---

# Hermes Agent安全测试结果

使用Cloud Code对Hermes Agent进行了15项端到端安全测试，综合结果如下：
- **拦截成功**：6道题（如危险RM命令、穿透注入、SQL注入等）。
- **绕过漏洞**：3道题（如转移字符RM命令、社会工程脚本执行、KL命令）。其中发现了2个高危漏洞（脚本内容检测不足、命令字符混淆绕过）和1个中危漏洞。
- **无匹配**：1道题（Git破坏性操作无防护）。

**测试结论**：综合安全评级为B级，但实际拦截率为60%。漏洞修复PR已提交官方仓库。这表明[[Hermes安全防御需额外加固]]。

> 来源：2026-05-25-258-🦞完美取代OpenClaw：Hermes Agent自主进化+安全防御+无缝迁移！GitHub登顶第一的AI智能体深度实.md