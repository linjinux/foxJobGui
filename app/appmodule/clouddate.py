
#！/usr/bin/env python
import tkinter as tk
from tkinter import filedialog
 
root = tk.Tk()
root.withdraw()
 
file_path = filedialog.askopenfilename()
 
print(file_path)