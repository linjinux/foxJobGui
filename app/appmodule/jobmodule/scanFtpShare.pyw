#!/usr/bin/env python3
import tkinter as tk
from tkinter.filedialog import askopenfilenames
import os
import csv

class ScanFtpShare(tk.Tk):
    def __init__(self):
        super(ScanFtpShare,self).__init__()
        self.path=tk.StringVar()
        self.title("Scan")
        self.setup_Ui()
        
    def selectPath(self):
        pathfile =  askopenfilenames()
        self.path.set(pathfile)       

    def setup_Ui(self):        
        self.label_lj=tk.Label(self,text="导入文件").grid(row = 0, column = 0)
        self.entry_lj=tk.Entry(self, textvariable = self.path).grid(row = 0, column = 1)
        self.button_lj=tk.Button(self, text = "导入路径", command = self.selectPath).grid(row = 0, column = 2)
        self.button_dc=tk.Button(self, text = "导出文件", command = self.editFile).grid(row = 1, column = 2)
      
    def editFile(self):
        file=self.path.get()
        file=eval(file)
        dcfile=os.path.abspath(os.path.dirname(file[0]))
        with open(file[0],'rt',encoding='utf-16') as input_file:
            filereader = csv.reader(input_file,delimiter='\t')
            global b
            global c
            b=0
            c=0
            for row_list in filereader:
                if not row_list[6].strip()=='' and row_list[0] != "狀態" and b==1: 
                    with open(os.path.join(dcfile,"FTP.csv"),'a',encoding='utf-16',newline="") as f:
                        f_csv = csv.writer(f,delimiter='\t')
                        list_line=[row_list[0],row_list[1],row_list[2],'','','','',row_list[3],\
                                   '','',row_list[6],'',row_list[8],row_list[9],\
                                   '',row_list[11],row_list[12],'','','','5']
                        f_csv.writerow(list_line)
                        f.close()
                elif b==0 and row_list[0] == "狀態":
                    with open(os.path.join(dcfile,"FTP.csv"),'a',encoding='utf-16',newline="") as f:
                        f_csv = csv.writer(f,delimiter='\t')
                        list_line=['狀態','名稱','IP','who','why/purpose','passwd','簽承諾書','Radmin',\
                                   'http','https','Ftp','Rdp','共用資料夾','共用印表機',\
                                   'NetBIOS 群組','製造商','MAC 位址','使用者','日期','註解','位址']
                        f_csv.writerow(list_line)
                        f.close()
                        b=1
                        
                if not row_list[8].strip()==''and row_list[0] != "狀態" and c==1:
                    with open(os.path.join(dcfile,"SHARE.csv"),'a',encoding='utf-16',newline="") as f:
                        f_csv = csv.writer(f,delimiter='\t')
                        list_line=[row_list[0],row_list[1],row_list[2],'','','','',row_list[3],\
                                   '','',row_list[6],'',row_list[8],row_list[9],\
                                   '',row_list[11],row_list[12],'','','','5']
                        f_csv.writerow(list_line)
                        f.close()
                elif c==0 and row_list[0] == "狀態":
                    with open(os.path.join(dcfile,"SHARE.csv"),'a',encoding='utf-16',newline="") as f:
                        f_csv = csv.writer(f,delimiter='\t')
                        list_line=['狀態','名稱','IP','who','why/purpose','passwd','簽承諾書','Radmin',\
                                   'http','https','Ftp','Rdp','共用資料夾','共用印表機',\
                                   'NetBIOS 群組','製造商','MAC 位址','使用者','日期','註解','位址']
                        f_csv.writerow(list_line)
                        f.close()
                        c=1

a=ScanFtpShare()
a.mainloop()
