Title: DockerFAQ
Date: 2015-04-30 10:44
Tags: Docker
Authors: Sin
Category: Technology

![](https://d3oypxn00j2a10.cloudfront.net/0.17.3/img/nav/docker-logo-loggedout.png)

**如何进入docker，并且退出**

docker attach 进入某个contaienr之后, _ctrl+p_ _ctrl+q_ ，让container后台运行，exit则直接退出container，整个container stop了.

**如何在host和container之间传递数据**

从container里复制文件或者目录到host上，命令如下

	docker cp 5e1ce281984a:/root ./

从host上复制文件或者目录到container里

	docker exec -i 5e1ce281984a bash -c "cat > /root/test.file" < test.file
	
上面命令要求container必须是运行中，复制的必须是文件


	tar -cf - ./horizon | docker exec -i 5e1ce281984a  /bin/tar -C /root -xf -
	
把当前的目录中的horizon目录复制到对应容器root中，这个不仅需要container是运行状态，还需要container中有tar程序

另外，在启动之前，可以使用run命令的 -v选项直接挂载host的目录到container中

[参考](http://stackoverflow.com/questions/22907231/copying-files-from-host-to-docker-container)
