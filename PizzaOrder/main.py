#Pizza order
#1/21
#Brayden Woodard

from tkinter import *
from tkinter import font as font

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.lblname = Label(self, text = "Customer Name:")
        self.lbladress = Label(self, text="Customer Adress:")
        self.lblphone = Label(self, text="Customer Phone:")
        self.lblsize = Label(self, text="Pick your Size")

        self.size = StringVar()
        self.size.set(None)
#size
        Radiobutton(self,
                    variable = self.size,
                    text="Small",
                    value="Small",
                    ).grid(row=4,column=0,sticky=W)
        Radiobutton(self,
                    variable = self.size,
                    text="Medium",
                    value="Medium",
                    ).grid(row=4,column=1,sticky=W)
        Radiobutton(self,
                    variable = self.size,
                    text="Large",
                    value="Large",
                    ).grid(row=4,column=2,sticky=W)
#crust type
        Radiobutton(self,
                    variable=self.size,
                    text="Stuffed",
                    value="Stuffed",
                    ).grid(row=7, column=0, sticky=W)
        Radiobutton(self,
                    variable=self.size,
                    text="Pan",
                    value="Pan",
                    ).grid(row=7, column=1, sticky=W)
        Radiobutton(self,
                    variable=self.size,
                    text="Deep",
                    value="Deep",
                    ).grid(row=7, column=2, sticky=W)
        Radiobutton(self,
                    variable=self.size,
                    text="Thin",
                    value="Thin",
                    ).grid(row=8, column=0, sticky=W)
        Radiobutton(self,
                    variable=self.size,
                    text="Square",
                    value="Square",
                    ).grid(row=8, column=1, sticky=W)
        Radiobutton(self,
                    variable=self.size,
                    text="None",
                    value="None",
                    ).grid(row=8, column=2, sticky=W)
        Label(self,text="Pick your toppings").grid(row=8,column=0,sticky=W)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 9, 0)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 9, 1)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 9, 2)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 10, 0)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 10, 1)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 10, 2)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 11, 0)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 11, 1)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 11, 2)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 12, 0)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 12, 1)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 12, 2)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 13, 0)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 13, 1)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 13, 2)
        self.pep = BooleanVar()
        self.create_cb(self.pep, "pepperoni", 13, 0)

        self.lblname.grid(row=0,column=0,sticky=W)
        self.lbladress.grid(row=1,column=0,sticky=W)
        self.lblphone.grid(row=2,column=0,sticky=W)
        self.lblsize.grid(row=3,column=0,sticky=W)

    def test(self):
        print(self.size.get())

    def create_cb(self,var,top,r,c):
        Checkbutton(self,
                    variable=var,
                    text=top,
                    ).grid(row=r,column=c,sticky=W)


















root = Tk()
root.title("First gui")
root.geometry("400x600")
#root.configure(bg="White")
root.attributes("-fullscreen", False)
app = App(root)
root.mainloop()