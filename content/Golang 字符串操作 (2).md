Title: Golang 字符串操作 (2)
Date: 2021-06-08 06:58:23
Tags: Golang
Slug: golang-strings-operation
Authors: sin
Summary: Golang 标准库 strings

### 代码片段

    :::go
    s1 := " aBc"
    s2 := "100a"
    s3 := s1 + s2
    fmt.Println(s3)

    // 前缀后缀
    fmt.Println(strings.HasPrefix(s3, "a"))      // false
    fmt.Println(strings.HasSuffix(s3, "0"))      // false

    // 包含
    fmt.Println(strings.Contains(s3, "9"))       // false

    // 找位置
    fmt.Println(strings.Index(s3, "0"))          // 5
    fmt.Println(strings.LastIndex(s3, "0"))      // 6
    // TODO IndexRune

    fmt.Println(strings.Replace(s3,"0","1",-1))  // " aBc111a",如果 n = -1 则替换所有字符串
    fmt.Println(strings.Count(s3,"0"))           // 2
    fmt.Println(strings.Repeat(s3,2))            // " aBc100a aBc100a"

    // 大小写
    fmt.Println(strings.ToLower(s3))             // " abc100a"
    fmt.Println(strings.ToUpper(s3))             // " ABC100A"

    // 去头去尾
    fmt.Println(strings.TrimSpace(s3))           // "aBc100a"
    fmt.Println(strings.Trim(strings.TrimSpace(s3),"a"))  // "Bc100"
    fmt.Println(strings.TrimLeft(strings.TrimSpace(s3), "a"))  // "Bc100a"
    fmt.Println(strings.TrimRight(strings.TrimSpace(s3),"a"))  // "aBc100"

    // 字符串切割和连接
    fmt.Println(strings.Split("a,b,c,d", ","))  // ["a", "b", "c", "d"]
    fmt.Println(strings.Join([]string{"a", "b", "c", "d"}, ","))

    // Map
    rdata := strings.Map(func(r rune) rune{
        if r != ' ' {
            return r
        }
            return -1
    }, s3)
    fmt.Println(rdata)     // aBc100a

#### 参考

 * [4.7 strings 和 strconv 包](https://blog.csdn.net/sanxiaxugang/article/details/60324012)
 * [Go 标准库介绍一: strings](https://www.cnblogs.com/action-go/p/11560190.html)
 * [golang标准库-strings](https://www.cnblogs.com/action-go/p/11560190.html)