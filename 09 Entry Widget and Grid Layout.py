# Importing packages
from tkinter import *

# Initialization
root = Tk()
root.geometry('655x433')

# Creating a function to see how command in buttons work for Button
def getvals():
    print(uservalue.get())
    print(passvalue.get())


# Label1 as a Username
user = Label(root,text = 'Username')

# Label2 as a Password
password = Label(root,text = 'Password')
#grid for user
user.grid()
#grid for password
password.grid()

# NOTES - VARIABLES CLASSES IN TKINTER
# booleanVar,DoubleVar,IntVar,StringWar 

uservalue = StringVar()
passvalue = StringVar()

# Creating Entry Widget
userentry = Entry(root,textvariable = 'uservalue') 
passentry = Entry(root,textvariable = 'passvalue') 

userentry.grid(row = 0,column = 1)
passentry.grid(row = 1,column = 1)

Button(text = 'Submit',command = getvals).grid()


root.mainloop()