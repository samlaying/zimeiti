---
title: "使用 HTML CSS 和 Javascript 创建令人印象深刻的旋转滑块模糊效果使用 HTML CSS 和 Javascript 创建令人印象深刻的旋转滑块"
author: "流浪字节"
source: https://www.bilibili.com/video/BV15T421a7QV
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - 前端开发
  - HTML
  - CSS
  - JavaScript
  - 动画效果
  - UI设计
type: video-note
bvid: BV15T421a7QV
duration: "33:12"
cover: "http://i2.hdslb.com/bfs/archive/bda654bd110ca46629b2395568be584ccecd8f83.jpg"
description: "https://www.youtube.com/watch?v=hfGz5AgHT-Ehttps://www.youtube.com/watch?v=hfGz5AgHT-E In this video, let&#39;s join Lun Dev to Create A Carousel Slider Blur Effects Impressive Using HTML CSS And Javascript. Combine using transform and filter to create impressive effects. This will be a design you c"
---

# 使用 HTML CSS 和 Javascript 创建令人印象深刻的旋转滑块模糊效果使用 HTML CSS 和 Javascript 创建令人印象深刻的旋转滑块

> [流浪字节](https://space.bilibili.com/122439591) | [BV15T421a7QV](https://www.bilibili.com/video/BV15T421a7QV) | 时长 33:12

## 项目简介
- 本视频由UP主“流浪字节”展示如何使用HTML、CSS和JavaScript创建一个具有旋转滑块模糊效果的轮播图（Carousel）。
- 核心效果包括：平滑过渡动画、无限循环滑动、模糊滤镜（Blur）、详细内容展开与隐藏，以及响应式设计。
- 关键组件：滑块项目（Item，包含图片、介绍内容和详细内容）、导航按钮（下一个、上一个、返回按钮）。

## 项目设置
### 创建文件
- 创建三个文件：`index.html`、`style.css`、`script.js`。
- 使用Google Fonts的Poppins字体：在CSS中通过`@import`或`link`标签引入。
- 图片准备：建议使用无背景图片；若有背景，可使用[remove.bg](https://www.remove.bg)网站去除背景。

### HTML基础结构
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>旋转滑块模糊效果</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- 内容将在这里编写 -->
    <script src="script.js"></script>
</body>
</html>
```

## HTML结构详解
### 头部（Header）
- 包含logo和导航链接，用于网站基础布局。
```html
<header>
    <div class="logo">Logo</div>
    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>
</header>
```

### 轮播图（Carousel）
- 主容器：`class="carousel"`，包裹整个滑块内容。
- 列表：`class="list"`，存放所有滑块项目。
- 每个项目（Item）包含三个部分：
  - 图片：`<img>`标签。
  - 介绍（Intro）：`class="intro"`，包含标题、主题、简短描述和“See more”按钮。
  - 详细内容（Detail）：`class="detail"`，默认隐藏，包含标题、详细描述、技术规格和结账按钮。
- 箭头按钮：`class="arrows"`，包含id为`prev`（上一个）、`next`（下一个）和`back`（返回）的按钮。
```html
<div class="carousel">
    <div class="list">
        <div class="item">
            <img src="image1.png" alt="Image">
            <div class="intro">
                <h2>Title</h2>
                <p>Topic</p>
                <p>Short description here.</p>
                <button class="see-more">See more</button>
            </div>
            <div class="detail">
                <h2>Detailed Title</h2>
                <p>Detailed description content.</p>
                <div class="specifications">
                    <div><p>Spec1</p><p>Value1</p></div>
                    <div><p>Spec2</p><p>Value2</p></div>
                </div>
                <div class="checkout">
                    <button>Add to Cart</button>
                    <button>Checkout</button>
                </div>
            </div>
        </div>
        <!-- 重复.item结构，共5个项目 -->
    </div>
    <div class="arrows">
        <button id="prev">◄</button>
        <button id="next">►</button>
        <button id="back">← Back</button>
    </div>
</div>
```

## CSS样式详解
### 全局样式
- 字体：`font-family: 'Poppins', sans-serif;`
- 移除默认边距：`margin: 0;`
- 链接样式：`text-decoration: none; color: #333;`

### 头部样式
- 最大宽度：`max-width: 1140px;`，默认宽度90%。
- 高度：`height: 50px;`
- 布局：`display: flex; justify-content: space-between; align-items: center;`
- 导航链接间距：`margin-left: 30px;`

### 轮播图样式
- 高度：`height: 800px; overflow: hidden; position: relative;`
- 列表定位：`position: absolute; top: 0; left: 0; width: 1140px; max-width: 90%; margin: auto; left: 50%; transform: translateX(-50%); height: 80%;`

### 项目样式
- 默认状态：`position: absolute; top: 0; left: 0; width: 70%; height: 100%; font-size: 15px;`
- 图片：`width: 50%; position: absolute; right: 0; top: 50%; transform: translateY(-50%);`
- 详细内容：默认隐藏，`opacity: 0; pointer-events: none;`（确保不可交互）。
- 介绍内容：`position: absolute; top: 50%; transform: translateY(-50%); width: 400px;`

### 全局CSS变量（用于项目位置控制）
- 在`:root`中定义变量，便于重用：
```css
:root {
    --item1-transform: translate(-100%, -5%) scale(1.5);
    --item1-filter: blur(30px);
    --item1-z-index: 5;
    --item1-opacity: 0;
    /* 类似定义位置2到5的变量 */
}
```
- 示例：第一项位置变量对应`transform: var(--item1-transform);`等。

### 动画效果
- 显示内容动画（`show-content`）：
```css
@keyframes show-content {
    from { transform: translateY(50px); filter: blur(10px); opacity: 0; }
    to { transform: translateY(0); filter: blur(0); opacity: 1; }
}
```
- 位置动画（如`position-item2`）：定义从其他位置移动到当前位置的初始值，用于滑动过渡。
- 应用动画到介绍内容元素，带有延迟创建序列效果：标题延迟0.7秒、主题延迟0.9秒、描述延迟1.1秒、按钮延迟1.3秒。

### 箭头按钮样式
- 容器：`position: absolute; bottom: 10px; width: 1140px; max-width: 90%; left: 50%; transform: translateX(-50%); display: flex; justify-content: space-between; align-items: center;`
- 下一个/上一个按钮：`width: 40px; height: 40px; border-radius: 50%; font-family: monospace; font-size: large; font-weight: bold; border: 1px solid #333;`
- 返回按钮：`font-family: 'Poppins'; font-weight: 500; border: none; border-bottom: 1px solid #333; background: transparent;`默认隐藏（`opacity: 0; pointer-events: none;`）。

### 详细内容展开样式
- 当carousel添加`show-detail`类时：
  - 其他项目移出屏幕：`left: 100%; opacity: 0; transition: left 0.5s, opacity 0.5s;`
  - 活动项目宽度扩展：`width: 100%;`
  - 介绍内容隐藏，详细内容显示：`opacity: 1; pointer-events: auto; right: 0; text-align: right; top: 50%; transform: translateY(-50%); width: 50%;`
  - 过渡效果使变化平滑。

### 背景装饰效果
- 使用`::before`伪元素在carousel内添加装饰：
```css
.carousel::before {
    content: '';
    width: 500px;
    height: 300px;
    background: linear-gradient(...); /* 多色渐变 */
    position: absolute;
    z-index: -1;
    border-radius: /* 随机值 */;
    filter: blur(50px);
    top: 50%;
    left: 50%;
    transform: translate(-10%, -50%);
    transition: transform 1s;
}
/* 当show-detail时，transform: translate(-10%, -50%) rotate(70deg); */
```

### 响应式设计
- **iPad屏幕**（宽度约768px）：
  - 项目宽度调整为`width: 90%;`
  - 规格内容添加`overflow: auto;`防止溢出。
- **移动屏幕**（宽度约480px）：
  - carousel高度：`height: 600px;`列表高度：`height: 100%;`
  - 项目宽度：`width: 100%;`字体缩小为`font-size: 10px;`
  - 介绍宽度：`width: 50%;`图片尺寸缩小（如`width: 40%;`）。
  - 标题字体：`font-size: 2em;`详细内容高度限制（`max-height: 100px; overflow: auto;`）。
  - 结账按钮使用`display: flex;`防止换行。

## JavaScript功能详解
### 元素获取
```javascript
const nextBtn = document.getElementById('next');
const prevBtn = document.getElementById('prev');
const backBtn = document.getElementById('back');
const seeMoreBtns = document.querySelectorAll('.see-more');
const carousel = document.querySelector('.carousel');
const list = document.querySelector('.list');
const items = document.querySelectorAll('.item');
```

### 事件监听
- 为next和prev按钮添加点击事件，调用`showSlider`函数。
- 为每个seeMore按钮添加点击事件：添加`show-detail`类到carousel。
- 为back按钮添加点击事件：删除`show-detail`类。

### showSlider函数（核心逻辑）
```javascript
function showSlider(type) {
    // 防止连续点击：禁用按钮2秒
    nextBtn.style.pointerEvents = 'none';
    prevBtn.style.pointerEvents = 'none';
    let unacceptClick = setTimeout(() => {
        nextBtn.style.pointerEvents = 'auto';
        prevBtn.style.pointerEvents = 'auto';
    }, 2000);
    // 清除之前的类
    carousel.classList.remove('next', 'previous');

    if (type === 'next') {
        // 移动第一个item到列表末尾，实现无限循环
        list.appendChild(items[0]);
        carousel.classList.add('next'); // 触发CSS动画
    } else if (type === 'previous') {
        // 移动最后一个item到列表开头
        list.prepend(items[items.length - 1]);
        carousel.classList.add('previous'); // 触发CSS动画
    }
}
```
- 点击next/prev时，传递类型参数（"next"或"previous"）。
- 使用`appendChild`和`prepend`移动DOM元素，不创建新元素，实现无限循环。
- 添加类（如`next`）到carousel，以触发对应的CSS动画（如位置变化动画）。

### 详细内容切换
- seeMore按钮点击事件：`carousel.classList.add('show-detail');`
- back按钮点击事件：`carousel.classList.remove('show-detail');`

## 实操步骤总结
1. **创建文件结构**：建立HTML、CSS、JavaScript文件。
2. **编写HTML**：构建头部、轮播图容器、包含5个项目的列表、箭头按钮。
3. **定义CSS样式**：设置全局字体、头部布局、轮播图定位、项目样式（使用绝对定位和变换）、定义CSS变量、创建动画关键帧、添加响应式媒体查询。
4. **编写JavaScript逻辑**：获取元素、添加事件监听器、实现`showSlider`函数处理滑动、处理详细内容切换、加入防连续点击机制。
5. **测试与优化**：在浏览器中测试滑动效果、动画流畅性、响应式布局，调整细节如动画延迟、模糊程度等。

## 总结
本视频详细讲解了如何使用HTML、CSS和JavaScript创建一个视觉印象深刻的旋转滑块模糊效果轮播图。核心要点包括：通过绝对定位和CSS变换精确控制项目位置；利用滤镜（blur）和透明度实现模糊与淡入淡出效果；运用CSS动画和JavaScript事件处理实现平滑过渡与无限循环滑动；以及通过响应式设计确保跨设备兼容性。整个项目强调动画的序列效果（如内容逐步显示）和用户交互的流畅性，适合前端开发者学习高级UI动画和交互实现。

---

## 原始字幕

i know youhi everybodywelcome everyone back to loon devs youtube channelin front of the screen is a slider with strange effectsat a glance everything in this design is quite simplehowever the smooth transition slider effect will make up for everythingIn the default state, the slider consists of three main components.Short Introduction,Image, and Navigation Buttons.The items are arranged in a row, they will fade and disappear.The special effect will appear as soon as we press the Next or Previous button.When pressing Next or Previous button, the images will move,the corresponding content of the sliders will also be displayed accordingly.Combined with Filter,Blur creates an extremely smooth feeling.You can press next or previous forever and never run out of sliders because it creates an infinite loop.When the user clicks the see more button,Other items will be pushed off the screen.To give up all the space for the currently active item,This will display more detailed content related to the product.If you want to return to the original state,Just click the back button.And that is our slider design using HTML, CSS and JavaScript in this video.if you find it interesting don't forget to like and subscribe to the channel to follow many good ideas and codes for free thank you very much here i have prepared some images to make this sliderall of these images are backgroundless images do not worry if you are having satisfactory photos but have a background visit the remove bg website then drop your photo here after just two secondsit will help you remove the backgroundnow i will create three files html css and javascriptin html i will format the code according to html5then embed the css and javascript paths hereand this is my websitebefore creating slidersi will spend some time creating the website headerheader will consist of two partslogo and nav因為現在的粉狀是很不好的所以我會去Google Fonts找到另一個粉狀我會選擇的粉狀是叫Poppins這裡,你可選擇的選擇你會選擇,或你可選擇全部的選擇然後選擇選擇選擇這個粉狀,選擇這個粉狀,選擇這個粉狀在開始的 CSS file現在在BodyI just declare font family,poppins.And it worked.Margin.0 to remove the margin.With link tags.I use text decoration.None,to remove the bottom lines and give the text a dark color.Header.I want the default width when accessing on devices with large screens to be 1140 pixels.For smaller screens,it will be 90% of that screen size.Margin.Auto,to put the header in the middle.Height.50pxUse DisplayFlex to put two elements on the same rowAnd with Justify ContentSpace betweenThe elements will be moved to both sidesAlign ItemsCenter to Center according to heightWith LogoI want the font to be bolder to make it stand outAs for the Nav elementsUse Margin Left30px to space themBecause the focus of this article is the sliderWe only need two minutes for the headerthe remaining time is for the sliderto create a complete carouselit will include the following elementsthe first element is listthe list will contain many items for the slidereach item will include three main elementsimage,introductionthis is the default information that will appear with the item when it is activatedand finally the detailed contentthis will be hidden informationit will only appear when the user clicks on the see more button to see more content about that product that product so now proceed to code according to this diagram i created a class called carousel that will contain the entire content of the slider in the carousel there will be a class list the list class will contain many items each item will consist of three elements image intro in the intro i will create brief content such as title topic short description and a see more button when the user clicks on this see more button the screen will display the content of the detail class in detail i will also create some more detailed content such as title detailed description technical specifications and to add to cart or checkout now buttons this is just sample information you can completely replace it with other information you want这就是一个组织的组织,你会看到一个组织的组织,现在我会有五个组织的组织,而且因为每个组织的组织,有三个组织,画面,进入,进入,进入,所以我会把它们加上更快,然后我会把它们加上更多织织,我会把它们加上更多织织织,然后我会把它们加上更多织织织,i want to create are the arrows includes next button previous button and back button this back button will be used to help users viewing the details content return to its original stateto help users viewing the details content returned to its original stateSo let's proceed with the codeI created a class arrowsInside there are three buttons with its nextprevious and backand this is the entire content of the HTML we will be working withCSS SideAt the carouselI want the carousel to be pushed up to the top of the screenbut this area already belongs to the headerso you'll notice that the header height is 50 pixelsso in the carousel we declare margin top minus 50 pixelsand so the carousel is located right on the screenhowever now our logo is hidden because the carousel is over ituse position combined with Z index to help the header overlap the carouselthe rule is that the element with the larger Z index will be placed on top of the other elementElements that do not declare Z-Index will be interpreted as 0.Height.800px.Overflow.Hidden, so that content longer than 800 pixels will be cut off.Position.Relative so that the elements inside can be positioned according to it. So let's go to the list class.Position.Absolute to move it according to position.Relative of the carousel class. The top and left distance of the carousel is 0. width 1140px max width 90% unlike header to put the element in the middle we use margin auto then for elements that declare position absolute to put it in between we have to use it left 50% and transform translate by minus 50% combined finally the height of the list will be 80% of the carousel coming to the item classesI again use position.absolute to move it to a position 0 from the top and left of the list class.Width.70% and height.100% of the size of the list class.The default font size is 15 pixels.The image within each item will be half the size of the item.Use position to move it to the right.To bring the image into the middle of the frame vertically i use top 50 and transformtranslate y-50 in initial state all content in the detail class will be hidden i will use opacity0 because the purpose of opacity is to make everything blurry but it doesn't really disappear so combine it with pointer events none to make the mouse pointer never touch itwith introthis is the content that will appear on the screen in the default state when details are not displayeduse positionabsolutetop50%transformtranslate y-50% to center the class according to heightalong with width400pixelsbefore continuing to codelet's sketch out this design togetherto make it easier to visualize and help code fasterthis red border will represent the frame of a carousele circle inside will represent one itemthe first item will be placed right on the left border of the carouselthe second item is arranged right next to itthe third item will be placed immediately after the second item and will be smaller in sizethe fourth item will be placed right on the right edge of the carousel and will be smaller in sizeand finally i have the fifth item the smallest and placed outside the carousel classI will number them to make it easier to seeLooking at this design, we will easily realize that the item in the second position is a large item and is completely located in the frameThen I will take this second item as the active item positionSo now we go back to the codeAll intro content of other items must be hiddenOnly information about the currently active item is displayedAnd it is the second itemTo display it, I will use opacity1 note that when hidden we used pointer events none so that the user cannot manipulate it then when it shows up must use pointer events auto so users can manipulate it to make each hiding and appearing smoother i declare transition opacity 0.5s to specify the opacity value change time as 0.5s let's look at this sketch again on the screen in this range there are only five items that means the sixth item onwards will be temporarily hidden so we have the items are at position n plus six they will all be hidden with opacity zero and pointer events none don't be mistaken no matter how many items there are the slider will work well because it will continuously take turns becoming an active item when the user clicks the next button our next problem is determining the position of the first five items on the screen因為第二項是一個空間的空間所以我會把位置的位置的位置先我會用 Excel記錄一下這些位置先它不是很重要的它是幫助我記錄一下我會用的Transform to moveFilter to blurZ-Index to determine哪個空間是在哪個空間然後Opacity to specify哪個空間是遍的或是遍的現在Code��터wn ignore some modecansform存放astrozenaccop男人感醒一个操作on reckthis père他 AGaru shirtsNext is the location for the first itemUse transform to move it 100% left, 5% up, and enlarge it 1.5xBecause it is not an active itemUse filterBlur 30 pixels to blur itI want it to overlap the activated itemSo its Z index must be greater than the second itemIf you want to hide it always,Set opacity 0and don't forget that elements declaring opacity 0 should be used with pointer events none to ensure users cannot manipulate itI will continue to record this data to make it easier to rememberSimilarly I will continue calculating for the position of the third itemIt will move to the right 50% and bottom 10%Shrink it to 0.8 times its original sizeBlur to make it look a bit blurryZ index will be smaller than the active itemand opacity1 because I still want it to be visible on the screennow the fourth itemit will move to the right 90% and bottom 20%shrink it to 0.4 times its original sizeblur to make it look blurrieropacty1 and Z index finally the fifth item this item will have to be farther away and smaller than the fourth item blur to make it look blurrier and use opacity zero to hide it and this is the entire position for the items in the slider the reason i have to record these changes is because the slider is active our items will constantly change positions and have to reuse these values many timesthe solution here is instead of rewriting these values many timesI will create global variablesglobal variables will be declared in the root sectionnormally the root location is after the bodyI proceed to declare global variables related to the item in position 1such as transform, filter, z-index and opacitycorresponds to each value we found when bouncing after creating global variables related to the item in position 1 so here i don't need to write its value directly instead i use the var function and call the corresponding global variable and it still works fine likewise i will create global variables related to items 2 3 4 and 5arım mouthsi  replaced them with the corresponding items所以從現在開始,每次需要用資料 related to the location of these items,我只要叫做合格的標準,現在是時候設定的測試按鈕,Position,Absolute to move the Position,Bottom,10px,Width,1140px,Max Width,90%, Use left 50% and transform translate x minus 50% to center the component. Use display flex to align content inside justify content space between to arrange buttons evenly to the sides. Align items center to ensure the buttons are on the same level. Next are two buttons previous and next because it is an id there will be a hash sign in front of it. width and height are 40 pixels to form a square border radius 50% to convert to circle font family monospace font size large font weight bold and the one pixel border is dark back button font family poppins font weight 500 delete the original border and replace it with a bottom borderLetter spacing is the spacing of lettersBackground colorTransparentits use is to click to switch from the slider state to view detailed content to the original stateSo in its original state, it will be hiddenOpacity0Pointer eventsNoneThe final step before processing JavaScriptThat is the redesign of the intro's contentThe title of the intro will be 2M in sizeBecause the item has a default font size of 15 pixelsso 2m will be 15 times 2 equals 30 pixelssimilarlytopic will be 4mfont weight500use line height to reduce the spacing of the linesfor short descriptionI will make the size smallerand finally the see more buttonbackground colortransparentdelete the default border and replace it with a bottom borderfontfamilypoppinsfontweightboldmargin top1.2 empadding top and bottom 5 pixelsand that's the shape for the class intro framenext is the part that creates the animation effect when it is activatedall components inside the intro includetitletopicshort descriptionsee more buttonit is temporarily hidden with opacity0it then runs an animation called show content to appear This animation will run within 0.5 seconds and will be delayed 1 second before running. Animation show content specifically works as follows. Initial. Content is moved 50 pixels down. And blurred with blur. When running animation. It started to return to its original position. Blur and opacity values are 0 for visibility. It doesn't stop there. I want to create a more dramatic effect by delaying the content behind it.if the title will be delayed 0.7 seconds before running the animationthen the following components will have a longer delayspecificallytopic will be delayed 0.9 secondsdescription will be delayed 1.1 secondsthe see more button will be delayed 1.3 secondsand this is exactly the effect i expectednow we will move on to javascript to workthe first thing to do is recall the html components we needthe first is the next button since it is an ID use get element by ID the previous button and back button are the samethe see more button is a special case because it is a class we will use query selectorand each item has a button so it has a lot of these buttonsso let's add the word allCarousel has only one so it will be query selectorListHTML is where the items are stored. And we only have one list class. When the user clicks on the next or previous button. Both of them run the same function. In this function it will call another function named show slider. To distinguish which button was clicked. Then the show slider of the next button will be passed into a type variable with the value next. The opposite is previous. Proceed with the function show slider.where type is the value the user passes inthe first thing i will do is get the list of all the items in the slider here to processif the user clicks on the next buttonthen our slider will move from right to lefti.e. the item in position 5 will go to position 4the fourth item will move to the third positionthe third item will move to position 2the second item will move to the first positionand the first item will move to the last position remember it creates an infinite loop so the key here is that we just need to move the first item to the last position the remaining positions will be moved accordingly so when the user presses next I use the following function append child with the input value being item 0 item 0 is the item in the first position append child is the function that moves the item to the end of the row and listHTML is the class containing all items everyone can see that the active item has changed if you are wondering using append child will cause the code to create more items rather than move them then look here here I have 6 items when done click next there are no new items added the location of the moved items however, it does not create a nice transition effect to create that when the user clicks the next buttonI added a next class to the carousel class to signal that I should create an effect for the next activeAnd the problem of creating effects is CSSIs it true that when the user presses the next button, the items will be moved to the left?So the first item originates from the item in position 2RightSo in the first itemI let it run an animation called position item 2 within 0.5 secondsanimationPositionItem2 has the value in from which is the initial value of a normal second itemthanks to that, it will create an effect that moves from position 2 to the first positionand it workedsimilarly, the third item will move to the position of the second itemso in the second itemcall an animation named PositionItem3 within 0.7 secondsthis animation will have the initial value which is the position of the third itemthanks to that it will create a moving effect for the second itemthe third item will move to the position of the fourth itemso in item 4call an animation named position item 4 within 0.9sthis animation will have an initial value that is the position of the fourth item thanks to that it will create a moving effect for the third item finally the fourth item will move from the position of the fifth item so in item 4 call an animation named position item 5 within 0.9 s this animation will have an initial value that is the position of the fifth item thanks to that it will create a moving effect for the fourth itemwhy is there still one undone item that is the fifth item but i said the fourth item is the last itembecause in principle the last item will be moved from the first itemand both of these positions have opacityzerowe can't see it so there's no need to do itnow when i proceed click on next buttonthe effect i expected has come trueso that's the event when the user clicks the next buttonnow there will be an event when the user clicks on the previous buttonbecause there is a next event as a sampleso the process of making this previous button will be much fasterwhen the user presses previouscontrast with nextslider tends to move to the rightitem1 will go to position2itemposition2 will increase to 3and so on until the last itemthis last item will be moved to the first position to form an infinite loopso let's proceed with the codewhen the user presses the previous buttonwe have position last which is the position of the last itemuse prepend to move it up to the first positionalong with thatadd a class named previous to the carousel to signal and create effects for the previous button click eventin csswhen the user presses the previous button1. Then the first item will move to the second item position. So in the second item, I run an animation called position item 1 for 0.5 seconds. Animation position item 1 has the initial value which is the default position of the first item. Thanks to that, it creates an effect of moving from the first position to the second position. The third item will be moved from the position of the second item, which is the animation, position ite独 equipped從第一個位置to second bigthe third itemv LED moved from the positionof the second itemwhich is the animationposition item 2similarlythe fourth itemvêtredocthe fifth itemwill be movedfrom the positionof the fourth itemI run an animationposition item 4we created theseanimationswhile makingthe next active effectsowe just reuse itand it worked however, please pay attention to this case when the user just presses the next button and then presses the previous button then our animation runs haphazardly that's because now in the carousel class there is both next and previous makes it not know which event to run the animation on to fix this, when running function shows slider let's delete all the previous next and previous classesI don't want the user to click the next and previous buttons continuouslySo at the beginning of the function show sliderI set the pointer event of these two buttons to noneAt this point, the user will not be able to click againI continue to create a variable unaccept click to specify the time for the user to click againUse setTimeout for regulationAfter 2 seconds, I will click the next button set timeout for regulation after two seconds the pointer event of these two buttons is auto so they can be clicked again normally use clear timeout to ensure the time restarts from the beginning when the animation runs next when the user clicks the see more button i need to display detailed content instead of intro because there are many see more buttonsso I need to use a loop.When the user clicks on any button,I proceed to add the show detail class to the carousel.At CSS,When capturing the show detail event,I will move the position of the third and fourth item off the screen with left,100% to make room for the active item.To create smoother transitions,then all items will have an additional transition left of 0.5 seconds.It will then be hidden.the opacity transition will also be 0.5 secondsin this statethe width of the second item will be enlarged by 100 percentthe intro content is hiddenthe image will be shifted 50 percent to the rightto create a smoother moving effecti will declare transitionright 0.5 secondsfinally the content of the detail will be displayedremember to add pointer eventsauto so users can operate it width 50% position absolute to change position right 0 text align right top 50% transform translate y-50% title of detail will have font size 4m the specifications use flex to make elements stay in the same row10px is the distance of the elements100%1px solid number 5555and margin top 20pxfor each div inside specificationsall have width 90pxtext align centerlex shrink 0 to fix this sizethe first p tag will have bold font to stand out with buttons inside the checkout class font family poppins background color transparent border dark margin left 5 pixels font weight 500 the second button will be distinguished by its blue color and that is the frame of detail next i need to create a more beautiful effect reuse the animation show content of the intro so nowAll classes insideDetail will also call animationShowContentto create a smoother effectThen the following components will add a delay value so that it runs the animation slower than the previous componentsWhen the carousel is in this stateI will hide the next button and the previous buttonand instead the back button will appear when the user clicks on the back buttonI will delete the show detail class in the carousel to return the slider to its original stateIt worked very well this slider is now workingHowever the background is too simple I will use beforeBefore is a virtual element generated right inside the carouselit will have width500 pixelsheight300 pixelsthe content attribute must be declared for this component to appearuse background linear gradient to create a multicolored backgroundpositionabsolute to move the positionzindex-1 to ensure it does not overlap any website contentborder radiusI choose 4 random numbers to create random curvesfilterblur to create a blur effecttop 50%left 50%transformtranslate-10%-50%transition1 secondwhen the carousel falls into the show detail stateI will use transform to move its position while also rotating its 70 degAnd that is the slider interface with animation effects that I want to aim for.We will spend the remaining few minutes implementing responsiveness.On the iPad screen,I will enlarge the width of the item to 90%.The initial default is 70%.Specifications are also having problems because the content is too long.I just added overflow.Auto so it creates a scroll bar.We come to the mobile screen.With each item, width will be 100%.The font will shrink to 10 pixels.The height of the carousel class will be 600 pixels.List will have a height equal to 100%.the intro class will have width 50%the size of the image will be reduced to 40%title font size is 2mbecause the content in the diaper is too longI will limit the height to 100 pixelswith overflowautoif the content is longera scrollbar will appearfinallythere are two checkout buttonsdisplayflex so it never goes down the line Width. Max Content. Float. Right. And this is the entire content for today's video project. If you find it interesting, don't forget to like to support me and subscribe to the channel to follow many new videos every day.and if you have any problems or ideas you want to shareplease leave a comment to share with methanks everyonesee you again in the next video