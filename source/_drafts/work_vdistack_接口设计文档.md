
## ��¼�ǳ��ӿ�

### ��¼�ӿ�

URL: ```/auth/login```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| identification || String || �û���#�⻧�� �����#��Ĭ��Ϊ���⻧��Ա || Y ||
|| password || String || �û����� || Y ||

### �ǳ��ӿ�

URL: ```/auth/logout```
Method: ```GET```    

## �⻧�ӿ�

### �����⻧

URL: ```/keystone/tenants```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| name || String || �������⻧�� || Y ||
|| description || String || ���⻧������ || N ||
|| customer_manager || String || ������ || N ||
|| default || bool || �Ƿ񴴽�Ĭ�����磬Ĭ�ϲ�������|| N ||
|| admin_name || string || ����Ա�� Ĭ��Ϊ admin || N ||
|| admin_password || string || ����Ա���� || N ||
|| admin_description || string || ����Ա���� || N ||

### �޸��⻧

URL: ```/keystone/tenants/<int:tenant_id>```
URL: ```/keystone/tenants```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || Integer || ��Ҫ�޸��⻧��id || Y ||
|| name || String || �޸ĵ��⻧�� || N ||
|| description || String || ���⻧������ || N ||
|| customer_manager || String || ������ || N ||
|| enabled || String || ���ý��� || N ||

### ��ȡ�⻧

#### 1 ��ȡ����

URL: ```/keystone/tenants/<int:tenant_id>```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || Integer || �⻧��Ψһid || Y ||

#### 2 ��ȡ����

URL: ```/keystone/tenants```
Method: ```GET```

## ��ӿ�

### ������

URL: ```/keystone/groups```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| parent_group_id || Integer || ������id || Y ||
|| name || String || ���� || Y ||
|| description || String || ������ || N ||

### ��ȡ��

**��֧�ֻ�ȡ���У�**

��ȡ��ǰ����Ϣ������children_set����������Ϣ

URL: ```/keystone/groups/<int:group_id>```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || ��Ҫ��ȡ�����id || Y ||

### �޸���

URL: ```/keystone/groups/<int:group_id>```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || ��Ҫ�޸ĵ����id || Y ||
|| name || String || ������ || N ||
|| description || String ||  ������ || N ||

### ɾ����

**ǰ�᣺**��ǰ��Ϊ���飬�����û���������

URL: ```/keystone/groups/<int:group_id>```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || ��Ҫɾ�������id || Y ||

## �û��ӿ�

### �����û�

URL: ```/keystone/users```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || ������һ���� || Y ||
|| name || String || �û���,���Ե�¼ �û���#�⻧�� || Y ||
|| password || String || ���� || Y ||
|| description || String || ���� || N ||
|| enabled || Bool || �Ƿ����� Ĭ������|| N ||
|| is_admin || Bool || �Ƿ�Ϊ�������Ա Ĭ�Ϸ� || N ||

### �޸��û���Ϣ

URL: ```/keystone/users/<int:user_id>```
Method: ```PUT```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| user_id || Integer || �û�Ψһid || Y ||
|| group_id || Integer || �û������飩 || Y ||
|| name || String || �û��� || N ||
|| password || String || ���� || N ||
|| description || String || ���� || N ||
|| enabled || Bool || �Ƿ����� Ĭ������|| N ||
|| is_admin || Bool || �Ƿ�Ϊ�������Ա Ĭ�Ϸ� || N ||

### ��ȡ�û�

URL: ```/keystone/users```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || ��ȡĳ��������û�  || Y ||
|| user_id || Integer || ��ȡĳ���û���Ϣ, �����user_id������Ҫ�й���ԱȨ�ޣ��иò�������group_id || N ||

### �Ƴ��û�

URL: ```/keystone/users```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || �����ָ��������������ɾ����adminȨ�ޣ�  || N ||
|| user_id || Integer || �û���id || Y ||


## ���������ӿ�

### ��������

URL: ```/nova/servers```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || Int || �⻧ID || Y ||
|| image_id || String || ӳ������ || Y ||
|| network_ids || List String || ��ȡ����network��id || Y ||
|| instance_type || String || ģ������, ������ڸò������Ժ��������cpu������memory���� || N ||
|| cpu || String ||  cpu���� || N ||
|| memory || String || �ڴ浥λM || N ||
|| instance_name || String || �������� || N ||
|| availability_zone || String || �������������������ṩ����Զ�ѡ�� || N ||
|| security_groups || List String || ����ǽ���� �ɶ��� || N ||
|| virtual_server_type || Integer || 2 ������1����˽������ Ĭ��Ϊ˽�� || N ||
|| default || Bool || ����Ĭ�������·�� Ĭ��ΪFalse || N ||

