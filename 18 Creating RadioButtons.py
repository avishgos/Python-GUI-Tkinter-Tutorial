# Importing Packages
from tkinter import *
import tkinter.messagebox as tmsg

def ordernow():
    print('')
    tmsg.showinfo('Order Recieved!',f"We have recieved your order {var.get()}. Thanks for Ordering")
root = Tk()
root.geometry('455x233')
root.title('Restaurant Ordering Management')

var = IntVar()
#var = StringVar()
#var.set(1)
Label(root,text = 'What would you like to have sir!',justify = LEFT,padx = 14,font = 'lucida 19 bold').pack()

# Radiobutton
ItemList = [ 'Pizza', 'Burger', 'Garlic Bread','French Fries','Choco Lava Cake','Momos']
for i, item in enumerate(ItemList):
    Radiobutton(root, text= item,padx=14,variable=var, value= i+1).pack(anchor='w')
    
#for i in range(len(ItemList)):
   

# radio = Radiobutton(root,text = 'Pizza',padx = 14,variable = var,value = 1).pack(anchor = 'w')
# radio = Radiobutton(root,text = 'Burger',padx = 14,variable = var,value = 2).pack(anchor = 'w')
# radio = Radiobutton(root,text = 'Garlic Bread',padx = 14,variable = var,value = 3).pack(anchor = 'w')
# radio = Radiobutton(root,text = 'French Fries',padx = 14,variable = var,value = 4).pack(anchor = 'w')
# radio = Radiobutton(root,text = 'Choco Lava Cake',padx = 14,variable = var,value = 5).pack(anchor = 'w')
# radio = Radiobutton(root,text = 'Momos',padx = 14,variable = var,value = 6).pack(anchor = 'w')

# Button
Button(root,text = 'Order Now',command = ordernow).pack()





root.mainloop()