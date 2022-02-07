Title: Golang YAML解析 - yaml.v2
Date: 2021-07-25 23:43:43
Tags: Golang
Slug: golang-yaml-v2
Authors: sin
Summary: Golang YAML解析

配置文件t2.yaml如下:

    :::yaml
    user: xuanmingyi
    host: node1
    password: 111111

    agent:
      enable: true

解析代码

    :::go
    package main

    import (
        "fmt"
        "io/ioutil"
        "os"

        yaml "gopkg.in/yaml.v2"
    )

    type agent struct {
        Enable bool `yaml:"enable"`
    }

    type config struct {
        User string `yaml:"user"`
        Host string `yaml:"host"`
        Password string `yaml:"password"`
        Agent agent `yaml:"agent"`
    }


    func main() {
        conf := new(config)

        // 读取内容
        content, err := ioutil.ReadFile("t2.yaml")
        if err != nil {
            fmt.Println(err)
            os.Exit(1)
        }

        // yaml解析
        err = yaml.Unmarshal(content, conf)
        if err != nil {
            fmt.Println(err)
            os.Exit(1)
        }

        fmt.Println(conf.User)
        fmt.Println(conf.Host)
        fmt.Println(conf.Password)

        fmt.Println(conf.Agent)
        fmt.Println(conf.Agent.Enable)
    }


输出为

    :::bash
    xuanmingyi
    node1
    111111
    {true}
    true