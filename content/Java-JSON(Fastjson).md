Title: Java-JSON(Fastjson)
Date: 2021-12-07 06:31:43
Tags: Java
Slug: java-json-fastjson
Authors: sin
Summary: Java中使用Fastjson

[Fastjson](https://mvnrepository.com/artifact/com.alibaba/fastjson) 是常用的JSON库之一

    :::xml
    <dependency>
        <groupId>com.alibaba</groupId>
        <artifactId>fastjson</artifactId>
        <version>1.2.78</version>
    </dependency>

#### JAVA对象转换为JSON字符串

    :::java
    String text = JSON.toJSONString(obj);

更具体的示例

    :::java
    JSONObject obj = new JSONObject();

    List<String> h1 = new ArrayList<String>();
    h1.add("hello31");
    h1.add("hello32");

    HashMap<String, String> h2 = new HashMap<String, String>();
    h2.put("a41", "hello411");
    h2.put("a42", "hello421");

    obj.put("a1", "hello1");
    obj.put("a2", "hello2");
    obj.put("a3", h1);
    obj.put("a4", h2);

    System.out.println(obj);
    // {"a1":"hello1","a2":"hello2","a3":["hello31","hello32"],"a4":{"a42":"hello421","a41":"hello411"}}


#### JSON字符串转换为JAVA对象

    :::java
    VO vo = JSON.parseObject("{...}", VO.class);

更具体的示例

    :::java
    @Data
    class VO {
        String a1;
        String a2;
        List<String> a3;
        HashMap<String, String> a4;
    }


    VO vo = JSON.parseObject("{\"a1\":\"hello1\",\"a2\":\"hello2\",\"a3\":[\"hello31\",\"hello32\"],\"a4\":{\"a42\":\"hello421\",\"a41\":\"hello411\"}}", VO.class);

    System.out.println(vo);
    // VO(a1=hello1, a2=hello2, a3=[hello31, hello32], a4={a42=hello421, a41=hello411})


#### @JSONField

设置JSON序列化和反序列化的Field名字

    :::java
    @Data
    class VO {
        @JSONField(name="name")
        String a1;

        @JSONField(name="age")
        int a2;
    }

    VO vo = new VO();
    vo.setA1("sin");
    vo.setA2(30);

    System.out.println(JSON.toJSONString(vo));
    // {"age":30,"name":"sin"}



#### 参考

* [Fastjson 简明教程](https://www.runoob.com/w3cnote/fastjson-intro.html)

