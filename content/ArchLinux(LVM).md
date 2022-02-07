Title: ArchLinux(LVM)
Date: 2021-10-30 13:26:43
Tags: Linux
Slug: archlinux-lvm
Authors: sin
Summary: ArchLinux 安装，使用LVM作为root

####  下载镜像

[ArchLinux官网](https://archlinux.org/)上可以直接下载ISO。



#### 启动

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211027064416.png)



选择启动。



#### 分区

我们选择MBR，不选择UEFI来启动。

首先设计一下分区表

| 设备      | 类型 | 挂载点 |
| --------- | ---- | ------ |
| /dev/sda1 | vfat | /boot  |
| /dev/sda2 | lvm  | /      |

格式化分区

    :::bash
    mkfs.vfat /dev/sda1

    pvcreate /dev/sda2
    vgcreate arch-vg /dev/sda2
    lvcreate -l 100%Free -n root arch-vg
    mkfs.ext4 /dev/arch-vg/root


#### 挂载分区

    :::bash
    mount /dev/arch-vg/root /mnt
    mkdir -p /mnt/boot
    mount /dev/sda1 /mnt/boot


#### 选择镜像地址

编辑 /etc/pacman.d/mirrorlist， 在文件的最顶端添加

    :::bash
    Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch

#### 安装基本系统

    :::bash
    pacstrap -i /mnt base base-devel linux linux-firmware

![png](https://gitee.com/xuanmingyi/imagebed/raw/master/img/20211027071128.png)



#### 配置系统

    :::bash
    genfstab -U /mnt >> /mnt/etc/fstab
    cp /etc/pacman.d/mirrorlist /mnt/etc/pacman.d/mirrorlist


#### 切换新系统并配置

    :::bash
    arch-chroot /mnt

    sed -i s/#zh_CN.UTF-8/zh_CN.UTF-8/g  /etc/locale.gen
    sed -i s/#en_US.UTF-8/en_US.UTF-8/g  /etc/locale.gen
    locale-gen

    echo LANG=en_US.UTF-8 > /etc/locale.conf

    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    hwclock --systohc --utc

    hostnamectl set-hostname arch


#### 安装必要软件

    :::bash
    pacman -Syu 
    pacman -S vim dhclient


#### LVM2支持

    :::bash
    pacman -S lvm2

    # 修改/etc/mkinitcpio.conf 在block和filesystems中添加 lvm2
    HOOKS="base udev ... block lvm2 filesystems"

    mkinitcpio -p linux


#### 安装bootloader

    :::bash
    pacman -S grub
    grub-install --target=i386-pc /dev/sda
    grub-mkconfig -o /boot/grub/grub.cfg


#### 修改root密码

    :::bash
    passwd


#### 创建用户

    :::bash
    useradd sin
    passwd sin
    mkdir /home/sin
    chown sin:sin /home/sin


#### 安装sudo

    :::bash
    pacman -S sudo

    visudo # 或者 vim /etc/sudoers

    # 添加一行
    sin ALL=(ALL:ALL) NOPASSWD:ALL


#### 安装openssh

    :::bash
    pacman -S openssh
    systemctl enable sshd
