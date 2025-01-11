# nova 学习笔记

## 简介

## 通过novaclient的使用了解nova的功能

### novaclient的安装

```bash
pip install python-novaclient
```

### novaclient的命令行用法

#### 用户认证

命令行工具的认证方法需要几个参数,可以设定成系统变量.具体可以通过```keystone help```查看.
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

#### nova snapshot

快照的真正含义是创建image，使用以上命令能达到目的：

```bash
nova image-create --show --poll <server> <name>
```

*server* 主机名字或者id
*name* 新建的image的名字

#### 创建虚拟机

从image创建一个虚拟机
```nova boot [Option arguments] <name>```

```bash
nova flavor-list
nova image-list
neutron net-list
nova boot --flavor e6046c10-de73-4b3a-aa6c-b093c565d766 --image c56f5c55-0b71-4480-a3c7-ee6bc0d828c4 --nic net-id=47d59cf9-c173-4cde-b000-90963925a025 --poll test
```

名为test的虚拟机就创建好了

#### 暂停/恢复暂停一个虚拟机 pause unpause

暂停虚拟机的具体作用还需要研究。在暂停状态vnc是不退出的。即qemu进程仍然在。

```bash
nova pause 01d4a68b-0c5b-4e13-8be7-bc0a9d6bf9de
nova unpause 01d4a68b-0c5b-4e13-8be7-bc0a9d6bf9de
```

#### 停止/开始虚拟机,类似关机开机 stop start

```bash
nova stop 01d4a68b-0c5b-4e13-8be7-bc0a9d6bf9de
nova start 01d4a68b-0c5b-4e13-8be7-bc0a9d6bf9de
```

#### 锁/解锁 虚拟机 lock unlock

不知道其作用

#### 挂起/恢复 suspend/resume

保存当前的状态，并关闭机器，resume开机恢复当前状态

```bash
nova suspend 01d4a68b-0volume_id:0cd62ba8-e7d7-4152-b821-ef44ae364ba8c5b-4e13-8be7-bc0a9d6bf9de
nova resume 01d4a68b-0c5b-4e13-8be7-bc0a9d6bf9de
```

#### 重启虚拟机 reboot

重启虚拟机区分软重启与硬重启
```nova reboot [--hard] [--poll] <server>```

*--hard* 硬重启

```bash
nova reboot --poll 01d4a68b-0c5b-4e13-8be7-bc0a9d6bf9de
nova reboot --hard 01d4a68b-0c5b-4e13-8be7-bc0a9d6bf9de
```

#### 重新创建rebuild

关闭虚拟机，re-image，re-boot 一个虚拟机
```
nova rebuild
```

```bash

```

### novaclient api用法 V2版本



## nova使用例子

#### 获取相应的images等信息

```python
from novaclient.v1_1 import client as nova_client
nova = nova_client.Client(username, password, tenant_name, AUTH_URL_V2)

# 获取availability_zones
availability = nova.availability_zones.list(detailed=False)

# 获取flavors列表
flavors = nova.flavors.list()

# 获取镜像列表 从这里获取的镜像列表是无法进行分类别的.
# 如果需要进行分类别,需要使用glanceclient提供的功能.
# 下面的操作是从novaclient中获取image的大小和相关信息
# 注意这里使用了img.to_dict(),该函数转换成dict以便获取OS-EXT-IMG-SIZE:size属性
images = nova.images.list()
class ImageInfo:
    def __init__(self, img):
        self.uuid = img.id
        self.name = img.name
        self.displayname = self.name+ " (" + \
            self.format_size(img.to_dict()['OS-EXT-IMG-SIZE:size']) + \
            ")"

    def format_size(self, size):
        size = float(size)
        if size < 1000:
            return str(size)+' B'
        if size < 1000000:
            return "{:.1f}".format(size/1000)+' KB'
        if size < 1000000000:
            return "{:.1f}".format(size/1000000)+' MB'
        if size < 1000000000000:
            return "{:.1f}".format(size/1000000000)+' GB'
images_list = []
for image in images:
    imageinfo = ImageInfo(image)
    images_list.append(imageinfo)
```


#### 获取安全组信息

```python
security_groups = nova.security_groups.list()
```

#### 获取网络的信息


#### 创建虚拟机