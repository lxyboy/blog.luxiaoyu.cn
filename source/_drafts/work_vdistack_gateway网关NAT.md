# route iptable

iptables -A INPUT -i eth0 -j ACCEPT

echo "1" > /proc/sys/net/ipv4/ip_forward


## SNAT

iptables -t nat -A POSTROUTING -s $innet -o $EXTIF -j MASQUERADE

$innet是一个网 192.168.1.0/24
$EXTIF是一个接口 eth0
MASQUERADE说明会自动获取eth0的ip地址

## DNAT

iptables -t nat -A PREROUTING -i eth1 -p tcp --dport 33001 -j DNAT --to-destination 192.168.230.129:3306


## 登录过程
1. gateway agent control 分配用户gatewayagent并调用gatewayagent接口设置端口映射，记录返回结果。

2. gateway agent 发现端口断开后 调用 gateway agent control 接口删除 该用户的端口映射规则，之后删除本地的规则。 gateway agent来决定端口号。


## SNAT python

```
import iptc
postrouting_chain = iptc.Chain(iptc.Table(iptc.Table.NAT), "POSTROUTING")
rule = iptc.Rule()
rule.src = "192.168.230.0/24"
rule.set_out_interface("eth1")
rule.target = iptc.Target(rule, 'MASQUERADE')
postrouting_chain.insert_rule(rule)
postrouting_chain.delete_rule(rule)
```

## DNAT

```
import iptc
prerouting_chain = iptc.Chain(iptc.Table(iptc.Table.NAT), 'PREROUTING')
rule = iptc.Rule()
rule.set_in_interface('eth1')
rule.protocol = 'tcp'
match = rule.create_match('tcp')
match.dport = '33001'
target = rule.create_target('DNAT')
target.to_destination = '192.168.230.129:3306'
prerouting_chain.insert_rule(rule)
prerouting_chain.delete_rule(rule)
```

### 可用于分配的注册端口

关于 /proc/sys/net/ipv4/ip_local_port_range
这个是动态分配的IP地址范围
默认为：32768 - 61000

关于 /proc/sys/net/ipv4/ip_local_reserved_ports
这个是可以供系统保留的端口
默认为空：可以手动添加

10000-20000, 20000-30000

### 配置可分配端口范围

可以在这个范围内分配端口
PORT_RANGE 


### 注意不要忘记做SNAT 仅仅做DNAT无效果的