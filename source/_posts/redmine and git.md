---
title: Redmine 和 git 集成
date: 2014-05-23 08:16:17
update: 2017-05-23 22:03:23

categories:
- Linux技术
 
tags: 
- 项目管理
- linux
- 开发工具

keywords:
 - redmine安装
 - redmine和git集成
 - 项目管理神器
---

## 环境

Ubuntu 14.04
Redmine 2.6.0

## Redminde安装

按照官网进行安装[http://www.redmine.org/projects/redmine/wiki/RedmineInstall](http://www.redmine.org/projects/redmine/wiki/RedmineInstall)

安装依赖时使用Bundler管理gems的依赖，如果遇到失败，主要原因为相应的系统库库未安装
例如：安装 rmagick 时 需要安装 apt-get install imagemagick libmagickwand-dev

对于gem的安装需要重新设定gem的源， 国外的源无法接通, 参照[http://ruby.taobao.org/](http://ruby.taobao.org/)。

官网步骤测试安装通过Redmine安装成功

### 关于Redmine运行在unicorn_rails

这个服务是用来跑redmine具体架构可以参照图

unicorn_rails -c config/unicorn.rb -E production -D
*-D*：说明以daemon形式运行
*-E*：传入参数说明是production运行Redmine

unicorn.rb文件的内容为

```txt
worker_processes 2

working_directory "/var/www/redmine-2.6.0"

listen "/run/redmine.socket", :backlog => 1024
#listen "0.0.0.0:8091", :tcp_nopush => true

timeout 60

user "www-data", "www-data"

stderr_path "/var/log/redmine/unicorn.stderr.log"
stdout_path "/var/log/redmine/unicorn.stdout.log"
```

*listen*是与外界通信的方式，可以选择socketfile或者通过监听地址，可以先采用监听地址判断服务器是否正常运行后再通过socket文件与nginx交互

*user*是说明服务运行与www-data:www-data用户组下这个原因是为了与nginx的用户组相同这样nginx就可以直接读取socket文件了。

###关于Redmine配置邮件

```txt
production:
  email_delivery:
    delivery_method: :smtp
    smtp_settings:
      address: "xxx.xxx.cn"
      port: '587'
      domain: "xxx.xxx.cn"
      authentication: :plain
      user_name: "xxxxxx"
      password: "xxxxxx" 
      openssl_verify_mode: 'none'
```

*注意*：配置文件都是空格，不要有tab，tab不被识别的


## git http backend部署说明

**注意**：该方法已被废弃，使用gitlab代替

参照官网部署[https://www.kernel.org/pub/software/scm/git/docs/git-http-backend.html](https://www.kernel.org/pub/software/scm/git/docs/git-http-backend.html)


##关于结合redmine用户认证

通过redmine2.6.0包下extra/svn/Redmine.pm的配置
具体配置方法可阅读Redmine.md（vim extra/svn/Redmine.pm）有说明
这个脚本使得apache2 basic auth能够认证Redmine的用户和密码。这个脚本问题多多。
在我的部署环境下需要通过注释apache配置文件中```perlAccessHandler```这个选项才解决错误问题。


##关于Redmine自动更新Activity

Redmine可以通过POST以下url进行更新：

http://redmine.host/sys/fetch_changesets?key=$_apikey

使用git post recieve
用来触发redmine获取changesets，主要
编辑服务器项目的git目录下```hook/post-receive```文件，并赋予可执行权限

```txt
#!/bin/sh
_apikey=jZcX1DERBQ07ftjwCqi5
curl http://redmine.host/sys/fetch_changesets?key=$_apikey
```

