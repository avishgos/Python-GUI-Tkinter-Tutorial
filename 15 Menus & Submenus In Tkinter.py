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
yourmenu = Menu(root)
m1 = Menu(yourmenu)
m1.add_command(label = 'New Project', command = myfunc)
m1.add_command(label = 'Save', command = myfunc)
m1.add_command(label = 'Save As', command = myfunc)
m1.add_command(label = 'Print As', command = myfunc)

yourmenu.add_cascade(label = 'File',menu = m1)

root.config(menu = yourmenu)


root.mainloop()