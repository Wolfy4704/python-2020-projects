from tkinter import *


HEIGHT = 500
WIDTH = 500
TITLE = "Calculator"
BACKGROUND = "darkgray"
FONT = "San_Serif"

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):

        self.output = Label(self,width=20, bg="white")
        self.output.grid(row=0, column=0, sticky=W)

        #side buttons
        self.bttndelete = Button(text="Delete", width=10, height=3)
        self.bttnclear = Button(text="Clear",width = 10, height = 3)
        self.bttndiv = Button(text="÷",width = 10, height = 3)
        self.bttntime = Button(text="x",width = 10, height = 3)
        self.bttnsub = Button(text="--",width = 10, height = 3)
        self.bttnequals = Button(text="=",width = 10, height = 3)

        self.bttndelete.grid(row=1, column=3, sticky=W)
        self.bttnclear.grid(row=1, column=2, sticky=W)
        self.bttndiv.grid(row=2, column=3, sticky=W)
        self.bttntime.grid(row=3, column=3, sticky=W)
        self.bttnsub.grid(row=4, column=3, sticky=W)
        self.bttnequals.grid(row=5, column=3, sticky=W)




        #number buttons
        self.bttn0 = Button(text="0",width = 10, height = 3)
        self.bttn1= Button(text = "1",width = 10, height = 3)
        self.bttn2 = Button(text = "2",width = 10, height = 3)
        self.bttn3 = Button(text = "3",width = 10, height = 3)
        self.bttn4 = Button(text = "4",width = 10, height = 3)
        self.bttn5 = Button( text = "5",width = 10, height = 3)
        self.bttn6 = Button(text = "6",width = 10, height = 3)
        self.bttn7 = Button(text = "7",width = 10, height = 3)
        self.bttn8 = Button(text = "8",width = 10, height = 3)
        self.bttn9 = Button(text = "9",width = 10, height = 3)
        self.bttn_plusMinus = Button(text="±", width=10, height=3)
        self.bttn_dot = Button(text=".", width=10, height=3)
        #grid numbers part
        self.bttn0.grid(row=5, column=1, sticky=W)
        self.bttn1.grid(row = 4, column = 0, sticky = W)
        self.bttn2.grid(row = 4, column = 1, sticky = W)
        self.bttn3.grid(row = 4, column = 2, sticky = W)
        self.bttn4.grid(row = 3, column = 0, sticky = W)
        self.bttn5.grid(row = 3, column = 1, sticky = W)
        self.bttn6.grid(row = 3, column = 2, sticky = W)
        self.bttn7.grid(row = 2, column = 0, sticky = W)
        self.bttn8.grid(row = 2, column = 1, sticky = W)
        self.bttn9.grid(row = 2, column = 2, sticky = W)
        self.bttn_plusMinus.grid(row=5, column=0, sticky=W)
        self.bttn_dot.grid(row = 5, column = 2, sticky = W)






def main():
    root = Tk()
    root.geometry(str.format("{}x{}",WIDTH,HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()

main()