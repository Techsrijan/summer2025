from tkinter import *
from PIL import Image,ImageTk
def msg():
    print("hi")
root=Tk()

doc=ImageTk.PhotoImage(Image.open('images/doctor.png'))
login=ImageTk.PhotoImage(Image.open('images/login.png'))
l=Label(root,text='Doctor',image=doc,compound=LEFT)
l.pack()
btn=Button(root,image=login,command=msg)
btn.pack()
root.geometry("400x500+120+50")
root.mainloop()