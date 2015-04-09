Title: CoreOS初体验
Date: 2015-02-04 01:45
Tags: CoreOS
Authors: Sin
Category: Technology

**CoreOS**

*CoresOS* 是一个小的标准Linux系统。与Ubuntu、CentOS等系列的系统不一样，他天生就是为集群而生，同时并不是在系统上装软件来实现应用功能，而是通过在系统上运行一个个的容器，在容器里运行应用来实现，这样避免了很多不必要的麻烦。

![](http://coreos.com/assets/images/brand/coreos-wordmark-horiz-color.png)

一句话

    CoreOS = Linux + Docker

**运行**

在官方网站上有VMware的支持，只需要下载一个CoreOS VMware镜像，直接打开(key在同一个压缩包里)。

![](http://ww4.sinaimg.cn/mw690/68ef69degw1eowp1kjt2lj20hz038glg.jpg)

使用命令即可登录。

    $ ssh -i insecure_ssh_key core@192.168.1.196

![](http://ww2.sinaimg.cn/mw690/68ef69degw1eowpan1gylj20ay01kgle.jpg)

**基本配置**

以上方式虽然机器可以通外网，但他是通过DHCP获得IP，要做的第一件事就是配置静态IP

在*/etc/systemd/network/static.network*中作如下配置

    [Match]
    Name=ens192

    [Network]
    Address=192.168.1.196/24
    Gateway=192.168.1.1
    DNS=114.114.114.114

然后重启一下机器就可以发现设置生效了

**Tip**

根据[文档](https://coreos.com/docs/cluster-management/setup/network-config-with-networkd/), 使用

    sudo systemctl restart systemd-networkd

就可以重启网络，但是好像没啥用。
