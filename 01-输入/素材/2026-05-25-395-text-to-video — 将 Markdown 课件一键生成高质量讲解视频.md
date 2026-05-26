---
title: "text-to-video — 将 Markdown 课件一键生成高质量讲解视频"
author: "冰冰一号00"
source: https://www.bilibili.com/video/BV1zqZeBME3V
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI
  - 提效
  - 教育技术
  - 开源工具
  - 自动化
  - 视频生成
type: video-note
bvid: BV1zqZeBME3V
duration: "9:14"
cover: "http://i0.hdslb.com/bfs/archive/85465998db6f9924a362aabba2f355c6b18eae32.jpg"
description: "用自然语言写教案，自动生成带语音+幻灯片的授课视频 基于通义千问（Qwen）大模型 + 浏览器自动化 + 音视频合成，全流程无需人工剪辑。 仓库地址：https://gitee.com/bingbingyihao/text-to-video"
---

# text-to-video — 将 Markdown 课件一键生成高质量讲解视频

> [冰冰一号00](https://space.bilibili.com/390314960) | [BV1zqZeBME3V](https://www.bilibili.com/video/BV1zqZeBME3V) | 时长 9:14

## Text-to-Video: 从Markdown课件一键生成高质量讲解视频

### 一、工具概述与核心价值
*   **核心功能**：将结构清晰的 **Markdown 课件**，一键自动转换为带有 **自然语音讲解** 和 **动态翻页幻灯片** 的高清 MP4 授课视频。
*   **解决痛点**：免除了传统视频制作中编写教案后，还需花费大量时间制作PPT、录制配音、剪辑视频的繁琐流程，将备课重心回归至教学本身。
*   **核心理念**：**“知识不该被格式锁死”**，让文字通过自动化技术“活起来”，实现从Markdown到声音、画面的一气呵成。
*   **适用人群**：教师、培训师、知识类内容创作者等，尤其适合在教育数字化和知识碎片化背景下，寻求高效视频生成方式的用户。

### 二、技术原理与设计目标
*   **技术栈**：
    1.  **大模型理解**：调用 **通义千问（Qwen）大模型** 理解教案逻辑，自动分章节、撰写口语化讲稿。
    2.  **幻灯片生成**：生成简洁美观的单页 **HTML** 格式幻灯片。
    3.  **语音合成**：使用 **Qwen-TTS** （支持 Qwen-Plus 和 Qwen3-TTS-Flash 模型）生成自然、节奏感强的语音。
    4.  **浏览器自动化**：使用 **Playwright** 驱动 Chromium 浏览器渲染 HTML 并录制翻页动画。
    5.  **音画合成**：使用 **FFmpeg** 将生成的 MP3 语音与录屏视频精准对齐，输出标准 MP4。
*   **五大设计目标**：
    1.  **易用性**：一行命令即可运行全流程（例如：`python main.py -i your.md -o output.mp4`）。
    2.  **智能化**：AI 深度理解教案，自动生成逻辑结构、讲稿和视觉化幻灯片，而非简单套用模板。
    3.  **可靠性**：每一步都有日志和临时文件，支持断点续跑，出错可快速定位。
    4.  **轻量化**：纯 Python 实现，不依赖 Node.js 或 Electron。HTML 幻灯片秒加载。
    5.  **可扩展性**：模块化设计（Parser， Scripter， Slides， TTS， Recorder， Composer），便于替换或集成新组件（如新 TTS 引擎）。

### 三、使用教程与实操步骤
#### 1. 环境准备与安装
*   **前提条件**：**Python 3.9** 或以上版本。
*   **安装步骤**：
    1.  克隆项目代码仓库，进入项目目录。
    2.  运行 `pip install -r requirements.txt` 安装依赖。
    3.  运行 `playwright install chromium` 安装浏览器驱动。
    4.  在 DashScope 控制台申请并获取 **API Key**，需开通 **Qwen-Plus** 和 **Qwen3-TTS-Flash** 模型权限。

#### 2. Markdown 输入规范
*   **结构要求**：输入必须为结构清晰的 Markdown。
    *   主标题：一级标题（`#`）
    *   章节：二级标题（`##`）
    *   正文：支持列表、代码块、LaTeX公式等丰富格式。

#### 3. 运行与参数说明
*   **基本命令**：`python main.py -i <输入教案.md> -o <输出视频.mp4> --api-key <你的Key> --voice <音色名> --speed <语速>`
*   **关键参数**：
    *   `-i`：指定 Markdown 输入文件。
    *   `-o`：指定输出视频文件名。
    *   `--api-key`：DashScope API Key（强烈推荐通过环境变量设置，勿硬编码）。
    *   `--voice`：指定语音音色（推荐 `Cherry`）。
    *   `--speed`：语速（推荐 `1.0` 为最自然语速）。
    *   `--resolution`：分辨率（默认 `1920x1080`）。
    *   `--fps`：帧率（默认 `24`）。
*   **首次运行**：会较慢，需启动模型和浏览器。所有中间结果（HTML 幻灯片、MP3 音频、JSON 日志等）均存储在 `temp/` 文件夹中，后续修改可复用中间结果，实现秒级重跑。

#### 4. 调试与输出
*   **中间产物**：`temp/` 目录包含所有中间文件，可单独检查：
    *   `slides.html`：可直接双击预览生成的幻灯片。
    *   `audio.mp3`：单独的语音文件。
    *   `debug/parse_data.json`：教案解析结果，用于检查章节划分是否正确。
*   **最终输出**：一个可直接使用的高清 MP4 视频文件。

### 四、架构、依赖与安全
*   **技术架构**：纯 Python 环境。核心依赖：DashScope SDK（AI）、Playwright（浏览器自动化）、FFmpeg（音视频处理）、Rich（终端美化）、Requests， JSON， Pathlib（基础功能）。
*   **安全与隐私**：
    1.  **全程本地处理**：教案解析、幻灯片渲染、音画合成均在用户本地电脑完成。
    2.  **API 安全调用**：API Key 仅用于安全地调用 DashScope 服务，每次请求只传输必要文本。
    3.  **数据不上传**：生成的语音（MP3）会从临时链接下载后存储为本地文件，不存于云端。
    4.  **敏感信息管理**：严禁将 API Key 等敏感信息写入代码或提交至公开仓库，建议使用环境变量或配置文件管理。
    5.  **`.gitignore`**：默认已忽略 `temp/` 和输出文件，防止中间产物泄露。

### 五、开源协议与社区贡献
*   **开源协议**：项目采用 **Apache License 2.0**，完全免费，允许商用、修改和再分发，只需保留原版权声明和 `NOTICE` 文件。
*   **贡献指南**：
    1.  **欢迎参与**：尤其鼓励新手从改进文档、报告 Bug、增加示例开始。
    2.  **扩展方向**：添加新 TTS 引擎（如11labs， Azure）、支持 PDF/PPTX 输入、搭建 Web UI、扩展多语言支持（`tts` 的 `lang` 参数已预留）。
    3.  **提交规范**：Fork 仓库 -> 新建功能分支 -> 编写代码（注意 PEP8 和类型注解） -> 提交 Pull Request 并关联 Issue。
*   **特别致谢**：感谢阿里云 DashScope 团队、Microsoft Playwright 团队、FFmpeg 社区以及 Rich 库作者等开源力量。

### 总结
Text-to-Video 是一个基于通义千问大模型和多种自动化技术的开源工具，它通过一行命令将结构化的 Markdown 课件智能转换为带有自然语音讲解和动态幻灯片的高质量视频，彻底革新了教育及知识内容的制作流程。其核心价值在于高度的易用性、智能化和可靠性，全程本地处理保障了数据安全，模块化设计和宽松的 Apache 2.0 开源协议为用户和开发者提供了极大的灵活性与扩展空间，真正实现了从文字到视听内容的无缝、高效转化。

---

## 原始字幕

我们今天聊的是Text to Video这个新能力。简单说,就是你用Markdown写好课件,它就能一键生成带讲解语音和翻页换灯片的完整授课视频。不用录音,不用剪辑,也不用调时间轴。整个流程背后,靠的是通意签问大模型理解你的教学逻辑,再结合浏览器自动化翻页,加上高质量语音合成技术,把文字真正讲出来。他支持QAIN Plus和QAIN 3 TTS Flash模型语音自然 节奏舒服你写的是教案他输出的是能直接用的课老师省力学生听得清Python 3.9以上就能跑开源免费用Apache 2.0协议这不只是工具升级而是把贝克这件事重新定义了一遍你有没有试过写完教案还得花半天做BBT录配音 剪视频太好时间了现在教育数字化和知识碎片化越来越快老师 培训师 内容创作者都急需一种更轻更快的视频生成方式Text to Video就是为这个痛点而生的它不让你从零开始折腾你只管把教案写成结构清晰的Markdown它自动帮你分章节理逻辑 写口语化讲稿自动生成简洁美观的单页HTML幻灯片用Quin TTS合成自然语音再用Playwrite录下翻页动画最后合成音画同步的高清MP4全程零设计零剪辑零PPT输出就是能直接发给学生的课备课这件事终于可以回归教学本身了我们设计Text to Video始终盯着五个核心目标第一是易用性你只需要一行命令比如Python Man T.BuyJuneration MDO-Alt-MP4敲回车就跑完全程第二是智能化它不是简单套模板而是让昆大模型真正都懂你的教案拆逻辑写讲稿生成视觉化HTM第三是可靠性每一步都留日志存临时文件件,出错了,马上定位,还能断点续跑,复用temp目录里的中间结果。第四是轻量化纯Python写的,不装Node.js,不绑Electron。换灯片是HTMA里没第三方依赖,打开就秒加载。第五是可扩展性六个模块清清楚楚Passer,Scripter,Slides,TTS,Recorder,Composer哪个想换就换哪个这五个目标不是口号是每天写代码时的标识好,我们马上动手试试先克隆代码仓库进到code目录用PIP装好依赖记得Python得是3.9以上再跑一句PenleyWriteInstallChromium把浏览器装上接着去Discope控制台开个API Key记得勾上QueenPlus和Queen3TTS Flash这两个权限然后直接运行命令PythonMindAPIAsample.mbAllOutput.mp4带上你的Key选个声音调好语速第一次跑会慢一点因为要启动大模型加载浏览器但所有中间文件都存进Time文件夹了下次改个字再跑秒级复用五分钟后你桌面上就多了一个outputmb4点开看看就是你的第一堂自动生成课我们来看详细使用说明输入必须是结构清晰的mardom主标题用一个警号章节用两个警号正文里可以写列表代码甚至latus公式比如它自动识别层级生成对应换灯片命令行参数很直观I指定你的教案文件O决定输出视频名分辨率默认1920xC2080帧率24都可调API Key和声音必须填推荐Cherry这个音色语速1.0最自然所有中间结果全存在Time文件夹里HTML换灯片双击就能预览MP3音频单独可听还有Debug里的JSON日志出问题先看ParseData JSON,确认分章对不对,再开Slide HTML,看看排版顺不顺眼。我们来看技术架构和依赖体系,整个系统跑在纯Python环境里,不碰NodeJS,也不用Electron。核心靠五类工具协同工作,Descope SDK负责调用Quain大模型,记读教案,写讲稿,也生成自然语音。Playwright驱动Chromium浏览器把HTN幻灯片一页页渲染出来在录下翻页动画音画合成交给FFM Papathon他把MP3和录屏精准对齐输出标准HD264加AAC的MP4终端体验Courage有彩色日志实时进度条出错一眼看清最后是Python自带的RequestJson和Paslo干好HTTP,配置和路径这些基础活所有依赖都列在Requirements.txt里PAD install.yar一行搞定我们特别重视安全和隐私所有处理解析教案,渲染幻灯片合成音化全都发生在你自己的电脑上原始markdown和中间文件一丁点都不会上传到服务器API Key只用来安全的调用Dash Scope每次请求只传必要的文本内容不带文件也不传任何原数据TTS生成的音频阿里云给的是带签名的临时链接我们下载完立刻存成本地MP3绝不往云端存一份TEMP文件夹里的东西默认不进Git你也记得在Gitignore里加上TEMP和Output细细到最后这条特别重要千万别把API Key写死在大马里更别提交到公开仓库推荐用环境变量或者自己加个ConfigusML支持MainTiply预留了扩展入口改起来很轻巧我们再来看开源协议和法律声明这个项目用的是Apache License 2.0完全免费你可以商用改代码再分发改完之后哪怕避原也没问题只要保留原来的版权声明还有Noting文件就行它还明确给了专利授权帮你避开不少法律隐患但。但得注意一点,协议写明按现状提供,不提供任何担保,出了问题作者不承担直接或间接损失。完整的协议文本就放在项目根目录的license文件里,打开就能看。另外提醒一句,你改代码加功能,完全可以,但别把API Key这类敏感信息编码进去,更别提交到公开仓库。用环境变量或者config要没有来管理既安全又规范欢迎你来一起贡献咱们特别欢迎新手朋友改文档Bobbug不是立markdown都是超有价值的起点想深入一点可以加新TTS引擎比如11lapse或azure支持PDF或PPTX输入甚至搭个webUI也行参与很简单先fork仓库再建个featurexx分支写代码时注意PP8和类型注解推上去最后提个Porequest记得关联issue我们最常看的是带TEMP日志和截图的bug报告还有更丰富的SampleMG示例比如数学推导编程实操中英混排这些场景也欢迎扩展语言支持TTS的Long参数已经预留好了幻灯片主题系统也在路上靠Prompt模板就能换风格有问题直接去GitHub Issues留言中英文都行最后我们想真诚的道一声感谢感谢阿里云Dash Scope团队Queen大模型API稳定低延迟是我们智能解析和内容生成的底气感谢Microsoft of Playwright的开发者们让浏览器自动化既可靠又优雅幻灯片渲染才这么顺滑感谢FFMPIC社区因视频处理的工业集机时合成流畅视频全靠它也特别感谢Rich Koo的作者终端里那些彩色日志实时进度条全靠它点亮这些开源力量像齿轮一样咬和运转拖起了整个工具链我们始终相信知识不该被格式锁死从你写的markdown开始到声音再到画面一气呵成这就是text to video的初心你的文字本就该活起来