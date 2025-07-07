from tkinter import *
def get_data():
    print(l.curselection())
    for i in l.curselection():
        print(i)

def delete_data():
    l.delete(l.curselection())


root=Tk()

f=Frame(root)

s=Scrollbar(f)


l=Listbox(f,height=10,width=5,yscrollcommand=s.set,selectmode=EXTENDED)
# l.insert(END,'abcdefghijklmnofhjfhjfhjfjhfjmoham')
for i in range(15):
    l.insert(END,i)
l.pack(side=LEFT)
s.config(command=l.yview)
s.pack(side=RIGHT,fill=Y)
f.pack()
btn=Button(root,text="get Radio button Data",bd="5",command=get_data)
btn.pack()

btn2=Button(root,text="delete",bd="5",command=delete_data)
btn2.pack()
root.geometry("400x500+120+50")
root.mainloop()