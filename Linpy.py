#！/usr/bin/env python
import tkinter as tk
from app.mainWindows import MainWindow
from tkinter import messagebox as message

class LoginWindow(tk.Tk):
    """初始化窗口"""
    def __init__(self):
        super(LoginWindow,self).__init__() #继承类
        width = 360   #登录界面宽度
        height = 250   #登录界面高度
        sw = (self.winfo_screenwidth()-width)//2  #获取x轴坐标
        sh = (self.winfo_screenheight()-height)//2  #获取y轴坐标
        self.title("登录界面")
        self.geometry("+{}+{}".format(sw,sh))
        self.resizable(0,0) #固定窗口不能拉伸
        self.setup_Ui()  #加载窗体

    #窗体模块
    def setup_Ui(self):
        #展示图片
        self.login_image = tk.PhotoImage(file="./app/img/login.png")
        self.Label_image = tk.Label(self,image = self.login_image)
        self.Label_image.pack()

        # 创建一个Label+enter
        self.Entry_user=tk.StringVar()
        self.Label_user = tk.Label(self,text='用户名:', bg='#FFFFFF').place(x=10,y=120)
        self.user = tk.Entry(self,textvariable=self.Entry_user,\
                                   highlightbackground='#98FB98',highlightthickness=1).place(x=10,y=150)

        # 创建一个Label+passwd
        self.Entry_passwd = tk.StringVar()
        self.Label_passwd = tk.Label(self,text='密码:', bg='#FFFFFF').place(x=10,y=180)
        self.passwd = tk.Entry(self,textvariable=self.Entry_passwd,show='*',\
                                     highlightbackground='#98FB98',highlightthickness=1).place(x=10,y=210)

        # 创建登录按钮
        self.loginphoto = tk.PhotoImage(file="./app/img/loginsub.gif")
        self.Button_login = tk.Button(self,text='login',image=self.loginphoto,\
                                      command=self.loginbt,compound="center").place(x=250, y=150)
    #登录验证
    def loginbt(self):
        name=self.Entry_user.get()
        passwd=self.Entry_passwd.get()
        if 0==0:
            self.destroy()
            main=MainWindow()
            main.mainloop()
        else:
            message.showerror("ERROR","Username or password error. Please enter again")

if __name__ == "__main__":
    this_login = LoginWindow()
    this_login.mainloop()




