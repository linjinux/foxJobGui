import tkinter as tk

class remoteWindow(tk.Tk):
    # 初始化窗口
    def __init__(self):
        super(remoteWindow, self).__init__()  # 继承类
        width = 500  # 登录界面宽度
        height = 300  # 登录界面高度
        sw = (self.winfo_screenwidth() - width) //2 # 获取x轴坐标
        sh = (self.winfo_screenheight() - height) // 2  # 获取y轴坐标
        self.title("链接信息")
        self.geometry("{}x{}+{}+{}".format(width, height, sw, sh))
        self.resizable(0, 0)  # 固定窗口不能拉伸
        self.setup_Ui()  # 加载窗体

    def setup_Ui(self):
        self.Label_connect_name = tk.Label(self,text='名称',width=6).place(x=10, y=10)
        self.Entry_connect_name = tk.Entry(self,text='', width=15).place(x=60, y=10)

        self.Label_connect = tk.Label(self, text='地址',width=6).place(x=10, y=60)
        self.Entry_connect = tk.Entry(self, text='', width=15).place(x=60, y=60)
        self.Entry_connect_port = tk.Entry(self, text='', width=6).place(x=190, y=60)

        self.Label_user_name = tk.Label(self, text='用户名',width=6).place(x=10, y=110)
        self.Entry_user_name = tk.Entry(self, text='', width=15).place(x=60, y=110)

        self.Label_user_passwd = tk.Label(self, text='密码',width=6).place(x=10, y=160)
        self.Entry_user_passwd = tk.Entry(self, text='',  show="*",width=15).place(x=60, y=160)

        self.Label_connect_protocol = tk.Label(self, text='协议', width=6).place(x=10, y=210)
        self.Entry_connect_protocol = tk.Entry(self, text='', width=15).place(x=60, y=210)

        self.Button_save = tk.Button(self, text='保存', width=10).place(x=10, y=260)
        self.Button_connect = tk.Button(self, text='启动链接', width=10).place(x=160, y=260)

remote=remoteWindow()
remote.mainloop()


