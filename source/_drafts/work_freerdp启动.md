#freerdp_启动

## 了解系统init upstart

### 任务的控制（Job Control）

#### start and stop

```
stop tty3
start tty3
```

#### status

```
status tty3
```

#### initctl list

列出所有的任务和他们的状态

```
initctl list
```

#### initctl emit

发出一个 自定义的事件

编辑文件：```/etc/init/luxy-start.conf```

```
start on luxyevent
exec echo --hello world-- >> /root/123.txt
```

```
initctl reload-configuration
initctl emit luxyevent
```


## plymouth 可以设定登录图标

##安装kdm kde登录管理器
## 配置文件 /etc/kde4/kdm/kdmrc

AutoLoginEnable=true
AutoLoginUser=cloudopen
AutoLoginPass=cloudopen

## 配置GNOME桌面
    
GNOME桌面启动左面图标

末尾名.desktop

```
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Name[en_HK]=RDPClient
Exec=/usr/bin/xfreerdp --no-nla -f --rfx --plugin rdpsnd --data alsa -- --plugin drdynvc --data tsmf -- 10.10.102.111
Icon=/home/cloudopen/icons/rdp.png
```