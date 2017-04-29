from tkinter import *
root = Tk()

root.title("Doggo")
canvas = Canvas(root, width=310, height=280)
canvas.pack()

img = PhotoImage(file="doggo.gif")
canvas.create_image(30,30, anchor=NW, image=img)

message = Label(root, text = "Doggo has infected your computer", font = "Helvetica 16 bold italic")
message.pack()


root.mainloop()

