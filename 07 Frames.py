# Importing package
from tkinter import *

#object initialization
root = Tk()

#geometry
root.geometry('655x333')

# Frame1
f1 = Frame(root,bg = 'grey',borderwidth = 6,relief = SUNKEN)
f1.pack(side = LEFT,fill = Y)

# Frame2
f2 = Frame(root,bg = 'grey',borderwidth = 9,relief = SUNKEN)
f2.pack(side = TOP,fill = X)

# Label1
l = Label(f1,text = 'Project Tkinter - PYCHARM',font = 'Helvetica 16 bold',fg = 'red')
l.pack(pady = 4)

# Lable2
l = Label(f2,text = 'Welcome to Jupyter Lab',font = 'Helvetica 16 bold',fg = 'red')
l.pack()

root.mainloop()