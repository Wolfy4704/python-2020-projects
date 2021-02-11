from tkinter import *


HEIGHT = 330
WIDTH = 350
TITLE = "Calculator"
BACKGROUND = "black"
FONT = "San_Serif"

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.screen = "0"
        self.create_widgets()

    def create_widgets(self):

        self.output = Label(self,width=50,height = 3, bg="black",fg="green", text=self.screen)
        self.output.grid(row=0, column=0, sticky=W)

        #side buttons
        self.bttnclear = Button(self,text="Clear",width = 50, height = 3,command = self.bttnpressclear)
        self.bttndiv = Button(self,text="÷",width = 10, height = 3)
        self.bttntime = Button(self,text="x",width = 10, height = 3)
        self.bttnsub = Button(self,text="--",width = 10, height = 3)
        self.bttnequals = Button(self,text="=",width = 10, height = 3)

        self.bttnclear.grid(row=1, column=0, sticky=W)
        self.bttndiv.grid(row=2, column=3, sticky=W)
        self.bttntime.grid(row=3, column=3, sticky=W)
        self.bttnsub.grid(row=4, column=3, sticky=W)
        self.bttnequals.grid(row=5, column=3, sticky=W)




        #number buttons
        self.bttn0 = Button(self,text="0",width = 10, height = 3,command = self.bttnpress0)
        self.bttn1= Button(self,text = "1",width = 10, height = 3,command = self.bttnpress1)
        self.bttn2 = Button(self,text = "2",width = 10, height = 3,command = self.bttnpress2)
        self.bttn3 = Button(self,text = "3",width = 10, height = 3,command = self.bttnpress3)
        self.bttn4 = Button(self,text = "4",width = 10, height = 3,command = self.bttnpress4)
        self.bttn5 = Button(self, text = "5",width = 10, height = 3,command = self.bttnpress5)
        self.bttn6 = Button(self,text = "6",width = 10, height = 3,command = self.bttnpress6)
        self.bttn7 = Button(self,text = "7",width = 10, height = 3,command = self.bttnpress7)
        self.bttn8 = Button(self,text = "8",width = 10, height = 3,command = self.bttnpress8)
        self.bttn9 = Button(self,text = "9",width = 10, height = 3,command = self.bttnpress9)
        self.bttn_plusMinus = Button(self,text="±", width=10, height=3,command = self.bttnpress_plusMinus)
        self.bttn_dot = Button(self,text=".", width=10, height=3,command = self.bttnpress_dot)
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
    def bttnpress0(self):
        if self.screen == "0":
            self.screen = "0"
        else:
            self.screen += "0"
        self.output.config(text=self.screen)
    def bttnpress1(self):
        if self.screen=="0":
            self.screen ="1"
        else:
            self.screen+="1"
        self.output.config(text = self.screen)
    def bttnpress2(self):
        if self.screen == "0":
            self.screen = "2"
        else:
            self.screen += "2"
        self.output.config(text=self.screen)
    def bttnpress3(self):
        if self.screen == "0":
            self.screen = "3"
        else:
            self.screen += "3"
        self.output.config(text=self.screen)
    def bttnpress4(self):
        if self.screen == "0":
            self.screen = "4"
        else:
            self.screen += "4"
        self.output.config(text=self.screen)
    def bttnpress5(self):
        if self.screen == "0":
            self.screen = "5"
        else:
            self.screen += "5"
        self.output.config(text=self.screen)
    def bttnpress6(self):
        if self.screen == "0":
            self.screen = "6"
        else:
            self.screen += "6"
        self.output.config(text=self.screen)
    def bttnpress7(self):
        if self.screen == "0":
            self.screen = "7"
        else:
            self.screen += "7"
        self.output.config(text=self.screen)
    def bttnpress8(self):
        if self.screen == "0":
            self.screen = "8"
        else:
            self.screen += "8"
        self.output.config(text=self.screen)
    def bttnpress9(self):
        if self.screen == "0":
            self.screen = "9"
        else:
            self.screen += "9"
        self.output.config(text=self.screen)

    def bttnpress_plusMinus(self):
        if self.screen == "0":
            self.screen = "1"
        else:
            self.screen += "1"
        self.output.config(text=self.screen)
    def bttnpress_dot(self):
        if self.screen == "0":
            self.screen = "1"
        else:
            self.screen += "1"
        self.output.config(text=self.screen)
    def bttnpressdiv(self):
        if self.screen == "0":
            self.screen = "1"
        else:
            self.screen += "1"
        self.output.config(text=self.screen)
    def bttnpresstimes(self):
        if self.screen == "0":
            self.screen = "1"
        else:
            self.screen += "1"
        self.output.config(text=self.screen)
    def bttnpresssub(self):
        if self.screen == "0":
            self.screen = "1"
        else:
            self.screen += "1"
        self.output.config(text=self.screen)
    def bttnpressuqual(self):
        if self.screen == "0":
            self.screen = "1"
        else:
            self.screen += "1"
        self.output.config(text=self.screen)
    def bttnpressclear(self):
        self.screen="0"
        self.output.config(text=self.screen)


def main():
    root = Tk()
    root.geometry(str.format("{}x{}",WIDTH,HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()

main()