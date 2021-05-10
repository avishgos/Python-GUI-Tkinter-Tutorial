from tkinter import *
root = Tk()
root.geometry("733x566")
root.title('Visual Code Studio')

def myfunc():
    print('I am a cool function!')

# Use these to create a non-drop down menus
mymenu = Menu(root)
mymenu.add_command(label = 'File', command = myfunc)
mymenu.add_command(label = 'Exit', command = quit)
root.config(menu = mymenu)


# Use these to create a drop down menus
# FILE
filemenu = Menu(root)
m1 = Menu(filemenu,tearoff = 0)
m1.add_command(label = 'New Project', command = myfunc)
m1.add_command(label = 'Save', command = myfunc)
#we can also add separator
m1.add_separator()
m1.add_command(label = 'Save As', command = myfunc)
m1.add_command(label = 'Print As', command = myfunc)
filemenu.add_cascade(label = 'File',menu = m1)
root.config(menu = filemenu)

# EDIT
m2 = Menu(filemenu,tearoff = 0)
m2.add_command(label = 'Cut', command = myfunc)
m2.add_command(label = 'Copy', command = myfunc)
#we can also add separator
m2.add_separator()
m2.add_command(label = 'Paste', command = myfunc)
m2.add_command(label = 'Find', command = myfunc)
filemenu.add_cascade(label = 'Edit',menu = m2)
root.config(menu = filemenu)

root.mainloop()