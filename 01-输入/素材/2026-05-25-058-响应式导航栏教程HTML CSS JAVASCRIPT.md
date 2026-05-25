---
title: "响应式导航栏教程HTML CSS JAVASCRIPT"
author: "流浪字节"
source: https://www.bilibili.com/video/BV1AG4y1X7Su
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - 前端开发
  - HTML
  - CSS
  - JavaScript
  - 响应式设计
  - UI动画
type: video-note
bvid: BV1AG4y1X7Su
duration: "35:04"
cover: "http://i0.hdslb.com/bfs/archive/a72b9e3fbc83bf1ff71a82094004e83d514ea36c.jpg"
description: "https://www.youtube.com/watch?v=vQWlgd7hV4A&amp;list=PLDyQo7g0_nsU2O7gEdh7cAgamyh0xZumZ"
---

# 响应式导航栏教程HTML CSS JAVASCRIPT

> [流浪字节](https://space.bilibili.com/122439591) | [BV1AG4y1X7Su](https://www.bilibili.com/video/BV1AG4y1X7Su) | 时长 35:04

## 响应式导航栏构建教程笔记

### 1. 项目概述与最终效果
- **目标**：构建一个现代化、可定制的响应式导航栏。
- **桌面端**：水平排列的导航链接。
- **移动端**：一个汉堡菜单按钮，点击后导航链接以动画形式逐个滑入屏幕。
- **核心优势**：
    - 高度可定制：可轻松调整动画延迟、速度、样式等。
    - 自动化：添加新链接时，动画会自动适配，无需手动修改延迟。

### 2. 环境准备与基础设置
1.  **创建项目**：新建一个项目文件夹，命名为 `navigation`（小写）。
2.  **基础文件**：创建 `index.html` 和 `style.css` 文件。
3.  **基础CSS重置**：在样式文件开头进行基础设置。
    ```css
    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }
    ```
4.  **引入字体**：使用 Google Fonts 的 **Poppins** 字体。

### 3. HTML 结构搭建
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Navigation</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <div class="logo">
            <h4>The Nav</h4>
        </div>
        <ul class="nav-links">
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Work</a></li>
            <li><a href="#">Projects</a></li>
        </ul>
        <div class="burger">
            <div class="line1"></div>
            <div class="line2"></div>
            <div class="line3"></div>
        </div>
    </nav>
    <script src="app.js"></script>
</body>
</html>
```
**关键点**：
- `<nav>` 作为主导航容器。
- 使用无序列表 `<ul>` 和列表项 `<li>` 包裹导航链接。
- 为移动端创建了一个 `.burger` 容器，内含三个空 `<div>` 用于模拟汉堡菜单的三根线条。

### 4. CSS 样式详解
#### 4.1 桌面端基础样式
```css
body {
    font-family: 'Poppins', sans-serif;
    background-color: #222;
    color: #eee;
}
nav {
    display: flex;
    justify-content: space-around;
    align-items: center;
    min-height: 8vh;
    background-color: #5d4954;
}
.logo {
    color: rgb(226, 226, 226);
    text-transform: uppercase;
    letter-spacing: 5px;
    font-size: 20px;
}
.nav-links {
    display: flex;
    justify-content: space-around;
    width: 30%;
}
.nav-links li {
    list-style: none;
}
.nav-links a {
    color: rgb(226, 226, 226);
    text-decoration: none;
    letter-spacing: 3px;
    font-weight: bold;
    font-size: 14px;
}
```
**关键点**：
- `nav` 使用 `flex` 布局，`justify-content: space-around` 实现链接均匀分布。
- 通过 `letter-spacing`、`text-transform: uppercase` 等属性美化文本。

#### 4.2 移动端样式 (响应式部分)
1.  **隐藏导航链接**：
    ```css
    .nav-links {
        position: absolute;
        right: 0px;
        height: 92vh;
        top: 8vh;
        background-color: #5d4954;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 50%;
        transform: translateX(100%);
        transition: transform 0.5s ease-in;
    }
    ```
    - 使用 `position: absolute` 将导航定位。
    - `transform: translateX(100%)` 将整个导航移出屏幕右侧，实现初始隐藏。

2.  **设置导航链接初始透明度**：
    ```css
    .nav-links li {
        opacity: 0;
    }
    ```

3.  **显示汉堡菜单按钮**：
    ```css
    .burger {
        display: block;
        cursor: pointer;
    }
    .burger div {
        width: 25px;
        height: 3px;
        background-color: rgb(226, 226, 226);
        margin: 5px;
        transition: all 0.3s ease;
    }
    ```
    - 在移动端显示汉堡按钮（默认隐藏）。
    - 设置汉堡线条的尺寸和间距。

4.  **创建动画**：
    ```css
    @keyframes navLinkFade {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0px);
        }
    }
    ```
    - 定义一个名为 `navLinkFade` 的动画，用于导航链接的淡入和滑动效果。

5.  **添加激活状态样式（通过JS切换类名）**：
    ```css
    .nav-active {
        transform: translateX(0%);
    }
    .toggle .line1 {
        transform: rotate(-45deg) translate(-5px, 6px);
    }
    .toggle .line2 {
        opacity: 0;
    }
    .toggle .line3 {
        transform: rotate(45deg) translate(-5px, -6px);
    }
    ```
    - `.nav-active`：将导航从屏幕外移回视图内。
    - `.toggle`：将汉堡菜单的三根线条变换为关闭按钮（X形）。

6.  **使用媒体查询**（教程中隐含，需自行添加以实现真正的响应式）：
    - 在屏幕宽度大于某个阈值时（如768px），应隐藏 `.burger` 并显示 `.nav-links`。

### 5. JavaScript 交互逻辑 (`app.js`)
```javascript
const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click', () => {
        // 1. 切换导航栏的显示/隐藏
        nav.classList.toggle('nav-active');

        // 2. 动画导航链接
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7}s`;
            }
        });

        // 3. 汉堡菜单动画
        burger.classList.toggle('toggle');
    });
};

navSlide();
```
**关键逻辑解释**：
1.  **获取元素**：获取汉堡按钮(`burger`)、导航容器(`nav`)和所有导航链接(`navLinks`)。
2.  **点击事件监听**：
    - **切换类名**：使用 `classList.toggle('nav-active')` 切换导航的显示状态。
    - **链接动画**：遍历每个链接(`navLinks`)，使用模板字符串和索引(`index`)为每个链接设置**不同的动画延迟**(`index / 7s`)，实现逐个出现的效果。
    - **汉堡动画**：使用 `classList.toggle('toggle')` 切换汉堡菜单的线条变换样式，实现打开/关闭动画。

