#关于python转exe可执行程序在其他系统上运行时出现的错误
###说明：python转exe在win10上执行，无法运行在win7系统上

#一.win7旗舰版x64
###运行错误提示

![](http://i.imgur.com/XF8b0K3.png)

###解决办法
>下载api-ms-win-crt-runtime-l1-1-0.dll复制到系统文件中就行了
>
>(1)下载文件api-ms-win-crt-runtime-l1-1-0.dll文件到您的桌面上。
>
>(2)将api-ms-win-crt-runtime-l1-1-0.dll文件放到提示丢失的文件的程序目录下。
>
>(3)如果第2步是行不通的。将文件api-ms-win-crt-runtime-l1-1-0.dll到系统目录下。

>C:\Windows\System (Windows 95/98/Me)
>
>C:\WINNT\System32 (Windows NT/2000)
>
>C:\Windows\System32 (Windows XP, Vista)
>
>C:\Windows\System32 (Windows 7/8/2008r2)
>
>C:\Windows\SysWOW64 (Windows 7/8/2008r2)

###按上述操作后，出现另一个错误
![](http://i.imgur.com/6lTm6lJ.png)
###继续解决
>从百度搜索，发现是win7运行库缺失问题
>
>下载VC运行库并安装

解决方法参考:[无法定位程序输入点](http://blog.sina.com.cn/s/blog_8fc890a20102wgva.html)

[Microsoft .NET Framework 4.6.1](https://www.microsoft.com/zh-CN/download/confirmation.aspx?id=48145)

[Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/zh-cn/download/confirmation.aspx?id=49982)

###仍然无法运行？
[安装更新](https://support.microsoft.com/zh-tw/kb/2999226)

在此网站找到对应的系统版本进行下载，安装
![](http://i.imgur.com/CXQ1GRj.png)

###已亲测解决
>测试系统
>![](http://i.imgur.com/E6sZPcm.jpg)
