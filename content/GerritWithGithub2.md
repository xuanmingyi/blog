Title: Gerrit With Github(2)
Date: 2015-07-16 15:36
Tags: gerrit
Authors: Sin
Category: Technology 

###引言
[上一篇](http://blog.xuanmingyi.com/gerrit-with-github1.html)中，初步部署好了Gerrit，然后可以使用Github账户登录，第一个登录的默认为Admin用户。

###加入*SSH Public Key*

* 把本机的公钥加入Gerrit中的*SSH Public Key*。
* 把本机的公钥加入到Github中的*SSH Public Key*。
* 把服务器上的公钥加入到*SSH Public Key*。

###导入Github中的项目

Github上创建项目，并在本地进行初始化。

	git clone git@github.com:xuanmingyi/test.git
	cd test
	echo "Hello world!">README.md
	git add README.md
	git commit -m "init project"
	git push origin master
	
使用ssh在Gerrit上创建项目

	ssh -p 29418 username@host gerrit create-project test #填上自己username和host
	
在服务器上找到git目录，并删除项目，导入Github项目

	cd ~/git
	rm -fr test.git
	git clone --bare git@github.com:xuanmingyi/test.git


给项目添加`.gitreview`文件

	cat >.gitreview <<EOF
	[gerrit]
	host=106.185.26.249
	port=29418
	project=test.git
	EOF
	
当修改好之后
	
	git add .
	git commit -m "new commit"
	git review

到这里，我们可以看到，已经走review了。


###后续

到这里，流程还只能把我们提交的代码合并到Gerrit的代码仓库里，在我们合并同时要推送到github上，我们还需要使用插件`Replication`。