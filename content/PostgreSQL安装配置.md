Title: PostgreSQL安装配置
Date: 2021-12-05 11:20:43
Tags: PostgreSQL,数据库
Slug: postgresql-install
Authors: sin
Summary: PostgreSQL安装使用

#### 安装PostgreSQL14

安装PostgreSQL14在[官网](https://www.postgresql.org/download/)上有介绍。非常全面。

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211202090805.png)

我们这里使用CentOS7

    :::bash
    # Install the repository RPM:
    sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

    # Install PostgreSQL:
    sudo yum install -y postgresql14-server

    # Optionally initialize the database and enable automatic start:
    sudo /usr/pgsql-14/bin/postgresql-14-setup initdb
    sudo systemctl enable postgresql-14
    sudo systemctl start postgresql-14


#### 登录数据库

切换用户，运行psql

    :::bash
    [root@centos7 ~]# su postgres
    bash-4.2$ psql
    could not change directory to "/root": Permission denied
    psql (14.1)
    Type "help" for help.

下面包括一些常用操作

    :::plain
    \l       # 列出所有数据库
    \c 数据库 # 连接数据库
    \d       # 列出所有表
    \d 表名   # 列表所有列
    \q       # 退出数据库 ctrl+d

#### 数据库常用操作

##### 创建与删除数据库

    :::sql
    create database xuanmingyi;
    drop database xuanmingyi;
##### 创建与删除表

    :::sql
    create table company(id int primary key not null, name text not null, age int not null);
    drop table company;

#### 数据操作

##### 插入

    :::sql
    insert into company (id, name, age) values (1, 'xxx', 12);

##### 更新

    :::sql
    update company set name='xmy' where id=1;

##### 查找

    :::sql
    select * from company where id = 1;

##### 删除

    :::sql
    delete from company where id = 1;


#### 用户以及权限

##### 创建用户

使用postgres用户登录postgresql

    :::sql
    create user xmy with password '123456';
    create database xmydb owner xmy;
    grant all privileges on database xmydb to xmy;

在Linux系统中添加用户

    :::bash
    adduser xmy

切换用户

    :::bash
    su xmy
    psql -d xmydb


##### 远程访问授权

修改配置文件*/var/lib/pgsql/14/data/postgresql.conf*

    :::ini
    listen_addresses = '*'

修改配置文件*/var/lib/pgsql/14/data/pg_hba.conf*

    :::ini
    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    host    all             all             0.0.0.0/0               md5


可以远程连接啦

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211202102821.png)
