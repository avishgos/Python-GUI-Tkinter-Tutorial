# Importing Packages
from tkinter import*


root = Tk()
root.geometry("433x544")
root.title("scroll bar")

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Label(widget)
l =Label(root,text="your large text",yscrollcommand = scrollbar.set)
l.pack()
scrollbar.config(command=l.yview)


root.mainloop()