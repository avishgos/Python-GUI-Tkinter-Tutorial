# Importing Packages
from tkinter import *

# Creating function for command in Button
def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")

root = Tk()
root.geometry("455x233")
root.title("Status bar tutorial")

# Statusvariable
statusvar = StringVar()
statusvar.set("Ready")

# Statusbar
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

# Button
Button(root, text="Upload", command=upload).pack()
root.mainloop()