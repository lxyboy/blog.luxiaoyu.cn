## NFS配置

环境ubuntu14.04

###服务器：

安装

sudo apt-get install nfs-kernel-server

配置编辑 /etc/exports中添加要导出的目录

```txt
/ubuntu *(ro,sync,no_root_squash)
/home *(rw,sync,no_root_squash)
```

```*```可以填可以访问的主机的ip地址或者主机名

重启

sudo service nfs-kernel-server start

### 客户端：

安装客户端

sudo apt-get install nfs-common

**question**

sudo mount -t nfs -o rw,intr,soft,nolock,tcp,user=administrator 10.10.100.47:/var/www/html/sharefiles /home/administrator/Documents/sharefiles