### ɾ������

**ע�⣺�����**

URL: ```/nova/servers```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || int ||�⻧id��|| True ||
|| virtual_server_id || int || ��������ID || True ||

### ��������

URL: ```/nova/command/<command>/<int:server_id>```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| command || string || ���� || Y ||
|| server_id || int || �����id || Y ||

�������������

|| *commandֵ* || *����* ||
|| pause || ��ͣ ||
|| unpause || ȡ����ͣ ||
|| stop || ֹͣ���з����� ||
|| start || ��ʼ���� ||
|| suspend || ���� ||
|| resume || �ָ� ||
|| reboot || ���� ������||

## ���� ·��

### ��ȡ�⻧��������

URL: ```/network/network```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| network_id || string || �����Ψһid || N ||
|| tenant_id || int || �⻧��id������Ա�����ṩ || N ||

### �����⻧��������

URL: ```/network/network```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || Integer || �⻧��ID || Y ||
|| network_name || String || �������ƣ�Ψһ�� || Y ||
|| dhcp_enabled || Bool || �Ƿ�����dhcp || N ||
|| dhcp_start_ip || String || dhcp��ʼip || N ||
|| dhcp_end_ip || String || dhcp����ip || N ||
|| gateway || String || ���� || Y ||
|| cidr || Srring || �����ַ ���磺192.168.22.0/24 || Y ||
|| dns || String || Ĭ��DSN || N ||

### ɾ���⻧��������

URL: ```/network/network```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| network_id || String || ����Ψһ��ʶ || Y ||

### ��ȡ�⻧�ⲿ����

�ⲿ����������Ƿ�����⻧����·�ɵģ��൱��·����wan�����ӵ�����

URL��```/network/external_network```
Method: ```GET```


### ��������·����

URL��```/network/router```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| name || String || ����·�ɵ����� || Y ||
|| tenant_id || int || �⻧��ID || �ǹ���ԱN ������ԱY ||
|| external_network_id || String || ����·�������ӵ��ⲿ����ID || Y ||

### ɾ������·����

URL��```/network/router```
Method: ```DETELE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| router_id || String || ����·��Ψһid  || Y ||

### ��ȡ����·��

URL��```/network/router```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || int || �⻧id  || N, ����ԱY ||

### ��ȡ����·�����ӵ��ڲ�����

URL��```/network/router_network```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| router_id || String || ����·��ID || Y ||
|| tenant_id || Int || �⻧ID || N������ԱY ||

### �����������絽����·��

URL��```/network/router_network```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| router_id || String || ����·��ID || Y ||
|| tenant_id || Int || �⻧ID || N������ԱY ||
|| network_id || String || ��������ID || Y ||

### �Ͽ��������絽����·��

URL��```/network/router_network```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| router_id || String || ����·��ID || Y ||
|| tenant_id || Int || �⻧ID || N������ԱY ||
|| network_id || String || ��������ID || Y ||


## �����������������û�

### ��������������û�

URL��```/nova/virtual_server_assign```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| server_id || Int || ��������ID || Y ||
|| user_id || Int || �û�ID || Y ||

### ȡ����������������û�

URL��```/nova/virtual_server_assign```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| server_id || Int || ����а���ɾ�� || Y ||


## ����

### ��������

URL��```/ticket/user```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| title || String || ���� || Y ||
|| content || String ||���ݡ�|| N ||

### �û���ȡ����

URL��```/ticket/user```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || ����Ψһid��|| N ||
|| status || string || ����״̬ || N ||

### �û�ɾ��ȡ������

URL��```/ticket/user```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || ����Ψһid��|| Y ||
|| cancel || bool || ȡ���� ɾ����Ĭ��Ϊȡ�� || N ||

### �û���ȡ��ȷ�Ϲ���

URL��```/ticket/confirm```
Method: ```GET```

### �û�ȷ�Ϲ���

URL��```/ticket/confirm```
Method: ```POST```

### ���Ź���Ա��ȡ����鹤��

URL��```/ticket/review```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || ����Ψһid��|| N ||
|| status || string || ����״̬ || N ||

### ���Ź���Ա��鹤��

URL��```/ticket/review```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| passwd || bool || �Ƿ�ͨ�� Ĭ��Ϊͨ�� || N ||
|| ticket_id || int || ����Ψһid��|| Y ||

### ��ά�����ѯ�����չ���

URL��```/ticket/receive```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || ����Ψһid��|| N ||
|| status || string || ����״̬ || N ||

### ��ά������չ���

URL��```/ticket/receive```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || ����Ψһid��|| Y ||

### ��ά�����ѯ��������

URL��```/ticket/handle```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || ����Ψһid��|| N ||
|| status || string || ����״̬ || N ||

### ��ά��������

URL��```/ticket/handle```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || ����Ψһid��|| Y ||

## ������v2��

�����滻ԭ����v1

### ��ȡ��������

URL��```/ticket/type```
Method: ```GET``

