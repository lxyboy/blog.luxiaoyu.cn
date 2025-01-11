#vdistackclientserver vdistackclientadmin的开发环境部署

## 环境

1. python 2.7.6
2. ubuntu 14.04
3. mysqlserver 5.5

## 搭建步骤

### step 0 Preinstall

```
sudo apt-get install git python-pip python-dev libmysqlclient-dev
```

### step 1 下载源码

```
git clone http://10.10.100.47:18080/luxy/vdistackclientadmin.git; cd vdistackclientadmin
pip install -r requirements.txt
pip install MySQL-python
pip install django-jsonfield
```

**注意** pip 安装可能会遇到失败的情况，原因是系统的环境缺少相应的库，安装即可

### step 2 配置数据库

在远程数据中添加数据库```vdistackclient```
数据库编码为utf-8

配置文件 ```vim vdistackclientadmin/settings.py```

修改片段

```
#...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "vdistackclient",
        'USER': "luxy",
        'PASSWORD': 'cloudopen',
        'HOST': '10.10.102.194',
        'PORT': '3306'
    }
}
#...
```

### step 3 初始化数据库

```
python manage.py migrate
```

### step 4 创建管理员账号密码

```
python manage.py createsuperuser
```

### step 5 开发模式运行服务器（用作测试）

```
python manage.py runserver 0.0.0.0:8000
```

### step 6 运行vdistackclientserver服务器

```
python vdistackclientserver.py
```

测试是否启动服务器

```
telnet 127.0.0.1 1234
# 如果输出 {"message": "please input mac_address and client_uuid", "method": "login", "method_type": "request"}
# 说明成功
```

### 注意点

1. pip和apt的源，修改之
http://topmanopensource.iteye.com/blog/2004853
http://mirrors.163.com/

2. 关于源码风格
PEP 8
http://legacy.python.org/dev/peps/pep-0008/