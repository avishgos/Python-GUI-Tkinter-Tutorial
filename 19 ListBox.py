from tkinter import *

def add():

    # gloabl i means we change i inside the function
    global i
    lbx.insert(ACTIVE,f"{i}")
    i += 1
i = 0
root = Tk()
root.geometry('455x233')

root.title('Listbox Tutorial')

# Listbox
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, 'First item of our listbox')

# Button
Button(root,text = 'Add item',command = add).pack()



root.mainloop()