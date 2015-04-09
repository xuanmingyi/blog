Title: Ubuntu刷机实录
Date: 2015-01-02 09:44
Tags: Ubuntu
Authors: Sin
Category: Technology

**参考资料**

[这个](https://developer.ubuntu.com/en/start/ubuntu-for-devices/installing-ubuntu-for-devices/)

**支持的机器**

要刷Ubuntu系统必须有Ubuntu支持的设备,Android现在是个机器就支持,但是Ubuntu就很勉强了,基本只支持Nexus系列,[这里](http://developer.ubuntu.com/en/start/ubuntu-for-devices/devices/)是官方支持的列表,当然[非官方的支持设备](https://wiki.ubuntu.com/Touch/Devices)还是很多的,更多的是WIP(Woring In Process).

**安装工具**

安装好Ubuntu桌面系统之后,如果是14.04之前的系统,需要先

    $ sudo add-apt-repository ppa:phablet-team/tools
    $ sudo add-apt-repository ppa:ubuntu-sdk-team/ppa
    $ sudo apt-get update

然后安装工具

    $ sudo apt-get install ubuntu-device-flash
    $ sudo apt-get install phablet-tools

安装ubuntu-device-flash的同时会安装adb和fastboot这两个有用的工具.

adb: 从终端连接到一个完整启动的设备
fastboot: 从终端通过USB连接到一个启动到bootloader的设备

**在Android上设置开发者模式**

1 打开 *设置/Settings* > *关于手机/About phone | 关于平板/About tablet | 关于/about*
2 找到 *版本号*/*Build number* , 连续点击7下, 弹出成功信息.

**打开USB调试**

1 打开 *设置/Settings* > *开发者选项/Developer options*
2 打开 *USB调试/USB Debugging*
3 然后物理连接到电脑
4 在设备屏幕上选择 *允许USB调试/Allow USB debugging*
5 在系统终端中获得已经连接的设备

    $ adb devices
    List of devices attached
    025d138e2f521413 device

**解锁机器**

1 使机器进入bootloader状态, 在机器关机状态下,也可以用一起按电源键和音量下键来进入bootleader状态.

    $ adb reboot bootloader

2 查看谁被是否已经被连接

    $ sudo fastboot devices

3 解锁机器

    $ sudo fastboot orm unlock

4 接受设备上的条款
5 重启机器

    $ sudo fastoobt reboot

**根据设备选择channel**

查看[文档](http://developer.ubuntu.com/en/start/ubuntu-for-devices/image-channels/),Nexus 7可以选择 *ubuntu-touch/ubuntu-rtm/14.09-proposed* 或者 *devel*

**刷机**

1 关机,按住音量减少键+电源键启动,进入*recovery mode*

2 输入命令

    $ ubuntu-device-flash --channel=devel --bootstrap

*Tips*: 

 * 当第一次刷入Ubuntu的时候,需要加上*--bootstrap*选项,以后刷就不需要这个选项了.
 * 可能需要翻墙...

3 等等等等等

到这里机器基本刷好了.

![效果](http://ww4.sinaimg.cn/mw690/68ef69degw1enwmdahcenj21w02io4qp.jpg)