### 6. 总结
本教程的核心是通过HTML构建基础结构，使用CSS Flexbox和Transform属性创建响应式布局与动画，并结合JavaScript的DOM操作和事件监听来实现交互。关键技巧在于：利用CSS的`transform`属性移动导航栏实现显示/隐藏，通过`@keyframes`定义动画，并由JavaScript根据列表项索引动态计算延迟时间，实现链接的依次淡入滑动效果。这种模式具有良好的可扩展性和可定制性，只需修改CSS变量或JavaScript中的计算参数即可调整动画表现。

---

## 原始字幕

Hello what's up everyoneOK finally back after like 3 weeksOh my god it's ok though'cause we are going to build a navigationin a pretty modern wayand I'm gonna show you a few tricksthat you can do some cool animations in JavaScriptSo we're gonna build a simple navigationand we're gonna also have a mobile versionAhh I just spoiled everything thereNo!OK anywaysSo on mobile it's gonna be like thisright and when you click we're gonna have this nice animation here and all the links are gonna nicely animate in like this and this is super customizable so you can make uh like the delay stronger or faster or slower and very very easy and like the animation here you can easily change it in css so we're gonna do one cool trick here in javascript that's gonna be enable us to do this好, more含小跟密語好,我先先前面,KAn unPPy我先 expand我先进去我先看到要去 we're gonna start obviously with our index.html we're gonna generate a new project we're gonna name this navigation okay with the lowercase n and yeah let's get started okay so we're gonna say nat we're gonna use html5 uh and we're gonna see we're gonna build a div with a class of logo here来钱吧��叫做DNavoriginal除了这个我们继续emosaUL我的LIListOk carries вполне进适 밀务你能ários真的突出很遠我们将来先用 likes and our project perfect good and for now i think we we are done with this so let's open this up in live server and the port is already in use so let me close that there we go okay i'm gonna put this here其實, I'll just maximize this for now because we still need to add our style.css we're gonna link it we're gonna say style and I'm gonna remove some basic things here我們會選擇的 padding我們會選擇 box size border box就讓我們不去一些問題OK那是現在我們開始了這個 nav所以哇我按OK我們可以選擇所有的基本 stylesand we can start so we're gonna say nav right we're gonna say display flex so all our so it comes like next to each other and then we're gonna say justify content space around so now it's gonna be like this we're also gonna say align items center which is gonna center it wurde Fr váy到Desp Merci underwater它 Komドを center4954I believeYeah okay it's that oneI think we're gonna remove this for nowJust so we can see what we're doingAnd we're gonna add this back later okayAnd I believe we also are using aWe go on Google FontsI usedPoppinsPoppinsI said hey man let me useLet me use something differentI'm using Montserrat and railway too often so I thought I'd switch it up try something new my lifegood so we just copy and paste this and then get the pop-ins go back to this and we're just gonna我們現在對方改造 vraiment成功的我們現在還是機iałem沒有拿出來就這麼 weit我們來 cambio我們選擇Vlog wäre一 type我還選擇I'm gonna go here just lower down a bit because you don't want to have that huge contrastit's not going to look that good if it's pure white so I'm just lowering that down and I also did text transform here and uppercase so all our text is uppercase we're gonna say letter spacing5pxit does exactlywhat it saysit just makes a bit of space in between each letterand let's add a font size of 22pxgood awesomemaybe20alright let's go with 20goodnow for our ul herewe're gonna add a class of nav links herealright我们现在再来返回我忘了再加这个我先说准备连续然后再来返回我们再来返回所以我们再来返回我们再来返回我们再来返回因为现在我现在再来返回如果我加上白色那是白色现在狗狗狗 写ало 也很有型假定就是탁ники召集結合假定沒有障礙放對 gew Blade卻则 máquina DesignPlus更多、更削減,比以风异Get, allen mét拨氏很好就要猜測 UniInA,这只有中国 rot我们将向 wack等等 görev青吉他我们将同系列为 Canada我们将黑色走 encourageWeinA, hit the same same lines just so were constant第一個部分 is add also an Sell好�ipped RIGHT MUCH BETTER GOOD GOOD GOOD ALRIGHT WE ALSO NEED TO REMOVE SO WE ska there we go awesome good good goodalright so that's it for our desktop view quite simple yeah not much not much nothing interestingokay so the way I build my my nav for the mobile is I basically do this and then in my navI'm gonna add a burger class hereso I'm gonna say burgerlike thatI'm gonna add three divs hereonetwothreelike you can do it with SVGsbut you can do it so fast with thisthat I kinda prefer this onesothe burger has like three lines rightso I'm gonna name them line oneline oneI'm actually gonna just copy thisand we're gonna say line twoLineTreeAndYeahThat's itThat's the whole thingGoodSo now if we go backIt's gonna be hereNow we're gonna be like hey but this kinda ruins our layoutWellNot really cause we're gonna display it noneSo it's only gonna appear in our mobile viewSo now hereWe're gonna say BurgerLike this其實我們不需要 display none因為我們不見 anything因為我們的 divs are empty這些 are empty所以我們要選擇Burger我們要選擇所有的 divs in here因為他們都會同樣的我們要給一個 width of 25px一個 height of 5px你可以玩玩這些如果不喜歡這就是我們要來這個thiscolor again just so we're consistent here good i'm gonna add a margin so it has a bit of spacing all right it's not working let's see why is it not working burger div div class burger div部分 misoks人根本不易 heaven souven你看孵我只不...ok所以它不是一个项目,它是一个项目的项目有我们的项目哇,那看起来那看起来很项目让我们再加上3个项目啊,有我们的项目你可以玩到这些项目你可以做2个项目如果你觉得它是太大那是什么...ok你留下3好好了有几次并出坏对rrre看 blank也不要 there we go and just to test it out we're gonna say body display none i always do this it's a habit okay so maybe the width can be bigger here so before it hits the break point you can maybe increase the width right you can go like 40 until it looks good so you can mess around with that直接做好就是它 doright here或者你能forward你可以做多95低朋友如果你想如果你想这样的 sair走..!要地不 cockpit等 Burn here但妳可是再回去要寻一些例えば几千丧被DD rogueuses the width of this so it's going to look nicer it's going to look more spaced out about this you can see what i'm saying just so just a quick fix here just so its going to look ok so i'm just going to take navlinks here and for this in particular imI'm just going to equal the width to 50?60?let's seeyeah! lighting it looks ok acrossyeah just play around with thatI want to cover mobile tässä是像귀好混合。好,囤子我們要完成 ,先看看這邊,I'm going to say position absolutewow okay there we goand we're going to sayI'm going to put it right zero pixelsso it's stuck here on the right sideI'm going to add a height oflet's see how much height I added hereI believe it's 8vhso to be full screenI'm going to say 92vhlike thatbut that's going to give us full screen Good and also we're gonna say top A to VH so it's gonna be right under our nav bar good We're also gonna copy the background here So let's copy this background to see what it actually looks like Good looks like that perfect and now all we need to do is display flex We're gonna say flex direction就是这样的所以它就像这样就是这样的就是这样的就是这样的因为我们改变因为我们改变所以我们改变所以我们改变所以我们改变有点所以我们有一个很大好 simplicity oke,全部 we can do is transform translates x 100% which is basically going to move this whole container off the screen and perfectly it's going to move it off the screen so it's here now we don't want this to scroll so all we do is body and we're going to say overflow x hidden there we go we cannot scroll anymore good awesome let's see we're gonna say we also want to make the let me just remove this for a second the original state of these is gonna be hidden so we're gonna say opacity zero and when we click on the burger it's gonna fade in nicely so start we're going to just say nav links li and we're going to say opacity 0 okay so what that does basically we cannot see anything goodAnd also let's put this backoverflowX to hiddenAnd the last step isget that burger and just say display blockSo we took it from display hidden2DisplayBlock on mobileand look at that nicely positioned and everything this is centered here and boom remember because it's still in the context of the nav which we added display flex so it's still going to have the nicely spaced around burger so there you go awesome another thing we can do is maybe add a cursor to thisCursorPointerSo boom there we goGreatAlrightLet'sLet'sWe still have like one or two things to do hereSo I'm thinking if we should do the JavaScript or notOkayWell let's think in CSS for a momentWhen we click on this burgerWe want the navigation to showSo the only thing we need to do is basically直接把这个 transform 把这个转移到0所以要做这个是 我们来到这个 bottom按下 navactive我们来说 transform translate x back to 0所以我们按这个转移动这个转移动转移动转移动那是它基本上有什么东西這也對 a transact好, awesome alright, let's leave it at that for now and then we're going to get to the other ones ok so I want you to create a app.js or name it whatever you want at the end of your html we're going to add it good now what we're going to do is make a function so we're going to say const nav slide就是同行的Aanonymous function Awesome Here we're going to declare We're going to get the burger And we're going to get the slider So we're going to say burger is equal to document.querySelector And we're going to say burger Good And we also want to get thethe nav which is document.querySelectorNavLinks awesomeso what we gonna happen is when we click on the burgerwe want the nav link to get the class of navactiveso let's do thatso we're gonna see navburgeraddEventListeneronClickwe want to run a functionand what we want to happen isthe nav shouldget a classlistso we're going to say classlistand we're going to saynot addbut toggleand we're going to toggle the classlistofNavActivelet's see how that worksand it doesn't workOK, why?Because we need to invoke this functionSo nav slideNow if youNow if you're going to have multiple functionsI'd recommend actually building a app functionHere and you can callAll your smaller functions hereJust to keep it cleanerBut for now I'm just going to do like thisso we're gonna invoke this functionso now if we clickthis slides in nicelygoodnow the problem ishow are we gonna animatethese in one by onewellfirst we need to makean animationso let's build out an animationwe're gonna go down herewe're gonna say addKeyframes and we're going to say nav link fade okay from and to so obviously we want from opacity 0 to 1 and also I actually want to add a little movement to this I'm going to say 50 pixels and it's going to go from 50 pixels0px它是在那裡的樣子好現在我們要加這個我們要加這個我們要加所有的 navlinks所以我們要加這個我們要加這個我們要加這個ConstNavLinks這些都是各種類似的這個,這個,這個,這個,這個我們說Document.QueryselectorQueryselectorAll我們說NavLinksLi這樣good so this is gonna be the toggle nav animate links just to be clear now the cool thing here is we can do this we can say nav links dot for each so for each link we're gonna run a function hereand also the cool thing here isso these are the individual links rightyou also have access to indexwhich if we console log this is just going to bring backthe individual like how many how many links we haveso in this case we have one two three one two three four rightbecause we have four here1,2,3,4 awesome now why do we want the index? well this way you can actually easily animate the the delay between each so let me just quickly show you so if I say here link.style.animation equal to we're gonna do backticks here and say nav link fade okay the animation we did0.5 seconds is going to last for ease four words and I'm going to interpolate it here with index and I'm going to divide this by 7 or by 5 so what does this mean? let's see and we're going to say seconds here so this would be the delay I'm going to console log this for you to see so if we say console logindex divided by 7 it's gonna give usf12 it's gonna give us a nice wow, what was that noise? a nice delay between each and it's gonna be equal so it's gonna look really smooth and it's really niceand the awesome thing is you can easily add more your if you have a designer or someone you can easily add more links here it's going to automatically recognize it it's going to add it it's你能夠再加多,如果有一個人的設計你能夠再加多多的連接它會自然的確認,它會自然的確定它會自然的確定然後,它就能夠再加多的連接它就能夠再加多的連接看,我可以再加多然後, boom很高的連接每個連接你能夠再加多的連接所以我可以做到0.5的動作, 它就能夠做到0.5的動作如果你想要有1.2的動作, 它就能夠做到0.2的動作所以它開始了一開始我相信我做了這個在我的最新的所以我們說0.3所以我們加了一個基本的時間 Awesome我們看看,能否做到這個效果Refresh我們再加了一個比較時間我來看看這個效果 here we go it works now we have a bit of problem here the problem is let's see how much delay i need here let's go one second yeah so it fades in afterthe nav openslet's go 1.5 hereyeah something like thatnow the problem is this stays like thiswe don't want thatwe want it toif we close it we want it to happen againso to do that is quite easywe just copy thiswe're going to say iflink.style.animationso if this exists, if our links have animation on itthen we're gonna saylink.style.animation is gonna be equal to nothingelse we're gonna add our animation Boom Not working Alright, so I'm extremely stupidthe reason why this didn't work is we need to add it in the event listeneroh my godjust copy everything from hereand paste it in hereand move this in herejust to make everything clearughJesusgoodactually let's move this backalignsoah ok nevermind here is the first line let's see boom boom there we go last thing okay I also added a background here just I just did it so the page is not empty but the last thing we have to do is just change the burger so to do that是很簡單的,我們加上1,2,3我們現在就有一個Toggle class我們說Toggle,我們說Line1我們先來Copy this2,32, oh wait2,33GoodAnd for each line we want something differentSo for this one, the first one, the upper one hereWe're gonna say transform, rotateWe're gonna say minus 45 degreesAnd we're gonna say translateWe're gonna move this minus 5 pixelsAnd this is the xAnd 6 pixelson the ywe're gonna copy thispaste it hereand here we're just gonna say minus hereand here it's gonna be plus 45 degreesand for the middle onelet's just get rid of itand say opacity zeroawesomealrightso all we have to dois just toggle it in here所以我們要在這個我會在這個對,這裡BurgerAnimation好,所以我們要選這個所以我們在這個我們在這個我們要選這個我們要選這個我們要選這個well we want to add on the burger class list of toggle we're gonna say oh I named the toggle okay so we're gonna toggle the toggle class wow awesome good let's see oh that works the middle one these don't work為什麼會是這個問題?我們來看看所以基本上這些應該會有這個我們來看看這個來1來2來3我們來加上這個to the line 1 line 2 and line 3 so this effect should take place herewhat did I miss what did I misstransform rotate好, here's one problem, here's the second problem wait, what's going on here? there we go so, kinda messed up my spacing in there好, make sure it's okay but we also want to add a transition to these so it doesn't look so boring so let's add, I think I used, let's see how much I used I used a 0.3 ease on this so try to go and find your burger div here再加上0.3s的Easeand we should be doneSo there we goAwesome, okay so there we goLook at that, niceAnd the cool thing again is you can add another one of theseAnd you don't have to modify the delay or anythingIt's just gonna work magicallyLook at that, it's just gonna work你也可以把这个剪掉让我们去剪掉有点有点有点那是大家希望你喜欢这个影片我知道这个影片是长的所以我对不起但这一切是很好的很好的希望你喜欢这个影片然后订阅任何东西你也想看我还想要做一些设计的影片就是这种生活,就是这种生活,就是这种生活,就是这种生活,而且...是的,享受你的日子,它是热烈的这里,所以我会去休息一下,OK, Peace!