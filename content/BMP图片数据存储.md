Title: BMP图片数据存储
Date: 2021-10-22 20:41:43
Tags: Xlib
Slug: bmp-image-storage
Authors: sin
Summary: BMP图片存储结构

#### BMP文件格式



BMP 维基百科上已经解释的非常清楚了。一图看懂！

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/BMPfileFormat.png)



下面我们使用一张图做为例子, 上王珞丹！

![bmp](https://gitee.com/xuanmingyi/imagebed/raw/master/img/wld.bmp)



图片是 450 x 675 x 24。 宽度是450，高度是675，24位色（一个像素使用24bit来表示）。

我们来看一下这个图片中DIB Header

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211022174220.png)



**宽度**:  十六进制 0x000001c2  等于 十进制 450

**高度**:  十六进制 0x000002a3  等于 十进制 675

计算一下 _450*3 = 1350_， 不能被4整除，还需要补足2个字节，这样子，才能和4的倍数对齐，所以padding为2。

数据大小为  _(450*3 + 2) *  675 =  912600_)   转换成十六进制 0x000decd8 ，如下图所示。



![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211022174557.png)



所有数据都能对的上了。这次我们直接从offset处获取数据。



接下来，我们显示我们的图片。



#### 显示BMP主要代码



    :::c
    unsigned char *load_bmp(const char *filename, int *offset, int *width, int *height)
    {
        int size;
        unsigned char *data;

        FILE *f = fopen(filename, "rb");
        fseek(f, 0, SEEK_END);
        size = ftell(f);
        data = malloc(size);
        memset(data, 0, sizeof(data));
        fseek(f, 0, SEEK_SET);
        fread(data, sizeof(unsigned char), size, f);
        fclose(f);

        *offset = get_int(data, 0xa);
        *width = get_int(data, 0x12);
        *height = get_int(data, 0x16);

        return data;
    }


    void setimage(Display *X, Window win, GC gc)
    {
        XImage *ximage;
        int depth = DefaultDepth(X, 0);
        int width, height, n;
        int rc;
        unsigned char *idata;
        unsigned char *buffer;
        int offset;

        idata = load_bmp("wld.bmp", &offset, &width, &height);
        buffer = malloc(width * height * 4);

        int i = 0;
        int _offset = 0;
        int padding = (4 - width * 3 % 4) % 4;

        for (int h = height - 1; h > 0; h--)
        {
            for (int w = 0; w < width; w++)
            {
                _offset = h * (width * 3 + padding) + w * 3;
                buffer[i * 4] = idata[offset + _offset];
                buffer[i * 4 + 1] = idata[offset + _offset + 1];
                buffer[i * 4 + 2] = idata[offset + _offset + 2];
                buffer[i * 4 + 3] = 0;
                i++;
            }
        }
        free(idata);

        ximage = XCreateImage(X, DefaultVisual(X, 0), depth, ZPixmap,
                              0, (unsigned char *)buffer, width,
                              height, 32, 0);
        rc = XPutImage(X, win, gc, ximage, 0, 0, 0, 0,
                       width,
                       height);
        test_or_die(rc);

        free(buffer);
    }

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211022180325.png)



#### 特别注意

* 我们常用的颜色其实是RGB,而BMP的存储格式是  B G R,但是，正好，xlib中的颜色顺序也是B G R。所以我们一一对应就可以了。如果使用其他图片库，比如[stb_image操作图片](/xlib-stb-image.html), 那么一定要注意颜色顺序。
* 注意BMP像素存储顺序和xlib中XImage像素存储顺序的不同。需要做一个转换