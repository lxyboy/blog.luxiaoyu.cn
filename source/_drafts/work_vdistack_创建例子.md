1. 管理员登录

2. 创建租户 tenant1  返回默认组 group_id = 3, tenant_id = 1

同时创建openstack 用户名openstack_tenant_id的用户，密码为openstack_tenant_id的md5值

3. 创建公司中的部门（Group概念） 

其中parent_group_id = 3为父亲部门的id

返回id = 4 则该新建部门的id为4

4. 创建该租户该部门的管理员用户 user1

group_id = 4  属于的部门为4
is_admin = true 是否为管理员为是

返回 id = 3 该用户的id = 3

5. 为该租户创建网络

id = f3077acf-3b3e-4d14-96b9-cf5e2d389aa3

6. 为该租户创建路由

id = a378915d-6156-4ed2-8ea5-b1b32f3b8aea

7. 连接路由器到网络

8. 为tenant1添加主机


