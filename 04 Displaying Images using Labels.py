from tkinter import *
from PIL import Image,ImageTk

root = Tk()

root.geometry('955x944')

# For PNG images
photo = PhotoImage(file = 'power_girl.png')

# For JPG images
image = Image.open('wine.jpg')
photo = ImageTk.PhotoImage(image)

label = Label(image = photo)
label.pack()

root.mainloop()

# Notes
# 1. Tkinter supports png type images
# 2.Tkinter does not supports JPG types images so we can use a library called PIL