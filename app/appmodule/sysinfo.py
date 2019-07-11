#!/usr/bin/env python3
import tkinter as tk
import psutil
class SysInfo(tk.Tk):
    def __init__(self):
        super(SysInfo,self).__init__()
        self.geometry("300x300")
        self.refresh_data()
        self.mainloop()
    
    def refresh_data(self):
        self.ff=tk.Label(self,text=psutil.cpu_percent(interval=1)).place(x=10,y=150)        
        self.after(10000, self.refresh_data)
 


'''
import os,psutil,datetime,time
syStem=os.name
if syStem=="posix":
    print("系统类型:类Unix")
elif syStem=="nt":
    print("系统类型:Windowns")
else:
    print("系统类型:未知")

print("CPU使用信息:")
cpuCount=psutil.cpu_count()
print("CPU的核心数:%d"%(cpuCount/2))
cpuPercent=psutil.cpu_percent(interval=1)
print("CPU使用率:{}".format(psutil.cpu_percent(interval=1)))

print("内存使用信息:")
info=psutil.virtual_memory()
swap=psutil.swap_memory()
print("内存总容量:%dMB\t空闲容量:%dMB"%(info.total/1024/1024,info.free/1024/1024))
if swap.total!=0:
    print("虚拟内存总容量:%dMB\t 虚拟内存空闲容量:%dMB"%(swap.total/1024/1024,swap.free/1024/1024))

print("磁盘使用信息:")
print(psutil.disk_partitions())
diskinfo=psutil.disk_partitions()
for partition in diskinfo:
    if syStem=="posix":
        diskpart=psutil.disk_usage(partition.mountpoint)
        print(diskinfo)
        print("分区名称:%s\t挂载点:%s\t容量/空闲(GB):%d/%d\t分区类型:%s\t"\
        %(partition.device,partition.mountpoint,diskpart.total/1024/1024/1024,\
	diskpart.free/1024/1024/1024,partition.fstype))
    elif syStem=="nt":
        print("还未获取信息")
    else:
        print("分区未知")

print("当前用户信息:")
users=psutil.users()
print(users)
for user in users:
    print("用户名:{}\t\t登陆点:{}\t用户ID:{}\t".format(user.name,user.terminal,user.pid))
boot=psutil.boot_time()
dt=datetime.datetime.fromtimestamp(boot)
print("系统开机的时间:{}".format(dt.strftime("%Y-%m-%d,%H:%M:%S")))
'''