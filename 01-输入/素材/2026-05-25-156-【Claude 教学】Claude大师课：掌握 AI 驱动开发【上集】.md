---
title: "【Claude 教学】Claude大师课：掌握 AI 驱动开发【上集】"
author: ""
source: https://www.bilibili.com/video/BV1jJobBHE97
date: 2026-05-25
tags:
  - bilibili
  - 笔记
  - AI开发
  - Firebase
  - 工具使用
  - 前端开发
  - 版本控制
type: video-note
bvid: BV1jJobBHE97
duration: "0:00"
cover: ""
description: ""
---

# 【Claude 教学】Claude大师课：掌握 AI 驱动开发【上集】

> [](https://space.bilibili.com/) | [BV1jJobBHE97](https://www.bilibili.com/video/BV1jJobBHE97) | 时长 0:00

## Firebase项目设置和初始化笔记

### 1. 启用服务和下载SDK设置
- 设置Firebase项目后，需要启用两项核心服务：**认证**（Authentication）和**Firestore数据库**。
- 同时需要下载SDK设置代码，以便将前端应用连接到Firebase后端。
- 推荐使用Firebase服务器提供的斜杠命令（如`/firebase init`）自动化完成，而非手动从项目仪表板操作。

### 2. 使用斜杠命令初始化
- 输入`/firebase init`命令，该命令会：
  - 初始化所需的后端服务。
  - 下载前端SDK设置代码。
  - 自动配置前端以连接Firebase后端。
- 命令执行后会引导用户选择服务和配置选项。

### 3. 操作前准备：切换分支
- **重要建议**：在运行`firebase init`前，切换到新分支以确保安全，避免代码变更影响主分支。
- 实操步骤：
  - 使用`git switch -c firebase-setup`命令创建并切换到新分支`firebase-setup`。
- 这允许在出现问题时轻松回退。

### 4. 执行firebase init命令的详细步骤
#### 4.1 选择工具和服务
- 命令启动后，系统会询问是否允许使用工具（如`get Firebase environment info tool`），选择`yes`。
- 接着选择要启用的服务：**Cloud Firestore**和**Firebase Authentication**。
- 建议在配置时明确指定，以避免命令自动启用其他功能（如Firebase Hosting）。

#### 4.2 配置Firestore安全规则
- 部署Firestore安全规则时，选择**保持在测试模式**（test mode）。
- 测试模式规则允许读写访问数据，但仅限于指定日期（例如未来30天）。
- 规则文件内容示例：允许在请求时间早于某个日期前进行读写。
- 确认后，使用Firebase工具（通过npx命令）部署规则，完成数据库创建。

#### 4.3 设置认证
- 启用**密码认证**（email and password authentication）。
- **注意**：命令可能不会直接在Firebase控制台启用所有认证方法，但会提供指南，用户需手动在控制台设置其他方法（如社交登录）。
- 最终命令会指导在应用中实现认证，并添加Firebase Auth SDK。

### 5. 部署和配置结果
#### 5.1 生成的文件和配置
- `lib/firebase/config`文件：包含所有SDK初始化代码和导出，包括认证和数据库服务。
- `firebase.json`文件：Firebase项目配置文件，存储数据库和规则设置。
- `firestore.rules`文件：Firestore安全规则文件（测试模式）。
- `firestore.indexes`文件：数据库索引文件（初期可能不需要）。
- SDK版本已安装，配置就绪，可直接在应用中导入使用。

#### 5.2 关键配置说明
- Firestore数据库已创建，并部署了测试模式规则，允许30天内的开放访问。
- Firebase Authentication已配置，支持密码认证。

### 6. 提交和合并更改
- 提交所有变更：
  - 使用`git add .`添加所有更改。
  - 使用commit消息命令（如课程中创建的）生成提交消息，确认后提交。
- 合并到主分支：
  - 切换到主分支：`git switch main`。
  - 合并分支：`git merge firebase-setup`。
- **建议**：在实际团队工作中，应先推送到GitHub进行代码审查，再合并。

## 核心要点总结
本笔记总结了通过Firebase服务器和斜杠命令（如`/firebase init`）自动化设置和初始化Firebase项目的关键步骤，包括启用认证与Firestore数据库、配置测试模式安全规则、下载SDK代码，并强调了使用Git分支进行安全版本控制的重要性。整个过程展示了AI驱动开发中工具集成的高效性，适用于快速搭建后端服务并连接前端应用，提升开发效率。

---

## 原始字幕

OK, then, so now we've got our Firebase project set up and we've registered a web app for that project now we need to do two things we need to enable the services we want to use like authentication and a Firestore database and we also need to pull down the SDK setup code and add it to this application so we can connect the Firebase backend project and we could do both of these things manually from the project dashboard on Firebase but since we have the Firebase server added we may as well use that instead and we can do that using one of the slash commandsthe server exposes to us which initializes services on the backend so let's start typing forward slash firebase and then we're going to hit tab on the init command and this commandinitializes any backend services we want and then also pulls down the sdk setup code we need andsets those services up on the front end now before we run this command i want to mention that i've already created and switched to a new branch because cloud code is about to add code changesi always like to make sure i do this on a new branch in case things go southso i switch to a branch called firebase setup by running the command git switchthen the c flag to create a new branch then the branch name firebase-setupanyway let's hit enter on that firebase init command then to start the processokay then so it wants to use the tool which is the get firebase environment info tooland i'm going to select yes to allow it to do thatthen the next one is the list firebase apps avait 70%アIP所以它指了 acronym star가는ほ patronsveldoodoo它就出 showing開店描述座 quaint它们来自 parab然後有些allah那我们可以用所以我们要这些买Cloud Firestore和 Firebase Authentication所以我只是在这些公式中但也会进入更多 detail所以它说Cloud Firestore和 Firebase AuthenticationFore the Firestore security rules保持 them in test mode for now只要 enable password authentication而 nothing else不设计 Firebase hosting只要 deploy security rules if needed in test mode now the reason i've gone this extra mile and i've said all this stuff is because sometimes when i just say something like this then it goes ahead and does those other things anyway so it will set up firebase rules or fire store rules such that we can't access the data unless we're authenticated and to begin with i want to be able to access that data and then sometimes for authentication it will enable different methods在它设定是否在当什么使用更新的使用而不是 homemade gas它也τα入Arch FM即使我们 vor nun我们ct ubi iht內有检查不 hard我 JUST Employee这是哪个东西是什么很漂亮的良amientos没事我就披ns gucken我们将在给我们的按照首先它所以会在行之钮 LC兰那么它需要预认色另 Nurse leaks and we hear什么 теперь再按Sื сравit's going to deploy the Firestore rules using this command right herethen it's going to enable authenticationit's going to guide you to enable email and password authentication in Firebaseyes so this is something I've experienced beforewhen I've asked it to enable authenticationit doesn't actually do it on the back end in the consolebut it gives me a guide of how to do thatwhich is really easy to followand then finally it says it's going to implement authentication in the app所以它會加上FyrebaseAuthSDK的進入所以這就好看所以我會選擇現在現在然後按Enter好,首先它會選擇FyrebaseSDK用這個功能所以讓它們做到好,現在它們要選擇一旦去看Fyrebase我會選擇所以我會選擇現在它們要選擇可以建设效能使用腐圈栀ght now It wants to use another tool to initialize Firebase productsso we've got Firestore with some rules right hereso I'm going to say yes for thatand then again another npm or npx this time commandso it's going to use Firebase tools to deploy the Firestore rules basicallythat's what this is doingso if we take a look over here we can see we've got this Firestore rules file that it's createdand if we take a little look at thatlet me just close this basically setting them up in test mode so it's allowing read and write if request time is before a certain date right here so i'm going to cross that off and i'm happy with that so i'm going to say yes you can deploy those alright so it looks like it's done now and it says right here firestore has been successfully deployed the database is now created with test mode rules that allow open access for the next 30 days awesomeit's created the databaseand it's deployed the security rulesand it's also got the SDK configured in this fileso if we take a look at thatit's in the lib folderthen in a firebase folderthis file right hereconfigthis is all the initialization codethat we could have copied from the firebase consolewhich I showed you i think at the end of the last lessonbut it's brought all of that setup code downand it's initialized these two services right hereauthentication and the database serviceit's also exported both of those有人就 Curlico可以借用其他 nightmare另一 realm roads這樣出了一把 wellsינו emotions可以希望 accusmosClaud Sakura的MCP Don't去所有說的 loop а寄些程式啟能做那個有兩天我們來ffentlich移民 conscientenCool virusカ月 pops被凱然后יע有 hopeful结果ик CHRISTI achbridgeis 00 outside光 check inperukeii tehd интересOK,so finally now I'm going 我们现在要告诉 CloudCode我已经有养电信号和积极但我现在不想要它们设定了一个设计的设计因为我们将它们将它们用了使用这个设计的设计所以我现在在这个设计我现在有养电信号和积极但没有需要设定的设计在这个设计之后然后我们再次按下好, so it looks like it's done all that now so we have the Firebase SDK installed using this version the configuration is set up we have the exports ready to use the Cloud Firestore is enabled with the security rules we have Firebase Authentication set up with email and password and then we've got these configuration files as well so Firebase.json, which is over here that is the Firebase project configuration so it's just the database and the rules, etc the different files we're usingwe have the Firestore rules which we saw beforeand then the Firestore indexeswhich are the database indexes which we don'treally need just yetanyway it says you can now import and use Firebasein your app this wayalright awesomeso now what I'd like to do is just commitall these changesand then I'd also like to merge them intothe main branch now like I said before I wouldnormally probably push this up to githubmaybe get a code review if I'm workingin a team and then merge it and pull down the changeswe're not doing github yet so i'm just going to merge it locally into the main branch first ofall we need to add all the changes so i'll just use bash mode right here and we'll say git addand then a full stop then we'll use the commit message command that we created earlier on in the course to come up with some kind of commit message so let's do that all right and it says right here the proposed commit message is this so we'll just say yes we're happy with that we'llwe'll proceed with that commit messageok and now that's done we've got the commiti'm going to switch to main and then merge this firebase setup branchso let me go into bash mode againit switch mainthen we're going to merge by going to bash mode againso git mergeand we want the firebasewas it firebase setup? i think solet's click enteralright, all done