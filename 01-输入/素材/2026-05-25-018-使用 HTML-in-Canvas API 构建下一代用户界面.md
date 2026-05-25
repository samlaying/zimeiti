---
title: "使用 HTML-in-Canvas API 构建下一代用户界面"
author: "GoldenSpiderAI"
source: https://www.bilibili.com/video/BV1LDGL6qEca
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - 前端
  - Canvas
  - WebGL
  - WebGPU
  - UI
  - 浏览器API
type: video-note
bvid: BV1LDGL6qEca
duration: "16:19"
cover: "http://i2.hdslb.com/bfs/archive/84f821f95dbba885b08ca364b372ad1d6afc17b2.jpg"
description: "原始视频网址：   https://www.youtube.com/watch?v=TUtKGTeFWjQ&amp;t=255s    原始视频发布日期：2026-05-21    视频名称：   使用 HTML-in-Canvas API 构建下一代用户界面    描述：   了解 HTML-in-Canvas API 如何让您直接将 HTML 元素绘制到画布中，同时保留语义信息（例如可访问性和交互性）。随后探索如何操控纹理以创建动态效果，同时仍保持类似交互式网站的体验。我们将全面介绍该 API 的丰富功能，展示潜在用例的演示，并了解初始设置流程。    #GoogleIO     活动：G"
---

# 使用 HTML-in-Canvas API 构建下一代用户界面

