# Importing package
from tkinter import *

# Initialization
root = Tk()
root.geometry('655x333')

# Creating a function to see how command in buttons work for Button b1
def hello():
    print('Hello My friend')

# Creating a function to see how command in buttons work for Button b2
def name():
    print('My name is Avish')

# Creating a function to see how command in buttons work for Button b3
def bachelors():
    print('I have completed my Btech in CSE and Post Graduate in Data Science')

# Creating a function to see how command in buttons work for Button b4
def Aspire():
    print('My aim is to be a Data Scientist at Apple')

# Creating Frame
frame = Frame(root,borderwidth = 6,bg = 'grey',relief = SUNKEN)
frame.pack(side = LEFT, anchor = 'nw')

# Button b1
b1 = Button(frame,fg = 'red',text = 'Greetings!',command = hello)
b1.pack(side = LEFT,padx = 23)

# Button b2
b2 = Button(frame,fg = 'red',text = 'Tell me your name',command = name)
b2.pack(side = LEFT,padx = 23)

# Button b3
b3 = Button(frame,fg = 'red',text = 'Background',command = bachelors)
b3.pack(side = LEFT,padx = 23)

# Button b4
b4 = Button(frame,fg = 'red',text = 'Aim',command = Aspire)
b4.pack(side = LEFT,padx = 23)


root.mainloop()