|| *Parameter* || *Type* || *Description* || *Required* ||

### ��ȡ�������⻧�û���

URL��```/ticket/tenant```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| status_id || int_list || ����״̬ || N ||
|| ticket_type_id || int_list || ���� ���� || N ||

### �����������⻧�û���

URL��```/ticket/tenant```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| action || string || �������� || N Ĭ��Ϊ create ||
|| ticket_name || string || ������ || N ||
|| ticket_content || string || �������� ||

action ����˵��

|| action�������� || ticket_type_id��Ӧ�Ĺ������� || ˵�� ||
|| create || 1 ��Դ�޸� || ���� ||
|| error_report || 3 ���ϱ��� || ���� ||
|| suggestion || 4 Ͷ�߽��� || �ύ ||

### ��ȡ�����������û���

URL��```/ticket/telecom```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| status_id || int_list || ����״̬ || N ||
|| ticket_type_id || int_list || ���� ���� || N ||

### ���������������û���

URL��```/ticket/telecom```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| action || string || �������� || N Ĭ��Ϊ accept ||
|| result || Bool || �����Ľ���� �Ƿ���� || N ||
|| ticket_id || int || ��Ҫ������ticket��id || N ||
|| extra || string || ���������Ķ�����Ϣ || N ||
|| ticke_name || string || ���� ��Դ��ͨ������ || N ||
|| ticket_content || string || ���� ��Դ��ͨ�������� || N ||

|| action�������� || ticket_type_id��Ӧ�Ĺ������� || ˵�� ||
|| accept || 1 ��Դ�޸� || ���� ||
|| send || 1 ��Դ�޸� ||  �ɵ�||
|| confirm || 1 ��Դ�޸ģ� 2 ��Դ��ͨ || �깤 ||
|| create || 2 ��Դ��ͨ || �ɵ� ||

### ��ȡ������ƽ̨����Ա��

URL��```/ticket/maintain```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| status_id || int_list || ����״̬ || N ||
|| ticket_type_id || int_list || ���� ���� || N ||

### ����������ƽ̨����Ա��

URL��```/ticket/maintain```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| action || string || �������� || N Ĭ��Ϊ accept ||
|| result || Bool || �����Ľ���� �Ƿ���� || N ||
|| ticket_id || int || ����ID || Y ||
|| extra || string || ���������Ķ�����Ϣ || N ||

|| action�������� || ticket_type_id��Ӧ�Ĺ������� || ˵�� ||
|| accept_platform_deal || 1 ��Դ�޸ģ� 2 ��Դ��ͨ || ƽ̨���� ||
|| accept_site_construction || 1 ��Դ�޸ģ� 2 ��Դ��ͨ��|| �ֳ�ʩ���ɵ� ||
|| send || 1 ��Դ�޸ģ� 2 ��Դ��ͨ || �����ύ ||
|| error_report_accept || 3 ���ϱ��� || ���� ||
|| error_report_done || 3 ���ϱ���  || �ѽ�� ||
|| error_report_site_construction || 3 ���ϱ��� || �ֳ�ʩ�� ||

## ����Ӳ�̽ӿ�

### ��ȡ����Ӳ����Ϣ

URL��```/storage/volumes```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id  || int || �⻧id || N ||

### ����Ӳ��

URL��```/storage/volumes```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || int ||���⻧ID��|| Y ||
|| volume_size || int || ��С ��λG || N ||
|| volume_name || string || Ӳ������ || N ||
|| volume_description || string || Ӳ������ || N ||

### ɾ��Ӳ��

URL��```/storage/volumes```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| volume_id || int || Ӳ��id || Y ||
|| tenant_id || int || �⻧ID || Y ||

### ����Ӳ�̸�����

URL��```/storage/server_attach```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || int || �⻧ID ||��Y ||
|| virtual_server_id || int || ��������ID || Y ||
|| volume_id || int || ��Ҫ���ڵĴ���ID || Y ||

���ؽ������ attachement ���� attachement�е� id Ϊ���ص�Ψһ��ʶ

### ж��Ӳ�̸�����

URL��```/storage/server_attach```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || int || �⻧ID ||��Y ||
|| virtual_server_id || int || ��������ID || Y ||
|| attach_id || int || ���ص�Ψһ��ʶ || Y ||