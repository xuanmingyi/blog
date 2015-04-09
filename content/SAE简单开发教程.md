Title: SAE简单开发教程
Date: 2015-01-01 07:23
Tags: SAE
Authors: Sin
Category: Technology

**SAE是什么**

SAE全称是Sina App Engine，可以方便的托管,只需要专注于网站代码逻辑就可以了，不需要管后台数据库是否可用，系统是否稳定等。不能说他有多好，但是相比于你花的钱，绝对是超值的，一天一块钱的服务，你还想有什么要求呢？废话不多说了，上教程。

**应用访问**

在一个应用创建好之后,可以通过 *应用名字.sinaapp.com* 来访问，例如 thinkspirit.sinaapp.com。

![](http://ww3.sinaimg.cn/mw690/68ef69degw1eneau30wvkj208m03mjrf.jpg)

**下载代码**

首先确定你的系统中有版本管理工具subversion(svn),SAE使用subversion来部署代码。

登陆SAE管理平台  http://sae.sina.com.cn/ 找到对应的应用，svn仓库地址可以在对应的项目-&gt;代码管理页面底部看到。

使用svn下载的命令如下


    svn co https://svn.sinaapp.com/thinkspirit/

然后输入对应的SAE安全邮箱和安全密码，如果他问你是否明文存储密码，可以打yes。


    Authentication realm: <https://svn.sinaapp.com:443> SAE User Auth for SVN
    Password for 'root':
    Authentication realm: <https://svn.sinaapp.com:443> SAE User Auth for SVN
    Username: xuanmingyi@qq.com
    Password for 'xuanmingyi@qq.com':
    
    -----------------------------------------------------------------------
    ATTENTION!  Your password for authentication realm:
    
    <https://svn.sinaapp.com:443> SAE User Auth for SVN
    
    can only be stored to disk unencrypted!  You are advised to configure
    your system so that Subversion can store passwords encrypted, if
    possible.  See the documentation for details.
    
    You can avoid future appearances of this warning by setting the value
    of the 'store-plaintext-passwords' option to either 'yes' or 'no' in
    '/root/.subversion/servers'.
    -----------------------------------------------------------------------
    Store password unencrypted (yes/no)? yes
    A    thinkspirit/1
    A    thinkspirit/1/config.yaml
    A    thinkspirit/1/index.php
    Checked out revision 1.

到这里，代码已经下载到本地了。

**修改代码**

打开对应的index.php文件，可以看到如下代码

    <?php
    echo '<strong>Hello, SAE!</strong>';

我们把他修改为


    <?php phpinfo(); ?>

**上传修改过之后的代码**

修改好了代码，使用svn上传到svn仓库，SAE就会帮你自动部署好。


    [root@localhost 1]# svn commit -m "add function phpinfo() to index.php"
    Sending index.php
    Transmitting file data .
    Committed revision 2.


**验证**
完成上传之后，打开原来的应用地址 thinkspirit.sinaapp.com 可以看到如下效果，到此为止，SAE的简单开发教程完成！
![](http://ww1.sinaimg.cn/mw690/68ef69degw1eneaobx7a7j20go0auwel.jpg)
