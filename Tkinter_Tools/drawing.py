from tkinter import *
from PIL import Image,ImageTk


HEIGHT = 400
WIDTH = 400
TITLE = "new program"
BACKGROUND = "darkgray"
FONT = "San_Serif"



class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.pack(fill = BOTH,expand = 1)
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self)
        # self.canvas.create_line(20,20,100,200)
        # self.canvas.create_line(200,35,200,300,dash=(25,3))
        # self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        # self.canvas.create_rectangle(30,10,120,80,fill="#fb1",outline="red",width=5)
        # self.canvas.create_oval(10, 10, 80, 80, outline="#f11",
        #                    fill="#1f1", width=2)
        # self.canvas.create_oval(110, 10, 210, 80, outline="#f11",
        #                    fill="#1f1", width=2)
        # self.canvas.create_arc(30, 200, 90, 100, start=0,
        #                   extent=210, outline="#f11", fill="#1f1", width=2)
        # points = [150, 100, 200, 120, 240, 180, 210,
        #           200, 150, 150, 100, 200]
        # self.canvas.create_polygon(points, outline='#f11',fill='#1f1', width=2)

        self.img = Image.open("pygame_badge-removebg-preview.png")
        self.pic = ImageTk.PhotoImage(self.img)

        self.canvas.create_text(50,50,anchor =NW,font="wingdings" ,text = "Somthing ")
        self.canvas.create_text(20, 30, anchor=W, font="Purisa",
                           text="Most relationships seem so transitory")
        self.canvas.create_text(20, 60, anchor=W, font="Purisa",
                           text="They're good but not the permanent one")
        self.canvas.create_text(20, 130, anchor=W, font="Purisa",
                           text="Who doesn't long for someone to hold")
        self.canvas.create_text(20, 160, anchor=W, font="Purisa",
                           text="Who knows how to love without being told")
        self.canvas.create_text(20, 190, anchor=W, font="Purisa",
                           text="Somebody tell me why I'm on my own")
        self.canvas.create_text(20, 220, anchor=W, font="Purisa",
                           text="If there's a soulmate for everyone")
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.create_image(10, 10, anchor=NW, image=self.pic)





        self.canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    root.geometry(str.format("{}x{}",WIDTH,HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()

main()






hello




