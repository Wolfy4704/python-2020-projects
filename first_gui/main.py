#first gui
#1/21
#Brayden Woodard

from tkinter import *
from tkinter import font as font

root = Tk()
root.title("First gui")
root.geometry("1000x500")
root.configure(bg="black")
root.attributes("-fullscreen", False)
lblfnt = font.Font(family = "Helvetica", size = 33, weight = "normal")

frame = Frame(root)
frame.configure(bg="black")
frame.grid()

lbl = Label(frame, text = "this is a terrible label",font = lblfnt)
lbl.grid()
lbl.configure(bg="black")
lbl.configure(fg="green")

bttn1 = Button(text = "Do not click")
bttn1.grid()

bttn2 = Button(frame, text = "Do click")
bttn2.grid()

bttn3 = Button(frame)
bttn3.grid()
bttn3["text"] = "fine click it"

keys = {"color": "red", "food": "pizza"}
favlbl = Label(frame,text = keys["color"])
favlbl.grid()


for i in range(10):
    x = Button(frame,text = "button"+str(i+1))
    x.grid()


root.mainloop()