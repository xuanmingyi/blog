Title: Rust字符串(String与&str)
Date: 2021-09-04 11:02:43
Tags: Rust
Slug: rust-string
Authors: sin
Summary: Rust 字符串简单使用

![logo](https://gitee.com/xuanmingyi/imagebed/raw/master/img/5a248db40dd54029a86f7f6dfe0bb283~tplv-k3u1fbpfcp-zoom-1.png)


一般提到**Rust字符串**我们指的是两个类型:

* **String(字符串类型)**
* **&str(字符串切片)**



### 字符串创建

    :::rust
    // 方法1
    let s1 = String::from("hello");

    // 方法2
    let s1 = "hello".to_string();



### 使用push_str更新字符串

    :::rust
    let mut s1 = String::from("foo");
    let s2 = String::from("boo");

    s1.push_str("boo");
    s1.push_str(&s2);

这里使用 **&str** 和 **&String**(Deref coercion)都可以。 



### 使用push添加字符

    :::rust
    let mut s1 = String::new();
    s1.push('我');
    s1.push('哈');


### 使用+字符串连接

我们先看一个错例

    :::rust
    let s1 = "hello";
    let s2 = "world";
    let s3 = s1 + s2; // 编译报错， 无法对两个&str做 + 运算

+的第一个参数必须是String

    :::rust
    let s1 = String::from("hello");
    let s2 = "world";
    let s3 = s1 + s2;



| 类型            | 结果                                                         |
| --------------- | ------------------------------------------------------------ |
| &str + &str     | 报错(`+` cannot be used to concatenate two `&str` strings)   |
| &str + String   | 报错(`+` cannot be used to concatenate a `&str` with a `String`) |
| String + &str   | 成功                                                         |
| String + String | 报错(expected `&str`, found struct `String`)                 |
| String + &String | 成功 Deref coercion |



**特别注意**

    :::rust
    let s1 = String::from("foo")
    let s2 = String::from("bar")
    let s3 = s1 + &s2; // s1 被借出 相当于 fn add(self, s: &str) -> String {...}

    // s1 不可用，s2可用


### format！宏

    :::rust
    let s1 = String::from("1");
    let s = format!("{} - {} - {}", s1, s2, s3);


### len()长度

这里的长度返回的是字符串所占byte数量，中文的话注意utf8, uincode 标量值

    :::rust
    let s1 = String::from("hello").len();
    let s2 = "world".len();
    let s3 = "中文".len();

    println!("s1.len()={} s2.len()={} s3.len()={}", s1, s2, s3); // s1.len()=5 s2.len()=5 s3.len()=6


### 遍历字符串

    :::rust
    for b in s1.bytes() {
        println!("{}", b);
    }

    for c in s1.chars() {
        println!("{}", c);
    }


### 切割字符串

    :::rust
    let s1 = String::from("中文");
    let s2 = &s1[0..3];

    println!("{}", s2);
