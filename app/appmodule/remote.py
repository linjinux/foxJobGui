#！/usr/bin/env python
import tkinter as tk
from os import system
from app.sharecode import root_app_directory

class RemoteWindow_W(tk.Tk):
    """remote module function"""
    def __init__(self):
        super(RemoteWindow_W, self).__init__()  # 继承类
        width = 500  # 登录界面宽度
        height = 300  # 登录界面高度
        sw = (self.winfo_screenwidth() - width) //2 # 获取x轴坐标
        sh = (self.winfo_screenheight() - height) // 2  # 获取y轴坐标
        self.title("链接信息")
        self.geometry("{}x{}+{}+{}".format(width, height, sw, sh))
        self.resizable(0, 0)  # 固定窗口不能拉伸
        self.setup_Ui()  # 加载窗体

    def setup_Ui(self):
        self.connect_name=tk.StringVar()
        self.Label_connect_name = tk.Label(self,text='名称',width=6).place(x=10, y=10)
        self.Entry_connect_name = tk.Entry(self,textvariable=self.connect_name, width=15).place(x=60, y=10)

        self.connect_addr=tk.StringVar()
        self.connect_port=tk.StringVar()
        self.Label_connect_addr = tk.Label(self, text='地址',width=6).place(x=10, y=60)
        self.Entry_connect_addr= tk.Entry(self, textvariable=self.connect_addr, width=15).place(x=60, y=60)
        self.Entry_connect_port = tk.Entry(self, textvariable=self.connect_port, width=6).place(x=190, y=60)

        self.user_name=tk.StringVar()
        self.Label_user_name = tk.Label(self, text='用户名',width=6).place(x=10, y=110)
        self.Entry_user_name = tk.Entry(self, textvariable=self.user_name, width=15).place(x=60, y=110)

        self.user_passwd=tk.StringVar()
        self.Label_user_passwd = tk.Label(self, text='密码',width=6).place(x=10, y=160)
        self.Entry_user_passwd = tk.Entry(self, textvariable=self.user_passwd,  show="*",width=15).place(x=60, y=160)

        self.connect_protocol=tk.StringVar()
        self.Label_connect_protocol = tk.Label(self, text='协议', width=6).place(x=10, y=210)
        self.Entry_connect_protocol = tk.Entry(self, textvariable=self.connect_protocol, width=15).place(x=60, y=210)

        self.Button_save = tk.Button(self, text='保存', width=10).place(x=10, y=260)
        self.Button_connect = tk.Button(self, text='启动链接', width=10,command=self.connect_Remote_Var).place(x=160, y=260)

    def connect_Remote_Var(self):
        app_root=root_app_directory()
        passwd=self.user_passwd.get()
        name=self.user_name.get()
        addr=self.connect_addr.get()
        port=self.connect_port.get()
        connect_name=self.connect_name.get()
        protocol=self.connect_protocol.get()
        self.start_Connect(app_root,passwd,name,addr,port,connect_name,protocol)

    def start_Connect(self,app_root,passwd,name,addr,port,connect_name,protocol):
        system("start {}/app/share/sysfile/putty.exe -{} {}@{} -pw {} -P {}".format(app_root,protocol,name,addr,passwd,port))

class RemoteWindow_L(RemoteWindow_W):
    def start_Connect(self,app_root,passwd,name,addr,port,connect_name,protocol):
        system("{} {}@{} -p {}".format(protocol,name,addr,port))
        