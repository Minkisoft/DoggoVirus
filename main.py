from tkinter import *
<<<<<<< HEAD
wills = Tk()

wills.title("Doggo")
canvas = Canvas(wills, width=310, height=280)
canvas.pack()
=======

>>>>>>> origin/master

for i in range(1, 10000000):
    var = str(i)
    var = Tk()
    var.title("Doggo")
    canvas = Canvas(var, width=310, height=280)
    canvas.pack()

<<<<<<< HEAD
message = Label(wills, text = "Doggo has infected your computer", font = "Helvetica 16 bold italic")
message.pack()
=======
    img = PhotoImage(file="doggo.gif")
    canvas.create_image(30,30, anchor=NW, image=img)
>>>>>>> origin/master

    message = Label(var, text = "Doggo has infected your computer", font = "Helvetica 16 bold italic")
    message.pack()

<<<<<<< HEAD
wills.mainloop()
=======
    var.mainloop()

>>>>>>> origin/master
