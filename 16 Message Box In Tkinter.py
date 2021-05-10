# Importing packages
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("733x566")
root.title('Visual Code Studio')

def myfunc():
    print('I am a cool function!')

def myhelp():
    print('I will help you')
    tmsg.showinfo('Help','Avish will help you with this GUI')

def rate():
    print('Please rate us with your experience')
    value = tmsg.askquestion('Was your Experience good?','Was your Experience good?')

    if value == 'yes':
        msg = 'Great! Rate us on App Store Please'
    else:
        msg = 'Tell us what went wrong. We will call you soon!'
    tmsg.showinfo('Experience',msg)

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

# HELP
m3 = Menu(filemenu,tearoff = 0)
m3.add_command(label = 'Help', command = myhelp)
m3.add_command(label = 'Rate Us', command = rate)
filemenu.add_cascade(label = 'Help',menu = m3)
root.config(menu = filemenu)

root.mainloop()