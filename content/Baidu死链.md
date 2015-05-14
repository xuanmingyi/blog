Title: Baidu死链
Date: 2015-05-014 08:52
Tags: Baidu
Authors: Sin
Category: Technology

**Baidu死链**

不是我吐槽，Googlebot早就把我网站的死链去除，然后抓取了新的链接，但是Baidu上还是大量的点开来是404的坏了的链接，两者就抓取数据而言，之间的差距不可同日而语。技术肯定不是问题，主要还是态度和对小站的资源的不屑。


**Baidu站长工具**

Baidu上的死链怎么去除呢？查看Baidu站长工具.

![](http://ww2.sinaimg.cn/large/68ef69degw1es3ie2bqv8j20rp0awq5c.jpg)


主要是生成这个xml文件，我写了一个小脚本来完成这件事。


	git clone https://github.com/xuanmingyi/baidu_dead_link.git
	cd baidu_dead_link
	python baidu_dead_link.py xuanmingyi.com > dead_link.xml


上传`dead_link.xml`文件到网站，然后填写如下工单。

![](http://ww3.sinaimg.cn/large/68ef69degw1es3irf03l1j20fo0fe0u3.jpg)

**Python Port解析**

    try:
        f = urllib2.urlopen(url)
    except urllib2.URLError as e:
        return e.code, e.url
    return f.code, f.url

百度的链接是以 `http://www.baidu.com/?link=` 的形式，这个页面 返回一个403， 临时重定向到真实URL，如果页面是404，我们就可以从URLError Exception中找到code和forward url。


**最后**

最后就是等。。百度还需要2-3天才能反应过来。
