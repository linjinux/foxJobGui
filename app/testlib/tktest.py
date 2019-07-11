import tkinter as tk
class Questions(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__()
        self.wm_title('CSSE1001 Queue')
        self.configure(background='white')
        self.resizable(width=False, height=True)    # 设置窗口宽度不可变，高度可变
        self.geometry("300x300")

        self.run()
        self.refresh_data()
        self.mainloop()
    
    def refresh_data(self):
        # 需要刷新数据的操作
        # 代码...
        self.ff=tk.Label(self,text=a).pack()
        
        self.after(1000, self.refresh_data)   # 这里的10000单位为毫秒
 
    def run(self):
        pass
 
if __name__ == '__main__':
    question = Questions()
