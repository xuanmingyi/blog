Title: Java-DateTime(时间)
Date: 2021-12-07 07:08:43
Tags: Java
Slug: java-datetime
Authors: sin
Summary: Java中的时间相互转换

常用时间库[joda-time](https://www.joda.org/joda-time/)

    :::xml
    <!-- https://mvnrepository.com/artifact/joda-time/joda-time -->
    <dependency>
        <groupId>joda-time</groupId>
        <artifactId>joda-time</artifactId>
        <version>2.10.13</version>
    </dependency>


#### 时间操作

首先我们搞情况有哪些时间相关的**Java**类型

    :::java
    import java.util.Date;
    import java.util.Calendar;
    import org.joda.time.DateTime;


###### 获取当前时间戳

当前时间戳返回的是毫秒数

    :::java
    System.currentTimeMillis();
    new Date().getTime();
    Calendar.getInstance().getTimeInMillis();
    DateTime.now().getMillis()


###### 从时间戳初始化DateTime

    :::java
    DateTime dateTime = new DateTime(222222);
    dateTime.toString("yyyy-MM-dd HH:mm:ss");
    // 1970-01-01 08:03:42


###### 格式化时间

    :::java
    new DateTime().toString("yyyy-MM-dd HH:mm:ss");
    // 2021-12-07 06:49:15

    DateTime dateTime = DateTimeFormat.forPattern("yyyy-MM-dd HH:mm:ss").parseDateTime("2020-01-01 22:22:22");
    dateTime.getYear();
    // 2020



#### 参考

* [java获取当前时间戳的方法](https://www.cnblogs.com/williamjie/p/9259591.html)
* [JAVA中Calendar与Date类型互转](https://blog.csdn.net/fz13768884254/article/details/82422752)

