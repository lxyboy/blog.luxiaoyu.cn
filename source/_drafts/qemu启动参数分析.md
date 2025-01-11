openstack qemu启动参数分析

### *-name* 设置 guest客户机的名字。

```txt
-name instance-0000000b
```

这个名字将会在SDL窗口的标题显示.这个名字也会被VNC服务器使用。

### *-S*

在启动的时候不开始CPU 必须在监视器里输入'c'

### *-machine* 通过 *name* 选择模拟机器

```txt
-machine pc-i440fx-trusty,accel=kvm,usb=off
```

可以通过：```qemu-system-x86_64 -machine help```命令来获取*name*
这里选择的是 *pc-i440fx-trusty* 代表：Ubuntu 14.04 PC (i440FX + PIIX, 1996) (default)
*i440FX* 代表芯片组名
*PIIX* 代表PCI ISA/IDE Accelerator

其他参数：

####*accel*

```accel=kvm```

被用作启用加速器.
在不同的体积结构上有不同的选项，例如 kvm，xen，tcg等。 默认为*TCG*。*TCG*全称为Tiny Code Generator。TCG是默认选项。在openstack选择kvm进行加速。

####*usb*

```usb=off```

**这个作用为止还为查询到**

### *-cpu*

```txt
-cpu Westmere,+rdtscp,+pdpe1gb,+dca,+pcid,+pdcm,+xtpr,+tm2,+est,+smx,+vmx,+ds_cpl,+monitor,+dtes64,+pclmuldq,+pbe,+tm,+ht,+ss,+acpi,+ds,+vme
```

#### *Westmere*

代表cpu模块的型号，可以通过下面命令来获取：

```bash
qemu-system-x86_64 -cpu help
```
#### Recognized CPUID flags

```txt
,+rdtscp,+pdpe1gb,+dca,+pcid,+pdcm,+xtpr,+tm2,+est,+smx,+vmx,+ds_cpl,+monitor,+dtes64,+pclmuldq,+pbe,+tm,+ht,+ss,+acpi,+ds,+vme
```

以上均为cpu的flag如果希望了解可以google或查询cpu手册[^foot-note-1](维基百科:CPUID)

### *-m* 配置内存

```txt
-m 64
```

配置64M内存 默认值为128M

### *-realtime* 以realtime特性运行qemu

```txt
-realtime mlock=off
```
这个作用还需要查找资料 off和on的区别

### *-smp*

```txt
-smp 1,sockets=1,cores=1,threads=1
```

*sockets* 说明cpu的个数
*cores* 指核心及一个cpu上有多少个核
*threads* 为超线程 **需要进一步了解**

*-smp 1*中的1指vcpus，我的理解vcpus=sockets*cores*threads

### *-uuid* 
指明系统的 UUID 唯一标识

### *-smbios*

```txt
-smbios type=1,manufacturer=OpenStack Foundation,product=OpenStack Nova,version=2014.1,serial=44454c4c-4200-1056-8036-c4c04f423358,uuid=b055c2bc-3897-46d0-a9d5-5f34b4fc853d
```
System Management BIOS这个可以参考[^foot-note-2](维基百科：System_Management_BIOS)

### *-no-user-config*

这个选项使得qemu不去加载任何一个用户提供的在sysconfdir中的配置文件, 但是仍然回去家在datadir中的配置文件 
注意：需要了解*sysconfdir* *datadir* 这两个

### *-nodefaults* 不创建默认设备

默认情况下。通常，qemu会创建类似串口，并口，[虚拟控制台(virtual console)](http://blog.csdn.net/dbzhang800/article/details/6939742),monitor device, vga adapter，软盘，cd-rom驱动器，和其他一些设备。*-nodefaults*选项将会禁用所有默认的设备。

**注意：**了解Monitor device是什么？

### -chardev

```txt
-chardev socket,id=charmonitor,path=/var/lib/libvirt/qemu/instance-0000000a.monitor,server,nowait
-chardev file,id=charserial0,path=/var/lib/nova/instances/a446169f-f31f-4827-826b-12667398acf0/console.log

-chardev pty,id=charserial1
```

**注意：**这个*chardev*有什么作用, 和*-mon*的关系又是什么？

### -mon 配置monitor到指定的chardev上

```txt
-mon chardev=charmonitor,id=monitor,mode=control
```

### *-rtc*

```txt
-rtc base=utc,driftfix=slew
```

设置时间相关的

### *-global*
设置默认的driver的属性prop为value值

```txt
-global kvm-pit.lost_tick_policy=discard
```

openstack中的这句作用未知

### *-no-hpet*

禁用 HPET（High Precision Event Timer）高精度事件记时器

### *-no-shutdown*

在guest关闭的时候仅仅关闭模拟器不退出QEMU。这个为了让instance转到monitor来提交disk image的改变。

### *-boot*

```-boot strict=on```

### *-drive*

```txt
-drive file=/var/lib/nova/instances/a446169f-f31f-4827-826b-12667398acf0/disk,if=none,id=drive-virtio-disk0,format=qcow2,cache=none  
-drive file=/var/lib/nova/instances/a446169f-f31f-4827-826b-12667398acf0/disk.swap,if=none,id=drive-virtio-disk1,format=qcow2,cache=none

```

### *-netdev*

```txt
-netdev tap,fd=25,id=hostnet0,vhost=on,vhostfd=27 -device virtio-net-pci,netdev=hostnet0,id=net0,mac=fa:16:3e:f1:25:ae,bus=pci.0,addr=0x3
```

### *-device*

添加一个设备

```txt
-device piix3-usb-uhci,id=usb,bus=pci.0,addr=0x1.0x2
-device virtio-blk-pci,scsi=off,bus=pci.0,addr=0x4,drive=drive-virtio-disk0,id=virtio-disk0,bootindex=1
-device virtio-blk-pci,scsi=off,bus=pci.0,addr=0x5,drive=drive-virtio-disk1,id=virtio-disk1
-device isa-serial,chardev=charserial0,id=serial0
-device isa-serial,chardev=charserial1,id=serial1
-device usb-tablet,id=input0
-device cirrus-vga,id=video0,bus=pci.0,addr=0x2
-device virtio-balloon-pci,id=balloon0,bus=pci.0,addr=0x6
```
#### ```-device piix3-usb-uhci```

添加usb设备

### *-vnc*

```-vnc 10.80.80.20:1```

### *-k*

使用的键盘布局和语言

```-k en-us```

[^foot-note-1]: [维基百科：CPUID](http://en.wikipedia.org/wiki/CPUID)
[^foot-note-2]: [维基百科：System_Management_BIOS](http://en.wikipedia.org/wiki/System_Management_BIOS)