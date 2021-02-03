from tkinter import *


HEIGHT = 500
WIDTH = 500
TITLE = "Menu bar Examples"
BACKGROUND = "white"
FONT = "San_Serif"

class App(Frame):

    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.test = 1
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit",command=self.onExit)
        fileMenu.add_command(label="Open", command=self.open)
        fileMenu.add_command(label="Save", command=self.save)
        menubar.add_cascade(label="File",menu=fileMenu)

        submenu = Menu(fileMenu)
        submenu.add_command(label="new feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")

        fileMenu.add_cascade(label="import", menu=submenu, underline=0)
        fileMenu.add_separator()

        self.frame1 = Frame(self,bg="red",width=250,height=250)
        self.frame1.grid(row=0,column=0)
        self.frame2 = Frame(self,bg="blue",width=250,height=250)
        self.frame2.grid(row=0,column=1)
        self.lbl1 = Label(self.frame1,text="testing").pack(padx=20,pady=20,fill=BOTH)
        self.lbl2 = Label(self.frame2,text="testing").pack(padx=20,pady=20,fill=BOTH)

        editMenu = Menu(menubar)
        editMenu.add_command(label="Sucide_Button", command=self.destroyf1)
        editMenu.add_command(label="Life_Button", command=self.createFrame)
        menubar.add_cascade(label="Edit", menu=editMenu)



    def onExit(self):
        self.quit()
    def open(self):
        pass
    def save(self):
        pass
    def destroyf1(self):
        self.frame1.destroy()
    def createFrame(self):
        self.test+=1
        self.frame3 = Frame(self, bg="red", width=250, height=250)
        self.frame3.grid(row=0, column=self.test)
        self.lbl3 = Label(self.frame3,text="testing").pack(padx=20,pady=20,fill=BOTH)


def main():
    root = Tk()
    root.geometry(str.format("{}x{}",WIDTH,HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()

main()