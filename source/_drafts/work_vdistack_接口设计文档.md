
## 登录登出接口

### 登录接口

URL: ```/auth/login```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| identification || String || 用户名#租户名 如果无#则默认为非租户人员 || Y ||
|| password || String || 用户密码 || Y ||

### 登出接口

URL: ```/auth/logout```
Method: ```GET```    

## 租户接口

### 创建租户

URL: ```/keystone/tenants```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| name || String || 创建的租户名 || Y ||
|| description || String || 对租户的描述 || N ||
|| customer_manager || String || 经理人 || N ||
|| default || bool || 是否创建默认网络，默认不创建　|| N ||
|| admin_name || string || 管理员名 默认为 admin || N ||
|| admin_password || string || 管理员密码 || N ||
|| admin_description || string || 管理员描述 || N ||

### 修改租户

URL: ```/keystone/tenants/<int:tenant_id>```
URL: ```/keystone/tenants```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || Integer || 需要修改租户的id || Y ||
|| name || String || 修改的租户名 || N ||
|| description || String || 对租户的描述 || N ||
|| customer_manager || String || 经理人 || N ||
|| enabled || String || 启用禁用 || N ||

### 获取租户

#### 1 获取单个

URL: ```/keystone/tenants/<int:tenant_id>```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || Integer || 租户的唯一id || Y ||

#### 2 获取所有

URL: ```/keystone/tenants```
Method: ```GET```

## 组接口

### 创建组

URL: ```/keystone/groups```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| parent_group_id || Integer || 父亲组id || Y ||
|| name || String || 组名 || Y ||
|| description || String || 组描述 || N ||

### 获取组

**不支持获取所有！**

获取当前组信息，返回children_set描述子组信息

URL: ```/keystone/groups/<int:group_id>```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || 需要获取的组的id || Y ||

### 修改组

URL: ```/keystone/groups/<int:group_id>```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || 需要修改的组的id || Y ||
|| name || String || 新名字 || N ||
|| description || String ||  新描述 || N ||

### 删除组

**前提：**当前组为空组，即无用户，无子组

URL: ```/keystone/groups/<int:group_id>```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || 需要删除的组的id || Y ||

## 用户接口

### 创建用户

URL: ```/keystone/users```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || 属于哪一个组 || Y ||
|| name || String || 用户名,用以登录 用户名#租户名 || Y ||
|| password || String || 密码 || Y ||
|| description || String || 描述 || N ||
|| enabled || Bool || 是否启用 默认启用|| N ||
|| is_admin || Bool || 是否为该组管理员 默认否 || N ||

### 修改用户信息

URL: ```/keystone/users/<int:user_id>```
Method: ```PUT```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| user_id || Integer || 用户唯一id || Y ||
|| group_id || Integer || 用户所在组） || Y ||
|| name || String || 用户名 || N ||
|| password || String || 密码 || N ||
|| description || String || 描述 || N ||
|| enabled || Bool || 是否启用 默认启用|| N ||
|| is_admin || Bool || 是否为该组管理员 默认否 || N ||

### 获取用户

URL: ```/keystone/users```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || 获取某组的所有用户  || Y ||
|| user_id || Integer || 获取某个用户信息, 如果有user_id必须是要有管理员权限，有该参数忽略group_id || N ||

### 移除用户

URL: ```/keystone/users```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| group_id || Integer || 如果不指定则在所有组中删除（admin权限）  || N ||
|| user_id || Integer || 用户的id || Y ||


## 虚拟主机接口

### 创建主机

URL: ```/nova/servers```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || Int || 租户ID || Y ||
|| image_id || String || 映像名称 || Y ||
|| network_ids || List String || 获取到的network的id || Y ||
|| instance_type || String || 模板名称, 如果存在该参数可以忽略下面的cpu参数和memory参数 || N ||
|| cpu || String ||  cpu个数 || N ||
|| memory || String || 内存单位M || N ||
|| instance_name || String || 主机名称 || N ||
|| availability_zone || String || 可用区域的名字如果不提供则会自动选择 || N ||
|| security_groups || List String || 防火墙名字 可多项 || N ||
|| virtual_server_type || Integer || 2 代表共享，1代表私有主机 默认为私有 || N ||
|| default || Bool || 创建默认网络和路由 默认为False || N ||

### 删除主机

**注意：解除绑定**

