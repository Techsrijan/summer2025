from tkinter import *

def msg():
    print("hello")

root=Tk()
root.title("My first window")
btn=Button(root,text="click me", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=msg)
# btn.pack(side=TOP,fill=X)
btn.place(x=100,y=50)

root.geometry("400x400+500+200")
root.resizable(0,0)
root.wm_iconbitmap('cal.ico')
root.mainloop()
