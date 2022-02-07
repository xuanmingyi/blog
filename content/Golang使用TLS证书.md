Title: Golang使用TLS证书
Date: 2021-06-25 22:49:23
Tags: Golang
Slug: golang-tls
Authors: sin
Summary: Golang 代码中使用SSL层

### 服务端代码

go语言使用TLS的测试代码

    :::go
    package main
    import (
        "fmt"
        "flag"
        "log"
        "net/http"
        "github.com/gorilla/mux"
    )

    func main() {
        cert_file := flag.String("cert-file", "ca.pem", "")
        cert_key_file := flag.String("cert-key-file", "ca-key.pem", "")
        flag.Parse()

        rotuer := mux.NewRouter()
        router.HandleFunc("/", func(w http.ResponseWriter, r *http.Request){
            fmt.Fprintf(w, "https index")
            return
        })

        srv := http.Server{
                Handler: router,
                Addr: ":8080",
        }
        err := srv.ListenAndServeTLS(*cert_file, *cert_key_file)
        if err != nil {
                log.Fatal("ListenAndServeTLS: ", err)
        }
    }

### 生产证书

    :::bash
    $ cat >ca-csr.json <<EOF
    {
        "CN": "Self Signed CA",
        "key": {
            "algo": "rsa",
            "size": 2048
        },
        "names": [{
            "C": "CN",
            "ST": "JiangSu",
            "L": "Nanjing",
            "O": "OG1",
            "OU": "OGU1"
        }]
    }
    EOF

自签名CA， O为Orginazation, OU为Orginazation Unit

使用下面命令生成ca证书

    :::bash
    cfssl gencert -initca ca-csr.json | cfssljson -bare ca


多出三个文件


* ca.pem
* ca-key.pem
* ca.csr


执行命令

    :::bash
    go run main.go --cert-file=ca.pem --cert-key-file=ca-key.pem



编译运行后访问 https://127.0.0.1:8000/ ，查看证书发现

![tls.png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/%E8%AF%81%E4%B9%A61.png)

从上面我们可以看出，初始化的自签名证书。



### 签名证书

    :::bash
    $ cat >server-csr.json <<EOF
    {
        "CN": "server",
        "key": {
            "algo": "rsa",
            "size": 2048
        },
        "names": [{
            "C": "CN",
            "ST": "JiangSu",
            "L": "WuXi",
            "O": "OG2",
            "OU": "OGU2"
        }]
    }
    EOF
    $ cat >config.json <<EOF
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
    $ cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=config.json -profile=www server-csr.json | cfssljson -bare server


使用ca来签名证书

| -ca             | ca证书                                                       |
| --------------- | ------------------------------------------------------------ |
| -ca-key         | ca的私钥                                                     |
| -config         | 配置文件，包括签名的一些参数                                 |
| -profile        | profiles中一个，可以在config中定义多个profile，这里选择一个。 |
| server-csr.json | 证书请求文件                                                 |

![证书](https://gitee.com/xuanmingyi/imagebed/raw/master/img/%E8%AF%81%E4%B9%A62.png)

### 客户端代码

#### 使用HTTPS访问百度

    :::go
    package main
    import (
        "fmt"
        "io/ioutil"
        "net/http"
    )
    func main() {
        resp, err := http.Get("https://www.baidu.com")
        if err != nil {
            fmt.Println("error: ", err)
            return
        }
        defer resp.Body.Close()

        body, err := ioutil.ReadAll(resp.Body)
        fmt.Println(string(body))
    }

验证通过

#### 错误验证

    :::bash
    // resp, err := http.Get("https://www.baidu.com") 
    resp, err := http.Get("https://127.0.0.1") 

错误验证，输出为

    :::bash
    error:  Get https://127.0.0.1:8000: x509: certificate signed by unknown authority

表示签名为未知的结构发布。

#### 跳过验证

    :::go
    package main
    import (
        "crypto/tls"
        "fmt"
        "io/ioutil"
        "net/http"
    )
    func main() {
        tr := &http.Transport {
            TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
        }

        client := &http.Client{Transport: tr}

        resp, err := client.Get("https://127.0.0.1:8000")
        if err != nil {
            fmt.Println("error: ", err)
            return
        }
        defer resp.Body.Close()

        body, err := ioutil.ReadAll(resp.Body)
        fmt.Println(string(body))
    }


我们使用 **InsecureSkipVerify: true** 参数 来跳过客户端验证。不去管证书是否权威有效，都算他有效。

#### 认证

    :::go
    package main
    import (
        "crypto/tls"
        "crypto/x509"
        "fmt"
        "io/ioutil"
        "net/http"
    )
    func main() {
        pool := x509.NewCertPool()
        caCertPath := "ca.pem"

        caCrt, err := ioutil.ReadFile(caCertPath)

        if err != nil {
            fmt.Println("ReadFile err: ", err)
            return
        }
        pool.AppendCertsFromPEM(caCrt)

        tr := &http.Transport {
            TLSClientConfig: &tls.Config{RootCAs: pool},
        }

        client := &http.Client{Transport: tr}

        resp, err := client.Get("https://127.0.0.1:8000")
        if err != nil {
            fmt.Println("error: ", err)
            return
        }
        defer resp.Body.Close()

        body, err := ioutil.ReadAll(resp.Body)
        fmt.Println(string(body))
    }

执行上述客户端代码

    :::bash
    error:  Get https://127.0.0.1:8000: x509: cannot validate certificate for 127.0.0.1 because it doesn't contain any IP SANs

**报错** 原因就是上面我们签名的证书是有问题的，没有包含hosts数据！

    :::bash
    $ cat >server-csr.json <<EOF
    {
        "CN": "server",
        "hosts": [
            "127.0.0.1",
            "localhost"
        ],
        "key": {
            "algo": "rsa",
            "size": 2048
        },
        "names": [{
            "C": "CN",
            "ST": "JiangSu",
            "L": "WuXi",
            "O": "OG2",
            "OU": "OGU2"
        }]
    }
    EOF


给csr文件添加hosts数据，用上面的命令重新签名生成。并且重启服务端测试代码，重新使用证书。

重新运行上面客户端代码,成功！

    :::bash
    https index

我们再把url替换成 https://172.16.0.106:8000, 这里是同一台机器。

    :::bash
    error:  Get https://172.16.0.106:8000: x509: certificate is valid for 127.0.0.1, not 172.16.0.106

要修改的话直接修改server-csr.json中的hosts字段