> [GoldenSpiderAI](https://space.bilibili.com/3546838527380108) | [BV1LDGL6qEca](https://www.bilibili.com/video/BV1LDGL6qEca) | 时长 16:19

## HTML-in-Canvas API 笔记

### 一、 概述：DOM vs Canvas 的困境与解决方案
1.  **DOM 的优势**：
    *   提供开箱即用的出色 UI 和文本布局解决方案。
    *   与浏览器功能深度集成，如：文本选择/复制、右键菜单、**无障碍（Accessibility）**、翻译、页面内查找、阅读模式、扩展、深色模式、浏览器缩放、自动填充等。
2.  **Canvas 的优势（包括 WebGL/WebGPU）**：
    *   提供底层访问能力，支持高性能的 2D 和 3D 图形渲染。
    *   是游戏、Google Docs 等需要复杂 UI 和性能的应用的理想选择。
3.  **传统困境**：
    *   在 Canvas 中渲染 UI 时，需要自行或通过框架处理响应式文本布局等逻辑，增加了代码量。
    *   **所有 DOM 附带的浏览器功能在 Canvas 渲染时完全失效**。
4.  **HTML-in-Canvas API 的诞生**：
    *   **核心作用**：作为一座桥梁，让你可以将 DOM 元素直接绘制到 Canvas 或 WebGPU 纹理中。
    *   **核心优势**：通过将 HTML 放在 `<canvas>` 标签内并更新元素变换，**内容不仅可交互，所有提到的浏览器功能也能保持连接**。

### 二、 核心原理与使用阶段
API 的使用分为三个阶段：**设置 Canvas、渲染元素、更新变换**。

#### 1. 设置 Canvas
*   **关键步骤**：在要绘制的 `<canvas>` 标签上设置 `layoutsubtree` 属性。
*   **作用**：让浏览器感知 Canvas 内的内容并将其设置为可访问。

#### 2. 渲染 DOM 元素
根据使用的渲染上下文，调用不同的 API 方法。
*   **2D 上下文**：使用 `drawElementImage(domElement, x, y)`。
    *   示例：在 `onpaint` 事件中调用，确保 UI（包括用户高亮或“页面内查找”的结果）始终更新。
*   **WebGL**：使用 `texElementImage2D`，参数与 `texImage2D` 相同，但用 DOM 元素引用替代图像源。
*   **WebGPU**：使用 `copyElementImageToTexture`，类似于 `copyExternalImageToTexture`。

#### 3. 更新元素变换（至关重要）
*   **方法**：将 API 调用返回的变换应用到 DOM 元素的 CSS `transform` 属性。
*   **目的**：告知浏览器元素在 Canvas 中的实际位置，**使交互和浏览器功能自动生效，无需额外集成**。
*   **重要注意事项**：
    *   每次重绘元素时，必须更新此变换。
    *   如果停止绘制某个元素，必须将其从 Canvas 元素中移除，否则它仍会向浏览器和无障碍系统呈现为页面的一部分。
    *   为避免模糊，需正确设置 Canvas 的 `width` 和 `height`（通常使用 `ResizeObserver`）。

### 三、 框架集成与进阶使用
1.  **Three.js 集成**（已提供实验性支持）：
    *   创建材质。
    *   使用 `new THREE.htmlTexture(domElement)` 设置材质的 `map`。
    *   使用几何体（如 Box）和该材质创建网格。
2.  **PlayCanvas 集成**：
    *   设置带 `layoutsubtree` 的 Canvas，创建 HTML 元素。
    *   创建 PlayCanvas 纹理，并添加事件监听器将其源设置为要渲染的 HTML 元素。
    *   添加事件监听器，以便浏览器重绘元素时上传纹理，保持更新。
    *   将 HTML 纹理作为材质的漫反射贴图。
    *   **最佳实践**：应检测 API 可用性并提供回退方案（polyfill）。

### 四、 功能演示与应用场景示例
API 的演示页面展示了多种强大能力：
1.  **复杂的文本布局**：同时支持从右到左（RTL）和垂直方向的文本渲染。
2.  **完整的交互性**：在 Canvas 或 3D 纹理中，仍可拖拽图片、右键保存、使用滑块、输入文本。
3.  **开发者工具集成**：元素可像普通 DOM 一样被右键检查和修改（如在 DevTools 中修改滑块步长）。
4.  **浏览器功能的无缝支持**：
    *   **无障碍**：内容在无障碍树中完全暴露，Lighthouse 可给出 100 分无障碍评分。
    *   **深色模式**：若 CSS 尊重深色模式，UI 会随浏览器设置自动更新。
    *   **页面内查找**：在 3D 场景中搜索文本也能正常工作。
5.  **富媒体集成**：
    *   可将 **动画 SVG** 渲染为纹理，无需额外代码即可播放。
    *   可实现**文本扭曲效果**，且文本选择、查找功能依然有效。
6.  **实用 3D 场景**：
    *   **3D 电子书**：所有文本由 DOM 布局，可实时更改字体样式。
    *   **浏览器翻译**：可将书中的文本一键翻译成其他语言（如德语），完美集成。
7.  **AI 与扩展集成**：
    *   由于所有内容都是暴露在 HTML 树中的文本，AI 智能体或简单的文本提取扩展可以直接访问、提取或朗读这些文本。
8.  **WebGPU 示例**：果冻滑块效果，支持正确的折射，并保持与输入滑块的交互。

### 五、 现状与未来
*   **API 状态**：目前处于 **Origin Trial** 阶段（截至 2026 年 5 月），可以在 Chrome 中实验性部署。
*   **采用情况**：Figma、Adobe、Miro、JetBrains 等知名应用已开始原型设计和探索。
*   **社区与标准**：提供 HTML-in-Canvas 示例集合和提交链接。Chrome 团队正与其他浏览器合作，推动该开放标准在未来的广泛实现。

### 总结
HTML-in-Canvas API 是一项革命性的浏览器标准，它通过允许将完整的 DOM 内容（包括所有交互性和浏览器集成特性）直接渲染到 Canvas、WebGL 或 WebGPU 纹理中，彻底解决了传统 Web 开发中高性能图形与富功能 UI 之间的矛盾。开发者可以利用熟悉的 DOM 和 CSS 来构建复杂的 2D/3D 界面，同时无缝保留文本选择、无障碍、翻译、页面内查找等所有关键浏览器功能，为创建下一代高性能、高交互性的 Web 应用开辟了全新可能。目前该 API 处于实验阶段，但已有主流框架和大型应用开始集成，预示着广阔的前景。

---

## 原始字幕

Hello, everyone.My name is Thomas and today I'm here to introduce the HTML in Canvas API.This API lets you draw DOM content directly into a Canvas or a WebGL and WebGPU texturewhile keeping the UI, interactable, accessible, and hooked up to your favorite browser features.所有 中 кноп mantra xant rainfall thunderstorm report make sure de SB trustworthy整个 Ito 내용必须用配て能根据一下很久就给你的 설游主是一个解期 aroma即使用虚拟那些油旧看脑セ�号the browser builds from that code.As you'll see, this API changes both the static HTML on the pageand updates the live DOM structure to enable interactivity.The DOM is the staple of WebUIand has incredible features hooked up through the browser.It offers great UI and text layout solutions out of the boxthat leverages semantically understood contentto create rich and interactable interfaces.它使用选择做 common operations across webpages, including simple things we take for granted, like selecting text to copy or right-clicking an image to save it. There are also a ton of browser integrations for features like accessibility, translate, find-in-page, reader mode, extensions, dark mode, browser zoom, and autofill, which are all pivotal to how users interact with the web. Canvas, along with WebGL and WebGPU, on the other hand,给 developers low-level access去 enable highly advanced 2D and 3D graphics. The power of Canvas is that it is a low-level system that can use various rendering stacks like WebGPU or rendering frameworks to drive that grid of pixels. Games and many web apps like Google Docs that have complex UI need this performant low-level access. However, because the Canvas is just a grid of pixels with some basic functionality, you'll need to handle a lot of logic like responsive text layout yourself or through a framework which adds to your bundle cost. Additionally, all these features I prattled off earlier for the DOM break completely when the UI is rendered into a canvas. Until now, that is. The HTML and Canvas API is the bridge that gives you the best of both worlds by letting you paint DOM elements into a canvas or web GPU texture.and the best part is that by putting the HTML inside the canvas tag and updating the transformthe content not only remains interactable but all the browser features I mentioned stay hooked up too. The API is available in Chrome today and we're actively engaged with other browsers on the open standard and hope to see it shipping across browsers in the future. Using the API3 phases, setting up your canvas, rendering into the canvas or into a texture, and finally updating the transform of the element to tell the browser where it actually is. Let's look at each of those steps through some code. The first thing to do is to set the layout subtree property on the canvas tag you're painting into. This causes the browser to be aware of the content in the canvas and sets it up to be接触的性 также Ladiesに61ена multi-teste yaRendering the element will require an explicit API call through a 2D context, WebGL, or WebGPU, which we'll take a look at next. For a 2D context, the call is drawElementImage, which takes the DOM element and an X and Y location of where to draw the element into the canvas.in this example we're doing this through the on paint event which triggers whenever the element is getting redrawn including when the user or something like find in page highlights the text this is the best way to make sure the ui is always updated but you can do this wherever it makes sense for your application the api method returns a transform that you can then apply to the css style transform property of the dom object to let the browser know wherethe element is being rendered.This is so that interactivityand browser functionalityworks automaticallywith no additional integrations.It's vital that you updatethis transformwhenever you repaint the element.If you stop painting the elementit's also criticalto remove itfrom the canvas elementor else it'll keepbeing presented to the browserand accessibility systemsas being part of the page.An important stepis to set the widthand height of the canvasto the right scale factorso that you avoid blurriness when rendering.To do this, you just need to make sure to add these few lines of code to set a resized observer.For WebGL, you still need to set the layout subtree propertyand add the HTML you wish to render inside of that canvas.To then paint the element into a texture,you'll use textElementImage2D, which matches exactly to the textImage2D WebGL method and take the same arguments except instead of an image source, you pass in a reference to the DOM element. For rendering using WebGPU, we also set up the canvas in the same way. Then we use the copy element image to texture method, which is similarly analogous to WebGPU's copy external image to texture method, which you may be familiar with. So those two functions just paint the DOM element into a texture, but just like in the 2D example it's also critical that we update the CSS transform of the element so that the browser knows where it is on the screen doing this in 3D space is a bit more complex and I won't show the full code here but you can see it in this code sample at a high level we apply a viewport transformation to map the 3D coordinate spaces to the CSS coordinate space and then use the canvas provided get element transformto get a transform we can then apply the same way that we did for the 2D casethat's all a little difficult and confusingbut luckily that's why we have amazing frameworks to help do that heavy liftingso that you can focus on easily using the featureI'm happy to share that 3JS has already landed experimental support for HTML and Canvaswhich you can dig into more at this linkusing the API with 3JS is very simple you can create a material and then set the map of that material using the new 3.html texture method passing in the DOM element to be rendered. Then you just create a mesh using some geometry like a box and applying that material and boom. Another framework that has also landed support is the Play Canvas framework which lets you build stunning HTML5 games and visualizations.the setup here is also very simple where you set up your canvas with layout subtree create an HTML element and then create a play canvas texture we then add an event listener that sets there you set up your canvas with layout subtree, create an HTML element, and then create a play canvas texture. We then add an event listener that sets the source of that texture to be the HTML element we want to be rendered. Finally, we add an event listener that just uploads the texture whenever the browser repaints the element so that it always stays up to date.now that we have the HTML texture we can use it as the diffuse map of a material which we can then apply to a cube and once again boomit's worth highlighting that this example will also detect if the API isn't available and fall back to using a polyfill for rendering while this doesn't hook up the browser features it is always a best practice to provide a fallback for your own projects as wellyou can see the full code sample at this linkfor a more complex exampleyou can see this shoe demowhere the style selector movesalong with the cursor to give a stunning 3D effectwhile leveraging simple HTML for the UIof course nowadays amazing coding toolslike anti-gravity and a host of otherscan also help do a lot of this coding for youbecause this is a brand new APIa lot of coding tools won't know about the APIunless you provide it with contextyou can pass in the explainer link and suggest the coding tool to reference the examplesbut even better is utilizing the modern web guidance linked herewhich will help the coding tool understand everything it needs to know for using the apiso now that we know the basics of the apilet's walk through some examples to showcase the full power of the api in practiceall of these examples can be found on the page at this linkin this first example we have some text being rendered both right to left and up and downand if we look over here into devtools we can see that it is indeed inside of the canvas element itself and we can still do things like drag the image around or right click to save itand there's even a little svg working there as wellaccessibility information is now also exposed even though this element is inside of the canvasand if we come over here into the accessibility tree view you can see all of that content which which would be accessible to for example a screen reader and if we go over here into Lighthouse we can see that we can even get an accessibility score of 100 even though all of that content is being put inside of the canvas in a slightly more practical world we have this simple WebGL example where you can see this UI is painted into a texture but I can actually still utilize the text utilize the slider or input text myselfand then because it's all just hooked up through DevTools I can even right click on this and say inspect to see this UI right here and I can actually even say well this is actually a super simple control and you can see that the UI will just update there automatically while staying fully interactive and exposed to all the other browser features as well and finally if your CSS respects dark mode then you can actually go in here and say update your browser customizationto dark mode and the UI will just update accordingly. Now, if you wanted something that looked a little bit more like a real billboard, you could also make something like this. And this is cool because this little pencil that you see here is actually an animated SVG that is now being rendered not only into the canvas as an animated SVG, but directly into the WebGL texture itself. And so now you can just play these SVGs without any kind of additional code. and of course all the text and interactivity remains fully functional as well. If you wanted to have something like a visually stunning overlay utilizing a 3D model, you can also do that. You can see here that you can still utilize the slider and it'll actually refract through the 3D model itself. And similarly, if I wanted to do something like find in page, I can go in here and search for a specimen. And you can see that even that piece here will also refract through the 3D model appropriately.You can also do this really neat text distortion effectas you drag the mouse aroundand learn about this experimental APIfor rendering HTML directly into a WebGL textureand this again just works as basic UIand if you wanted toyou can even select the textand see that the effect is being appliedto that selection of textand if you wanted to again find in pageall of this just works automaticallyand hooked up through the same HTMLthat you know and lovenow we have perhaps againjust a slightly more practical example something that you might actually want to do. Here you can see a kind of 3D book that has all been rendered using WebGL. And again, this all just works as text being laid out thanks to the HTML in Canvas API. Because this is all just laid out with the DOM and HTML, I can even go in here and decide I maybe want a more classical font to read Sherlock Holmes in, and it'll just update in there directly. And then I say, okay, maybe that isn't really too easy for me to read, so I want something more like blocky and funny looking and can select out here this different text and boom, it all just updates that font and you can really just choose anything that you want. So we'll go ahead and switch it back to a more normal font so that we can kind of see what we're looking at. And now I want to talk about perhaps one of my own personal favorite parts of this API. Speaking as somebody who lives in a country where I don't speak the language perfectly, a really important feature for me is the browser-provided translate. And so I'm able to go in here and just use that translation to say translate this over into German and read Die Abenteuer des Sherlock Holmes and it just automatically updates all of that different text. That means that I can now have these beautiful 3D scenes while still letting my users pick any language that they want to experience that in. Now, it wouldn't be Google I.O. unless I also had the chance to at least somewhere mention AI and that's actually another place where this API comes in handy. because all of this is just text exposed in the HTML tree something like an indexing crawler or an AI agent would be able to engage with all of it as just text so let's say I wanted my agent to extract all of the text in all of these different pages rather than having to leaf through them maybe I wanted to read it out loud to me I can then go in and have something like an agent or even a simple extension like a text extractor use that as an access to text directly because it's all just text myself or an agent can then copy out this text maybe somewhere to read it out loud this last example is actually a web gpu example and here we can see this fun jelly slider that some of you may have seen before but now it actually refracts fully and correctly with this little number right here and of course since it's all just hooked up through an input slider we can even go over here into the dev tools and say changing the step from a 1 to a 5and boom it automatically updatesso that rounds to the nearest fiveand is still very fun and engagingwhile of course also staying hooked upto those browser featureseven in this early stage of the APIit's already getting some amazing appslike Figma, Adobe, Miro and JetBrainswho have all started prototypingand exploring what the APIcan enable for their web appsas of May 2026the API is an origin trialwhich means you can already experiment with deploying it to production in Chrome, but you will have to sign up your origin at this link to enable the API. So hopefully that gives you an overall sense of the API, how to use it, and what it enables for you to create. So now all that's left is for you to go and create something amazing and, of course, share what you make. We have an awesome HTML in Canvas Read Me file where we're hoping to keep track of some of the incredible things people are making, and there's a submission link for you to include your own amazing creations or finds. And with that, I just want to say thank you for listening today and I can't wait to see some of the amazing ways that you'll use this API. Thank you.