Title: Golang Map集合(5)
Date: 2021-06-08 22:16:19
Tags: Golang
Slug: golang-map-collection
Authors: sin
Summary: Golang 标准库 map 简介

### 基本操作

    :::go
    var aMap map[string]string
    fmt.Println(aMap == nil)     // true
    //aMap["a11"] = "abc"        // 报错
    //fmt.Println(aMap["a11"])

    aMap = make(map[string]string)  // 创建一个map
    fmt.Println(aMap == nil)        // false

    aMap["a11"] = "abc"
    fmt.Println(aMap["a11"])   // 输出"abc"

    val, ok := aMap["a12"]
    fmt.Println(val)  // val == "" 
    fmt.Println(ok)   // false

### 直接赋值

    :::go
    aMap := map[string]string{
        "a11": "abc",
        "a12": "bbc",
        "a13": "cbc",
    }
    fmt.Println(aMap["a11"])

### 遍历

    :::go
    aMap["a11"] = "abc"
    aMap["a12"] = "bbc"
    aMap["a13"] = "cbc"
    for key := range aMap {
      fmt.Println(key, aMap[key])
    }
    for key, val := range aMap {
      fmt.Println(key, val)
    }
    //a11 abc
    //a12 bbc
    //a13 cbc

### 删除元素

    :::go
    delete(aMap, "a11")  // 删除a11元素
    delete(aMap, "b11")  // 不存在b11元素，不报错