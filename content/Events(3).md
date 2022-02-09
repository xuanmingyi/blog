Title: Xlib-Events(3)
Date: 2021-10-14 23:18:43
Tags: Xlib
Slug: xlib-events
Authors: sin
Summary: Xlib 事件

#### Event Types

| **Event Category**                      | **Event Type **                                              |
| :-------------------------------------- | ------------------------------------------------------------ |
| Keyboard events 键盘事件                | **KeyPress** **KeyRelease**                                  |
| Pointer events 鼠标事件                 | **ButtonPress**  **ButtonRelease**  **MotionNotify(运动事件)** |
| Window crossing events 窗体进入离开事件 | **EnterNotify** **LeaveNotify**                              |
| Input focus events                      | **FocusIn** **FocusOut**                                     |
| Keymap state notification event         | **KeymapNotify**                                             |
| Exposure events                         | **Expose** **GraphicsExpose** **NoExpose**                   |
| Structure control events                | **CirculateRequest** **ConfigureRequest ** **MapRequest** **ResizeRequest** |
| Window state notification events        | **CirculateNotify** **ConfigureNotify** **CreateNotify** **DestroyNotify** **GravityNotify** **MapNotify** **MappingNotify** **ReparentNotify** **UnmapNotify** **VisibilityNotify** |
| Colormap State Change Events            | **ColormapNotify**                                           |
| Client Communication Events             | **ClientMessage** **PropertyNotify** **SelectionClear** **SelectionNotify** **SelectionRequest** |



下面我们详细测试解释

##### 主体结构

    :::c
    #include <stdio.h>
    #include <X11/Xlib.h>

    static Display *dpy;
    static int screen;
    static int sw, sh;
    static Window root;
    static int running = 1;

    typedef void (*handler)(XEvent *);

    static void *handlers[LASTEvent];

    void default_handler(XEvent *ev)
    {
        printf("default event handler: ev.type = %d\n", ev->type);
        return;
    }

    // ======代码1=============
    void xxxx(XEvent *ev)
    {
    }
    // =======================

    void init()
    {
        dpy = XOpenDisplay(NULL);

        XSetWindowAttributes wa;

        screen = DefaultScreen(dpy);
        sw = DisplayWidth(dpy, screen);
        sh = DisplayHeight(dpy, screen);
        root = RootWindow(dpy, screen);

        // ======代码2=============
        wa.event_mask = Mask;
        // =======================

        XChangeWindowAttributes(dpy, root, CWEventMask, &wa);
        XSelectInput(dpy, root, wa.event_mask);

        for (int i = 0; i < LASTEvent; i++)
        {
            handlers[i] = default_handler;
        }

        // ======代码3=============
        handlers[XXXX] = xxxx;
        // =======================
    }

    void run()
    {
        XEvent ev;
        XSync(dpy, False);
        while (running && !XNextEvent(dpy, &ev))
        {
            handler caller = handlers[ev.type];
            if (caller != NULL)
            {
                caller(&ev);
            }
        }
    }

    int main()
    {
        init();
        run();
    }


执行命令

    :::makefile
    event_test: event_test.c
        gcc event_test.c -o event_test -lX11


启动Xephyr，同时启动event_test测试。



#### 测试文章



* [**ButtonPress 和 ButtonRelease **](/xlib-events-buttonpress-buttonrelease.html)
* [**MotionNotify**](/xlib-events-motionnofity.html)

