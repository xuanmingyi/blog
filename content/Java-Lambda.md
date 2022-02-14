Title: Java Lambda
Date: 2022-02-14 09:21:48
Tags: Java,Lambda
Slug: java-lambda
Authors: sin
Summary: Java Lambda表达式

### Java中的函数式编程

#### filter

filter 用来过滤出数据,下列代码把大于10的元素过滤出来

    :::java
    Integer[] mylist = {1, 3, 5, 7, 3, 2, 3, 4, 5, 64};
    Arrays.stream(mylist).filter(number -> number > 10).forEach(item -> System.out.printf("%d ", item));


#### map

map 用来对每一个元素做操作,下列代码把每个元素扩大3倍

    :::java
    Integer[] mylist = {1, 3, 5, 7, 3, 2, 3, 4, 5, 64};
	Arrays.stream(mylist).map(number -> number * 3).forEach(item -> System.out.printf("%d ", item));

#### forEach

forEach用来操作每个元素

虽然都是对所有元素进行操作，而map和forEach差别还是蛮大的。 

map主要关注于返回值，返回值组成一个新的stream

forEach主要关注于操作，而忽略返回值