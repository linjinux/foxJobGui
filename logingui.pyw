import tkinter as tk
from tkinter import messagebox as message

class loginWindow(tk.Tk):
    #打开一个窗口
    def __init__(self):
        super(loginWindow,self).__init__() #继承类
        width = 360   #登录界面宽度
        height = 250   #登录界面高度
        sw = (self.winfo_screenwidth()-width)//2  #获取x轴坐标
        sh = (self.winfo_screenheight()-height)//2  #获取y轴坐标
        self.title("登录界面")
        self.geometry("+{}+{}".format(sw,sh))
        self.resizable(0,0) #固定窗口不能拉伸
        #self.frame.iconbitmap("./img/stu.ico")   #ICO图片位置

        #加载窗体
        self.setup_Ui()
        #自动账号加载
        #self.load_file_info()

    def setup_Ui(self):
        #展示图片
        self.login_image = tk.PhotoImage(file="./img/login.png")
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
        self.loginphoto = tk.PhotoImage(file="img/loginsub.gif")
        self.Button_login = tk.Button(self,text='login',image=self.loginphoto,\
                                      command=self.loginbt,compound="center").place(x=250, y=150)

#tk.messagebox.showinfo("系统消息","用户文件读取出现异常！")

    def loginbt(self):
        name=self.Entry_user.get()
        passwd=self.Entry_passwd.get()
        if name=="linjinux" and passwd=="123":
            print(name,passwd)
            print((passwd))
            print('button')
        else:
            message.showerror("ERROR","Username or password error\nPlease enter again")


if __name__ == "__main__":
    this_login = loginWindow()
    this_login.mainloop()




