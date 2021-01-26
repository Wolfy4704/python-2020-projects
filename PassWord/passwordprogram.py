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
        self.user_tb = Entry(self)
        self.pw_tb = Entry(self)
        self.lbl1 = Label(self, text="Enter login")
        self.lbl2 = Label(self, text="UserName")
        self.lbl3 = Label(self, text="Password")
        self.bttn_submit = Button(self,text = "submit")
        self.bttn_submit["command"]=self.submit
        self.output = Text(self)

        self.lbl1.grid(row=0, column=0, columnspand = 3)
        self.lbl2.grid(row=1, column=0, sticky=NW)
        self.lbl3.grid(row=2, column=0, sticky=SW)
        self.bttn_submit.grid(row=3, column=0, sticky=W)
        self.user_tb.grid(row=1, column=1, sticky=W)
        self.pw_tb.grid(row=2, column=1, sticky=W)
        self.pw_tb.config(show = "*")
        self.output.grid(row = 4,column = 0, columnspan=2)
        self.output.config(width=40, height = 25)


    def submit(self):
        username = user_tb.get()
        password = pw_tb.get()
        if username in self.usernames:
            if password in self.passwords:
                message = "you got in"
            else:
                message = "wrong password"
                self.trys += 1
        else:
            message = "wrong username"
            self.trys += 1
        self.output.delet(0,0, END)
        self.output.insert(0,0, message)
        if self.trys > 3:
            message = "Calling the cops you better run"
            self.output.delet(0, 0, END)
            self.output.insert(0, 0, message)
            self.user_tb.configure(state=DISABLED)
            self.pw_tb.configure(state=DISABLED)
            self.bttn_submit.config(state = DISABLED)






def main():
    root = Tk()
    root.title("Login")
    root.geometry("300x500")
    root.attributes("-fullscreen", False)

    root.mainloop()








main()


