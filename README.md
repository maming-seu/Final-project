# Final-project
实验语言：python3
所用拓展库：
实现目标：编写一个python脚本程序，以实现自动的动态数据收集工作
所支持操作系统：linux ubantu18.04
具体功能：
    操作系统信息、
    硬件配置、
    进程、
    网络、
    服务、
    日志、
cmd命令：
    日期：date
    os：cat /etc/issue
    kernel：uname -a
    cpu：cat /proc/cpuinfo
    mem：cat /proc/meminfo
    uptime：uptime
    硬盘：fdisk -l
    硬盘分区：fd -h
    软件信息：dpkg --get-selections
    周期运行软件：crontab -l
               ls -l /etc/cron*
    在跑服务：service --status-all
    驱动：lsmod
    用户组信息：cat /etc/passwd
    网络信息：
    网卡：ifconfig -a
    路由表：netstat -rn
    arp缓存：arp -a
    进程网络连接：netstat -anp
    进程操作文件信息：lsof
    进程信息：ps auxwwem
    当前用户历史执行命令：vi /root/.bash_history

注意需要
    sudo python3 livedataget.py
    并且要保证安装过net-tools负责需要提前sudo apt install
