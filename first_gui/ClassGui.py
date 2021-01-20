from tkinter import *
from tkinter import font as font

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.clicks = 0
        self.colors = ["red","blue","green","black","yellow"]
        self.color_index = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbltotal = Label(self, text = "total clicks:")
        self.lblnumclicks = Label(self,text = str(self.clicks))
        self.addbttn = Button(self,text = "+ to count")
        self.minbttn = Button(self,text = "- from count")
        self.colorbttn = Button(self,text = "change color")

        self.addbttn["command"] = self.add_to_count
        self.minbttn["command"] = self.sub_count

        self.colorbttn.grid()
        self.lbltotal.grid()
        self.lblnumclicks.grid()
        self.addbttn.grid()
        self.minbttn.grid()

    def add_to_count(self):
        self.clicks +=1
        print(self.clicks)
        self.lblnumclicks.config(text=str(self.clicks))

    def sub_count(self):
        self.clicks -=1
        print(self.clicks)
        self.lblnumclicks.config(text=str(self.clicks))

    #def change_color(self):



root = Tk()
root.title("First gui")
root.geometry("1000x500")
root.configure(bg="black")
root.attributes("-fullscreen", False)
app = App(root)



root.mainloop()