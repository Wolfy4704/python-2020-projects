from tkinter import *
from tkinter import messagebox as mb, filedialog
from tkinter import colorchooser


HEIGHT = 200
WIDTH = 200
TITLE = "new program"
BACKGROUND = "white"
FONT = "San_Serif"

class App(Frame):

    def __init__(self,master):
        super(App, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self.master)
        self.master.config(meni=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="open", command=self.onOpen)
        menubar.add_cascade(label="file", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

        def onOpen(self):
            ftypes = [("Python files","*.py",("Plane Text","*.txt"),("Allfiles","*"))]
            dlg = filedialog.Open(self,filetypes=ftypes)
            f1 = dlg.show()
            if f1 != "":
                text = self.readFile(f1)
                self.txt.insert(END, text)

        def readFile(self, filename):
            with open(filename,r) as f:
                text = f.read()
                return text



        





    #     self.btn = Button(self, text="Choose Color",
    #                       command = self.onChoose)
    #     self.btn.place(x=30,y=30)
    #
    #     self.frame = Frame(self,border=1,
    #                        relief=RIDGE, width=100, height=100)
    #     self.frame.place(x=160, y=30)
    #
    # def onChoose(self):
    #     (rgb, hx) = cc.askcolor()
    #     self.frame.config(bg=hx)










    #     error = Button(self, text="Error", command=self.onError, bg="white")
    #     error.grid(row=1, column=0)
    #     blah = Button(self, text="Blah", command=self.onBlah,bg="white")
    #     blah.grid(row=1, column=1)
    #     eh = Button(self, text="Eh", command=self.onEh,bg="white")
    #     eh.grid(row=2, column=0)
    #     brrrr = Button(self, text="BRRRR", command=self.onBRRRR,bg="white")
    #     brrrr.grid(row=2, column=1)
    #
    # def onError(self):
    #     mb.showerror("Error", "you did something wrong dumbass")
    #     self.master.destroy()
    # def onBlah(self):
    #     mb.showwarning("Blah", "dont fuck up again")
    # def onEh(self):
    #     result = mb.askquestion("Quit", "are you sure you want to quit?")
    #     if result == "yes":
    #         mb.showinfo("Info", "Bye!")
    #         self.master.destroy()
    #     else:
    #         return
    # def onBRRRR(self):
    #     mb.showinfo("BRRRR", "BRRRRRRRRRRRRRRRR")


def main():
    root = Tk()
    root.geometry(str.format("{}x{}",WIDTH,HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()

main()