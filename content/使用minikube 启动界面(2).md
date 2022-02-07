Title: 使用minikube 启动界面(2)
Date: 2021-06-17 22:59:59
Tags: Kubernetes
Slug: minikube-k8s-2
Authors: sin
Summary: 启动k8s界面

### 启动界面

    :::bash
    minikube dashboard

### 端口转发

使用端口转发来访问dashboard， 注意这里需要指定–namespace kubernetes-dashboard.并且需要安装socat工具。

    :::bash
    yum install -y socat
    minikube kubectl -- port-forward --address 0.0.0.0 svc/kubernetes-dashboard --namespace kubernetes-dashboard  8081:80

访问界面 http://192.168.65.179:8081

![minikube-2-1.png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/minikube-2-1.png)