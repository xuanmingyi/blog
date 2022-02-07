Title: 网络基础(1)-IPTABLES 的简单使用
Date: 2021-06-24 10:00:43
Tags: Linux
Slug: linux-iptables-1
Authors: sin
Summary: iptables 工具简单使用

### 参考

- [iptables详解（1）：iptables概念](https://www.zsythink.net/archives/1199)
- [iptables详解（2）：iptables实际操作之规则查询](https://www.zsythink.net/archives/1493)
- [iptables详解（3）：iptables规则管理](https://www.zsythink.net/archives/1517)
- [iptables详解（4）：iptables匹配条件总结之一](https://www.zsythink.net/archives/1544)
- [iptables详解（5）：iptables匹配条件总结之二（常用扩展模块）](https://www.zsythink.net/archives/1564)
- [iptables详解（6）：iptables扩展匹配条件之’–tcp-flags’](https://www.zsythink.net/archives/1578)
- [iptables详解（7）：iptables扩展之udp扩展与icmp扩展](https://www.zsythink.net/archives/1588)
- [iptables详解（8）：iptables扩展模块之state扩展](https://www.zsythink.net/archives/1597)
- [iptables详解（9）：iptables的黑白名单机制](https://www.zsythink.net/archives/1604)
- [iptables详解（10）：iptables自定义链](https://www.zsythink.net/archives/1625)
- [iptables详解（11）：iptables之网络防火墙](https://www.zsythink.net/archives/1663)
- [iptables详解（12）：iptables动作总结之一](https://www.zsythink.net/archives/1684)
- [iptables详解（13）：iptables动作总结之二](https://www.zsythink.net/archives/1764)
- [iptables详解（14）：iptables小结之常用套路](https://www.zsythink.net/archives/1869)



### 准备工作

重新安装一个新的**Centos7**系统，关闭firewalld，因为firewalld也是使用iptables规则。打开firewalld会自动生成很多iptables规则。



    :::bash
    $ systemctl stop firewalld
    $ iptables -t nat -nvL
    Chain PREROUTING (policy ACCEPT 8 packets, 1194 bytes)
     pkts bytes target     prot opt in     out     source               destination       

    Chain INPUT (policy ACCEPT 8 packets, 1194 bytes)
     pkts bytes target     prot opt in     out     source               destination 

    Chain OUTPUT (policy ACCEPT 13 packets, 1729 bytes)
     pkts bytes target     prot opt in     out     source               destination 

    Chain POSTROUTING (policy ACCEPT 13 packets, 1729 bytes)
     pkts bytes target     prot opt in     out     source               destination     

### Example.01 docker

首先看一下docker中iptables的使用，分别是nat表和filter表。raw和mangle表没有被docker使用。

    :::bash
    $ yum install docker
    $ systemctl start docker

![iptables-1.jpg (3812×758) (gitee.com)](https://gitee.com/xuanmingyi/imagebed/raw/master/img/iptables-1.jpg)



### SNAT

我们用docker启动一个镜像，然后安装ping和tcpdump，结构如下。

![iptables-2](https://gitee.com/xuanmingyi/imagebed/raw/master/img/iptables-2.jpg)

docker0 和 ens33 之间数据转发需要打开ipforward

![iptables-3.jpg](https://gitee.com/xuanmingyi/imagebed/raw/master/img/iptables-3.jpg)



### DNAT

重新启动一个镜像，映射一个**1234**端口到容器的**5678**

    :::bash
    $ docker run -it --rm -p1234:5678 ubuntu bash

![iptables-4.jpg](https://gitee.com/xuanmingyi/imagebed/raw/master/img/iptables-4.jpg)
