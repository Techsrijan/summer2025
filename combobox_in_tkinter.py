from tkinter import *
from tkinter import ttk
def get_data():
    a=c.get()
    b=c1.get()
    d=c2.get()

    dob=a+"-"+b+"-"+d
    print(dob)
root=Tk()
# l=['AP',"UP",'MP']
d=[]
m=[]
y=[]

for i in range(1,31):
    d.append(i)
for i in range(1,13):
    m.append(i)
for j in range(1998,2009):
    y.append(j)

c=ttk.Combobox(root,value=d)
c.set('SELECT YOUR Date')
c.pack()

c1=ttk.Combobox(root,value=m)
c1.set('SELECT YOUR Month')
c1.pack()

c2=ttk.Combobox(root,value=y)
c2.set('SELECT YOUR Year')
c2.pack()
btn=Button(root,text="get Check button Data",bd="5",command=get_data)
btn.pack()
root.geometry("400x500+120+50")
root.mainloop()