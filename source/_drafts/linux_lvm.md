# Linux LVM learning

### 基本概念

- Physical Volume, PV, 物理卷
  可以在上面建立卷组的媒介，可以是硬盘分区，也可以是硬盘本身或者回环文件（loopback file）。物理卷包括一个特殊的 header，其余部分被切割为一块块物理区域（physical extends）
- Volume Group, VG, 卷组
  将一组物理卷收集为一个管理单元。卷组可以视为一个由若干个物理卷组合而成的“磁盘”。卷组同时也能够包含若干个逻辑卷（logical volume）
- Logical Volumn, LV, 逻辑卷
  一种特殊的虚拟分区，从属于卷组，可以由若干块物理区域构成。

## 基本操作

#### Physical Volume, PV, 物理卷

```
# 维护命令
# pvscan # 在系统中的所有磁盘中搜索已存在的物理卷
# pvdisplay [<物理卷>] # 显示 全部/指定 物理卷的属性信息
# pvs # pvdisplay 简约版，仅能得到物理卷的概要信息
# pvchange [-x {y|n}] [-u] # 用于指定物理卷的 PE 是否允许分配或重新生成物理卷的 UUID
# pvmove <源物理卷> [<目的物理卷>] # 将同一 VG 下的 PV 内容进行迁移，若不指定目的物理卷则由 LVM 决定

# 创建与删除命令
# pvcreate <设备名> # 用于在磁盘或磁盘分区上创建物理卷初始化信息，以便对该物理卷进行操作
# pvremove <物理卷> [-d][-f][-y] # 删除物理卷
```

#### Volume Group，卷组相关操作

```
# 维护命令
# vgscan # 在系统中搜索所有已存在的 vg
# vgck <卷组> # 用于检查卷组中卷组描述区域信息的一致性
# vgdisplay [<卷组>] # 显示 全部/指定 卷组的属性信息
# vgrename <旧卷组名> <新卷组名> # 卷组重命名
# vgchange [-a {y|n}] [-x {y|n}] # 用于指定卷组是否允许分配或者卷组容量是否可伸缩

# 创建与删除命令
# vgcreate <卷组> # 用于创建 LVM 卷组
# vgremove <卷组> # 用于删除 LVM 卷组

# 扩充与缩小命令
# vgextend <卷组> <物理卷> # 向卷组中添加物理卷来增加卷组的容量
# vgreduce <卷组> <物理卷> # 向卷组中删除物理卷来减小卷组的容量

# 合并与拆分命令
# vgmerge <目的卷组> <源卷组> # 将源卷组合并至目的卷组，要求两个卷组的物理区域大小相等且源卷组是非活动的(inactive)
# vgsplit <源卷组> <目的卷组> <源物理卷> # 将源卷组的源物理卷拆分到目的卷组
# vgexport <卷组> # 用于输出卷组，将非活动的(inactive)的卷组导出，可用于其他系统中使用
# vgimport <卷组> <物理卷> # 用于输入卷组

# 备份与恢复命令
# vgcfgbackup <卷组> # 备份卷组的元信息至 /etc/lvml/backup 目录中
# vgcfgrestore <卷组> # 从备份文件中恢复指定卷组
```

#### Logical Volume，逻辑卷相关操作

```
# 维护命令
# lvscan # 在系统中搜索所有已存在的 lv
# lvdisplay [<逻辑卷>] # 显示 全部/指定 逻辑卷的属性信息
# lvrename {<卷组> <旧逻辑卷名> <新逻辑卷名> | <旧逻辑卷路径名> <新逻辑卷路径名>}
# lvchange # 更改逻辑卷的属性

# 创建与删除命令
# lvcreate <逻辑卷> <卷组> # 用于创建卷组中的逻辑卷
lvcreate -n ubuntu-home-lv -L 150G ubuntu-home-vg
# lvremove <逻辑卷> <卷组> # 用于删除卷组中的逻辑卷
lvremove /dev/ubuntu-home-vg/ubuntu-home-lv

# 扩充与缩小命令
# lvextend -L +<增量> <逻辑卷> # 根据增量对逻辑卷容量进行扩充
# lvreduce -L -<减量> <逻辑卷> # 根据减量对逻辑卷容量进行缩小
```

#### Btrfs

```
mkfs.btrfs -L data /dev/mapper/ubuntu--home--vg-ubuntu--home--lv
```

#### Automount

```
lsblk
blkid
```

```
#modify /etc/fstab
/dev/disk/by-uuid/447dc1cc-4f9b-40a0-bba3-adfa525d4671 /root btrfs defaults 0 1
# restart systemd
systemctl daemon-reload
```

