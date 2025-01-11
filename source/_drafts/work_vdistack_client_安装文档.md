## 安装系统

1. 安装系统 ubuntu14.04 server
2. 配置/etc/apt/sources.list
3. apt-get update
4. apt-get install xorg openbox alsa-base libgstreamer0.10-0 libgstreamer-plugins-base0.10-0 idesk python-pip slim feh
5. apt-get install jzrdpclient

*注意：jzrdpclient需要添加配置本地 apt源服务器并编译deb安装包*

### 配置idesk openbox

```
# 确保用户在video组和audio组
sudo usermod -a -G video cloudopen
sudo usermod -a -G audio cloudopen

# 配置openbox
mkdir -p ~/.config
cp -r /etc/X11/openbox/ ~/.config/openbox/

# 配置idesk
cp /usr/share/idesk/dot.ideskrc ~/.ideskrc
mkdir .idesktop
vim ~/.idesktop/rdpclient.lnk

# 配置idesk自启动
vim ~/.config/openbox/autostart
```

### alsa 默认声卡配置
根据当前终端设备配置默认声卡

vim ~/.asoundrc

```
defaults.ctl.card 1
defaults.pcm.card 1
```

### 配置客户端web配置界面

git clone http://git.cloud-open.cn/vdistackclient
子目录 vdistackclientsettings

```
# 进入其目录 安装依赖
sudo pip install -r requirements.txt
# 创建配置目录
sudo mkdir -p /etc/vdistack
# 设置配置
sudo vim /opt/vdistackclientsettings/vdisettings/settings.py
```


### example

#### ~/.config/openbox/autostart

```
(sleep 2; idesk &)&

feh --bg-fill /home/cloudopen/background.jpg
```

#### ~/.idesktop/rdpclient.lnk

```
table Icon
  Caption: Gnome-Terminal
  Command: /opt/rdpclient/bin/
  Icon: /usr/share/idesk/folder_home.xpm
  Width: 48
  Height: 48
  X: 50
  Y: 20
end
```

#### ~/.idesktop/shutdown.lnk

```
table Icon
  Caption: ShutDown
  Command: sudo shutdown -h now
  Icon: /usr/share/idesk/folder_home.xpm
  Width: 50
  Height: 50
  X: 50
  Y: 120
end
```

#### ~/.asoundrc

```
defaults.ctl.card 1
defaults.pcm.card 1
```

#### /etc/apt/sources.list

```
deb http://192.168.5.131/ubuntu /
deb http://mirrors.ustc.edu.cn/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-backports main restricted universe multiverse
``` 

```deb http://192.168.5.131/ubuntu /```
这个为本地的apt服务器所在的位置