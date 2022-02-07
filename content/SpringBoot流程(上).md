Title: SpringBoot流程(上)
Date: 2021-11-26 16:29:43
Tags: Spring,Java
Slug: spring-boot-flow
Authors: sin
Summary: SpringBoot流程(上)

#### SpringBoot启动流程

Spring启动流程，最重要的就是这个函数。我们也是从这里开始入手。

    :::java
    SpringApplication.run(DemoApplication.class, args);

在网上，我找到一个比较不错的[分析图](https://www.processon.com/view/link/59812124e4b0de2518b32b6e)

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126141850.png)



启动代码主要分成2部分。


* **构造SpringApplication**
* **执行run方法**


#### 构造SpringApplication

构造函数包括一系列重载函数，最后调用下面这个函数

    :::java
    @SuppressWarnings({ "unchecked", "rawtypes" })
    public SpringApplication(ResourceLoader resourceLoader, Class<?>... primarySources) {
        this.resourceLoader = resourceLoader;
        Assert.notNull(primarySources, "PrimarySources must not be null");
        this.primarySources = new LinkedHashSet<>(Arrays.asList(primarySources));
        // #1 侦测web application type
        this.webApplicationType = WebApplicationType.deduceFromClasspath();
        // #2 获取bootstrap registry initializers
        this.bootstrapRegistryInitializers = getBootstrapRegistryInitializersFromSpringFactories();
        // #3
        // 获取 ApplicationContextInitializer 设置initializers
        // 获取 ApplicationListener 设置listeners
        setInitializers((Collection) getSpringFactoriesInstances(ApplicationContextInitializer.class));
        setListeners((Collection) getSpringFactoriesInstances(ApplicationListener.class));

        // #4 获取main函数所在类
        this.mainApplicationClass = deduceMainApplicationClass();
    }


###### #1 侦测web application type

有三种类型的web application type



* NONE
* SERVLET  
* REACTIVE



###### #2 获取bootstrap registry initializers 

Bootstrapper 同时调用初始化

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126161935.png)


###### #3 设置initializers和listener

修改一下代码，方便调试的时候可以直接查看变量

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126151012.png)


*setInitializers*只是简单的设置，不赘述

    :::java
    public void setInitializers(Collection<? extends ApplicationContextInitializer<?>> initializers) {
        this.initializers = new ArrayList<>(initializers);
    }


*listeners*同理

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126155500.png)



获取实例的方法如下，我们跟进去看下代码易得

    :::java
    private <T> Collection<T> getSpringFactoriesInstances(Class<T> type, Class<?>[] parameterTypes, Object... args) {
        ClassLoader classLoader = getClassLoader();
        // Use names and ensure unique to protect against duplicates
        // 从每个包的META-INF/spring.factories处获取实现了对应接口的class
        Set<String> names = new LinkedHashSet<>(SpringFactoriesLoader.loadFactoryNames(type, classLoader));

        // 利用反射实例化！
        List<T> instances = createSpringFactoriesInstances(type, parameterTypes, classLoader, args, names);

        // 根据order权重排序，初始化是有顺序的，数字越小越靠前
        AnnotationAwareOrderComparator.sort(instances);
        return instances;
    }

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126160205.png)

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126160352.png)


###### #4 获取main函数所在类

    :::java
    this.mainApplicationClass = deduceMainApplicationClass();

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126143913.png)

这一步，我们把定义的*DemoApplication*侦测到

#### 参考

* [SpringBoot启动原理](https://juejin.cn/post/6947316816079224862)