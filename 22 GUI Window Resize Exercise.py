# Create a GUI window which takes input as width and height
# And upon clicking apply,it should be able to chage its size accordingly

from tkinter import *
root = Tk()

def resize():
    print("You Gui is resized")
    root.geometry(f"{height.get()}x{width.get()}")

root.geometry("344x233")


Label(root, text="Window resizer", font="comicsansms 13 bold").grid(column=4)
Label(root, text="Height").grid(row=1, column=1)
Label(root, text="Width").grid(row=2, column=1)

height = StringVar()
width = StringVar()

Entry(root, textvariable=height).grid(row=1, column=2)
Entry(root, textvariable=width).grid(row=2, column=2)

Button(root, text="resize", command=resize).grid(row=3, column=2)
root.mainloop()