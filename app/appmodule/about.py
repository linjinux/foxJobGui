#！/usr/bin/env python
import tkinter as tk

class AboutWindow(tk.Tk):
	"""docstring for ClassName"""
	def __init__(self):
		super(AboutWindow, self).__init__()
		self.geometry("200x150+300+300")
		self.name="name:{}".format("Linpy")
		self.version="version:{}".format("1.0")
		self.author="author:{}".format("linjinux")
		self.Label_name=tk.Label(self,text=self.name,font=("Arial", 18)).place(x=1,y=10)
		self.Label_version=tk.Label(self,text=self.version,font=("Arial", 18)).place(x=1,y=50)
		self.Label_author=tk.Label(self,text=self.author,font=("Arial", 18)).place(x=1,y=90)

