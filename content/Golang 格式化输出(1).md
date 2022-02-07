Title: Golang 格式化输出(1)
Date: 2021-06-08 00:13:04
Tags: Golang
Slug: golang-format-printf
Authors: sin
Summary: Golang 标准库 fmt

### 代码片段

    :::go
    // 整数
    fmt.Printf("%b\n", 8)             // 二进制: 1000
    fmt.Printf("%08b\n", 8)           // 二进制: 00001000
    fmt.Printf("%c\n", '宣')          // Unicode字符: 宣
    fmt.Printf("%d\n", 0x80)          // 十进制: 128
    fmt.Printf("%04d\n", 8)           // 十进制: 0008
    fmt.Printf("%o\n", 8)             // 八进制: 10
    fmt.Printf("%04o\n", 8)           // 八进制: 0010
    fmt.Printf("%x\n", 15)            // 十六进制: f
    fmt.Printf("%X\n", 15)            // 十六进制: F
    fmt.Printf("%08X\n", 15)          // 十六进制: 0000000F

    // 浮点数
    fmt.Printf("%f\n", 1.233333333)   // 浮点数: 1.233333
    fmt.Printf("%.8f\n", 1.233333333) // 浮点数: 1.23333333
    fmt.Printf("%g\n", 1.233333333)   // 浮点数: 1.233333333

    // 指针
    var num int = 123
    fmt.Printf("%p\n", &num)          // 地址: 0xc0000a6018

    // 默认格式
    fmt.Printf("%v\n", &num)          // 地址: 0xc0000a6018

    // 默认%v
    type A struct {}
    func (a A) String() string {     // 注意函数签名
        return "sssss"
    }
    var a A
    fmt.Printf("%v\n", a)             // sssss
