# Linux_ssr_script

ssr启动安装脚本

fork 自 [Chalres Xu](https://github.com/shadowsocksr-backup/shadowsocksr.git)，感谢作者的贡献！


# 引子
也许是使用Linux的大佬都不屑于写这么简单的教程吧，所以关于如何在Linux上安装使用ssr客户端的教程比较少又比较模糊。

所以我就来写这个教程吧，同时因为Linux克隆github的仓库奇慢并且可能会出现超时的情况（在此感谢GFW），文中及脚本的git仓库均位于我自己搭建的[gogs](https://gogs.io/)。

# 安装
首先确认一下自己自己安装了git。

#### ubuntu
```
sudo apt-get install git
```
#### Centos
```
sudo yum install git
```

然后在具有写权限的目录执行如下命令获取到ssr脚本仓库
```
git clone http://git.mrwang.pw/Reed/Linux_ssr_script.git
```
进入刚刚克隆的仓库目录并赋予`ssr`脚本执行权限
```
cd Linux_ssr_script && chmod +x ./ssr
```
然后将脚本放入可执行脚本的目录
```
sudo mv ./ssr /usr/local/sbin/
```
这样就完成了脚本的安装

# 使用
输入`ssr`，便会有如下的提示：
``` shell
ShadowSocksR python client tool
if you have not installed ssr, run `ssr install` first
Usage:
	 ssr help

 Install/Uninstall
	 ssr install      install shadowsocksr client
	 ssr uninstall    uninstall shadowsocksr client

 Config and Subscribe
	 ssr update       update subscription from http://ss.pythonic.life
	 ssr config       edit config.json
	 ssr xclip        paste configs from clipboard to config.json

 Start/Stop/Restart
	 ssr start        start the shadowsocks service
	 ssr stop         stop the shadowsocks service
	 ssr restart      restart the shadowsocks service

 Testing and Maintenance
	 ssr test         get ip from cip.cc using socks5 proxy
	 ssr log          cat the log of shadowsocks
	 ssr shell        cd into ssr installation dir
	 ssr clean        clean ssr configuration backups
```
我们是第一次使用，所以首先执行
```
ssr install 
```
脚本它会下载ssr客户端并移动到合适的位置，现在我们来编辑配置文件
```
ssr config
```
在里面输入你的节点连接信息，然后保存。
#### 启动
现在，来启动ssr进行哲学上网吧！
```
ssr start
```
#### 关闭
关闭ssr可以输入
```
ssr stop
```
