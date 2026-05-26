---
title: "解决LangExtract中文分词问题"
card_type: 方法卡
layer: 处理
source: "[[2026-05-25-302-LangExtract-小而美的结构化数据提取工具.md]]"
date: 2026-05-25
tags:
  - 卡片/方法
  - 主题/AI工具
  - 素材/教程
related:
  - "[[LangExtract：结构化数据提取工具]]"
---

# 解决LangExtract中文分词问题

[[LangExtract：结构化数据提取工具]]默认分词器仅支持ASCII字符，导致中文无法正确解析。解决方法：
1. 使用[[DeepWake：GitHub项目解读工具]]定位分词核心模块。
2. 修改代码，扩展支持Unicode和UTF-8字符集。
3. 验证后，程序可成功处理中文文本。社区已有PR(#27)提交中日文支持修复。
> 来源：[[2026-05-25-302-LangExtract-小而美的结构化数据提取工具.md]]