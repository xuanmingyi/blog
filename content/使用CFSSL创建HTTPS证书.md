Title: 使用CFSSL创建HTTPS证书
Date: 2021-06-24 22:16:43
Tags: Linux
Slug: cfssl-https-certificate
Authors: sin
Summary: 使用CFSSL工具 构建SSL证书

### 创建CA证书

    :::bash
    $ cat > ca-csr.json <<EOF
    {
        "CN": "我自己的签名中心",
        "key": {
            "algo": "rsa",
            "size": 2048
        },
        "names": [{
            "C": "CN",
            "ST": "JiangSu",
            "L": "NanJing",
            "O": "私人组织",
            "OU": "15单元"
        }]
    }
    EOF
    $ cfssl gencert -initca ca-csr.json | cfssljson -bare ca

### 签名服务器证书

    :::bash
    $ cat > config.json <<EOF
    {
        "signing": {
            "default": {
                "expiry": "87600h"
            },
            "profiles": {
                "www": {
                    "usages": ["signing", "key encipherment", "server auth", "client auth"],
                    "expiry": "87600h"
                }
        }
        }
    }
    EOF
    $ cat > server-csr.json <<EOF
    {
        "CN": "我自己的网站",
        "key": {
            "algo": "rsa",
            "size": 2048
        },
        "names": [{
            "C": "CN",
            "ST": "JiangSu",
            "L": "NanJing",
            "O": "还是私人组织",
            "OU": "还是15单元"
        }]
    }
    EOF
    $ cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=config.json -profile=www server-csr.json | cfssljson -bare server


添加nginx中的配置

    :::nginx
    listen 81 ssl http2 default_server;
    listen [::]:81 ssl http2 default_server;

    root /usr/share/nginx/html;
    ssl_certificate /etc/nginx/ssl/server.pem;
    ssl_certificate_key /etc/nginx/ssl/server-key.pem;


使用浏览器查看证书



![zhengshu.png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/%E8%AF%81%E4%B9%A63.png)



### 参考

- [CFSSL创建HTTPS证书](http://blog.leanote.com/post/criss/CFSSL%E5%88%9B%E5%BB%BAHTTPS%E8%AF%81%E4%B9%A6)