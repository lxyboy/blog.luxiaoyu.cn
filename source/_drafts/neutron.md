# openstack neutron学习笔记


### neutronclient api

```python
from neutronclient.v2_0 import client as neutron_client

username = "project2"
password = "cloudopen"
tenant_name = "project2"
AUTH_URL_V2 = "http://10.10.102.10:5000/v2.0"

neutron = neutron_client.Client(username=username, password=password, tenant_name=tenant_name, auth_url=AUTH_URL_V2)
## 列出网络
networks = neutron.list_networks()['networks']
```