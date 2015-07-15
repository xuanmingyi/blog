Title: Gerrit With Github(1)
Date: 2015-07-16 01:42
Tags: gerrit
Authors: Sin
Category: Technology 


###更新系统
安装完Ubuntu系统后更新。

	sudo apt-get update -y
	sudo apt-get upgrade -y
	sudo apt-get install default-jdk maven2 git

###创建gerrit用户
创建gerrit用户，然后换到gerrit用户。

	sudo adduser gerrit
	su gerrit   # 换到gerrit用户下

###编译Github插件
下载Github插件，然后编译

	git clone https://gerrit.googlesource.com/plugins/github
	cd github
	mvn install
	
![](http://ww3.sinaimg.cn/mw690/68ef69degw1eu3w0amjndj20mr0910uw.jpg)

显示`BUILD SUCCESSFUL`就表示编译好了。

###下载Gerrit，并且部署

####下载
在[下载地址](https://gerrit-releases.storage.googleapis.com/index.html)中下载最新版本[gerrit-2.11.2.war](https://www.gerritcodereview.com/download/gerrit-2.11.2.war),然后直接部署。

####初始化部署
	部署中Enter为直接回车

	java -jar gerrit-2.11.2.war init -d ~/test_gerrit

	
	*** Gerrit Code Review 2.11.2
	***

	Create '/home/gerrit/test_gerrit'     [Y/n]? # 主目录，如果没有，则需要创建，直接回车

	*** Git Repositories
	***
	
	Location of Git repositories   [git]: # git存放目录

	*** SQL Database
	***

	Database server type           [h2]: # 选用h2默认数据库，以后可以改成MySQL等
	
	*** Index
	***

	Type                           [LUCENE/?]: # 索引引擎 LUCENE
	
	*** User Authentication
	***

	Authentication method          [OPENID/?]:HTTP         # 使用HTTP认证
	Get username from custom HTTP header [y/N]? Y          # 使用header认证
	Username HTTP header           [SM_USER]: GITHUB_USER  # Github认证
	SSO logout URL                 : /oauth/reset          # Logut 
	
	*** Review Labels
	***

	Install Verified label         [y/N]? Enter # 默认
	
	*** Email Delivery
	***

	SMTP server hostname           [localhost]: smtp.qq.com  # SMTP服务器
	SMTP server port               [(default)]:              # SMTP端口
	SMTP encryption                [NONE/?]:
	SMTP username                  [gerrit]: xuanmingyi      # 用户
	xuanmingyi's password          :                         # 密码
    	          confirm password :                         # 确认密码
	
	
	# 以下全部默认选项，一路回车
	
	*** Container Process
	***
	Run as                         [gerrit]:
	Java runtime                   [/usr/lib/jvm/java-7-openjdk-amd64/jre]:
	Copy gerrit-2.11.2.war to /home/gerrit/test/bin/gerrit.war [Y/n]?
	Copying gerrit-2.11.2.war to /home/gerrit/test/bin/gerrit.war

	*** SSH Daemon
	***

	Listen on address              [*]:
	Listen on port                 [29418]:

	Gerrit Code Review is not shipped with Bouncy Castle Crypto SSL v151
  		If available, Gerrit can take advantage of features
  		in the library, but will also function without it.
	Download and install it now [Y/n]?
	Downloading http://www.bouncycastle.org/download/bcpkix-jdk15on-151.jar ... OK
	Checksum bcpkix-jdk15on-151.jar OK

	Gerrit Code Review is not shipped with Bouncy Castle Crypto Provider v151
	** This library is required by Bouncy Castle Crypto SSL v151. **
	Download and install it now [Y/n]?
	Downloading http://www.bouncycastle.org/download/bcprov-jdk15on-151.jar ... OK
	Checksum bcprov-jdk15on-151.jar OK
	Generating SSH host key ... rsa... dsa... done

	*** HTTP Daemon
	***

	Behind reverse proxy           [y/N]?
	Use SSL (https://)             [y/N]?
	Listen on address              [*]:
	Listen on port                 [8080]:
	Canonical URL                  [http://localhost:8080/]:

	*** Plugins
	***

	Installing plugins.
	Install plugin reviewnotes version v2.11.2 [y/N]?
	Install plugin replication version v2.11.2 [y/N]?
	Install plugin download-commands version v2.11.2 [y/N]?
	Install plugin singleusergroup version v2.11.2 [y/N]?
	Install plugin commit-message-length-validator version v2.11.2 [y/N]?
	Initializing plugins.
	No plugins found with init steps.

	Initialized /home/gerrit/test
	Executing /home/gerrit/test/bin/gerrit.sh start


到这里初始化部署已经完成了。

###添加Github插件
	
	cp ~/github/github-oauth/target/github-oauth-*.jar ~/test_gerrit/lib/
	cp ~/github/github-plugin/target/github-plugin-*.jar ~/test_gerrit/plugins/github.jar


###重新部署

	java -jar gerrit-2.11.2.war init -d ~/test_gerrit
	
	..... # 一路回车
	
	# 这次会出现Github插件配置
	*** GitHub Integration
	***

	GitHub URL                     [https://github.com]:       # 直接回车
	GitHub API URL                 [https://api.github.com]:   # 直接回车

	NOTE: You might need to configure a proxy using http.proxy if you run Gerrit behind a 	firewall.

	*** GitHub OAuth registration and credentials
	***

	Register Gerrit as GitHub application on:
	https://github.com/settings/applications/new

	Settings (assumed Gerrit URL: http://localhost:8080/)
	* Application name: Gerrit Code Review
	* Homepage URL: http://localhost:8080/
	* Authorization callback URL: http://localhost:8080/oauth
	
	# 到这里需要转跳到 注册Github应用一节！获得`Client ID`和`Client Secret`再跳回	
	
	After registration is complete, enter the generated OAuth credentials:
	GitHub Client ID               : Client ID
	GitHub Client Secret           : Client Secret #不回显
    	          confirm password : Client Secret #不回显
	Gerrit OAuth implementation    [HTTP/?]:
	HTTP Authentication Header     [GITHUB_USER]:

	Initialized /home/gerrit/test
	.....
	
	
这次需要重建索引

	java -jar gerrit-2.11.2.war reindex -d ~/test_gerrit
	
修改配置文件 `~/test_gerrit/etc/gerrit.config`

	canonicalWebUrl = http://localhost:8080/
	改成你自己的IP的URL
	canonicalWebUrl = http://106.185.26.249:8080/

	
启动Gerrit

	test_gerrit/bin/gerrit.sh start


完成初步部署。

###注册GITHUB应用
访问[https://github.com/settings/applications/new](https://github.com/settings/applications/new)，`Homepage URL` 和 `Authorization callback URL`分别填上 你服务器的IP和端口，和 IP端口加上oauth。

比如你的服务器IP为106.185.26.249

* Homepage URL 为 http://106.185.26.249:8080/
* Authorization callback URL 为 http://106.185.26.249:8080/oauth
	
![](http://ww2.sinaimg.cn/mw690/68ef69degw1eu3yxrdrloj20kz0g7406.jpg)

获得`Client ID`和`Client Secret`。

