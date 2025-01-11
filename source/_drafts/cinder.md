# cinder 学习笔记

## 简介

## 通过cinderclient的使用了解cinder的功能




### cinderclient api用法 V1版本

#### cinder显示当前可用于启动的volume

需要说明的是，这个volume的显示需要客户端进行筛选。服务端可能未提供服务器筛选功能。这里需要满足的选项是：status = available and bootable = true。

```python
from cinderclient.v1.client import Client as cinder_client

username = "project2"
password = "cloudopen"
tenant_name = "project2"
AUTH_URL_V2 = "http://10.10.102.10:5000/v2.0"
cinder = cinder_client(username, password, tenant_name, AUTH_URL_V2)
volumes = cinder.volumes.list(detailed=True)
for volume in volumes:
    if volume.status == "available" and volume.bootable == "true":
        print volume

```