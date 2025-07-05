from tkinter import *
root=Tk()
def msg(event=''):
    print("hi")

root.bind("<Control-n>",msg)
main_menu=Menu(root)
root.config(menu=main_menu)
# creating file menu
filemenu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=filemenu)

# cerating sub menu inside filemenu
filemenu.add_command(label="New",accelerator='Ctrl+n',command=msg)
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit)



# creating submenu
link_menu=Menu(filemenu,tearoff=0)
link_menu.add_command(label="Lf")
link_menu.add_command(label="CR")
filemenu.add_cascade(label='Link Seprator',menu=link_menu)
# save_menu=Menu(filemenu,tearoff=0)
# save_menu.add_command(label="save as",accelerator="Ctrl+O")
# save_menu.add_command(label="Hello",accelerator="Ctrl+O")
#
# filemenu.add_cascade(label="SAVE",menu=save_menu)

# creating Editfile menu
editmenu=Menu(main_menu)
main_menu.add_cascade(label="Edit",menu=editmenu)

root.geometry("500x600+200+200")

root.resizable(0,0)
root.mainloop()