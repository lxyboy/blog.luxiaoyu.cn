# glance 学习笔记

## 简介

## 通过 glanceclient 了解 glance 功能

### glanceclient 的安装

```bash
pip install python-glanceclient
```

### glanceclient 的命令行用法

#### 用户认证

命令行工具的认证方法需要几个参数,可以设定成系统变量.具体可以通过```glance help```查看.
必须的几个变量为:

命令行参数:

* *--os-username* 
* *--os-password*
* *--os-tenant-name*
* *--os-auth-url*

或者系统环境变量:

* *OS_USERNAME*
* *OS_PASSWORD*
* *OS_TENANT_NAME*
* *OS_AUTH_URL*

#### glance image-list

列出你能使用的images

通过命令```glance help image-list```查看具体用法

##### 列出snapshot的image

```bash
glance image-list --property-filter image_location=snapshot
```

### glanceclient api 用法

#### 认证过程 

glanceclient api 只能根据3个参数进行初始化：

1. :param string endpoint: A user-supplied endpoint URL for the glance service.
2. :param string token: Token for authentication.
3. :param integer timeout: Allows customization of the timeout for client http requests. (optional)

所以在使用的时候必须获取以上参数

关于*endpoint*需要在keystone中获取相应的glance服务的endpoint
关于*token* 可以在keystone中直接获取

```python
from keystoneclient.v2_0.client import Client as keystone_client
from glanceclient.v1.client import Client as glance_client
username = "project2"
password = "cloudopen"
tenant_name = "project2"
AUTH_URL_V2 = "http://10.10.102.10:5000/v2.0"

keystone = keystone_client(username=username, password=password, tenant_name=tenant_name, auth_url=AUTH_URL_V2)
# 获取glance_endpoint
glance_endpoint = keystone.service_catalog.url_for(service_type='image')
# 关于第二个参数token需要使用dict方式传 代码中是从kwargs中获取的
glance_token = keystone.auth_ref.auth_token
# 获取glance client 
glance = glance_client(glance_endpoint, token=keystone.auth_token)
```

*注意：* 这里的token是有时效的。为保证每次正确暂时可以调用就认证，将来可以采取失效再认证的方式

#### 获取images列表

可以通过```images = glance.images.list()```进行获取

#### 筛选 Property image_type为snapshot的 images

这里的filter的参数根据glanceclient源码分析得到，具体参照*glanceclient/v1/images.py*中list函数

```python
filters={'properties':{'image_type':'snapshot'}}
images = glance.images.list(filters=filters)
list(images)
```