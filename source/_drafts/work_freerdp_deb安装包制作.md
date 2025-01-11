#Freerdp 安装包制作

## 手动安装

freerdp相关

```
mkdir -p /opt/rdpclient/bin
mkdir -p /opt/rdpclient/lib
cp client/X11/xfreerdp /opt/rdpclient/bin/
find ./ -name "lib*.so.*.*.*" | sudo xargs -i cp {} /opt/rdpclient/lib/
# 这步是为了出现ld的错误
rm /opt/rdpclient/lib/libfreerdp-common.so.1.1.0-beta1
cd /opt/rdpclient/lib;ldconfig `pwd` 
```

添加vdistackclientrdpclient的Qt程序

```
cp vdistackclientrdpclient /opt/rdpclient/bin/
cp libQt*.so.*.*.* /opt/rdpclient/lib/
cp libicu*.so.*.* /opt/rdpclient/lib/
cp -r platforms /opt/rdpclient/bin/
cp libQt5DBus.* /opt/rdpclient/lib
cd /opt/rdpclient/lib;ldconfig `pwd`  
```

## 安装包制作

目录结构：

```
RDPClientDeb
├── DEBIAN
│   ├── control
│   ├── postinst
│   └── postrm
└── opt
    └── rdpclient
        ├── bin
        │   └── xfreerdp
        └── lib
            ├── libfreerdp-cache.so.1.0.2
            ├── libfreerdp-channels.so.1.0.2
            ├── libfreerdp-codec.so.1.0.2
            ├── libfreerdp-core.so.1.0.2
            ├── libfreerdp-gdi.so.1.0.2
            ├── libfreerdp-kbd.so.1.0.2
            ├── libfreerdp-rail.so.1.0.2
            └── libfreerdp-utils.so.1.0.2
```

build脚本

```
#!/bin/sh

cd /home/stack
mkdir -p /home/stack/build
dpkg -b RDPClientDeb/ build/jzrdpclient-`date "+%Y%m%dd%H%m%S"`.deb
cd build
dpkg-scanpackages . /dev/null | gzip -9c > Packages.gz
```


## 搭建apt-get自定义源服务器

简单来说就是http服务器 nginx

## 安装包升级

配置apt-get源服务器

sudo vim /etc/apt/sources.list
```
deb http://192.168.44.130/ubuntu /
```

下面的命令还是会更新所有
sudo apt-get upgrade -y --force-yes jzrdpclient