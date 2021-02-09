from tkinter import *
from tkinter.ttk import *

HEIGHT = 200
WIDTH = 200
TITLE = "List boxes and combo boxes"
BACKGROUND = "darkgray"
FONT = "San_Serif"

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        self.listbox = Listbox(self,selectmode=EXTENDED)
        self.listboxitems = ["test1","test2","test3","test4","test5"]
        for i in range(len(self.listboxitems)):
            self.listbox.insert(END,self.listboxitems[i])
        self.listbox.pack(side=LEFT)

        self.itemslistcb = [1,2,3,4,5,"hello"]
        self.combobox = Combobox(self,value=self.itemslistcb)
        #self.combobox.config(value = self.itemslistcb)
        #self.combobox["value"]=self.itemslistcb
        self.combobox.current(5)
        self.combobox.pack(side=LEFT)

        self.progressbar = Progressbar(self,length=500,value=25)
        self.progressbar.pack(side=LEFT)

        self.increase = Button(self,text=">>>>>",command=self.inc)
        self.increase.pack(side=LEFT)
        self.decrease = Button(self, text=">>>>>", command=self.dec)
        self.decrease.pack(side=LEFT)

        self.submit = Button(self,text="Try me",command=self.update)
        self.submit.pack(side=LEFT)

    def inc(self):
        self.progressbar['value'] = self.progressbar['value']+1

    def dec(self):
        self.progressbar['value'] = self.progressbar['value'] - 1

    def update(self):
        cbtext=self.combobox.get()
        print(cbtext)

        #x = self.listbox.get(ANCHOR)
        #print(x)
        x = ""
        selected = self.listbox.curselection()
        for i in selected:
            x+=" ",self.listbox.get([i])
            self.itemslistcb.append(self.listbox.get([i]))
        self.combobox["value"]=self.itemslistcb
        print(x)

        self.listbox.insert(END,cbtext)



def main():
    root = Tk()
    #root.geometry(str.format("{}x{}",WIDTH,HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()

main()