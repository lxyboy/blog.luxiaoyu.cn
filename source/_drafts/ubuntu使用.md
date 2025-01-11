#ubuntu使用

windows读linux linuxreader

快速配置启动项
sysv-rc-conf
以上脚本只适用sysv的
而ubuntu使用的启动方式不同可以参照如下方法手动启动服务


echo "manual" | sudo tee /etc/init/network-manager.override


#### gnome-terminal使用技巧
开始新标签页快捷键 ctrl + shift + t
关闭标签页快捷键 ctrl + shirft + w

####grep使用

查找当前目录下的文件包含文本

grep -n "local-filesystems" -r /etc/init
vim

grep -i 不区分大小写

#### apt-file 查找头文件在哪个包

apt-get install apt-file
apt-file update
apt-file search sys/filio.h

####lsof使用

查找当前端口是否被使用

lsof -i:8000

#### 备份系统
sudo tar -cvf ./ubuntu.tgz --exclude=/proc --exclude=/lost+found --exclude=/media --exclude=/mnt --exclude=/sys /

#### 还原
tar -xvpzf  ubuntu.tgz -C /


###系统进程说明


#### 1
*avahi-daemon* 是 Avahi 是*Zeroconf*规范的开源实现。Apple公司的Bonjour程式也是*Zeroconf*的开源实现。如果不用可以关闭。

ubuntu关闭avahi功能

echo "manual" | sudo tee /etc/init/avahi-daemon.override
echo "manual" | sudo tee /etc/init/avahi-cups-reload.override

#### 2
*cups* 全称 *Common Unix Printing System* 普通打印机
echo "manual" | sudo tee /etc/init/cups-browsed.override
echo "manual" | sudo tee /etc/init/cups.override

#### 3
*cgroups* 全称 *control*

#### 4
*kerneloops* opps的意思为哎哟，当kernel出错时向kerneloops.org发送错误

关闭*kerneloops*： kerneloops是通过systemV方式启动的，关闭方法：
ubuntu 14.04上

```
sudo mv /etc/rc5.d/S20kerneloops /etc/rc5.d/K20kerneloops
```

#### 5
*uml-switch* 这个进行是用户模式linux直接转换使用， *uml*全称user mode linux也可以认为是一种运行环境隔离的技术，该进程应该可以被停止

```
sudo service uml-utilities stop
```

#### 6
*dbus-daemon* dbus daemon auto start by dbus
*polkitd* 
*upowerd* 
*rtkit-daemon*

#### 7 gnome

*bamfdaemon* 提供桌面图标在bar上


###系统启动方式
upstart systemd systemV
对于ubuntu采用upstart的启动方式，通过/etc/init/rc*相关脚本再调用systemv&systemd的启动方式。细节需要好好研究参考man手册和[http://www.ibm.com/developerworks/cn/linux/1407_liuming_init2/](http://www.ibm.com/developerworks/cn/linux/1407_liuming_init2/)


### 桌面安装ubuntu 14.04 gnome
1 (最简) 基于GNOME
    sudo apt-get install --no-install-recommends ubuntu-gnome-desktop

  sudo apt-get install xorg gnome-core gnome-system-tools gnome-app-install（这个更小）
  
  sudo apt-get install language-selector-gnome ibus-libpinyin
  

### awk

cat /etc/passwd |awk  -F ':'  '{print $1"\t"$7}'

### 移除某个包
dpkg -l | grep gnome | awk -F " " '{print $2}'| sudo xargs -i apt-get -y remove {}

###  debin,ubuntu删除所有带 rc 标记的dpkg包

dpkg -l | grep ^rc | cut -d' ' -f3 | sudo xargs dpkg --purge  


### ubuntu安装字体

拷贝文件到/usr/share/fonts/windows
cd /usr/share/fonts/windows
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv


### 关于ulimit的限制

ulimit -SHn 65535

### 用户组

id luxy

### 关于转换文件名编码
convmv -f GB2312 -t UTF-8 -r --nosmart --notest *.*