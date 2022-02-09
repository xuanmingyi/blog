Title: Events后续 ButtonPress 和 ButtonRelease(4)
Date: 2021-10-14 23:28:43
Tags: Xlib
Slug: xlib-events-buttonpress-buttonrelease
Authors: sin
Summary: Xlib中 ButtonPress 和 ButtonRelease 事件

这是[上一篇文章Events(3)](/xlib-events.html)的补充说明



| **Event Mask**    | **Event Type** | **Structure**        | **Generic Structure** |
| ----------------- | -------------- | -------------------- | --------------------- |
| ButtonPressMask   | ButtonPress    | XButtonPressedEvent  | XButtonEvent          |
| ButtonReleaseMask | ButtonRelease  | XButtonReleasedEvent | XButtonEvent          |



##### **XButtonEvent** 代码结构

    :::c
    typedef struct {
        int type;		/* of event */
        unsigned long serial;	/* # of last request processed by server */
        Bool send_event;	/* true if this came from a SendEvent request */
        Display *display;	/* Display the event was read from */
        Window window;	        /* "event" window it is reported relative to */
        Window root;	        /* root window that the event occurred on */
        Window subwindow;	/* child window */
        Time time;		/* milliseconds */
        int x, y;		/* pointer x, y coordinates in event window */
        int x_root, y_root;	/* coordinates relative to root */
        unsigned int state;	/* key or button mask */
        unsigned int button;	/* detail */
        Bool same_screen;	/* same screen flag */
    } XButtonEvent;
    typedef XButtonEvent XButtonPressedEvent;
    typedef XButtonEvent XButtonReleasedEvent;


##### 样例代码

    :::c
    // ======代码1=============
    void buttonpress(XEvent *e)
    {
        XButtonEvent *ev = &e->xbutton;
        printf("button press event, button: %d, x y = %d %d\n", ev->button, ev->x, ev->y);
        return;
    }

    void buttonrelease(XEvent *e)
    {
        XButtonEvent *ev = &e->xbutton;
        printf("button release event, button: %d, x y = %d %d\n", ev->button, ev->x, ev->y);
    }
    // =======================


    // ======代码2=============
    wa.event_mask = ButtonPressMask | ButtonReleaseMask;
    // =======================


    // ======代码3=============
    handlers[ButtonPress] = buttonpress;     // 4
    handlers[ButtonRelease] = buttonrelease; // 5
    // =======================


在我电脑上:

* 鼠标左键为1
* 鼠标中键辊轮为2
* 鼠标右键为3
* 鼠标中键滚轮向前滑动是4
* 鼠标中键滚轮向后滑动是5



#### 效果

![gif](https://gitee.com/xuanmingyi/imagebed/raw/master/img/keypresskeyrelease2.gif)