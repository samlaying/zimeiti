---
title: "Gemini 3 Deepthink保姆级全攻略！零基础必看的全场景实战指南"
author: ""
source: https://www.bilibili.com/video/BV1MkZABeEJY
date: 2026-05-26
tags:
  - bilibili
  - 笔记
  - AI工具
  - 深度推理
  - 生产力提升
  - 数据分析
  - 编程辅助
  - 谷歌Gemini
type: video-note
bvid: BV1MkZABeEJY
duration: "0:00"
cover: ""
description: ""
---

# Gemini 3 Deepthink保姆级全攻略！零基础必看的全场景实战指南

> [](https://space.bilibili.com/) | [BV1MkZABeEJY](https://www.bilibili.com/video/BV1MkZABeEJY) | 时长 0:00

## Gemini 3 DeepThink 核心认知与入门指南
### 1. 模型定位与核心特点
*   **深度推理**：模型的核心是模拟“深度思考”，会启动多个子代理并行推理，特别擅长处理**多步骤推理问题**。
*   **长耗时**：单次查询通常需要 **10 到 20 分钟**，不适合需要快速响应的简单问题。
*   **适用场景**：适用于**严肃研究、复杂编码或战略性规划**等**推理重要性高于速度和成本**的场景。
*   **订阅要求**：仅对 **Google Ultra 订阅用户**开放。

### 2. 核心应用场景与实战案例
#### 2.1 草图转3D可打印模型
这是官方演示中展示的惊艳功能，能将简单草图转换为可用于3D打印的STL文件。
*   **关键步骤**：
    1.  **生成清晰草图**：使用图像生成工具（如Nanobanano）创建一张**单一、清晰**的物体草图（如耳机支架），避免复杂艺术元素干扰。
    2.  **使用精准提示词**：
        > `Transform this attached sketch into a functional 3d object. Generate a single file HTML using Three.js that builds the geometry based on the sketch. The geometry must be a manifold watertight mesh suitable for 3D printing. Implement orbit controls with 360 degree inspection. Include a download print ready STL button using the Three.js STL exporter. Use a minimalist dark mode UI overlay.`
    3.  **生成与下载**：将生成的HTML代码保存为`.html`文件并用浏览器打开，即可获得一个可交互的3D模型预览，并附带**下载STL文件**的功能。
*   **输出价值**：不仅提供3D预览，还会给出模型的**总高度、总体积和预估重量**等实用打印参数。

#### 2.2 深度研究与结构化思考
*   **与Deep Research的区别**：Deep Research工具侧重于**大规模信息搜集**，而Deep Think侧重于**对问题本身进行更深度的推理**，得出更深刻的见解。
*   **实战提示词示例**：
    > `I'm writing a long-form piece / making a YouTube video on why AI isn't a bubble. Map out every argument, counter-argument and piece of evidence I need. Flag anywhere my reasoning has logical gaps or where I need stronger sourcing.`
*   **输出特点**：能够生成结构清晰、包含论点、证据和来源的框架，适用于准备复杂论述或视频脚本。

#### 2.3 金融与深度基本面分析
利用其深度推理能力，对复杂投资标的进行多维度分析。
*   **实战提示词示例**：
    > `Walk me through a deep fundamental analysis of Adobe. Consider the macroeconomic headwinds, sector trends, balance sheet, and competitive moat. Where is the consensus wrong?`
*   **优势**：模型会花费长时间深入分析各个维度，可能发现被市场共识忽略的见解或矛盾点。

#### 2.4 数据洞察与模式发现
适用于分析用户自己的业务数据、健康数据或财务数据，发现非显性规律。
*   **关键提示**：**无需在提示词中过度指示“思考方式”**，因为模型内置了链式推理模式。
*   **实战提示词示例**：
    > `Analyze my YouTube channel data thoroughly. Find non-obvious patterns, correlations, and actual insights I'm probably missing. Look at the upload times, days... what's the best performance?... Give me the five biggest changes I should make based on the data.`
*   **输出价值**：提供基于量化数据的、可执行的行动建议，帮助用户优化策略。

#### 2.5 原型开发与单次编码
具有强大的编码能力，尤其擅长一次性（One-shot）生成小规模、可视化的代码项目。
*   **适用场景**：快速搭建**数据可视化小应用**或**项目原型**，用于测试想法或实验，而非构建完整商业应用。
*   **特点**：用户无需具备高深编程知识，即可在约10-15分钟内获得可运行的代码。

## 核心要点总结
Google Gemini 3 DeepThink 是一个为**深度、多步推理任务**设计的强大AI模型，其核心价值不在于快速响应，而在于**对复杂问题进行长时间、多代理并行思考**，从而提供超越常规模型的洞察力。它特别适用于将创意草图转化为可打印的3D模型、进行结构化研究分析、深入剖析金融数据、从海量数据中挖掘隐藏模式，以及快速开发小型代码原型。使用时应为其较长的推理时间做好准备，并充分利用其内置的推理能力，避免提示词过于繁琐。对于Ultra订阅用户而言，当面临需要深度“思考”而非简单“问答”的挑战时，DeepThink是一个值得尝试的生产力工具。

---

## 原始字幕

Gemini DeepThink is here, let's dive into the tutorialso in order to activate Google Gemini DeepThinkit is just here on the tools tab and you type in DeepThinknow do remember that DeepThink is only available for the ultra subscribersand that is because at the moment this is a model that essentially spins upmultiple different sub-agents and then does a bunch of reasoning in a parallelso this is a model that is particularly powerful for multi-step reasoning problemsIt's important to know that Gemini 3 DeepThink is essentially worth trying if you rely regularly on AI for serious research, coding or strategic planning where reasoning matters more than the speed and the subscription cost. And before I dive into this tutorial, please do remember that DeepThink is essentially a model that will take around 10 to 20 minutes per query.So this isn't something you want to use if you're trying to get a response super quickly.so in the google demo video one of the things they showed us that google deep think is actually goodat and something that i found was really cool is that you can basically take any sketch and then convert that to a stl 3d model so i actually used nano banana to generate this image of a sketch of a headphone stand don't think about the design here this is purely just a sketch and so what i actually did for the prompt was i said a sketch of a headphone stand no headphone on it and a singlethe reason i've done this is because in that short demo they did show us that we could make these things and in the sketch that they used it was a singular image with nothing else in there make sure you're using this prompt because if you don't essentially nanobanano will generate you an image that just has a bunch of different artistic things on it and it isn't really useful for the model so you want a clear image so this is simply a simple sketch and so once you have this okay and you've got your prompt in you can essentially say here and this is a prompt from my community transformto attach sketch into a functional 3d object generate a single file html using 3.js that builds the geometry based on the sketch the geometry must be a manifold watertight mesh suitable for 3d printing implement orbit controls with 360 degree inspection include a download print ready stl button using the 3.stl exporter and use a minimalist dark mode ui overlay yada yada yada and then essentially what happens is once you get this field and you click copy andand then if you paste this into note and then you save this as a html if i decide to now open that html you can see that the you know object is right here and this is what we got to see from the demo from google's actual demo video and yeah i think this does look really really cool and arguably the biggest thing is not the 3D object itself the biggest thing is of course being able to have an STL file that you can literally just download and I think it's super useful that the fact you have the total height the total solid volume and the estimated weight so one of these things are super useful for people who are wanting to 3D print things of course there are different ways that you can achieve this and of course you can debate on the complete accuracy of the model but I think something like this is super usefuland so yeah that is one of the basic use cases but let's actually dive into some other use casesso another thing is standard research deep think is going to think longer and harder about this problem so if you have something that is essentially a issue where you want to think about the problem a lot longer and you really just need a lot more you know insight this is i guess you could say thinking about the problem itself which is where this is a little bit different to deep research deep research tools are basically focused on gathering large amounts of information but deep think is essentially focusing on the actual problem itself and reasoning about that conclusion so i just want to make that clear because it is a little bit of the same product but with slightly different outcomes they're just reasoning about the problem to a greater extent so this agentic research prompt here is where i've said i've i'm writing a long-form piece making youtube video on why ai isn't a bubble map out every argument counter argument and piece ofI need flag anywhere my reasoning or my logical gaps or where I need stronger sourcing and thisgives me a really good prompt it gives me act one the crucial bubble you know it talks aboutthe different stances and you know why they're different and then you know the core arguments then the shift and yada yada yada and it actually does come with sources as well so if you want to do some kind of research in here it does come with the sources as well now notably it doesn't you knowgo through as many sources as deep research will but deep think is just something that where you know if you want to go through this kind of problem maybe you've got a research problem that includes a problem that you really need to think about this is going to be a use case as well so for me for some super obscure or weird or strange topics this is where i would probably use deep think because it's still going to be a useful tool and that's probably i would only use it after the deep research probably just didn't give me something i want to use now this is another用一 calmly在的� parap,在那个金融上有什么又或者说有多 Pause DOUG Tapia可能不作用什么IVE通知 weg就眼ồngaan来说但是我说,在这边是有 reasonable的애不 지相对 Kaybank的合理os Linda irяла消费有的问题直接用这些�ardeş所以Comince the model is going to think longer and harder about the problem you may be able to see different insights about a specific stock that you didn't know before so i use this prompt once again this one's in my community walk me through a deep fundamental analysis of adobe consider the macronomic headwinds sector trends balance sheet and competitive mode where is the consensus wrong and so when you have deep think this is why i would use this model for this kind of research because the model is going to think harder about all of the different problems whereas with deep授设言,是想去想要想吃什么 Warnerさん的问题但是,这样来想会想需要你 但是,它不会只想要想 ask contain норм가지技术别的情况所以修行使用可以 olar,它其实给我们 23家装 видеоaran去 интер级运測,我们的 COMPETITIVE MOAT盾町摇向观伤而且简 With推养把各个门袄法 随 dynamics複视的效果多的误令是处于虚估的最�그� belong STOP案 byiyetion�순光是什么变化的讓我認為這些言論 س就是要匯選數一些助理的人也忍不識僕不是在 нос位思 tomar這μο sights到失去連連鎖都不在研究如果研究幾乎ろ números先問你這個商量他們在捏資因為I've instantly made now remember how I said deep think is a model that reasons for much longer andharder about the problem one thing that it is really good at is when you have different data sources and you're essentially able to use that to come to new conclusions so I've got this prompt which is basically youtube data analysis prompt and quick tip for your prompting guys don't overdoit with the prompting the model already has an inbuilt chain of thought reasoning mode so youyou don't need to say think like this or think like that it is going to completely go ahead and thinklong term so please understand that it's going to really reason ahead like it's already designed to reason a lot so i've said analyze my youtube channel data thoroughly find non-obvious patterns correlations and actual insights i'm probably missing look at the upload times and days what's the best performance and basically i just said after all of these things give me the five biggest changes i should make based on data and so it reasoned for around 15 to 20 minutes and this alleen später damages並これでcalculate整理會了我們給了 STEM結果那也需要趴上朋友 whichever屆指通回最好的真相 algunas delivered ihe reason this kind of thing is useful is because it is going to think longer and harderabout any problem than you would okay and considering that if you're working maybe on a business maybe you've got a project at school maybe you've got your health data it's going to be able to reason about that data set in a way that you might not have seen so we all know that analyzing data and spotting trends is super useful because that's how we can predict the future make changes and adjust our path and so if you have any online business maybe you've got some messy data maybe even your finances this is going to be something that is super super useful where you want to get real actionable steps that are completely based on the actual data so it's not just hey chatty i'm feeling down what should i do this is pure quantitative data where you can take that stuff analyze it and it's going to reason for a long time about it所以它给了一些明显的评论,它给了一些明显的评论,它给了一些明显的评论,然后它叫做评论。所以,这个东西是非常用的,而且,我说,传统的模式不可能会这样的,因为它们不是很熟悉的,当然,这些模式是好评论,我其实提供了一个SIMS的3D屏幕建设,我其实找了一个同样的文章,and just tweaked it a bit and so deepthink can essentially create things like this now of course i will say that these things are pretty useful but i will say that these things are useful in the sense that they're like demos and stuff so of course you can't really build full scale applications but things like this is still pretty useful in terms of your ability to mess around and develop maybe early prototypes for things that you want to test so i think deepthink is just something that has a level of coding ability that is incredible because it's meant to one-shot things and so i'm not sure about you guys i don't usually code that much it's not really a part of my everyday workflow but sometimes i do like to code up small things where i can not only visualize data but i can make small experiments to test things before i have to and that is where this is something that can be useful now i'm not sure what you want to use this for but of course like i said there are a million different things that individuals could use this for maybe like roomi don't know i'm not that creative i don't have the best ideas right now what i'm trying to do is showcase you guys the very best few cases you can and if you want to one shot something in around 10 to 15 minutes and you can leave deep think for reasoning on the problem that is going to be something that it can do of course if you enjoyed this video and you want to get the prompts don't forget to join the community or if you want the cheat sheet which is where you simply just download this image and the prompts in the community it's all going to be in there it's always updated every single day because i make these videos every single day otherwise let me know what other videos youC and I'll see you guys in the next one