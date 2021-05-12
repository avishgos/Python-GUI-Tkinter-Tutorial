from tkinter import *

root = Tk()
root.geometry('655x444')
root.title('More tips and Tricks in Tkinter GUI')

# To change the feather bitmap image to custom image
root.wm_iconbitmap('4.png')

# To change to whole background colour of our GUI
root.configure(background='red')

# To retrive the size of our current screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")

root.mainloop()