import tkinter as tk

class mainWindow(tk.Tk):
    def __init__(self):
        super(mainWindow,self).__init__()
        width = 200  # 登录界面宽度
        height = 300  # 登录界面高度
        sw = self.winfo_screenwidth() - width - 15 # 获取x轴坐标
        sh = (self.winfo_screenheight() - height) // 2  # 获取y轴坐标
        self.title("功能按钮")
        self.geometry("{}x{}+{}+{}".format(width,height,sw,sh))
        self.resizable(0, 0)  # 固定窗口不能拉伸
        #载入功能按钮
        self.function_module()

    def function_module(self):
        self.Button_ssh_shell = tk.Button(self, text='SSH 远端',width=10).place(x=10, y=10)
        self.Button_local_shell = tk.Button(self, text='本地终端',width=10).place(x=110, y=10)
        self.Button_cloud_date = tk.Button(self, text='云盘数据',width=10).place(x=10, y=60)
        self.Button_system = tk.Button(self, text='系统资源',width=10).place(x=110, y=60)
        self.Button_job_module = tk.Button(self, text='工作组件',width=10).place(x=10, y=110)
        self.Button_about = tk.Button(self, text='关    于',width=10).place(x=110, y=110)

#main=mainWindow()
#main.mainloop()
