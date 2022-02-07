Title: RabbitMQ安装使用
Date: 2021-11-02 21:45:43
Tags: RabbitMQ
Slug: rabbitmq-install
Authors: sin
Summary: RabbitMQ安装使用

#### 安装使用

在centos7中，我们使用RabbbitMQ比较简单，只需要yum安装就可以了。

    :::bash
    yum install epel-release
    yum install rabbitmq-server

#### 启动rabbitmq

    :::bash
    systemctl start rabbitmq-server
    systemctl enable rabbitmq-server

#### 开启management

    :::bash
    rabbitmq-plugins list
    rabbitmq-plugins enable rabbitmq_management
    systemctl restart rabbitmq-server

#### 访问管理界面

注意需要关闭防火墙和selinux，或者添加例外。访问**15672**端口。默认的用户名密码是**guest/guest**

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211102214325.png)

#### WSL

在WSL中使用rabbitmq，我们需要注意。



修改配置文件*/etc/rabbitmq/rabbitmq-env.conf*

    :::ini
    NODE_IP_ADDRESS=127.0.0.1

重新启动

    :::bash
    sudo /etc/init.d/rabbitmq-server restart
