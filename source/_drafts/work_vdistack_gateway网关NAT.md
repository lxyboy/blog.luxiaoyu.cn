# route iptable

iptables -A INPUT -i eth0 -j ACCEPT

echo "1" > /proc/sys/net/ipv4/ip_forward


## SNAT

iptables -t nat -A POSTROUTING -s $innet -o $EXTIF -j MASQUERADE

$innet��һ���� 192.168.1.0/24
$EXTIF��һ���ӿ� eth0
MASQUERADE˵�����Զ���ȡeth0��ip��ַ

## DNAT

iptables -t nat -A PREROUTING -i eth1 -p tcp --dport 33001 -j DNAT --to-destination 192.168.230.129:3306


## ��¼����
1. gateway agent control �����û�gatewayagent������gatewayagent�ӿ����ö˿�ӳ�䣬��¼���ؽ����

2. gateway agent ���ֶ˿ڶϿ��� ���� gateway agent control �ӿ�ɾ�� ���û��Ķ˿�ӳ�����֮��ɾ�����صĹ��� gateway agent�������˿ںš�


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

### �����ڷ����ע��˿�

���� /proc/sys/net/ipv4/ip_local_port_range
����Ƕ�̬�����IP��ַ��Χ
Ĭ��Ϊ��32768 - 61000

���� /proc/sys/net/ipv4/ip_local_reserved_ports
����ǿ��Թ�ϵͳ�����Ķ˿�
Ĭ��Ϊ�գ������ֶ����

10000-20000, 20000-30000

### ���ÿɷ���˿ڷ�Χ

�����������Χ�ڷ���˿�
PORT_RANGE 


### ע�ⲻҪ������SNAT ������DNAT��Ч����