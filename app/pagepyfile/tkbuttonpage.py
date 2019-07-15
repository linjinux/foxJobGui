#!/usr/bin/env python3
import tkinter
from tkinter import *
global s
s='sssss'
def func1():
    s='fucked!'
    outputtext.set(s)
root = Tk()

buttonfrm = Frame(root)
buttonfrm.pack()

textframe = Frame(root)
textframe.pack(side=LEFT)

btnfrm=Frame(root)
btnfrm.pack(side=BOTTOM)

inputbutton= Button(buttonfrm,text="Input",command=func1)
inputbutton.pack

outputbutton= Button(buttonfrm,text="Output")
outputbutton.pack()


inputtext=StringVar() 
inputmsg=Label(textframe,textvariable=inputtext, relief=RAISED) 
inputtext.set(s) 
inputmsg.pack() 

s='changed!' 
outputtext=StringVar() 
outputmsg=Label(textframe,textvariable=outputtext, relief=RAISED) 
outputtext.set(s) 
outputmsg.pack() 

#run & exit button 
runbutton = Button(btnfrm, text="RUN!",fg='red') 
runbutton.pack() 

exitbutton = Button(btnfrm, text="EXIT!",command=root.quit) 
exitbutton.pack() 
root.mainloop()

