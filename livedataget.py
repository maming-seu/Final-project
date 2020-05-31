import os
import time
date = "date >> livedata.txt"
systeminfo = "cat /etc/issue >> livedata.txt"



os.system("date")

os.system("echo 'date:' > livedata.txt")

##########################################################################################################data###############
print("建议使用-sudo python3 livedataget.py-来执行程序，因为有些指令需要root权限，否则不能得到预期全部信息——by57117224帅b马鸣宇")
print("还有一点：脚本需要预先安装net-tools，如果运行结果不完整可以试下apt install安装完再试一次")
print("************************date******")

print("collecting date...")
os.system(date)         #collect date
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("date collected")

print("collecting uptime information...")
os.system("echo 'uptime information:' >> livedata.txt")
os.system("uptime | cat >> livedata.txt")   #collect uptime 
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("uptime information collected")

##########################################################################################################os###############

print("************************os******")

print("collecting os information...")
os.system("echo 'os information:' >> livedata.txt")
os.system(systeminfo)   #collect os info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("os information collected")

print("collecting kernel information...")
os.system("echo 'kernel information:' >> livedata.txt")
os.system("uname -a | cat >> livedata.txt")   #collect kernel info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("kernel information collected")

print("collecting user information...")
os.system("echo 'user information:' >> livedata.txt")
os.system("cat /etc/passwd >> livedata.txt")    #collect user info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("user information collected")

##########################################################################################################hardware###############

print("************************hardware******")

print("collecting hardware information...")
os.system("echo 'hardware information:' >> livedata.txt")
time.sleep(1)
print("collecting cpu information...")
os.system("echo 'cpu information:' >> livedata.txt")
os.system("cat /proc/cpuinfo >> livedata.txt")   #collect cpu info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("cpu information collected")

print("collecting mem information...")
os.system("echo 'mem information:' >> livedata.txt")
os.system("cat /proc/meminfo >> livedata.txt")   #collect mem info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("mem information collected")

print("collecting disk information...")
os.system("echo 'disk information:' >> livedata.txt")
os.system("fdisk -l | cat >> livedata.txt")   #collect disk info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("disk information collected")

print("collecting disk partition information...")
os.system("echo 'disk partition information:' >> livedata.txt")
os.system("df -h | cat >> livedata.txt")   #collect disk partition info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("disk partition information collected")
print("hardware information collected")

##########################################################################################################software###############

print("************************software******")

print("collecting software information...")
os.system("echo 'software information:' >> livedata.txt")
os.system("dpkg --get-selections | cat >> livedata.txt")   #collect software info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("software information collected")

print("collecting crontab  information...")
os.system("echo 'crontab  information:' >> livedata.txt")
os.system("crontab -l | cat >> livedata.txt")   #collect crontab  info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("crontab information collected")

##########################################################################################################progress###############

print("************************progress******")

print("collecting basic progress information...")
os.system("echo 'basic progress information:' >> livedata.txt")
os.system("ps auxwwem | cat >> livedata.txt")   #collect basic progress info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("basci progress information collected")

print("collecting progress network connection information...")
os.system("echo 'progress network connection information:' >> livedata.txt")
os.system("netstat -anp | cat >> livedata.txt")   #collect progress' network connection info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("progress network connection information collected")

print("collecting progress file operation information...")
os.system("echo 'progress file operation information:' >> livedata.txt")
print("waiting paitiontly pls, cause there is a 10s sleep for running the cmd _______by 57117224mmy ")
os.system("lsof | cat >> livedata.txt")   #collect progress' file operation info
time.sleep(10)
os.system("echo '************************************************************' >> livedata.txt")
print("progress file operation information collected")

############################################################################################################network###############

print("************************network******")

print("collecting network information...")
os.system("echo 'network information:' >> livedata.txt")
time.sleep(1)
print("collecting network card information...")
os.system("echo 'network card information:' >> livedata.txt")
os.system("ifconfig -a | cat >> livedata.txt")   #collect network card info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("network card information collected")

print("collecting routing table information...")
os.system("echo 'routing table information:' >> livedata.txt")
os.system("netstat -rn | cat >> livedata.txt")   #collect routing table  info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("routing table information collected")

print("collecting arp cache  information...")
os.system("echo 'arp cache information:' >> livedata.txt")
os.system("arp -a | cat >> livedata.txt")   #collect arp cache info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("arp cache information collected")
print("network information collected")

############################################################################################################service###############

print("************************service******")

print("collecting service information...")
os.system("echo 'service information:' >> livedata.txt")
os.system("service --status-all | cat >> livedata.txt")   #collect service info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("service information collected")

############################################################################################################drivers###############

print("************************drivers******")

print("collecting drivers information...")
os.system("echo 'drivers information:' >> livedata.txt")
os.system("lsmod | cat >> livedata.txt")   #collect drivers info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("drivers information collected")

############################################################################################################logs###############

print("************************logs******")

print("collecting history cmd information...")
os.system("echo 'history cmd information:' >> livedata.txt")
os.system("cat /root/.bash_history >> livedata.txt")   #collect history cmd info
time.sleep(2)
os.system("echo '************************************************************' >> livedata.txt")
print("history cmd information collected")








