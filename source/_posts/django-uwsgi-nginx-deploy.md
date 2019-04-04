---
title: Django uwsgi nginx 部署小记
date: 2015-04-05 08:16:17
updated: 2015-04-06 10:12:11

categories: 
- Python技术

tags: 
- python
- django
- nginx

keywords: 
 - nginx 
 - uwsgi
 - python
 - Django部署
---

## 环境

* ubuntu 16.10
* nginx version: nginx/1.10.1 (Ubuntu)
* uwsgi version: 2.0.12-debian


**提示**：
* 这里的uwsgi使用的是通过ubuntu deb包安装的uwsgi程序
* pip配置国内镜像[^1]
* apt-get配置国内镜像[^2]
[^1]: pip镜像配置方法：[http://blog.luxiaoyu.cn/mirrors_in_china/](http://blog.luxiaoyu.cn/mirrors_in_china/)
[^2]: apt-get镜像配置方法：[http://blog.luxiaoyu.cn/mirrors_in_china/](http://blog.luxiaoyu.cn/mirrors_in_china/)
  
## 安装

```bash
sudo apt-get update
# 安装uwsgi uwsgi-core uwsgi-plugin-python  单独通过pip安装uwsgi的不同点之后描述
sudo apt-get install uwsgi uwsgi uwsgi-core uwsgi-plugin-python nginx python-dev python-virtualenv
```

## 创建django工程projectname

```bash
# 切换到当前Home目录
cd ~
# 创建virtualenv虚拟环境目录及项目虚拟环境projectname
mkdir venv
virtualenv venv/projectname --no-wheel --no-setuptools
# 进入虚拟环境 这是会出现类似 (projectname) luxy@ubuntu:~$的提示符
source venv/projectname/bin/activate
# 升级pip 并安装django
pip install -U pip
pip install django
# 创建django工程目录及django工程并进入django工程
mkdir -p project; cd project
django-admin startproject projectname; cd projectname
# 测试django工程是否正常运行 进入界面进行验证
python manage.py runserver 0.0.0.0:8000
# 创建静态文件目录这个目录可以用来收集django自带的静态文件，参照django配置
mkdir -p ~/www/projectname.yourdomain.com
```

wsgi应用程序在projectname的`projectname/wsgi.py`这个文件中定义

## 配置uwsgi配置

ubuntu的uwsgi deb包安装的配置文件在 `/etc/uwsgi`目录中

```txt
/etc/uwsgi/
├── apps-available
│   └── README
└── apps-enabled
    └── README
```

`/usr/share/uwsgi/conf/default.ini`这个文件为每个app的默认的配置

apps-enabled文件夹中是每个uwsgi app有效的配置文件
apps-available中配置项目 projectname 的wsgi配置文件 
`vim /etc/uwsgi/apps-available/projectname.uwsgi.ini`
然后通过ln -s 链接到 apps-enabled文件夹中


```ini /etc/uwsgi/apps-available/projectname.uwsgi.ini
[uwsgi]
# http协议 可不添加
http = 0.0.0.0:9902
# wsgi socket协议 可不添加
socket = 127.0.0.1:9901

chdir = /home/luxy/project/projectname
wsgi-file = projectname/wsgi.py
processes = 10
threads = 5
uid = www-data
git = www-data
virtualenv = /home/luxy/venv/projectname
```

链接配置文件到 `/etc/uwsgi/apps-enabled/` 文件夹下并重启uwsgi服务
```bash
sudo ln -s /etc/uwsgi/apps-available/projectname.uwsgi.ini /etc/uwsgi/apps-enabled/projectname.uwsgi.ini
sudo service uwsgi restart
```

## 配置nginx服务器

```apache /etc/nginx/sites-enabled/projectname.nginx.conf
server {
        listen 80 ;
        listen [::]:80 ipv6only=on;

        root /usr/share/nginx/html;
        index index.html index.htm;

        server_name projectname.yourdomain.com;

        location /static{
                root /home/luxy/www/projectname.yourdomain.com;
        }
        location /uploads{
                root /home/luxy/www/projectname.yourdomain.com;
        }
        location /{
                uwsgi_pass unix:/var/run/uwsgi/app/projectname.uwsgi/socket;
                uwsgi_param QUERY_STRING $query_string;
                uwsgi_param REQUEST_METHOD $request_method;
                uwsgi_param CONTENT_TYPE $content_type;
                uwsgi_param CONTENT_LENGTH $content_length;
                uwsgi_param REQUEST_URI $request_uri;
                uwsgi_param PATH_INFO $document_uri;
                uwsgi_param DOCUMENT_ROOT $document_root;
                uwsgi_param SERVER_PROTOCOL $server_protocol;
                uwsgi_param REQUEST_SCHEME $scheme;
                uwsgi_param HTTPS $https if_not_empty;
                uwsgi_param REMOTE_ADDR $remote_addr;
                uwsgi_param REMOTE_PORT $remote_port;
                uwsgi_param SERVER_PORT $server_port;
                uwsgi_param SERVER_NAME $server_name;
        }
}
```

重启nginx服务`sudo service nginx restart`
