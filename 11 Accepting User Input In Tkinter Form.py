# Importing packages
from tkinter import *

root = Tk()
root.geometry('644x344')

# Heading
Label(root,text = 'Welcome to Avish Travels',font = 'comicsansms 13 bold',pady = 15, bg = 'blue',fg = 'white',borderwidth = 3,relief = SUNKEN).grid(row = 0,column = 3)

# Text for our form
name = Label(root,text = 'Name')
phone = Label(root,text = 'Phone')
gender = Label(root,text = 'Gender')
emergency = Label(root,text = 'Emergency Contact')
payment = Label(root,text = 'Payment Mode')

# Pack Text for our form
name.grid(row = 1 ,column = 2)
phone.grid(row = 2 ,column = 2)
gender.grid(row = 3,column = 2)
emergency.grid(row = 4 ,column = 2)
payment.grid(row = 5 ,column = 2)

# Tkinter variables for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()

#checkbox
foodservicevalue = IntVar()

# Entry for our form
nameentry = Entry(root,textvariable = namevalue )
phoneentry = Entry(root,textvariable = phonevalue )
genderentry = Entry(root,textvariable = gendervalue )
emergencyentry = Entry(root,textvariable = emergencyvalue )
paymententry = Entry(root,textvariable = paymentvalue )

# Packing the entries
nameentry.grid(row = 1, column = 3 )
phoneentry.grid(row = 2, column = 3 )
genderentry.grid(row = 3, column = 3 )
emergencyentry.grid(row = 4, column = 3 )
paymententry.grid(row = 5, column = 3 )

# Checkbox & Packing it
foodservice = Checkbutton(text = 'Want to prebook your meals?',variable = foodservicevalue)
foodservice.grid(row = 6,column = 3)

# Accepting User Input
def getvals():
    print('Submitting Forms')

    print(f'{namevalue.get(), phonevalue.get() ,gendervalue.get() ,emergencyvalue.get() ,paymentvalue.get(),foodservicevalue.get()}')


with open('records.txt',"a") as f:
    f.write("namevalue.get(), phonevalue.get() ,gendervalue.get() ,emergencyvalue.get() ,paymentvalue.get(),foodservicevalue.get()\n")


# Button and Packing it to a command
Button(text = 'Submit to Avish Travels',command = getvals).grid(row = 7,column = 3)



root.mainloop()