URL: ```/nova/servers```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || int ||租户id　|| True ||
|| virtual_server_id || int || 虚拟主机ID || True ||

### 主机操作

URL: ```/nova/command/<command>/<int:server_id>```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| command || string || 命令 || Y ||
|| server_id || int || 虚拟机id || Y ||

关于命令参数：

|| *command值* || *描述* ||
|| pause || 暂停 ||
|| unpause || 取消暫停 ||
|| stop || 停止运行服务器 ||
|| start || 开始运行 ||
|| suspend || 挂起 ||
|| resume || 恢复 ||
|| reboot || 重启 软重启||

## 网络 路由

### 获取租户虚拟网络

URL: ```/network/network```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| network_id || string || 网络的唯一id || N ||
|| tenant_id || int || 租户的id，管理员必须提供 || N ||

### 创建租户虚拟网络

URL: ```/network/network```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || Integer || 租户的ID || Y ||
|| network_name || String || 网络名称（唯一） || Y ||
|| dhcp_enabled || Bool || 是否启动dhcp || N ||
|| dhcp_start_ip || String || dhcp起始ip || N ||
|| dhcp_end_ip || String || dhcp结束ip || N ||
|| gateway || String || 网关 || Y ||
|| cidr || Srring || 网络地址 例如：192.168.22.0/24 || Y ||
|| dns || String || 默认DSN || N ||

### 删除租户虚拟网络

URL: ```/network/network```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| network_id || String || 网络唯一标识 || Y ||

### 获取租户外部网络

外部网络该网络是分配给租户虚拟路由的，相当于路由器wan口连接的网络

URL：```/network/external_network```
Method: ```GET```


### 创建虚拟路由器

URL：```/network/router```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| name || String || 虚拟路由的名称 || Y ||
|| tenant_id || int || 租户的ID || 非管理员N ，管理员Y ||
|| external_network_id || String || 虚拟路由器连接的外部网络ID || Y ||

### 删除虚拟路由器

URL：```/network/router```
Method: ```DETELE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| router_id || String || 虚拟路由唯一id  || Y ||

### 获取虚拟路由

URL：```/network/router```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || int || 租户id  || N, 管理员Y ||

### 获取虚拟路由连接的内部网络

URL：```/network/router_network```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| router_id || String || 虚拟路由ID || Y ||
|| tenant_id || Int || 租户ID || N，管理员Y ||

### 连接虚拟网络到虚拟路由

URL：```/network/router_network```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| router_id || String || 虚拟路由ID || Y ||
|| tenant_id || Int || 租户ID || N，管理员Y ||
|| network_id || String || 虚拟网络ID || Y ||

### 断开虚拟网络到虚拟路由

URL：```/network/router_network```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| router_id || String || 虚拟路由ID || Y ||
|| tenant_id || Int || 租户ID || N，管理员Y ||
|| network_id || String || 虚拟网络ID || Y ||


## 分配管理独享主机给用户

### 分配独享主机给用户

URL：```/nova/virtual_server_assign```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| server_id || Int || 虚拟主机ID || Y ||
|| user_id || Int || 用户ID || Y ||

### 取消分配独享主机给用户

URL：```/nova/virtual_server_assign```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| server_id || Int || 如果有绑定则删除 || Y ||


## 工单

### 创建工单

URL：```/ticket/user```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| title || String || 标题 || Y ||
|| content || String ||内容　|| N ||

### 用户获取工单

URL：```/ticket/user```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || 工单唯一id　|| N ||
|| status || string || 工单状态 || N ||

### 用户删除取消工单

URL：```/ticket/user```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || 工单唯一id　|| Y ||
|| cancel || bool || 取消， 删除，默认为取消 || N ||

### 用户获取待确认工单

URL：```/ticket/confirm```
Method: ```GET```

### 用户确认工单

URL：```/ticket/confirm```
Method: ```POST```

### 电信管理员获取待审查工单

URL：```/ticket/review```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || 工单唯一id　|| N ||
|| status || string || 工单状态 || N ||

### 电信管理员审查工单

URL：```/ticket/review```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| passwd || bool || 是否通过 默认为通过 || N ||
|| ticket_id || int || 工单唯一id　|| Y ||

### 运维管理查询带接收工单

URL：```/ticket/receive```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || 工单唯一id　|| N ||
|| status || string || 工单状态 || N ||

### 运维管理接收工单

URL：```/ticket/receive```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || 工单唯一id　|| Y ||

### 运维管理查询带处理工单

URL：```/ticket/handle```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || 工单唯一id　|| N ||
|| status || string || 工单状态 || N ||

### 运维管理处理工单

URL：```/ticket/handle```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| ticket_id || int || 工单唯一id　|| Y ||

## 工单（v2）

可以替换原工单v1

### 获取工单种类

URL：```/ticket/type```
Method: ```GET``

