## 环境
### 开发测试环境

1. python 2.7.8
2. 自己的编辑器

### openstack环境

openstack keystone 普通用户入口地址 10.10.102.11:5000
openstack keystone 管理员用户入口地址 10.10.102.11:35357

这两项已经在settings.py中配置

### vdistack平台git地址

```
http://git.cloud-open.cn/vdistack
```

### 自用mysql库

```
apt-get install mysql-server-5.5
```

## 搭建步骤

### step 0 Preinstall

```
apt-get install python-pip python-dev libmysqlclient-dev libpq-dev libffi-dev
# Fix 'Module_six_moves_urllib_parse' object has no attribute 'SplitResult' 
pip install six --upgrade
```

### step 1 下载源码

```
git clone http://git.cloud-open.cn/vdistack; cd vdistack
pip install -r requirements.txt
```

**注意** pip 安装可能会遇到失败的情况，原因是系统的环境缺少相应的库，安装即可

### step 2 配置数据库

配置源码中的数据库 ```vim settings.py```

```
MYSQL_USER = 'luxy'
MTSQL_PASS = 'cloudopen'
MYSQL_HOST = '192.168.5.4'
MYSQL_PORT = '5432'
MYSQL_DB = 'vdistack'
```

配置alembic数据库 ```vim alembic.ini```

```
sqlalchemy.url = postgresql://luxy:cloudopen@192.168.5.4/vdistack
```

### step 3 初始化

```
alembic upgrade head
python manage.py db_data_init
```

### step 4 运行

```
python manage.py runserver
```

### step 5 

默认的管理员用户名为 admin
密码为 cloudopen

参考当前[接口说明](http://redmine.cloud-open.cn/documents/1)

## 其他

### portal环境及部署环境uwsgi+nginx

```
sudo apt-get install uwsgi uwsgi-core uwsgi-plugin-python nginx
cd /opt/vdistack
sudo cp /opt/vdistack/uwsgi.ini /etc/uwsgi/apps-available/
# 编辑uwsgi.ini
sudo ln -s /etc/uwsgi/apps-available/uwsgi.ini /etc/uwsgi/apps-enabled/uwsgi.ini
sudo touch /tmp/vdistack.sock
sudo chmod www-data:www-data /tmp/vdistack.sock

# 编辑/opt/vdistack/portal/portal/app.js 修改api路径
sudo vim /etc/nginx/sites-enabled/default
sudo service uwsgi restart
sudo service nginx restart
```

/etc/nginx/sites-enabled/default

```
server {
        listen 80 default_server;
        listen [::]:80 default_server ipv6only=on;
        root /opt/vdistack/portal;
        index index.html index.htm;
        server_name localhost;
        location /ubuntu {
                alias /home/cloudopen/build;
                try_files $uri $uri/ =404;
        }
        location /portal{
        }

        location /static/{
                root /opt/vdistack/portal/portal/;
        }
        location / {
                uwsgi_pass unix:///tmp/vdistack.sock;
                include /opt/vdistack/uwsgi_params;
        }
}
```


### 注意点

1. pip和apt的源，修改之
http://topmanopensource.iteye.com/blog/2004853
http://mirrors.163.com/

2. 关于源码风格
PEP 8
http://legacy.python.org/dev/peps/pep-0008/

3. 查阅源码中README.md

### 其他补充

1. 编辑器推荐 pycharm
2. flask文档  http://10.10.100.47:9000/sharefiles/luxy/docs/flaskdocs/
3. python文档 http://10.10.100.47:9000/sharefiles/luxy/docs/pythondocs/
4. zerkeugdocs文档 http://10.10.100.47:9000/sharefiles/luxy/docs/werkzeugdocs/