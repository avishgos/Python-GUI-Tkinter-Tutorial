# Importing packages
from tkinter import *
import tkinter.messagebox as tmsg

def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo('Amount Credited!',f"We have credited {myslider2.get()} dollars to your bank account")

root = Tk()
root.geometry('455x233')

root.title('Slider Tutorial')

# Vertical Slider
# myslider = Scale(root,from_=0,to = 100)
# myslider.pack()


# Label
Label(root,text = 'How many dollars do you want?').pack()

# Horizontal Slider
myslider2 = Scale(root,from_=0,to = 100,orient = HORIZONTAL,tickinterval = 50)
myslider2.set(25)
myslider2.pack()


# Button
Button(root,text = 'Get Dollars!',pady = 10,command = getdollar).pack()



root.mainloop()