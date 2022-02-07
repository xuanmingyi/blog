Title: 使用minikube 构建k8s集群(1)
Date: 2021-06-16 22:51:41
Tags: Kubernetes
Slug: minikube-k8s-1
Authors: sin
Summary: 使用minikube构建k8s

### 操作系统准备

在开始构建k8s集群之前，我们选取centos7作为操作系统，最小化安装。

    :::bash
    yum update -y
    yum upgrade -y
    yum install net-tools bridge-utils vim
    sed -i "s/enforing/disabled/g" /etc/selinux/config
    setenforce 0
    getenforce
    swapoff -a
    sed -i "s/^\/dev\/mapper\/centos-swap/#\/dev\/mapper\/centos-swap/g" /etc/fstab

### 设置静态网络

修改配置文件/etc/sysconfig/network-scripts/ifcfg-ens33

    :::bash
    #BOOTPROTO="dhcp"
    #IPV6_ADDR_GEN_MODE="stable-privacy"
    #ONBOOT="no"

    BOOTPROTO=static
    ONBOOT=yes
    IPADDR=192.168.65.179
    NETMASK=255.255.255.0
    GATEWAY=192.168.65.2
    DNS1=114.114.114.114

    systemctl restart network

### 安装docker

    :::bash
    yum install -y yum-utils
    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    yum install docker-ce docker-ce-cli containerd.io
    systemctl restart docker

### 安装Golang

由于我们需要使用golang，所以安装一下比较新的版本1.16.5，并且设置国内proxy

    :::bash
    yum install wget
    wget https://studygolang.com/dl/golang/go1.16.5.linux-amd64.tar.gz
    tar vzxf go1.16.5.linux-amd64.tar.gz
    // .bashrc
    export GOROOT=/root/go
    export GOPATH=/root/gopath
    export PATH=$GOROOT/bin:$GOPATH/bin:$PATH

    go env -w GOPROXY=https://goproxy.cn

### 安装git

    :::bash
    yum install git

### 安装Minikube

    :::bash
    // 根据gopath安装
    git clone --branch v1.21.0  https://github.com/kubernetes/minikube.git
    git clone https://github.com/go-bindata/go-bindata.git
    yum install gcc
    make -j4 linux
    cp out/minikube-linux-amd64 /usr/local/bin/minikube

### 准备镜像

    :::bash
    docker pull registry.aliyuncs.com/google_containers/kube-apiserver:v1.20.7
    docker pull registry.aliyuncs.com/google_containers/kube-controller-manager:v1.20.7
    docker pull registry.aliyuncs.com/google_containers/kube-scheduler:v1.20.7
    docker pull registry.aliyuncs.com/google_containers/kube-proxy:v1.20.7
    docker pull registry.aliyuncs.com/google_containers/pause:3.2
    docker pull registry.aliyuncs.com/google_containers/etcd:3.4.13-0
    docker pull registry.aliyuncs.com/google_containers/coredns:1.7.0
    docker tag registry.aliyuncs.com/google_containers/kube-apiserver:v1.20.7 k8s.gcr.io/kube-apiserver:v1.20.7
    docker tag registry.aliyuncs.com/google_containers/kube-controller-manager:v1.20.7 k8s.gcr.io/kube-controller-manager:v1.20.7
    docker tag registry.aliyuncs.com/google_containers/kube-scheduler:v1.20.7 k8s.gcr.io/kube-scheduler:v1.20.7
    docker tag registry.aliyuncs.com/google_containers/kube-proxy:v1.20.7 k8s.gcr.io/kube-proxy:v1.20.7
    docker tag registry.aliyuncs.com/google_containers/pause:3.2 k8s.gcr.io/pause:3.2
    docker tag registry.aliyuncs.com/google_containers/etcd:3.4.13-0 k8s.gcr.io/etcd:3.4.13-0
    docker tag registry.aliyuncs.com/google_containers/coredns:1.7.0 k8s.gcr.io/coredns:1.7.0

    docker pull zengjie19/gcr.io-k8s-minikube-storage-provisioner:v5
    docker tag zengjie19/gcr.io-k8s-minikube-storage-provisioner:v5 gcr.io/k8s-minikube/storage-provisioner:v5


### kubelet安装

下载**对应版本**的[kubelet](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#client-binaries)，然后copy到对应目录下

    :::bash
    tar vzxf kubernetes-client-linux-amd64.tar.gz
    cp kubernetes/client/bin/kubectl /usr/local/bin/

### 启动！Start

    :::bash
    minikube start --driver=none

### 启动nginx

编写配置文件**deployment.yaml**

    :::yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: myapp
    spec:
      selector:
        matchLabels:
          app: myapp
      replicas: 2 # tells deployment to run 2 pods matching the template
      template:
        metadata:
          labels:
            app: myapp
        spec:
          containers:
          - name: myapp
            image: nginx:latest
            ports:
            - containerPort: 80

然后执行如下命令

    :::bash
    docker pull nginx
    kubectl create -f deployment.yaml
    kubectl expose deployment myapp --type=NodePort

    kubectl get service 
    NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
    kubernetes   ClusterIP   10.96.0.1              443/TCP        98m
    myapp        NodePort    10.108.66.77           80:30079/TCP   70m

    curl http://192.168.65.179:30079


![minikube-1-1.png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/minikube-1-1.png)