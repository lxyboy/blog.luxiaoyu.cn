---
title: VC运行库依赖问题
date: 2013-12-23 12:16:17
update: 2013-12-23 22:03:23

categories:
- windows技术
 
tags: 
- windows开发
- windows

keywords:
 - vc运行库依赖
 - 动态链接库依赖
 
---

## vc运行库

集成自己的程序时遇到一问题，在windows xp sp3  32bit下运行时，LoadLibaray函数返回错误，错误代码14001。查找该错误：

>用程序无法启动，因为应用程序的并行配置不正确。This application has failed to start because the application configuration is incorrect. Reinstalling the application may fix this problem.

凭感觉可能是由于程序在装载的时候动态链接函数未找到相应函数，比方加载的dllA，dllA依赖dllB，但dllB不存在。

一般来说在安装软件的时候都会安装相应的依赖文件。依赖问题应该是不太会产生的。

现在看自己的程序，由于自己编写程序的时候用了vs2010运行时库(msvcr100)。而程序依赖的dll文件在编译的时候却是用到了vs2008的运行库(msvcr90)，自己的系统中又没有2008的运行库。导致错误产生。

解决办法：

1. 安装vs2008运行时库
2. 把依赖的dll文件重新用vs2010运行库编译一遍。


*注意：*最好统一运行时库，如果不行则把依赖的dll文件打包放到应用程序目录下。