#！/usr/bin/env python
import tkinter as tk
from platform import uname
from app.appmodule.remote import RemoteWindow_W
from app.appmodule.remote import RemoteWindow_L
from app.appmodule.about import AboutWindow
from app.appmodule.localterminal import LocalTerminal
from tkinter import messagebox as message
class MainWindow(tk.Tk):
    """main windows function"""
    def __init__(self):
        super(MainWindow,self).__init__()
        width = 200  # 登录界面宽度
        height = 300  # 登录界面高度
        sw = self.winfo_screenwidth() - width - 15 # 获取x轴坐标
        sh = (self.winfo_screenheight() - height) // 2  # 获取y轴坐标
        self.title("功能按钮")
        self.geometry("{}x{}+{}+{}".format(width,height,sw,sh))
        self.resizable(0, 0)  # 固定窗口不能拉伸
        #载入功能按钮
        self.setup_Ui()

    def setup_Ui(self):
        self.Button_remote_shell = tk.Button(self, text='远     端',command=self.remote,width=8).place(x=10, y=10)
        self.Button_local_shell = tk.Button(self, text='本地终端',width=8,command=self.localterminal).place(x=110, y=10)
        self.Button_cloud_date = tk.Button(self, text='云盘数据',width=8).place(x=10, y=60)
        self.Button_system = tk.Button(self, text='系统资源',command=self.sysinfo,width=8).place(x=110, y=60)
        self.Button_job_module = tk.Button(self, text='工作组件',width=8).place(x=10, y=110)
        self.Button_about = tk.Button(self, text='关    于',command=self.about,width=8).place(x=110, y=110)

    def remote(self):
        if uname()[0] == "Linux":
            print("hello")
            self.destroy()
            remote=RemoteWindow_L()
            remote.mainloop()
            self.main=MainWindow()
            self.main.mainloop()
        elif uname()[0] == "Windows":
            self.destroy()
            remote=RemoteWindow_W()
            remote.mainloop()
            self.main=MainWindow()
            self.main.mainloop()
        else:
            message.showerror("ERROR", "This program does not support the system yet. Please contact the developer.")

    def localterminal(self):
        terminal=LocalTerminal()

        

    def about(self):
        self.destroy()
        about=AboutWindow()
        about.mainloop()
        self.main=MainWindow()
        self.main.mainloop()

    def sysinfo(self):
        print("hello")
		