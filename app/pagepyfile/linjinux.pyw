#!/usr/bin/env python3
from tkinter import *
#from tkinter.filedialog import *
from tkinter.messagebox import *
import os

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master



def author():
    showinfo(title="作者",message="linjinux")

def power():
    showinfo(title="版权信息",message="2018-03-15,foxconn")


top=Tk()
top.wm_title("菜单")
top.geometry("400x300+300+100")

#菜单部分
# 创建一个菜单项，类似于导航栏
menubar=Menu(top)
# 创建菜单项
fmenu=Menu(top)
for item in ["作者","其他说明"]:
    if item=="作者":
        fmenu.add_command(label=item,command=author)
    else:
        fmenu.add_command(label=item,command=power)
# add_cascade 的一个很重要的属性就是 menu 属性，它指明了要把那个菜单级联到该菜单项上，
# 当然，还必不可少的就是 label 属性，用于指定该菜单项的名称
menubar.add_cascade(label="关于",menu=fmenu)
# 最后可以用窗口的 menu 属性指定我们使用哪一个作为它的顶层菜单
top['menu']=menubar

#内容部分

top.mainloop()
