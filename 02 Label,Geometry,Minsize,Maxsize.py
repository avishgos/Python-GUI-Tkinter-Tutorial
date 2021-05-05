# Label is a widget with which user does not interact.
# With button, user does interacts

# importing tkinter package
from tkinter import *   

#initialization
root = Tk()     

# Widht x Height
root.geometry('644x243')

# Width , Height
root.minsize(600,300)

# Width , Height
root.maxsize(1200,998)

# Label
avi = Label(text = 'Avish is a good boy and this is his GUI')

# Packing avi so it can be displayed
avi.pack()

# Event Loop
root.mainloop()     