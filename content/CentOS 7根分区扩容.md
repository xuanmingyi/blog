Title: CentOS 7根分区扩容
Date: 2021-06-24 11:00:00
Tags: Linux
Slug: centos-7-extend-lvm-root
Authors: sin
Summary: CentOS 7 扩容LVM根分区

CentOS7 默认使用xfs作为文件系统，首先分区

    :::bash
    fdisk -l /dev/sda
    n    创建新分区
    p    主分区
    回车  开始
    回车  结束
    w    保存

    mkfs -t xfs /dev/sda3

接下来把sda3作为扩展分区加入到逻辑组中

    :::bash
    pvcreate /dev/sda3     # 创建pv
    vgextend cl /dev/sda3  # 新的pv加入到vg
    lvextend -l +100%free  /dev/mapper/cl-root   # 把cl-root扩展100%free
    xfs_growfs /dev/mapper/cl-root    # xfs_growfs 增加容量
