---
title: Ubuntu下NFS配置
date: 2017-04-24 08:16:17
update: 2017-04-24 22:03:23

categories:
 - Linux技术
 
tags: 
 - linux日常
 - linux
 
keywords:
 - NFS配置教程
 - NFS配置
---

## NFS配置

环境ubuntu14.04

###服务器：

安装

sudo apt-get install nfs-kernel-server

配置编辑 /etc/exports中添加要导出的目录

```txt
/ubuntu *(ro,sync,no_root_squash)
/home *(rw,sync,no_root_squash)
```

`*`可以填可以访问的主机的ip地址或者主机名

重启

sudo service nfs-kernel-server start

### 客户端：

安装客户端

sudo apt-get install nfs-common

**question**

sudo mount -t nfs -o rw,intr,soft,nolock,tcp,user=administrator 10.10.100.47:/var/www/html/sharefiles /home/administrator/Documents/sharefiles

