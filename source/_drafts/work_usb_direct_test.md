## FreeRDP

目前各大发行版linux均为1.0.2版本的FreeRDP，但是该版本不支持USB重定向。
如果需要使用USB重定向必须自己重新编译FreeRDP。我采用的是github上的稳定版本：
*stable-1.1*

```
apt-get install git-core build-essential cmake libssl-dev libxinerama-dev libxcursor-dev libxdamage-dev libxv-dev libxkbfile-dev libasound2-dev libcups2-dev libxml2 libxml2-dev libxrandr-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libxi-dev libavutil-dev libavcodec-dev libudev-dev uuid-dev libdbus-glib-1-dev libusb-1.0-0-dev libjpeg-dev
# 安装pcsc开发包 支持smartcard重定向 这个功能linux下无法使用
apt-get install libpcsclite1 libpcsclite-dev
```

编译选项

```
#1.1
cmake -DCMAKE_BUILD_TYPE=Debug -DWITH_SSE2=ON -DWITH_CUPS=ON -DCHANNEL_URBDRC=ON .
# master
cmake -DWITH_WAYLAND=OFF -DWITH_CUPS=ON -DWITH_PCSC=ON -DWITH_FFMPEG=OFF -DWITH_GSTREAMER_0_10=ON -DWITH_JPEG=ON -DCHANNEL_URBDRC=ON -L ..

# gatewaybranch
cmake -DWITH_CUPS=ON -DWITH_PCSC=ON -DWITH_FFMPEG=OFF -DWITH_GSTREAMER_0_10=ON -DWITH_JPEG=ON -DCHANNEL_URBDRC=ON -DWITH_GSTREAMER_1_0=OFF -DWITH_WAYLAND=OFF  ..
```

### 编译该版本后对于USB重定向

其他修改说明，对于USB重定向，源码中有相关内容过滤USB的种类，
例如：CLASS_SMART_CARD CLASS_MASS_STORAGE都是被注释掉的，也就是说源码中对于U盘等设备会直接提示不支持，修改这部分代码就可以支持U盘等设备，但不知道作者为何要过滤掉U盘这些设备。我注释了全部后，测试以下内容。

### 测试方法

./xfreerdp -sec-nla /rfx /sound:sys:alsa /microphone:sys:alsa /usb:id,dev:2a5f:1000 /v:10.10.102.110 /u:HappyUser /p:HappyUser


client/X11/xfreerdp /rfx /rfx-mode:video -sec-nla /sound:sys:alsa /microphone:sys:alsa /dvc:tsmf:decoder:gstreamer,sys:alsa /v:10.10.102.111

### 结果

#### 罗技摄像头

windows 7 能自识别并在设备管理器中识别为 Webcam C170

用QQ进行测试，可以正常使用

#### 密码键盘系列

windows 7 识别为 HID 输入设备 但是无法进行数据， 由于不能接受ScrollLock的原因
暂时无法解决

**更新**最后再次尝试可以正常工作

#### 扫描枪中崎

windows识别为usb输入设备， 正常

#### 不知名的扫描枪

windows识别，并正常工作

#### 打印机中崎

本地安装驱动失败，未测

#### 建行，农行，招行

招行能够正确识别但是虚拟机中其客户端非正常工作

建行，农行UKEY均失败

#### 腾讯无线随身WIFI

系统可以识别，但是安装驱动后无法使用，失败

#### U盘，SANDISK

第一次我的SANDISK可以正常工作，之后不知道原因我的SANDISK无法正常识别
换虚拟机也无法正常识别

毛伟杰的U盘正常识别

#### USB蓝牙

正常工作，无问题

#### FAST USB网卡

正常识别，安装驱动正常工作


## 第三方程序 usbgateway

USBKey工作正常


## USBIP 开源程序

###理论论文：

http://inet-lab.naist.jp/~eiji-ka/publications/remote-dev/acs11-hirofuchi.pdf

###开源实现：

#### 资源

#####linux 

linux kernel 3.13
drivers/staging/usbip/

ubuntu中内核模块usbip-core.ko, usbip-host.ko可以自行编译或者
apt-get install linux-image-3.13.0-45-generic linux-image-extra-3.13.0-45-generic

用户程序需要自己编译在
linux内核源码中drivers/staging/usbip/userspace下

```
# linux usbip服务器 192.168.100.189
#**kernel 3.13.0-45-generic**
sudo insmod /lib/modules/3.13.0-45-generic/kernel/drivers/staging/usbip/usbip-core.ko
sudo insmod /lib/modules/3.13.0-45-generic/kernel/drivers/staging/usbip/usbip-host.ko
sudo ./usbip list -l
sudo ./usbip bind --busid 2-1
sudo ./usbip unbind --busid 2-2

sudo ./usbipd
```

###### linux usbip客户端

```
sudo ./usbip list --remote 192.168.100.189
sudo ./usbip attach --remote 192.168.100.189 --busid 1-1.2
sudo lsusb
```

成功，可以重定向

##### windows客户端驱动和程序
http://sourceforge.net/p/usbip/

```
# windows usbip
# 安装驱动
usbip -l 192.168.1.110
usbip -a -D 192.168.1.110 2-1
```
失败，提示错误

linux到windows的重定向失败（windows的驱动的最新维护日期是2011年太老）。


## 结果

1. 使用Freerdp部分正常，例如简单的设备HID U盘等，对于USBKey（网银盾）基本失败。
2. 使用USBGateWay 非开源USBIP重定向，成功，试用14天。
3. 使用USBIP的开源实现，在linux到linux的USB重定向成功（不是我们要的）