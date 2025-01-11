## 安装

###安装前准备事项

####检查你的cpu是否有硬件虚拟化支持

想要运行kvm，你的处理器必须支持硬件虚拟化。 Intel和AMD都为他们的处理器开发了相应的拓展，Intel叫做 **Intel V-x**, Amd叫**AMD-V**。

* 方法一：
检查你的处理器是否支持可以使用以下命令：

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

如果结果为0： 你的CPU不支持硬件虚拟化。
如果结果为1及以上： 你的CPU支持，但是你还是必须**保证**在BIOS中硬件虚拟化已经被开启。

* 方法二：
使用 ```kvm-ok```命令[^foot-note-1]：
输出结果：

>INFO: /dev/kvm exists

>KVM acceleration can be used 
	
如果输出结果为：

>INFO: Your CPU does not support KVM extensions 

>KVM acceleration can NOT be used 

你仍然可以安装虚拟机，但是会比装有KVM拓展的慢一些。

#### 尽量使用64bit的内核

推荐在主机上运行一个64bit的内核是因为：

1. VMs可以使用多于2GB的RAM。
2. VMs既可以使用64bit的操作系统也可以使用32bit的操作系统

查看你的处理器是否支持64bit，可以运行如下命令：

```bash
egrep ' lm ' /proc/cpuinfo
```

如果结果为0：cpu不支持64bit
如果结果等于大于1：cpu支持。*LM* 代表 *Long Mode*。

可以运行一下命令查看当前的操作系统位数：

```bash
uname -m
```

如果结果为```x86_64```说明你当前运行的是64bit的操作系统。如果你看见 i386，i486，i586，i686说明你运行的是32位操作系统。


###安装KVM

####安装必要的软件包

下面的安装都是在ubuntu server 14.04上进行安装的。

首先得安装软件包：

```bash
apt-get install qemu-kvm libvirt-bin bridge-utils
```

1. ~*libvirt-bin* 为qemu和kvm instances管理提供 libvirt 接口。~
2. *qemu-kvm* 为虚拟机后端。
3. *bridge-utils* 为虚拟机提供网桥支持。

####~ 添加用户到组中~

```bash
adduser `id -un` libvirtd
```

> Adding user `root' to group `libvirtd' ...

> Adding user root to group libvirtd

> Done.

添加结束后，你**必须重新登录**，这样你的用户在libvirtd组中才真正生效。
可以通过```id -a```查看当前用户的信息
**注意：**如果是图形界面的重新登陆是指注销当前的环境,不要因为麻烦仅仅重启当前的terminal

#### 确认安装成功

可以用过一下命令来确认安装成功：

```bash
virsh -c qemu:///system list
```
安装成功输出为：

>  Id    Name                           State

> ----------------------------------------------------

>  

如果你看到的像这样：

> libvir: Remote error : Permission denied

> error: failed to connect to the hypervisor

说明哪里有错误发生（比方说你没有重新登录？），你必须解决这个问题才能继续下去。
关键点在于：你没有读写权限去访问 */var/run/libvirt/libvirt-sock*[^foot-note-2] 或者 */dev/kvm*[^foot-note-3]。

#### 可选的：安装图形管理界面 virt-manager

如果你安装有图形界面可以考虑安装图形界面虚拟机管理器：

```bash
apt-get install virt-manager
```
运行*virt-manager*
通过virt-manager创建虚拟机。

### Other

命令行起虚拟机，直接使用命令（下面命令是用来启动windows vmware image，当时的环境是桌面版ubuntu）：

```bash
kvm -m 1024M -hda /host/VirtualOS/keystone/Ubuntu-cl1.vmdk -boot order=cd -display sdl -vga vmware
```

## 网络

### 创建一个kvm的mac地址脚本

