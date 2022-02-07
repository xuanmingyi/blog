Title: Events后续 MotionNotify(5)
Date: 2021-10-22 17:21:43
Tags: Xlib
Slug: xlib-events-motionnofity
Authors: sin
Summary: Xlib中的MotionNotify事件

这是[上一篇文章Events(3)](http://www.lithum.tech/index.php/archives/29/)的补充说明



| **Event Mask**    | **Event Type** | **Structure**      | **Generic Structure** |
| ----------------- | -------------- | ------------------ | --------------------- |
| PointerMotionMask | MotionNotify   | XPointerMovedEvent | XMotionEvent          |
| ButtonMotionMask  | MotionNotify   | XPointerMovedEvent | XMotionEvent          |



##### XMotionEvent代码结构

    :::c
    typedef struct {
        int type;		/* of event */
        unsigned long serial;	/* # of last request processed by server */
        Bool send_event;	/* true if this came from a SendEvent request */
        Display *display;	/* Display the event was read from */
        Window window;	        /* "event" window reported relative to */
        Window root;	        /* root window that the event occurred on */
        Window subwindow;	/* child window */
        Time time;		/* milliseconds */
        int x, y;		/* pointer x, y coordinates in event window */
        int x_root, y_root;	/* coordinates relative to root */
        unsigned int state;	/* key or button mask */
        char is_hint;		/* detail */
        Bool same_screen;	/* same screen flag */
    } XMotionEvent;
    typedef XMotionEvent XPointerMovedEvent;





##### 样例代码

    :::c
    // ======代码1=============
    void motionnotify(XEvent *e)
    {
        XMotionEvent *ev = &e->xmotion;
        if (ev->state & Button2Mask)
        {
            printf("button 2 motion\n");
        }
        printf("motion notify event: state=%d , x y = %d %d\n", ev->state, ev->x, ev->y);
        return;
    }
    // =======================

    // ======代码2=============
    wa.event_mask = PointerMotionMask | ButtonMotionMask;
    // =======================

    // ======代码3=============
    handlers[MotionNotify] = motionnotify;
    // =======================


运行后，我按动滚轮移动来验证代码



![gif](https://gitee.com/xuanmingyi/imagebed/raw/master/img/motion.gif)