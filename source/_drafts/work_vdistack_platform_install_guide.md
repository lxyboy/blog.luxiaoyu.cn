## ��Ҫ��װ��

1. Openstack ����
2. VDIStack
3. GatewayController
4. VDIStack Client
5. Client���������

## 1. Openstack ����
Openstack���� �� VDIStack �������������²���

Openstack��������Ҫ����һ����߹���Ա�û���ƽ̨�Ĺ���Ա��role_platform_admin����ӵ�и��û���Ȩ�ޡ�

VDIStack����Ҫ�����ò���vdistack/settings.py��

```
# ����openstack Ĭ�Ϲ���Ա�û�����AUTH_URL
ADMIN_OS_TENANT_NAME = "admin"
ADMIN_OS_USERNAME = "admin"
ADMIN_OS_PASSWORD = "cloudopen"
ADMIN_OS_AUTH_URL = "http://10.10.102.11:35357/v2.0"

# ����openstack��ͨ�û�AUTH_URL
USER_OS_AUTH_URL = "http://10.10.102.11:5000/v2.0"
```

## 2. VDIStack����

�ο� ```vdistack��������``` ����

## 3. GatewayControl ����

ʹ�����е�vdigatewaycontrol����������VDIStack��

```
git clone http://git.cloud-open.cn/vdigateway
cd vdigateway/vdigatewaycontrol
```

�������ݿ�

vim vdigatewaycontrol/settings.py

DATABASES��Ŀ

��ʼ�����ݿ�

```
python manage.py runserver 0.0.0.0:8001
```

��������������
����README�еĲ���

## 4. GatewayAgent
```
git clone http://git.cloud-open.cn/vdigateway
cd vdigateway/vdigatewayagent
```

�������ݿ�

vim vdigatewayagent/settings.py

DATABASES��Ŀ

��ʼ�����ݿ�

```
python manage.py runserver 0.0.0.0:8002
```

��������������
����README�еĲ���
