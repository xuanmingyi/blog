Title: Spring Elasticsearch Neumann
Date: 2022-02-11 09:22:03
Tags: Spring,Elasticsearch,Java
Slug: spring-elasticsearch-neumann
Authors: sin
Summary: Spring Elasticsearch Neumann 使用指南

### 简介

从文档 [Spring Data Elasticsearch - Reference Documentation](https://docs.spring.io/spring-data/elasticsearch/docs/current/reference/html/) 可以查看到Spring 与 Elasticsearch之间的版本关系。

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20220210152607.png)



这里由于项目的需要，我们选取的是 Neumann版本，对应的是



* Spring Data Elasticsearch 4.0.x
* Elasticsearch 7.6.2
* Spring Framework 5.2.12
* Spring Boot 2.3.x



官方文档 [Spring Data Neumann goes GA](https://spring.io/blog/2020/05/12/spring-data-neumann-goes-ga)，注意需要使用的是这个文档。





### Elasticsearch 和 数据库 对比



|           SQL数据库           |     Elasticsearch      |
| :---------------------------: | :--------------------: |
|          column(列)           |      field(字段)       |
|            row(行)            |     document(文档)     |
|           table(表)           |      index(索引)       |
|         schema(模式)          |     mapping(映射)      |
| database server(数据库服务器) | Elasticsearch 集群实例 |





### 测试方法

我们使用如下测试代码作为测试基础



    :::java
    package com.example.demo;

    import org.junit.jupiter.api.Test;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.boot.test.context.SpringBootTest;

    @SpringBootTest
    public class ElasticsearchTests {

        @Autowired
        private ElasticsearchRestTemplate elasticsearchRestTemplate;

        @Test
        void testQuery() {
            // 测试代码
        }
    }

只需要修改**testQuery**内代码，就可以完成针对不同代码的测试。



#### 查询所有文档

查询一个索引中的所有数据。类似于查询语句

    :::sql
    select * from metric_server;

接下来是获取Elasticsearch数据

    :::java
    @Data
    class TestObject {
        private String name;
        private String region;
        private String resourceId;
    }

    @Test
    void testQuery() {
        Query query = new NativeSearchQueryBuilder()
                .withQuery(matchAllQuery())
                .build();

        IndexCoordinates indexCoordinates = IndexCoordinates.of("metric_server");

        List<TestObject> objs =  elasticsearchRestTemplate.queryForList(query, TestObject.class, indexCoordinates);

        for ( int i = 0 ; i < objs.size() ;i++) {
            System.out.println(objs.get(i));
        }
    }


![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20220210213133.png)



#### 根据条件简单查询



加上条件再做查询,类似于以下

    :::sql
    select * from metric_server where name = 'agenttest';

代码也比较简单，使用**termQuery**来匹配

    :::java
    @Test
    void testQuery() {
        TermQueryBuilder termQueryBuilder = QueryBuilders.termQuery("name", "agenttest");

        Query query = new NativeSearchQueryBuilder()
                .withQuery(termQueryBuilder)
                .build();

        IndexCoordinates indexCoordinates = IndexCoordinates.of("metric_server");

        List<TestObject> objs =  elasticsearchRestTemplate.queryForList(query, TestObject.class, indexCoordinates);

        for ( int i = 0 ; i < objs.size() ;i++) {
            System.out.println(objs.get(i));
        }
    }


##### 各匹配类型说明

|   Query类型   |               说明               |
| :-----------: | :------------------------------: |
|  matchQuery   |     分词，然后调用termQuery      |
|   termQuery   |         不分词，严格匹配         |
| wildcardQuery |            通配符匹配            |
|  fuzzyQuery   |             模糊匹配             |
|  rangeQuery   |             范围匹配             |
| booleanQuery  | 布尔匹配(几个匹配之间做布尔运算) |



#### 根据条件做复杂查询



做一个比较复杂的查询

    :::sql
    select * from metric_server where name = 'agenttest' and timestamp > '2021-02-10 00:00:00'


    :::java
    @Test
    void testQuery() {
        long sinceTime = System.currentTimeMillis() - 1000L*60*60;;

        BoolQueryBuilder boolQueryBuilder = QueryBuilders.boolQuery();

        boolQueryBuilder.must(termQuery("name", "agenttest"));
        boolQueryBuilder.must(QueryBuilders.rangeQuery("timestamp").gte(sinceTime));
        // boolQueryBuilder.filter(QueryBuilders.rangeQuery("timestamp").gte(sinceTime));
        // 同上

        Query query = new NativeSearchQueryBuilder()
                .withQuery(boolQueryBuilder)
                .build();

        IndexCoordinates indexCoordinates = IndexCoordinates.of("metric_server");

        List<TestObject> objs =  elasticsearchRestTemplate.queryForList(query, TestObject.class, indexCoordinates);

        for ( int i = 0 ; i < objs.size() ;i++) {
            System.out.println(objs.get(i));
        }
    }

运行如下图

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20220211000208.png)



其中**filter**和**must**在这里是一致的，但是他们在ES里还是有差别的，详细参考 



* [ElasticSearch中must和filter的区别](https://blog.csdn.net/fechinchu/article/details/112235154)
* [Es检索 must与filter区别](https://blog.csdn.net/weixin_45362084/article/details/112171627?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_paycolumn_v3&utm_relevant_index=1)



### 查询并排序



### 分页

### 集合 





### 参考



* https://www.cnblogs.com/jelly12345/p/14765477.html
* https://www.jianshu.com/p/56e755415e63
* https://blog.csdn.net/weixin_43814195/article/details/85281287
* https://www.cnblogs.com/moxiaotao/p/10843523.html
* https://blog.csdn.net/xx105/article/details/83827755
* https://blog.51cto.com/shadowisper/2393555
* https://blog.csdn.net/qq_42764468/article/details/107570357
