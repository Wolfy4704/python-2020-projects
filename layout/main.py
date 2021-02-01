from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style, Button
Height = 300
Width = 280

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH,expand=1)
        self.create_widgets()

    def create_widgets(self):
        Label(text="Absolute positioning").place(x=0,y=0)
        Label(text="Absolute positioning").place(x=0, y=20)
        Button(text = "click me").place(x=Width/2, y=Height/2)
        img1 = Image.open("eyes.png")
        firstimg = ImageTk.PhotoImage(img1)
        self.lbl1 = Label(self,image=firstimg)
        self.lbl1.image = firstimg
        self.lbl1.place(x=0,y=60)


def main():
    root = Tk()
    root.geometry("300x280+300+300")
    app = App(root)
    root.mainloop()

main()