|| *Parameter* || *Type* || *Description* || *Required* ||

### 获取工单（租户用户）

URL：```/ticket/tenant```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| status_id || int_list || 多项状态 || N ||
|| ticket_type_id || int_list || 多项 总类 || N ||

### 工单操作（租户用户）

URL：```/ticket/tenant```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| action || string || 见下面表格 || N 默认为 create ||
|| ticket_name || string || 工单名 || N ||
|| ticket_content || string || 工单内容 ||

action 参数说明

|| action工单操作 || ticket_type_id对应的工单种类 || 说明 ||
|| create || 1 资源修改 || 申请 ||
|| error_report || 3 故障报修 || 申请 ||
|| suggestion || 4 投诉建议 || 提交 ||

### 获取工单（电信用户）

URL：```/ticket/telecom```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| status_id || int_list || 多项状态 || N ||
|| ticket_type_id || int_list || 多项 总类 || N ||

### 工单操作（电信用户）

URL：```/ticket/telecom```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| action || string || 见下面表格 || N 默认为 accept ||
|| result || Bool || 操作的结果， 是否接受 || N ||
|| ticket_id || int || 需要操作的ticket的id || N ||
|| extra || string || 描述操作的额外信息 || N ||
|| ticke_name || string || 创建 资源开通工单名 || N ||
|| ticket_content || string || 创建 资源开通工单内容 || N ||

|| action工单操作 || ticket_type_id对应的工单种类 || 说明 ||
|| accept || 1 资源修改 || 受理 ||
|| send || 1 资源修改 ||  派单||
|| confirm || 1 资源修改， 2 资源开通 || 完工 ||
|| create || 2 资源开通 || 派单 ||

### 获取工单（平台管理员）

URL：```/ticket/maintain```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| status_id || int_list || 多项状态 || N ||
|| ticket_type_id || int_list || 多项 总类 || N ||

### 工单操作（平台管理员）

URL：```/ticket/maintain```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| action || string || 见下面表格 || N 默认为 accept ||
|| result || Bool || 操作的结果， 是否接受 || N ||
|| ticket_id || int || 工单ID || Y ||
|| extra || string || 描述操作的额外信息 || N ||

|| action工单操作 || ticket_type_id对应的工单种类 || 说明 ||
|| accept_platform_deal || 1 资源修改， 2 资源开通 || 平台受理 ||
|| accept_site_construction || 1 资源修改， 2 资源开通　|| 现场施工派单 ||
|| send || 1 资源修改， 2 资源开通 || 验收提交 ||
|| error_report_accept || 3 故障报修 || 受理 ||
|| error_report_done || 3 故障报修  || 已解决 ||
|| error_report_site_construction || 3 故障报修 || 现场施工 ||

## 虚拟硬盘接口

### 获取所有硬盘信息

URL：```/storage/volumes```
Method: ```GET```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id  || int || 租户id || N ||

### 创建硬盘

URL：```/storage/volumes```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || int ||　租户ID　|| Y ||
|| volume_size || int || 大小 单位G || N ||
|| volume_name || string || 硬盘名字 || N ||
|| volume_description || string || 硬盘描述 || N ||

### 删除硬盘

URL：```/storage/volumes```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| volume_id || int || 硬盘id || Y ||
|| tenant_id || int || 租户ID || Y ||

### 挂在硬盘给主机

URL：```/storage/server_attach```
Method: ```POST```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || int || 租户ID ||　Y ||
|| virtual_server_id || int || 虚拟主机ID || Y ||
|| volume_id || int || 需要挂在的磁盘ID || Y ||

返回结果中有 attachement 其中 attachement中的 id 为挂载的唯一标识

### 卸载硬盘给主机

URL：```/storage/server_attach```
Method: ```DELETE```

|| *Parameter* || *Type* || *Description* || *Required* ||
|| tenant_id || int || 租户ID ||　Y ||
|| virtual_server_id || int || 虚拟主机ID || Y ||
|| attach_id || int || 挂载的唯一标识 || Y ||