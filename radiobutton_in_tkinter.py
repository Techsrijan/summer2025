from tkinter import *
def get_data():
    print(i.get())
    if i.get()==1:
        print("male")
    elif i.get()==2:
        print("female")

    print(j.get())

root=Tk()
lf=LabelFrame(root,text="select Gender")
i=IntVar()
r1=Radiobutton(lf,text='Male',variable=i,value=1)
r1.pack()
r2=Radiobutton(lf,text='FeMale',variable=i,value=2)
r2.pack()
lf.pack()

hf=LabelFrame(root,text="Select your Religion")
j=IntVar()
h1=Radiobutton(hf,text='Hindu',variable=j,value=1)
h1.pack()
h2=Radiobutton(hf,text='Muslim',variable=j,value=2)
h2.pack()
h3=Radiobutton(hf,text='sikh',variable=j,value=3)
h3.pack()
h4=Radiobutton(hf,text='Isai',variable=j,value=4)
h4.pack()
hf.pack()
btn=Button(root,text="get Radio button Data",bd="5",command=get_data)
btn.pack()
root.geometry("400x500+120+50")
root.mainloop()