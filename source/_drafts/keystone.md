# keystone 学习笔记

## 简介

keystone主要有两个功能:

1.用户管理
2.服务目录管理

主要概念:

* *User* *用户*
* *Credentials* *证书*
* *Authentication* *认证*
* *Token* *令牌*
* *Tenent* *租户*
* *Service* *服务*
* *Endpoint* *访问端点*
* *Role* *角色*


## 通过keystoneclient的使用了解keystone的功能

### keystoneclient的安装

```bash
pip install python-keystoneclient
```

### keystoneclient的命令行用法

#### 用户认证

命令行工具的验证方法需要几个参数,可以设定成系统变量.具体可以通过```keystone help```查看.
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

另外解释一下关于 *--os-region-name* :
这个是对于region_name的解释:

> Name of a region to select when choosing an endpoint from the service catalog.

翻译:

> 从系统服务目录中选择的一个Region为region_name的endpoint.

我的理解是可以根据这个来分布不同的机房.比方说机房1中布置了一套nova, 机房2中布置了一套nova. 然后在输入keystone的时候使用不同的region来区分.这样用户认证后可以对不同的机房操作.

#### 当前认证用户使用

### keystoneclient的api用法 V2版本

#### 认证方法

首先通过v2版本的client进行认证:

```python
from keystoneclient.v2_0 import client as keystone_client
AUTH_URL_V2 = 'http://10.10.102.10:5000/v2.0'
keystone = keystone_client.Client(username="admin", password="cloudopen", tenant_name="admin", auth_url=AUTH_URL_V2)
# 未指定region则使用默认的region
# 如果指定region 则:
#keystone = keystone_client.Client(username="admin", password="cloudopen", tenant_name="admin", auth_url=AUTH_URL_V2, region_name="regionOne")
```

之后便可以使用相应的users,tenants,tokens,services,roles,extensions,endpoints,ec2等模块

另外为了再次初始化相应的验证,可以保存:

```python
auth_ref = keystone.auth_ref
new_keystone = keystone_client.Client(auth_ref=auth_ref)
```

#### 使用过程

举例说明:

```python
# 列出当前用户的roles
keystone.users.list_roles(keystone.user_id, keystone.tenant_id)
# 列出所有的用户
keystone.users.list()
# 列出所有的tenants() 
keystone.tenants.list()
```
**注意:** 这里面涉及到当前的*User*在当前*Tenant*中的*Roles*,只有满足相应服务设定的*Roles*的权限相应的操作才能执行. 这里需要MARK!~~TODO~~.进一步了解如何管理各个服务Roles权限.


## keystone的原理 


## keystone 使用例子

```python

# 创建tenant
new_tenant = keystone.tenants.create(tenant_name, description="", enabled=True)
print new_tenant.id

# 创建用户
new_user = keystone.users.create(name, password=None, email=None, tenant_id=None, enable=True)
```



## 源码分析 

### 创建tenant

```txt
usage: keystone tenant-create --name <tenant-name>
                              [--description <tenant-description>]
                              [--enabled <true|false>]
Arguments:
  --name <tenant-name>  New tenant name (must be unique).
  --description <tenant-description>
                        Description of new tenant. Default is none.
  --enabled <true|false>
                        Initial tenant enabled status. Default is true.
```

## install

bin/keystone-manage -v db_sync


这个文件使用命令创建keystone数据 
tools/sample_data.sh


###原型的实现

1. 创建租户
a.1 建立openstack租户, 租户名为 uuid1字符串，描述为JZTenant的描述
a.2 建立openstack租户的用户，用户名为 租户的id， 密码为 租户id的md5
a.3 为租户建立JZGroup顶层组，组名为openstack租户的id
a.4 建立JZTenant 赋予 openstack_tenant_id 为 创建的openstack租户的id
a.5 并赋予租户的顶层组的tenant_id 为 创建的JZTenant的id

2. 修改租户

3. 获取租户

4. 删除租户
未真正删除，保留30天通过脚本删除


1. 创建 暂停 删除 租户

```
#a添加租户
# a.1 openstack建立租户
# a.2 为租户建立组
# a.2 关联租户
# a.3 创建租户的顶层组
# a.4 创建默认admin用户
# a.5 把admin用户加入顶层组
# a.6 赋予默认的admin该组权限

#b删除租户tenant1
# b.1 查找tenant1顶层组
# b.2 遍历顶层组：查找JZUserGroup中group_id的项，删除JZUserJZGroupJZRole中的权限，更新待删除的用户的列表delete_user_list，删除该JZUserGroup
# b.3 删除delete_user_list中的用户

#old
# b.1 遍历JZUser中所有tenant为tenant1的用户
# b.2 查找JZUserJZGroup中所有user_id为JZUser.id的所有记录JZUserJZGroup_set
# b.3 根据JZUserJZGroup_set中的id查找JZUserJZGroupJZRole中role_id为JZUserJZGroup.id的记录删除
# b.4 删除JZUserJZGroup对象
# b.5 根据group_id删除JZGroup中所有的子节点
# b.6 删除JZUser中的所有tenant1的用户

#c 暂停租户
# 设置JZTenant的enbaled为False

#d 获取租户列表
直接返回所有JZTenant

```

2. 租户部门结构

```
# 1根据JZTenant获取父亲组
# 2根据父亲部门获取相应子组
# 3根据组获取该组的孩子
```

## ip 地址
地址 10.10.102.11  
用户名 cloudopen
密码 cloudopen

sudo su -

adminrc cloudopenrc

### 处理函数包含必要的参数 required

### 使用函数判断并处理参数 若并无添加参数，返回默认，若有无效则返回失败

## 默认使用session进行登录判断，必须确保客户端使用cookie

## type 如果是int必须确保能够转换为int类型


3. 网络
保证一个网络中一个子网
