from tkinter import *

def Avish(event):
    print('You clicked on the buton')

root = Tk()

root.title('Events in Tkinter')
root.geometry('644x334')

# Creating widgets
widget = Button(root,text = 'Click me Please!')
widget.pack()

# Binding the widgets
widget.bind('<Button-1>',Avish)
widget.bind('<Double-1>',quit)    #quits the screen when double clicked
root.mainloop()