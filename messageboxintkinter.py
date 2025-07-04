from tkinter import *
from tkinter import messagebox
def open_msgbox():
    #f=messagebox.askyesno("Asking Data","Do you want to save this file")
    f = messagebox.showerror("Asking Data", "Do you want to save this file")
    print(f)
    if f==True:
        print("file is saved")

root=Tk()
root.title("My first window")
root.geometry("400x400+500+200")
root.resizable(0,0)
btn=Button(root,text="GET TEXT DATA", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=open_msgbox)

btn.place(x=150,y=150)
root.wm_iconbitmap('cal.ico')
root.mainloop()
