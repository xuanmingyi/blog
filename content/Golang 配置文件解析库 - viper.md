Title: Golang 配置文件解析库 - viper
Date: 2021-07-26 23:53:43
Tags: Golang
Slug: golang-viper
Authors: sin
Summary: Golang 配置解析

### 简介

[viper](https://github.com/spf13/viper)配置库支持如下特性

-  设置默认值
-  支持JSON，TOML，YAML，HCL，envfile，Java配置文件
-  实时监控配置文件，当改变时重新读取
-  从环境变量读取
-  从远程读取配置文件，包括etcd和consul，同时监控修改
-  从命令行读取
-  从buffer中读取
-  setting explicit values



### 配置文件

    :::yaml
    Address: "Wuxi"
    Postcode: 214000

### 解析代码

    :::go
    package main

    import (
        "fmt"

        "github.com/spf13/viper"
    )

    func main() {
        v := viper.New()

        //v.SetConfigName("config")  // 默认就是config
        v.SetConfigType("yaml")
        v.AddConfigPath(".")

        if err := v.ReadInConfig(); err != nil {
            fmt.Printf("err:%s\n", err)
        }

        fmt.Println(v.Get("Postcode"))
    }

### 其他资料

- [golang常用库：配置文件解析库/管理工具-viper使用](https://www.cnblogs.com/jiujuan/p/13799976.html)
- [Github viper库](https://github.com/spf13/viper)

