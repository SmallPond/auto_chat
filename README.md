@author：Small_Pond

@date:2017.7.17    2017.8.5   2017.11.12

@version：v0.1     v0.2       v1.0

@V0.2相对v0.1加入可在群聊中发送信息

>v1.0 整体程序架构发生了改变
>
>1.使用了apscheduler来实现任务的定时发送

>2.编写了MyChat 类， 实现了简单的封装。 不在像v0.2版本那么粗糙

>3.加入了运行此程序的操作系统判断， 可生出终端界面的二维码


##说明：在dist文件下的exe文件，依旧是v0.2版本生成的。如果需要v1.0版本的exe可执行文件，私我

##此程序依赖的第三方库：
>1.itchat

>2.apscheduler

都可通过pip 安装

	pip install itchat 
	pip install apscheduler

###程序功能：基于itchat的微信定时发送消息

###程序说明：对配置文件task_file.txt进行配置时，可使用‘#’开头注释一行文字

##使用方法：

1.在文件task_file.txt中进行配置

![](http://i.imgur.com/cu9WGIR.png)

2.在命令行运行chat.py程序
	
	python chat.py 


##微信显示结果



###基本测试

![](http://i.imgur.com/nkauloR.png)

###群聊测试

![](http://i.imgur.com/jRr1YRE.png)
