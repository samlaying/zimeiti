---
title: "从Gemini网页获取认证Cookie"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-169-【全网首发】Gemini网页会员也能当API用教你接入小龙虾等工具，国内网络也可用.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
related:
  - "[[Gemini网页订阅转API全流程]]"
---

# 从Gemini网页获取认证Cookie

获取用于API认证的Cookie步骤：
1.  使用浏览器的无痕/隐私模式登录Gemini网页版。
2.  按F12打开开发者工具，切换到“应用”(Application)标签。
3.  在左侧存储栏找到Cookie，选择`GMI`开头的条目。
4.  复制相关变量（如`sessionid`和`token`）的值，填入项目的环境变量文件中。

这是将[[Gemini网页订阅转API全流程|网页订阅转化为API调用]]的核心认证步骤。

> 来源：[[2026-05-25-169-【全网首发】Gemini网页会员也能当API用教你接入小龙虾等工具，国内网络也可用]]