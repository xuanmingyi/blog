Title: SAE简单开发教程
Date: 2015-01-01 20:59
Tags: SAE
Authors: Sin
Category: Technology

AE运行是在云端，但是开发是在本地，为了统一开发和部署环境，新浪自己开发了一套SAE运行时环境,环境下载地址是在[文档](http://sae.sina.com.cn/doc/)的[资源下载](http://sae.sina.com.cn/doc/download.html)标签中，大约20M的php本地开发环境。

**资源下载**

下载完成后，解压压缩包，获得如下环境：

![](http://ww4.sinaimg.cn/mw690/68ef69degw1enfve65j8hj20ev066jrt.jpg)

**运行环境**

![运行环境](http://ww2.sinaimg.cn/mw690/68ef69degw1enfvizjqbhj208206ngm0.jpg)

由于需要打开一些服务，所以需要使用管理员身份运行，当第一次初始化服务的时候，需要用户允许mysql和redis运行

![mysql](http://ww3.sinaimg.cn/mw690/68ef69degw1enfve3zq6xj20ex0a0dgw.jpg)

![redis](http://ww4.sinaimg.cn/mw690/68ef69degw1enfve5m1hmj20ex09ywfh.jpg)

到这里，如果没有问题，就能看到如下命令行界面，这表示模拟环境运行成功。

![成功](http://ww4.sinaimg.cn/mw690/68ef69degw1enfvnaaeyqj20io0c33za.jpg)

快打开浏览器输入localhost 看看有啥惊喜吧

tips：

如果你没有运行成功，可以查看他给出的提示信息，很有可能使因为端口被占用，比如你已经开了一个apache，这将导致80端口被占用，那么模拟环境将无法启动一个apache，最后导致模拟环境启动失败。如果还不能解决，请查文档，也欢迎留言交流。