这里的*52:54:00*是QEMU的[OUI](http://en.wikipedia.org/wiki/Organizationally_unique_identifier)。


```bash
MACADDR="52:54:00:$(dd if=/dev/urandom bs=512 count=1 2>/dev/null | md5sum | sed 's/^\(..\)\(..\)\(..\).*$/\1:\2:\3/')"; echo $MACADDR
```

有几个不同的方法让虚拟机接入外部网络。

1. 默认的网络配置是 *Usermode Network*，数据是通过NAT转到主机网卡接口传到外网的。
2. 另外，可以通过配置 *Bridged Networking* 使外部主机可以直接接入VMs上的服务。

### 用户模式网络（*Usermode Network*）

默认的配置，vm系统能够接入网络的服务，但是不能够被网络上的其他机器接入。举个例子，vm主机能够访问web网站，但是不能够架一个被外部访问的web服务器。

### 桥接网络（*Bridged Networking*）

桥接网络能够让虚拟接口通过物理网口连接到外部的网络。
**注意：**一般无线设备无线网卡都不支持桥接（存在疑问？）。

#### 在主机上创建一个网桥

检查是否安装了*bridge-utils*。如果未安装请安装之```apt-get install bridge-utils```。

设置网桥接口，编辑文件 ```/etc/network/interfaces```**设置成自己的地址**：

```txt
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet manual

auto br0
iface br0 inet static
        address 192.168.44.21
        netmask 255.255.255.0
        gateway 192.168.44.2
        dns-nameservers 202.96.209.133
        bridge_ports eth0
        bridge_stp off
        bridge_fd 0
        bridge_maxwait 0

auto eth1
iface eth1 inet dhcp
```

重新启动网络:

```bash
/etc/init.d/networking restart
```

在用网桥模式的时候，kvm guest在开始和停止的时候"freezes"了几秒，这是因为linux网桥要获取硬件的mac地址。解决办法是添加下面的代码到你的网桥配置中：

```txt
post-up ip link set br0 address f4:6d:04:08:f1:5f
```

请替换 *f4:6d:04:08:f1:5f* 为 物理网络适配器的地址[^foot-note-4]。

#### User Mode Networking

```bash
kvm -m 1024M -hda Ubuntu-cl1.vmdk -boot order=cd -display sdl -vga vmware -net nic -net user
```

这个模式中 ping 等命令会失败。

> User mode networking is great for allowing access to network resources, including the Internet. By default, however, it acts as a firewall and does not permit any incoming traffic. It also doesn't support protocols other than TCP and UDP - so, for example, ping and other ICMP utilities won't work.

#### Tap Interface(guest on a bridge)

#### Tap Interface(guest on a tap, nat directly)

```bash
kvm -drive file=Ubuntu-cl1.vmdk -boot dc -m 300M -netdev tap,id=tapnet,ifname=tap0,script=no -device rtl8139,netdev=tapnet,mac=96:83:DA:A0:06:34
```




#### Tap Interface(bridged)

这种方式比较特殊，整个guest完全暴露在网络里。

```bash
kvm -m 1024M -hda Ubuntu-cl1.vmdk -boot order=cd -display sdl -vga vmware -net nic -net tap
```

在host主机中配置如下：

```txt
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet manual

auto br0
iface br0 inet static
	address 10.10.100.42
	broadcast 10.10.100.255
	netmask 255.255.252.0
	gateway 10.10.100.1
	dns-nameservers 202.96.209.5
	bridge_ports eth0
	bridge_stp off
	bridge_fd 0
	bridge_maxwait 0
```

在guest中的ubuntu配置如下：

```txt
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp
```

###Qemu Document/Networking

####Create a network backend 创建一个网络后端

根据你的环境，有几种可以选择的网络后端，可以这样创建网络后端：

```bash
-netdev TYPE,id=NAME,...
```

*id* 选项指明了虚拟网络设备关联的网络后端名称。如果你的guest需要多个虚拟网络设备，则每个虚拟网络设备都需要衙门自己的网络后端，*id*就是用来区别后端名称的。

####Network backend types 网络后端的种类

大多数情况，如果你没有特殊的网络需求仅仅是重guest中访问web网页，user networking 是一个好的选择。但是，如果你需要你的guest作一个web服务器，tap 最好的选择。

##### User Networking (SLIRP) 用户模式网络 （相当于VMware中的NAT模式）

这是默认的网络后端，通常情况下是最容易使用的。这种方式不需要root或者administrator权限。但这种方式有下面几个限制：

1. 需要很多开销，因此性能是很差的。
2. ICMP协议无法工作（无法使用ping命令）。
3. guest主机没法从host和外部网络接入。

用户模式网络使用[slirp](http://en.wikipedia.org/wiki/Slirp)实现，在qemu中它提供全功能的TCP/IP栈，并使用这个栈实现一个虚拟的NAT'd网络。

下面是这个典型（默认）的网络：
![QEMU User networking（SLIRP）](http://wiki.qemu.org/images/9/93/Slirp_concept.png)

你能够配置用户模式网络使用 *-netdev user* 命令行选项。
添加以下的qemu命令会改变网络配置使用*192.168.76.0/24*代替默认的*10.0.2.0/24*并启动guest DHCP 分配从*9*开始（代替*15*）：

```bash
-netdev user,id=mynet0,net=192.168.76.0/24,dhcpstart=192.168.76.9
```

**TO understand**

>You can isolate the guest from the host (and broader network) using the restrict option. For example -netdev user,id=mynet0,restrict=y or -netdev type=user,id=mynet0,restrict=yes will restrict networking to just the guest and any virtual devices. This can be used to prevent software running inside the guest from phoning home while still providing a network inside the guest. You can selectively override this using hostfwd and guestfwd options.

TODO:

```txt
-netdev user,id=mynet0,dns=xxx

-netdev user,id=mynet0,tftp=xxx,bootfile=yyy

-netdev user,id=mynet0,smb=xxx,smbserver=yyy

-netdev user,id=mynet0,hostfwd=hostip:hostport-guestip:guestport

-netdev user,id=mynet0,guestfwd=

-netdev user,id=mynet0,host=xxx,hostname=yyy
```

##### Tap 网络

Tap 网络后端使用host的tap网络设备。它提供很不错的性能并且可以创建任何种类的网络拓扑。不幸的是，它需要在host中设定网络拓扑，在不同的操作系统中方法是不同的。一般来说，它需要你有root权限。

```bash
-netdev tap,id=mynet0
```

##### Tap 网络补充说明

TUN and TAP 是虚拟网络内核设备，完全用软件实现的虚拟设备。
TAP模拟一个链路层的设备，它可以操作二层网络包，例如以太网帧。可以把TAP看成一个虚拟网卡。
更多详细的说明请参考：

1. [TUN/TAP Wikipedia](http://en.wikipedia.org/wiki/TUN/TAP).
2. [tuntap.txt](https://www.kernel.org/doc/Documentation/networking/tuntap.txt)

QEMU 会在你的主机添加一个名为(tapN)虚拟的网络设备，你可以像配置网卡一样配置这个网络设备。在linux host上这个的实现是通过TUN/TAP，因此，你必须确保你的host的内核支持TUN/TAP（*/dev/net/tun*这个设备必须存在）；在windows主机上可以通过安装TAP-win32，这个包含在[OpenVPN](https://community.openvpn.net/openvpn/wiki/ManagingWindowsTAPDrivers)包中。

创建一个虚拟主机：

```bash
sudo kvm -smp cpus=1 -boot order=cd,menu=on -m 300M -drive file=test2.img -netdev tap,id=tapnet1,ifname=tap0,script=no,downscript=no -device virtio-net,mac=52:54:00:bd:cb:01,netdev=tapnet0
```

*sudo*：需要管理员权限创建tap虚拟网卡。
*-netdev tap*：创建host的tap接口并连接host的TAP网络接口。
*script=no,downscript=no*：为创建的网卡进行配置，这里no说明不执行脚本，默认情况下qemu使用*/etc/qemu-ifup*和/*etc/qemu-ifdown*这两个脚本对创建的虚拟网卡进行配置，由于这里未使用，这两个脚本以后分析。

创建成功后，虚拟主机运行起来了，但是并未有网络连接。在虚拟主机guest中执行```lspci```：

> 00:03.0 Ethernet controller: Ret Hat, Inc Virtio network device

可以看到guset主机中已有网络设备。
另外，在host主机中运行```ip link list```:

> tap0: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT group default qlen 500

可以看到qemu在host创建的虚拟网卡的state未down的状态。**qemu是通过连接guest中的网络设备到host中的tap设备，必须保证tap设备的状态未启用状态**。通过命令```sudo ip link set tap0 up```启动tap0设备。这时候guest其实就可以通过host的tap0虚拟网络接口进行通信了（可以理解成有一台主机（guest）和通了一根网线，但网线未插到路由器或者交换机上）。

现在我们为了让host虚拟网卡tap0加入一个网络，可以使用多种方法：

###### 方法一 （相当于VMWare中的桥接模式）
在host主机上创建linux bridge， 通过linux bridge连接tap0和真实的物理网卡eth0,并通过eth0连接外网。

我们使用eth0所在网络和网络中的dhcp，网关。相应的操作如下：
1. 添加linux bridge

```bash
sudo brctl addbr br0
sudo brctl addif br0 eth0
```

2. 配置网卡，```sudo vim /etc/network/interface```

```txt
auto eth0
iface eth0 inet manual
```

3. 设定网卡
```bash
sudo ip link set eth0 down
sudo ip link set eth0 up
sudo ip link set eth0 promisc on
sudo ip link set tap0 up
sudo ip link set tap0 promisc on
sudo ip link set br0 up
sudo dhclient br0
sudo brctl addif br0 tap0
```

在guest主机上进行网路测试：

配置网络```sudo vim /etc/network/interface```

```txt
auto eth0
iface eth0 inet dhcp
```
运行脚本重启网络

```bash
sudo ifdown eth0
sudo ifup eth0
```

进行网路测试```ifconfig```查看当前网络设定
如果正确获得host主机所在网络的ip地址并且能够ping通host网络的主机则表示设定成功。

关闭方法
1. 关闭虚拟机

2. 删除linux bridge 重新配置 eth0

```bash
sudo brctl delif br0 eth0
sudo ip link set br0 down
sudo brctl delbr br0
sudo dhclient eth0
```

###### 方法二 （相当于VMware中的host-only模式）
同样创建linux bridge，不过linux bridge不连接任何host主机的网络接口（eth0）。

启动2台虚拟机使用tap0和tap1

```bash
sudo kvm -smp cpus=1 -boot order=cd,menu=on -m 300M -drive file=test.img -netdev tap,id=tapnet0,ifname=tap0,script=no,downscript=no -device virtio-net,mac=52:54:00:bd:cb:01,netdev=tapnet0
sudo kvm -smp cpus=1 -boot order=cd,menu=on -m 300M -drive file=test2.img -netdev tap,id=tapnet1,ifname=tap1,script=no,downscript=no -device virtio-net,mac=52:54:00:bd:cb:02,netdev=tapnet1
```

```bash
sudo brctl addbr privatebr0
sudo brctl addif privatebr0 tap0
sudo brctl addif privatebr0 tap1
sudo ip link set privatebr0 up
sudo ip link set tap0 up
sudo ip link set tap1 up
sudo ifconfig privatebr0 192.168.44.1
```

进入虚拟机guest1配置ip

```bash
sudo ifconfig eth0 192.168.44.100
```

进入虚拟机guest2配置ip

```bash
sudo ifconfig eth0 192.168.44.101
```

host guest1 guest2之间能够相互ping通则正确设定网络。

**补充说明**：
1. guest需要上网：

guest配置默认路由

*192.168.44.1*为host主机*privatebr0*的ip地址

```
route add default gw 192.168.44.1
```

host主机进行配置：
打开host主机的ip转发功能，设置host主机的nat转发,```sudo vim /etc/sysctl.conf```。

```txt
net.ipv4.ip_forward=1
```

使内核转发生效：

```
sudo sysctl -p
```

设置host主机nat转换：

```
sudo iptables -t nat -A POSTROUTING -s 192.168.44.0/24 -o eth0 -j MASQUERADE
```

这里*eth0*通过eth0接口能够访问互联网。

测试，在guest主机中ping外网ip看看能否接通。

2. guest需要dhcp设定ip：TODO



#### 配置 ubuntu-vm-builder 创建一个默认的网桥vm

#### 生成一个KVM MAC地址

#### 重配置一个存在的vm

## 创建客户机

目前，kvm已经安装完成，下面是如何创建第一个VM。可以通过如下你个工具：

1. virt-manager
2. virt-install
3. ubuntu-vm-builder

### 通过virt-manager创建虚拟机

## 管理

[^foot-note-1]: 如果显示找不到命令，可以根据提示安装 ```apt-get install cpu-checker```

[^foot-note-2]: libvirt-sock的的权限```srwxrwx--- 1 root libvirtd 0 2010-08-24 14:54 /var/run/libvirt/libvirt-sock```

[^foot-note-3]: kvm的权限```crw-rw---- 1 root kvm 10, 232 Sep 16 14:32 /dev/kvm```改变权限```chown root:libvirtd /dev/kvm```, 重新登录或者重启内核模块 ```rmmod kvm```, ```modprobe -a kvm```

[^foot-note-4]: If your VM host "freezes" for a few seconds after starting or stopping a KVM guest when using bridged networking, it is because a Linux bridge will take the hardware address of the lowest numbered interface out of all of the connected interface. To work around this, add the following to your bridge configuration:```post-up ip link set br0 address f4:6d:04:08:f1:5f```and replace f4:6d:04:08:f1:5f with the hardware address of a physical ethernet adapter which will always be part of the bridge.



