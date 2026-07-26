---
title: "css网格布局Bento Grids"
author: "码码评测"
source: https://www.bilibili.com/video/BV1fvnhzHEYK
date: 2026-05-27
tags:
  - bilibili
  - 笔记
  - 前端
  - CSS
  - 网页设计
  - 响应式布局
  - 布局技巧
  - 开发工具
type: video-note
bvid: BV1fvnhzHEYK
duration: "3:37"
cover: "http://i1.hdslb.com/bfs/archive/2eda570a0021535bf234abfffa386fb735adc40f.jpg"
description: ""
---

# css网格布局Bento Grids

> [码码评测](https://space.bilibili.com/62613973) | [BV1fvnhzHEYK](https://www.bilibili.com/video/BV1fvnhzHEYK) | 时长 3:37

## Bento Grids 设计风格
### 什么是 Bento Grids
- Bento Grids 是一种灵感来自日本便当盒的网页设计风格，将网页内容分割成不同大小和形状的区块，视觉上整齐有序。
- 这种设计方法在近几年非常流行，通过 CSS 网格布局实现，具有高度的灵活性和响应式能力。

## CSS 网格布局基础
### 创建网格容器
- 使用 `Grid Template Columns` 和 `Grid Template Rows` 属性定义网格的列和行。
- **具体例子**：创建一个四列和两行的网格，每列和每行的大小设置为 200 像素，间距（Gap）设为 1em。
  ```css
  .grid-container {
    display: grid;
    grid-template-columns: 200px 200px 200px 200px;
    grid-template-rows: 200px 200px;
    gap: 1em;
  }
  ```
- 初始状态下，网格项（盒子）会按顺序依次排列。

### 命名网格区域
- 使用 `Grid Area` 属性为每个网格项指定唯一的名称，例如 `box1`、`box2`、`box3` 等，以便在布局中引用。
  ```css
  .box1 { grid-area: box1; }
  .box2 { grid-area: box2; }
  .box3 { grid-area: box3; }
  .box4 { grid-area: box4; }
  .box5 { grid-area: box5; }
  ```

### 定义布局结构
- 使用 `Grid Template Areas` 属性是关键步骤，通过字符串来定义网格中每行的盒子排列。
- 每个字符串代表网格的一行，字符串中的空格分隔列，盒子名称（如 `box1`）作为标识符。
- **具体例子**：
  - 第一行字符串：`"box1 box2 box2 box3"`，表示 `box1` 占一列，`box2` 跨两列，`box3` 占一列。
  - 第二行字符串：`"box1 box4 box5 box5"`，表示 `box1` 继续占一列，`box4` 占一列，`box5` 跨两列。
  ```css
  .grid-container {
    grid-template-areas:
      "box1 box2 box2 box3"
      "box1 box4 box5 box5";
  }
  ```
- 这会创建一个类似便当盒的布局，其中 `box2` 和 `box5` 跨越多列。

## 调整和自定义布局
- 通过修改 `Grid Template Areas` 中的字符串，可以轻松调整布局大小和位置。
- **具体建议**：例如，将 `box1` 放在更多位置（如第一行和第二行的第一列），并让其他盒子变小，只需微调字符串即可实现完全不同的布局。
  ```css
  /* 修改后的布局示例 */
  grid-template-areas:
    "box1 box1 box2 box3"
    "box4 box4 box5 box5";
  ```
- 这种灵活性使得 Bento Grids 在响应式设计中非常强大。

## 响应式设计
### 使用媒体查询实现响应式
- 针对不同屏幕尺寸，使用 CSS 媒体查询（Media Queries）重新排列网格区域。
- **完整实操步骤**：
  1. **平板设备**：调整网格为 3x3 布局，修改 `Grid Template Columns` 和 `Grid Template Rows` 的值，并重新定义 `Grid Template Areas`。
     ```css
     @media (max-width: 1024px) {
       .grid-container {
         grid-template-columns: 1fr 1fr 1fr;
         grid-template-rows: auto auto auto;
         grid-template-areas:
           "box1 box2 box2"
           "box1 box4 box5"
           "box3 box4 box5";
       }
     }
     ```
  2. **移动设备**：调整为两列四行的网格，进一步优化布局以适合小屏幕。
     ```css
     @media (max-width: 768px) {
       .grid-container {
         grid-template-columns: 1fr 1fr;
         grid-template-rows: auto auto auto auto;
         grid-template-areas:
           "box1 box2"
           "box3 box2"
           "box4 box5"
           "box4 box5";
       }
     }
     ```
- 通过这种方式，可以确保 Bento Grids 在桌面、平板和移动设备上都能良好显示。

## 总结
- 核心要点：Bento Grids 利用 CSS 网格布局，通过 `Grid Template Areas` 属性定义灵活的区块排列，结合媒体查询实现响应式设计，使网页布局像日本便当盒一样整齐且自适应，非常适合现代网页开发。

---

## 原始字幕

这种像日本便当盒的网站是最近几年非常火的设计风格Bental Greets这种设计方法会将网页内容分割成不同的大小和形状视觉效果看起来就像日本便当盒那样不同的食物被不同的区块整齐的分割开来一样但是你知道如何构建吗?如何让它具有响应时?想要创建这个布局,我们需要了解Grid Area是如何工作的首先我们需要CSS网格布局使用Grid Template Columns和Grid Template Rows来创建四列和两行为了简单起见它们都是200像素大小然后我们把间距Gap设为1EM现在来看这些盒子它们都一个一个的挨着排列接下来我们需要在网格中定义它们的确切位置首先我们需要对盒子进行命名每一个盒子都需要一个名称为此我们使用Grid Area属性网格区域的名称就是Box1,Box2,Box3等等现在每个盒子都有了网格区域的名称我们现在可以决定这些网格区域应该有多大换句话说它们应该跨越多少列或行然后我们使用Grid Template Areas属性这是最关键的一步在这个属性上我们可以定义字符串一个字符串就是网格中的一行我们的目标是网格设计所以在第一行中我们需要box1 box2再次box2和box3现在我们来写另外一个字符串我们在第二行中这样做在网格的第二行中我们需要再次box1 box4 box5和再次ox5。现在我们可以看到我们视频开头的第一个网格布局了。对于初学者来说,这可能有点难以理解,但Grid Template Areas属性包含了盒子的信息,确切地说明每个盒子应该放在哪里。注意看,每个字符串都是一行,字符串的空格分格列,每一个盒子都有一个网格区域作为它的标志符这个属性可以让我们非常容易的改变布局只需要改变这些字符串例如我可以通过把box1放在这里和这里来让它变得更大并让所有其他的盒子变小一点只需要做一点微小的调整我们将会得到一个完全不同的布局这在响应式网页设计时会非常强大对于较小的显示屏我们使用AdMedia媒体查询我们重新排列网格区域让所有的盒子都能合适地放在小的显示屏上我们需要改变Grid Template Columns和Grid Template Rows的值例如我们可以使用3x3的网格现在在Grid Template Errors中我创建一个看起来像这样子的设计我们只是重新排列5个网格区域为5个盒子这样我们就有了3x3的布局现在这样更窄一些完美适合平板设备当然移动屏幕也是同样的道理我们可以再做同样的事情但这次只用两列和四行所以根据屏幕的尺寸我们可以总是改变Grid Template Areas的属性来创建合适的网格布局到这里你就掌握CSS网格布局来创建Bentor Grid的方法了如果这期视频对你有帮助欢迎关注马马评测我们下期再见