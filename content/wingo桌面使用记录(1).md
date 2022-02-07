Title: Wingo 桌面使用记录(1)
Date: 2021-09-18 06:47:43
Tags: Wingo
Slug: wingo-desktop-1
Authors: sin
Summary: Wingo 桌面使用记录

### wingo桌面简介

我们了解，**window manager**其实一个应用程序，我们这里开发[wingo fork](https://github.com/xuanmingyi/wingo)，当开发到一定程度的时候，作为主要的WM使用，提高工作效率。


### 编译以及启动桌面

    :::bash
    git clone https://github.com/xuanmingyi/wingo.git
    cd wingo
    ./xephyr-wingo

![wingo-1](https://gitee.com/xuanmingyi/imagebed/raw/master/img/wingo-1.png)



#### 查看*key.wini*文件,特殊按键如下

    :::ini
    #     shift   -> Shift
    #     control -> Control
    #     mod1    -> alt
    #     mod4    -> super (the "windows" key)

#### 启动urxvt

    :::ini
    Mod4-t := Shell "urxvt"

#### 启动gmrun

    :::ini
    Mod1-F2 := Shell "gmrun"

#### 切换workspace

    :::ini
    Mod4-left := Workspace (GetWorkspacePrev)
    Mod4-right := Workspace (GetWorkspaceNext)

    Mod1-1 := WorkspaceGreedy "1"
    Mod1-2 := WorkspaceGreedy "2"
    Mod1-3 := WorkspaceGreedy "3"
    Mod1-4 := WorkspaceGreedy "4"

