from tkinter import *


for i in range(1, 100):
    var = str(i)
    var = Tk()
    var.title("Doggo")
    canvas = Canvas(var, width=310, height=280)
    canvas.pack()

    img = PhotoImage(file="doggo.gif")
    canvas.create_image(30,30, anchor=NW, image=img)

    message = Label(var, text = "Doggo has infected your computer", font = "Helvetica 16 bold italic")
    message.pack()

    var.mainloop()

