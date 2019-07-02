import tkinter as tk

class mainWindow(tk.Tk):
    def __init__(self):
        super(mainWindow,self).__init__()
        width = 200  # 登录界面宽度
        height = 300  # 登录界面高度
        sw = self.winfo_screenwidth() - width - 15 # 获取x轴坐标
        sh = (self.winfo_screenheight() - height) // 2  # 获取y轴坐标
        print(self.winfo_screenheight())
        print(self.winfo_screenwidth())
        self.title("功能按钮")
        self.geometry("{}x{}+{}+{}".format(width,height,sw, sh))
        self.resizable(0, 0)  # 固定窗口不能拉伸

    def function_module(self):




main=mainWindow()
main.mainloop()
