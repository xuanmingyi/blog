Title: Golang string和其他类型之间的转换(3)
Date: 2021-06-08 21:13:43
Tags: Golang
Slug: golang-string-convert-others
Authors: sin
Summary: Golang string类型转换

### 代码片段

    :::go
    fmt.Println(strconv.Atoi("1111"))   // 1111 <nil>
    fmt.Println(strconv.Itoa(1111))     // 1111

    // PasteXXX
    fmt.Println(strconv.ParseInt("1111", 10, 64))  // 1111 <nil>
    fmt.Println(strconv.ParseUint("ff", 16,64))    // 255 <nil>
    fmt.Println(strconv.ParseBool("TRUE"))             // true <nil>
    fmt.Println(strconv.ParseFloat("1.111", 64)) // 1.111 <nil>

    // FormatXXX
    fmt.Println(strconv.FormatInt(255, 16))   // ff
    fmt.Println(strconv.FormatUint(255, 16))  // ff
    fmt.Println(strconv.FormatBool(true))          // true
    // 复杂，查链接
    fmt.Println(strconv.FormatFloat(1.1111, 'E', -1, 32)) // 1.1111E+00


### 参考

- [Go基础系列: 数据类型装换(strconv包)](https://www.cnblogs.com/f-ck-need-u/p/9863915.html)