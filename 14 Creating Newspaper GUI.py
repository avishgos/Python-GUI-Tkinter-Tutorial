# Importing packages
from tkinter import *
from PIL import ImageTk,Image

# Function for a line break in every 100 character
def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

root = Tk()
root.geometry('1000x1000')
root.title('AAA News - Aapka Apna Akhabaar')


# Function for texts and photos
texts = []
photos = []
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")

#TODO: As images are not sized according to us, we have to resize it.
    image = image.resize((200,200), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

# Outer Frame
f0 = Frame(root,width = 800,height = 70)
Label(f0,text = 'Indian Cricket Team',font = 'lucida 33 bold').pack()
f0.pack()
Label(f0,text = 'May 8,2021',font = 'lucida 13 bold').pack()
f0.pack()


# Frames for packing

#Frame 1
f1 = Frame(root,width = 900,height = 200,pady = 25)
Label(f1,text = texts[0],padx = 22,pady = 22).pack(side = 'left')
Label(f1, image = photos[0],anchor = 'e').pack()
f1.pack(anchor = 'w')

#Frame 2
f2 = Frame(root,width = 900,height = 200)
Label(f2,text = texts[1],padx = 22,pady = 22).pack(side = 'right')
Label(f2, image = photos[1],anchor = 'e').pack()
f2.pack(anchor = 'w')

#Frame 3
f3 = Frame(root,width = 900,height = 200)
Label(f3,text = texts[2],padx = 22,pady = 22).pack(side = 'left')
Label(f3, image = photos[2],anchor = 'e').pack()
f3.pack(anchor = 'w')


root.mainloop()