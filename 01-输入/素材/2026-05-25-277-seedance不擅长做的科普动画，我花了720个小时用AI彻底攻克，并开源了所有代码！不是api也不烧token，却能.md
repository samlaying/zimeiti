---
title: "seedance不擅长做的科普动画，我花了720个小时用AI彻底攻克，并开源了所有代码！不是api也不烧token，却能一句话接入龙虾生成AE质感的动画视频"
author: "浙大猫学长"
source: https://www.bilibili.com/video/BV1GySZBGEJC
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI视频
  - 工具推荐
  - 提效
  - 开源
  - 前端开发
  - 科普动画
type: video-note
bvid: BV1GySZBGEJC
duration: "3:53"
cover: "http://i2.hdslb.com/bfs/archive/c39a78516ba3b880deb6aa93eb62dd8ddfde0799.jpg"
description: "npx create-vibe-motion | github: vibe-motion/skills"
---

# seedance不擅长做的科普动画，我花了720个小时用AI彻底攻克，并开源了所有代码！不是api也不烧token，却能一句话接入龙虾生成AE质感的动画视频

> [浙大猫学长](https://space.bilibili.com/198345535) | [BV1GySZBGEJC](https://www.bilibili.com/video/BV1GySZBGEJC) | 时长 3:53

## VibeMotion：用AI编程攻克精准动画

### 1. VibeMotion 的核心价值与定位
*   **解决的问题**：在 AI 生成视频的工作流中，`C-Dance` 等工具完成了 **70%** 的工作，但剩余 **30%** 中，尤其是需要**精准控制**和**算法驱动**的 **25%** 部分（如科普动画），是其不擅长的。
*   **解决方案**：`VibeMotion` 是一个**通过让 AI 编程来制作动画**的技术。
*   **核心优势**：
    *   **擅长领域**：因其代码/算法驱动的特性，**尤其擅长制作科普动画**。
    *   **素材来源**：可以从任何网页上喜欢的**开源动效代码**中获取灵感和素材，让 AI 进行魔改并渲染为视频。
    *   **与 C-Dance 的关系**：两者是互补关系。**70% 的常规 AI 视频由 C-Dance 生成，而需要精准控制的 25% 交给 VibeMotion。**

### 2. 核心组件与标准化
为了降低小白门槛，UP主进行了一个月的标准化工作，推出了两个核心组件：

#### 2.1 CreateVibeMotion（开发环境一键搭建）
*   **功能**：通过**一行命令** (`npx create-vibe-motion`)，快速搭建一个本地的 VibeMotion 开发环境。
*   **目标**：用户只需专注于“**Vibe（感知/构想）**”想要的动画效果，**预览、调试、渲染**等复杂功能均已集成，做到了**开箱即用**。

#### 2.2 VibeMotion Skills（动画技能库与一键调用）
*   **功能**：安装后，可以通过与 AI（如“龙虾”）的**对话**来生成视频。
*   **特点**：**几乎不消耗 Token**。用户可以将自己创作的动画作为 “Skill” 上传，形成一个**开源社区**，让全球的 AI 都能复用这些动画效果。
*   **愿景**：使其成为 VibeMotion 开源社区的发源地，甚至有潜力成为百万级仓库。

### 3. 实操案例演示
UP主以 GSAP 动画社区的 `RollingTags` 动效为例，演示了完整流程。

#### 3.1 准备阶段：获取动效代码
1.  在 GSAP 动画社区找到目标动效（如 `RollingTags`）。
2.  进入其 **CodePen** 页面。
3.  点击右下角的 **Export**，选择 **Export ZIP**。
4.  解压后得到动效代码文件夹，用 VSCode 或 Cloud Code 等编辑器打开。

#### 3.2 搭建环境并启动
1.  在终端中执行命令：`npx create-vibe-motion`
2.  **推荐模型**：UP主推荐使用 **MiniMax 的 M2.7 大模型**。原因：编程能力提升，且**指令遵循能力极强**，完美契合基于 Skills 的 VibeMotion 工作流。
3.  安装 `MiniMax Multi-Model Toolkit` 这个 Skill 以使用该模型。
4.  命令执行完成后，目录下会生成 `VibeMotion App` 文件夹。
5.  让 AI（如 M2.7）**启动预览**，此时会显示模板自带的默认动画。

#### 3.3 替换与调整动画
1.  **替换动画**：向 AI 发出指令：“将 `index.html` 中的 `RollingTags` 的动画效果替换 `VibeMotionApp` 中的默认动画，背景要透明像素”。
2.  **AI 自动化过程**：M2.7 会自动阅读项目结构、分析动画代码、生成代码并替换，**全程无需人工干预**。
3.  **参数调整**：AI 已将新动画的参数暴露在 UI 面板。可根据需要调整（如将文字颜色从默认的黑色改为其他颜色，并将文字改为“VibeMotion”）。

#### 3.4 渲染输出
1.  向 AI 指令：让其渲染一个 **ProRes 4444** 编码、**带透明通道**的视频（接近无损）。
2.  **替代方案**：若不要求透明背景，可使用 **H.264** 编码，视频体积会更小。

## 总结核心要点
本视频介绍了 **VibeMotion** 这一通过 AI 编程生成精准动画的技术，它精准弥补了 C-Dance 等 AI 视频工具在**算法驱动、精准控制动画**（如科普动画）上的短板。UP主通过 `CreateVibeMotion`（一键搭建环境）和 `VibeMotion Skills`（对话生成动画、构建开源社区）这两个标准化工具极大降低了使用门槛。通过一个完整案例，展示了如何从网页获取开源动效、利用 AI 大模型（如 MiniMax M2.7）自动完成代码替换与渲染，实现从想法到带透明通道视频的快速、低成本产出，最终旨在构建一个可共享、可复用的 AI 动画技能开源生态。

---

## 原始字幕

如果说C-Dance完成了AI做视频的70%那它打通了剩余的35%这就是RideMotion一个通过让AI编程来做动画的技术有了它你在网页上浏览到任意喜欢的动效只要代码开源都可以让AI魔改效果并渲染为视频比如这是开头尺子动画的来源这是卡片动效的来源由于RideMotion有代码或者说算法驱动所以尤其擅长这座科普像动画譬如我之前视频中出现的这些动画而这就是C-Dance总不擅长的因此我在说70%的AI视频可以交由C-Dance生成而需要精准控制的那25%交给Vibemotion没想到吧这个丙2动画也是由Vibemotion改造生成的那小白能掌握吗没问题猫学长花了整整一个月将Vibemotion做了标准化首先是CreateVibemotion可以通过一行命令快速搭建一个本地的Vibemotion开发环境你只管VibEye想要的动画效果预览 调餐 渲染这些复杂的功能猫学长都配合一些开源库集成好了做到了开箱即用第二个是ViveMotion Skills安装后你的龙虾通过对话就能生成视频并且几乎不需要Token虽然目前Skills上只有我自己研发过的动效但这个仓库将是ViveMotion开源社区的发源地任何人都可以将你vibe出来的动画作为Skills上传让全世界的龙虾都能复用你做的动画废话不多说立马也是比如我在GSAP动画社区里随便拿一个动效作为教学案例就这个RollingTags的吧有点滚通洗衣机的味道我们点这个code pen然后再点右下角的export有一个export zip解压之后我们就得到这个动效的代码将这个desk的文件夹用代码编辑器比如VSCode打开虽然Cloud Code有VSCode的插件但猫学长还习惯用中端的Cloud Code进行webcoding其中一个方便的点就是当第一个字符是赶在号时这就变成了shile模式可以快速的执行中端命令还记得那行命令吗NPX Create Vibe Motion中间有两个小横杠Vibe Motion 启动在安装依赖的过程中猫学长推荐MiniMax新一代的大模型M2.7这一代除了编程能力稳步提升之外还极大的提升指令遵循能力而这正好完美契合了基于Skills的Vibe Motion原来Coding Plan改名为Token Plan还附赠了一些多模态的热度安装MiniMax Multi-Model Toolkit这个Skill就能使用啦Create Vibemotion执行完后可以看到目录下多了Vibemotion App这个文件夹先让M2.7帮我们启动预览这就是模板自带的模板动画我们需要将这个动画替换为刚刚下载的RollingTax那就接着和智能体说将index.html中的RollingTax的动画效果替换ViveMotionApp中的默认动画背景要透明像素M2.7就会阅读项目结构分析动画生成代码最后替换动画全程不需要人工干预动画已经替换了但我发现姿势白色的看不清不过AI已经将新动画的参数及文字颜色暴露在了UI面板我现在调成黑色然后再把文字改成ViveMotion最后我们让M2.7选一个ProRes 4444带透明通道的视频这是一个接近无损的视频编码格式如果你不要求背景透明的话用H264也可以体积还能小很多如果学会的话就赶紧来Skills仓库提交PR吧也许OneMotion将会是下个百万级仓库我是猫学长我们下期再见