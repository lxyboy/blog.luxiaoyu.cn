## python optparse 用法

### example

```python
import optparse
parser = optparse.OptionParser(
    usage='%prog --arg1=1 --arg2=arg2'
    )

parser.add_option(
    '-a', '--arg1',
    default='1',
    dest='arg1',
    type='int',
    help='first arg')
    
parser.add_option(
    '-b', '--arg2',
    default='secondarg',
    dest='arg2',
    help='second arg')
    
options, args = parser.parse.parse_args()

print options.arg1
print options.arg2

```

测试

python testoptparse.py -a 123 -b "helloworld"

python testoptparse.py --arg1=123 --arg2="helloworld"

## Paste

TODO

## WebOb

http处理库
TODO


## Paste.deploy 
配置一个wsgi-app

编辑文件*test_paste_deploy.ini*

```ini
[composite:main]
use = egg:Paste#urlmap
/ = home
/blog = blog
/home = home

[app:home]
use = egg:Paste#static
document_root = %(here)s/htdocs

[app:blog]
use = egg:Paste#static
document_root = %(here)s/blogs
```

```
from paste.deploy import loadapp
```

## Routes 1.3



## oslo 介绍

[官网参照连接](https://wiki.openstack.org/wiki/Oslo)

```txt
oslo.concurrency>=0.1.0  # Apache-2.0
oslo.config>=1.4.0  # Apache-2.0
oslo.messaging>=1.4.0
oslo.db>=1.0.0  # Apache-2.0
oslo.i18n>=1.0.0  # Apache-2.0
oslo.serialization>=1.0.0               # Apache-2.0
oslo.utils>=1.0.0                       # Apache-2.0
```

###oslo.messaging 
处理队列消息oslo.messaging kombu PyYAML eventlet amqp anyjson greenlet

对kombu的高层封装

###oslo.i18n>=1.0.0
国际化

###oslo.db

SQLAlchemy封装

###oslo.config 

对配置文件的设置，对命令行选项的配置（可能）


### requests

import requests
request_url = "http://192.168.100.1:8000/login"
params = {"username": "hello", "password": "password"}
res = requests.post(request_url, params=params)



### python socket

```
import socket
port = 3306

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", port))
s.listen(5)

while 1:
    conn, addr = s.accept()
    print "Connected by", addr
    while 1:
        data = conn.recv(1024)
        if not data: break
        print "Recv 1:, data
        conn.sentall(data)
    conn.close()
```

### python struct

网络转换
记住在64位系统上与32位系统上Long的长度是不一样的

struct.pack("!cIII", 'E', 4001, 0, 13)

! 号用来转换网络字节序