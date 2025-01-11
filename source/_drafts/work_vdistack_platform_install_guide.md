## 需要安装的

1. Openstack 环境
2. VDIStack
3. GatewayController
4. VDIStack Client
5. Client管理服务器

## 1. Openstack 环境
Openstack环境 与 VDIStack 链接需配置以下参数

Openstack环境中需要包含一个最高管理员用户，平台的管理员（role_platform_admin）就拥有该用户的权限。

VDIStack中需要的配置参数vdistack/settings.py：

```
# 配置openstack 默认管理员用户密码AUTH_URL
ADMIN_OS_TENANT_NAME = "admin"
ADMIN_OS_USERNAME = "admin"
ADMIN_OS_PASSWORD = "cloudopen"
ADMIN_OS_AUTH_URL = "http://10.10.102.11:35357/v2.0"

# 配置openstack普通用户AUTH_URL
USER_OS_AUTH_URL = "http://10.10.102.11:5000/v2.0"
```

## 2. VDIStack配置

参考 ```vdistack开发环境``` 该文

## 3. GatewayControl 配置

使用其中的vdigatewaycontrol（将来移至VDIStack）

```
git clone http://git.cloud-open.cn/vdigateway
cd vdigateway/vdigatewaycontrol
```

配置数据库

vim vdigatewaycontrol/settings.py

DATABASES项目

初始化数据库

```
python manage.py runserver 0.0.0.0:8001
```

进入管理界面配置
配置README中的参数

## 4. GatewayAgent
```
git clone http://git.cloud-open.cn/vdigateway
cd vdigateway/vdigatewayagent
```

配置数据库

vim vdigatewayagent/settings.py

DATABASES项目

初始化数据库

```
python manage.py runserver 0.0.0.0:8002
```

进入管理界面配置
配置README中的参数
