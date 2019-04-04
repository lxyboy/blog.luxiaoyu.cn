---
title: 国内开发者常用镜像
date: 2017-04-07 08:16:17
update: 2017-04-16 22:03:23

categories:
- Linux技术
 
tags: 
- mirrors
- linux日常
- linux

keywords:
 - 镜像服务器
 - pip速度慢
 - pip加速
 - pip缓存
 - pipmirror
 - apt-get速度慢
 - apt-get加速
 - apt-get
 - pip download
 - pip配置
---

## 前言

在国内开发软件，需要各种网络资源，但是很多开源软件的在中国进行更新的带宽都非常小，安装需要等待许久时间，因此这里就记录下我学习中
经常要用到的镜像加速的方法


## pip加速

现推荐下面几个的pip包安装源

* https://mirrors.aliyun.com/pypi/simple/
* https://pypi.doubanio.com/simple/
* https://pypi.mirrors.ustc.edu.cn/simple/

使用方法很简单 
`pip install django -i https://mirrors.aliyun.com/pypi/simple/`

这存在两个问题，第一每次安装都需要输入参数太麻烦
第二每创建一个新的虚拟环境pip安装时都需要到镜像站点重新下载。
第一个问题的办法是创建[pip配置文件](https://pip.pypa.io/en/stable/user_guide/#config-file)。
第二问题的办法在pip文档上有说明[从本地安装python包](https://pip.pypa.io/en/stable/user_guide/#installing-from-local-packages)。

这里给出我的配置文件`~/.pip/pip.conf`
**注意：** 我的pip版本为9.0版本[^1]

```
[global]
index-url = http://pypi.doubanio.com/simple
trusted-host = pypi.doubanio.com

[install]
find-links = /home/luxy/www/pip-downloads

[download]
dest = /home/luxy/www/pip-downloads

#如果存在则重写
#exists-action = w

[list]
format = columns
```

配置结束之后，可以通过以下两个命令进行缓存安装
```bash
# 缓存安装包到 /home/luxy/www/pip-downloads
pip download django
# 安装django 如果在/home/luxy/www/pip-downloads中找不到，则会通过index-url进行安装
pip install django
```


## apt-get 加速

apt-get 是在 ubuntu系统中的包管理软件，经常使用，因此加速很有必要，下面推荐几个加速的站点

apt-get [配置生成器](http://mirrors.ustc.edu.cn/help/ubuntu.html)

把生成的内容替换到 `/etc/apt/sources.list` 文件中

* 网易: [http://mirrors.163.com/.help/ubuntu.html](http://mirrors.163.com/.help/ubuntu.html)
* USTC：[http://mirrors.ustc.edu.cn/help/ubuntu.html](http://mirrors.ustc.edu.cn/help/ubuntu.html)
* 北京理工大学 [http://mirror.bit.edu.cn/ubuntu/](http://mirror.bit.edu.cn/ubuntu/)
* 北京交通大学 [http://mirror.bjtu.edu.cn/ubuntu/](http://mirror.bjtu.edu.cn/ubuntu/)

详细的配置方法在help文件中就能找到


[^1]: pip从6.0版本开始不使用`pip install --download-cache`。详见[pip Release Notes](https://pip.pypa.io/en/stable/news/)。