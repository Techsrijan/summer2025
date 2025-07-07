from tkinter import *
def get_data():
   print(i.get())
   if i.get()==1:
       print("hindi")
   print(j.get())
   print(k.get())

root=Tk()


lf=LabelFrame(root,text="select your language")

i=IntVar()
j=IntVar()
k=IntVar()

ch=Checkbutton(lf,text="hindi",variable=i)
ch.pack()
ch1=Checkbutton(lf,text="english",variable=j)
ch1.pack()
ch2=Checkbutton(lf,text="punjabi",variable=k)
ch2.pack()
lf.pack()
btn=Button(root,text="get Check button Data",bd="5",command=get_data)
btn.pack()
root.geometry("400x500+120+50")
root.mainloop()