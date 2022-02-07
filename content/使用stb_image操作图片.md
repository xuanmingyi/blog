Title: 使用stb_image操作图片
Date: 2021-10-13 21:11:43
Tags: Xlib
Slug: xlib-stb-image
Authors: sin
Summary: 在Xlib中 使用stb_image库操作图片

### 项目介绍

[stb](https://github.com/nothings/stb)项目是一个**ALLINONE**的*c*解决方案，其中有一个[stb_image.h](https://github.com/nothings/stb/blob/master/stb_image.h)，可以用来操作图片。 推荐给大家的博客

* [简单易用的图像解码库介绍 —— stb_image](https://glumes.com/post/android/stb-image-introduce/)

* [用stb_image.h轻松地加载图片到程序中（比如纹理）](https://www.codenong.com/cs105610298/)



### Example

    :::c
    #define STB_IMAGE_IMPLEMENTATION
    #include "stb_image.h"

    #define STB_IMAGE_WRITE_IMPLEMENTATION
    #include "stb_image_write.h"

    #define COLOR_L 3

    int main()
    {
        int width, height, depth;
        unsigned char *buffer;
        buffer = stbi_load("wld.jpg", &width, &height, &depth, 0);
        unsigned char *newbuffer = (unsigned char *)malloc(width * height * COLOR_L);

        unsigned char r, g, b, grey;
        for (int n = 0; n < height; n++)
        {
            for (int m = 0; m < width; m++)
            {
                // 第n行,m列像素
                r = buffer[n * width * COLOR_L + m * COLOR_L];
                g = buffer[n * width * COLOR_L + m * COLOR_L + 1];
                b = buffer[n * width * COLOR_L + m * COLOR_L + 2];
                grey = 0.3 * r + 0.59 * g + 0.11 * b;
                newbuffer[n * width * COLOR_L + m * COLOR_L] = grey;
                newbuffer[n * width * COLOR_L + m * COLOR_L + 1] = grey;
                newbuffer[n * width * COLOR_L + m * COLOR_L + 2] = grey;
            }
        }

        stbi_image_free(buffer);
        stbi_write_png("wld.png", width, height, depth, newbuffer, width * depth);
        stbi_write_jpg("wld2.jpg", width, height, depth, newbuffer, 100);

        return 0;
    }

程序使用**stbi_load**读取数据，使用**stbi_write_png**和**stbi_write_jpg**写入数据。



![wld](https://gitee.com/xuanmingyi/imagebed/raw/master/img/wld.jpg)



针对每个像素，我们做了一个加权取值， 得

![wld](https://gitee.com/xuanmingyi/imagebed/raw/master/img/wld.png)