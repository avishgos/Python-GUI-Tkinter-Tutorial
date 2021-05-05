from tkinter import *

root = Tk()
root.geometry('444x233')

# Changing title from tk to 'My gui with Avish'
root.title('My GUI with Avish')

# Important Label Attributes
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font - ('comicsansms',19,'bold')  OR 'comicsansms 19 bold'
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN - RAISED - GROOVE - RIDGE

# Use of bd,fg,padx,pady,font,borderwidth,relief
title_label = Label(text = "SimpleText allows text editing and text -underline, italic, bold, etc.", bg = 'red',fg = 'white',padx = 113,pady = 93,font = ('comicsansms',19,'bold'),borderwidth = 3,relief = SUNKEN)


# Important Pack Attributes(1.ANCHOR 2.SIDE 3.FILL 4.PADX 5.PADY)

#To use sw and se we have to include SIDE
# Side = top , bottom ,left , right

title_label.pack(anchor = 'ne')     #nw,ne
title_label.pack(side = BOTTOM,anchor = 'sw',fill = X)   #se,sw
title_label.pack(side = LEFT,fill = Y,padx = 34,pady = 34)   


root.mainloop()