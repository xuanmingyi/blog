Title: Spring源码导入IDEA
Date: 2021-11-26 10:23:43
Tags: Spring,Java
Slug: spring-source-import-idea
Authors: sin
Summary: Spring源码导入IDEA并运行测试

#### 参考文章

* [Idea导入SpringBoot源码终极版(基于Gradle)](https://blog.csdn.net/hell_oword/article/details/111757888)



#### IDEA、JDK 与Gradle

* [IntelliJ *IDEA*](https://www.jetbrains.com/idea/download/#section=linux)

* 使用[sdkman](https://sdkman.io/)安装JDK11,注意安装的版本是11.0.12-open，不要使用11.0.11.j9-adpt
* 使用[sdkman](https://sdkman.io/)安装Gradle



#### 源码准备

如果是linux上，比如我用的mint，直接可以下载拉取代码

    :::bash
    git clone https://github.com/spring-projects/spring-boot.git

如果在windows上，请注意，你有可能会碰到**Filename too long**的报错，这种情况下，如果使用win8以上系统，你可以如下设置,[参考](https://blog.csdn.net/liuxiao723846/article/details/78329223)

    :::bash
    git config --global core.longpaths true


切换到对应*v2.5.7* tag

    :::bash
    git tag v2.5.7


#### 添加测试模块(参考上面文章)

新建模块


![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126100825.png)

名字改为*spring-boot-debug*

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126100941.png)



修改build.gradle文件，把java插件改成application



    :::groovy
    plugins {
        id 'application'
    }

    group 'org.springframework.boot'
    version '2.5.7'

    repositories {
        mavenCentral()
    }

    dependencies {
        annotationProcessor("org.projectlombok:lombok:1.18.22")
        annotationProcessor(project(":spring-boot-project:spring-boot-tools:spring-boot-configuration-processor"))
        implementation(project(":spring-boot-project:spring-boot-starters:spring-boot-starter-web"))
        implementation(enforcedPlatform(project(":spring-boot-project:spring-boot-dependencies")))
        implementation(project(":spring-boot-project:spring-boot"))
        implementation("jakarta.validation:jakarta.validation-api")
        implementation("org.projectlombok:lombok:1.18.22")
    }

    application {
        mainClass="org.springframework.debug.DemoApplication"
    }


*DemoApplication.java*代码

    :::java
    package org.springframework.debug;

    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;


    @SpringBootApplication
    public class DemoApplication {

        public static void main(String[] args) {
            SpringApplication.run(DemoApplication.class, args);
        }
    }



现在可以在模块中随便写一些测试代码


![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126101235.png)

同时，我们给对*SpringApplication.java*代码Banner代码上下打印出标识符号，如图所示。

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126101402.png)

运行这个application，如图输出则表示成功

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211126101526.png)
