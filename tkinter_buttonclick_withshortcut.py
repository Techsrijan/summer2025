from tkinter import *
from tkinter import messagebox
root=Tk()
def open_messagebox(event=''):
    f=messagebox.showwarning("show warning","Dont do this")

btn1=Button(root,text="open message box",fg="red",bg="yellow",
            command=open_messagebox)
btn1.pack()


root.bind("<Control-o>",open_messagebox)




root.geometry("500x600+200+200")

root.resizable(0,0)
root.mainloop()