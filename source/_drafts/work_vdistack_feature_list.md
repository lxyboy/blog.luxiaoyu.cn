feature list vdistack

v1.0.1
电信管理员的租户列表，工单状态，工单处理
运维管理员租户开户，桌面管理，工单处理
租户管理员仅能管理该租户的资源
普通用户分组 按部门（1层）
支持系统默认镜像
支持WIN7 64bit虚拟桌面（32bit镜像需要做并上传，这部分不属于开发，xp桌面相同）
支持后台更新（实现方式为cs架构，需要配合vdistackclientserver，vdistackclientadmin）
支持独享桌面
支持基于数据中心部署的AD域服务器的桌面登录认证（开发无关）
支持客户本地AD域服务桌面认证（vdiclient支持）
硬盘创建删除（支持需后端openstack接口可用）
支持私有网络的的创建删除（租户创建可拥有默认网络prefix为default）
限流（需要讨论暂时未做）
工单v2
支持x86终端
定制操作系统（使用ubuntu发行版本14.04desktop，添加开机启动项vdistackrdpclient）
支持终端保存桌面信息
自动登录获取桌面列表
用户配置界面（配置部分rdp选项）
下载连线包（该功能未实现）
后台系统升级（openstack不清楚，vdistack平台10条内命令，vdistackclientserver10条内命令，vdistack与vdistackclientserver都可平滑升级，openstack不清楚）
监控模块 延后

v1.0
支持用户与桌面绑定
支持桌面启动/休眠（？suspend？）/重启
支持虚拟桌面绑定虚拟网络
Hyper-v/kvm的支持（有限制需要询问毛伟杰）
支持云主机的创建/关闭
路由支持连接私有网络
DHCP支持
端口映射（需要通过vdigatewayagent）
外网IP分配（即floatingip分配，绑定主机默认分配）
支持租户的创建（删除不支持）
工单版本v1
外网网关接入同上面端口映射（需要通过vdigatewayagent）
