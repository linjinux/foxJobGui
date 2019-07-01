#!/usr/bin/env python
from tkinter import Tk
from tkinter import Label
import tkinter as tk
from app.share.connect_sql import Sqlconn


loginWindow = tk.Tk()
nScreenWidth, nScreenHeight = loginWindow.maxsize()
loginWindowidth = 360 #登录界面宽度
loginWindowHeight = 250 #登录界面度
#loginWindow.geometry("{}x{}+{}+{}".format(loginWindowidth, loginWindowHeight, (nScreenWidth-loginWindowidth)//2, (nScreenHeight-loginWindowHeight )//2))
#loginWindow.attributes("-alpha", 0.6) #窗口透明度60
loginWindow.geometry("+{}+{}".format((nScreenWidth-loginWindowidth)//2, (nScreenHeight-loginWindowHeight)//2))
loginWindow.resizable(0, 0) #阻止窗口大小调整
loginWindow.title('Login')
img=tk.PhotoImage(file="img/login.png")
tk.Label(loginWindow, image=img, compound=tk.CENTER).pack()

#用户名与密码
tk.Label(loginWindow,text='NAME:', bg='#FFFFFF').place(x=10,y=120)
tk.Label(loginWindow,text='PWD:', bg='#FFFFFF').place(x=10,y=180)
#用户名输入框
var_usr_name=tk.StringVar()
entry_usr_name=tk.Entry(loginWindow,textvariable=var_usr_name,highlightbackground='#98FB98',highlightthickness=1)
entry_usr_name.place(x=10,y=150)
#密码输入框
var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(loginWindow,textvariable=var_usr_pwd,show='*',highlightbackground='#98FB98',highlightthickness=1)
entry_usr_pwd.place(x=10,y=210)


def loginbt():
    name=var_usr_name.get()
    usrpwd=var_usr_pwd.get()
    dbdir="D:/C3409188-HOME/PyTk/app/share/userDate/date.db"
    sql="select name,password from user_tb where name='{}' and password='{}'".format(name,usrpwd)
    conn=Sqlconn()
    date=conn.selectdb(sql,dbdir)
    if any(date):
        print(111)
        loginWindow.destroy()
        mainWindow = tk.Tk()
        mainWindow.mainloop()
    else:
        print(222)
        tk.Message(loginWindow, text='用户名或密码错误',bg='#FFFFFF', width=150).place(x=220,y=210)
    date.close()


#登录按钮
loginphoto=tk.PhotoImage(file="img/loginsub.gif")
buttonLogin=tk.Button(loginWindow,text='login',image=loginphoto,command=loginbt,compound="center").place(x=250,y=150)
#test=tk.Label(loginWindow, text='hello world', bg='red').pack()

loginWindow.mainloop()
























'''
class loginWindow(Tk):
    def __init__(self,loginWindowidth,loginWindowHeight,title):
        super(loginWindow,self).__init__()   #继承Tk类的__init__方法
        nScreenWidth,nScreenHeight = self.maxsize()
        self.loginWindowidth=loginWindowidth
        self.loginWindowHeight=loginWindowHeight
        self.geometry("+{}+{}".format((nScreenWidth-loginWindowidth)//2, (nScreenHeight-loginWindowHeight)//2))
        self.title(title)


root=loginWindow(360,250,title="Login")
root.mainloop()

conn = sqlite3.connect("userDate/date.db")
cur = conn.cursor()
cur.execute("create table user_tb (id int primary key,name varchar(20),password varchar(20))")
conn.commit()
conn.close()

cu.execute("create table user_tb (id int identity(1,1) primary key,name varchar(20),password varchar(20))")
cu.execute('insert into user_tb (name,password) values ("linjinux","linjinux123.")')


'''