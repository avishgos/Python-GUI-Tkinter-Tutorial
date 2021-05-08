from tkinter import *

root = Tk()

# Canvas width and height
canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_height}x{canvas_width}")

# Title
root.title("Avish's GUI")

# Declaring Canvas
can_widget = Canvas(root,width = canvas_width, height = canvas_height)
can_widget.pack()

# The line goes from x1,y1 to x2,y2
can_widget.create_line(0,0,800,400,fill = 'red')
can_widget.create_line(0,400,800,0,fill = 'red')

# To create a rectangle specify parameters in this order - coordinates of top left and coordinate of bottom right
can_widget.create_rectangle(3,5,700,300,fill = 'blue')

# Create text function in GUI
can_widget.create_text(200,200,text = 'PYTHON')

# Create a oval
can_widget.create_oval(344,233,244,455)


root.mainloop()