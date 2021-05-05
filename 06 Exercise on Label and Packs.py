from tkinter import *

root = Tk()

root.geometry('500x400')
root.title('My GUI with Avish')

title_label = Label(text = 'READY',bg = 'black',fg = 'white',padx = 113,pady = 93,font = ('comicsansms',19,'bold'),borderwidth = 3,relief = SUNKEN)
title_label.pack(side = BOTTOM,fill = X,padx = 15, pady = 25)


root.mainloop()