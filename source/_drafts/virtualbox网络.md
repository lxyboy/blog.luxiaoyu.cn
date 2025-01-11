## virtualbox 网络

ctrl+g开启host-only adapter模式 vboxnet0

设置其网络地址为172.16.0.1  在172.16.0.0/24网段
设置dhcp服务器


##在guest主机中设置dhcp并设置gw为172.16.0.1

```bash
route add default gw 172.16.0.1
```

在guest主机及中```/etc/network/interface```设置dns-nameserver 为 114.114.114.114或其他dns

##在host中设置ip转发

sudo vim /etc/sysctl.conf

```
net.ipv4.ip_forward=1
```

sudo sysctl -p

主机设置路由转发

添加
sudo iptables -t nat -A POSTROUTING -s 172.16.0.0/24 -o eth0 -j MASQUERADE
删除
sudo iptables -t nat -D POSTROUTING -s 172.16.0.0/24 -o eth0 -j MASQUERADE


## 测试&&排错

1. guest ping 172.16.0.1 gw能 ping 通

2. host ping 172.16.0.1 能ping通

3. host ping guest 能ping通

4. guest ping host 能ping通

5. guest ping 114.114.114.114能ping通

6. guest ping www.baidu.com能ping通

