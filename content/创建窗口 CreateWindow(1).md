Title: 创建窗口 CreateWindow(1)
Date: 2021-10-11 16:43:43
Tags: Xlib
Slug: xlib-createwindow-1
Authors: sin
Summary: 使用Xlib库 创建窗口

### 介绍

[Xlib手册](https://tronche.com/gui/x/xlib)  is based on X11 release 6。


### 创建窗口 XCreateWindow

    :::c
    #include <stdio.h>
    #include <stdlib.h>
    #include <X11/Xlib.h>


    int main() {
        Display *X;
        Window win;
        GC gc;
        XSetWindowAttributes attributes;
        XKeyEvent event;


        X = XOpenDisplay(NULL);

        attributes.background_pixel = XWhitePixel(X, 0);
        attributes.border_pixel = 0x3344ff;

        win = XCreateWindow(X,
            XRootWindow(X, 0),
            100, 100, 200, 200,
            15,
            DefaultDepth(X, 0),
            InputOutput,
            DefaultVisual(X, 0),
            CWBackPixel | CWBorderPixel,
            &attributes);

        XSelectInput(X, win, KeyPressMask);

        gc = XCreateGC(X, win, 0, NULL);
        XMapWindow(X, win);
        while(1){
            XNextEvent(X, (XEvent*)&event);
            switch(event.type) {
                case KeyPress:
                    {
                        XFreeGC(X, gc);
                        XCloseDisplay(X);
                        exit(0);
                    }break;
                default:
                    {
                        printf("%p", &event);
                    }break;
            }
        }
        return 0;
    }



创建**XCreateWindow**，显示窗口 **XMapWindow**。

    :::makefile
    wmgo: main.c
        gcc main.c -o wmgo -lX11 -O3

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211011160753.png)

### 添加cursor

上述代码还没有鼠标指针。给窗口添加个向右的[XDefineCursor](https://tronche.com/gui/x/xlib/window/XDefineCursor.html)。

    :::c
    XDefineCursor(X, win, XCreateFontCursor(X, XC_right_ptr));

![cursor.gif](https://gitee.com/xuanmingyi/imagebed/raw/master/img/cursor.gif)