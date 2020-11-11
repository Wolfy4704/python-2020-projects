import random
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import calendar
import time
import datetime

def gmtnow(alarm):
    """geting Greenwich Mean Time this is based on
Unix time (also know as epoch time this is the number of
second that have elapsed since the unix epoch,
minus leap seconds
the unix epoch is 00:00:00 utc on 1 January 1970"""
    seconds = calendar.timegm(time.gmtime())
    #we need to brake this down to the current seconds
    #so there are 6o seconds in a min so if we devided by 60
    #the mainder is the current seconds
    current_sec = seconds%60
    #now we need to figure out the minutes that have passed
    minutes = seconds//60
    current_min = minutes%60
    #hours
    hours = minutes//60
    current_hour = hours%24

    #set time zone mt time
    current_hour -= 6

    #now lets figure out the am pm tag and set this to a 12 hour clock
    if current_hour >= 12:
        tag = "PM"
        current_hour -= 12
        if current_hour == 0:
            current_hour += 12
    else:
        if current_hour == 0:
            tag = "AM"
            current_hour = 12
    if current_hour <10:
        adjusted_hour = "0"+str(current_hour)
    else:
        adjusted_hour = str(current_hour)

    if current_min <10:
        adjusted_min = "0"+str(current_min)
    else:
        adjusted_min = str(current_min)

    if current_sec <10:
        adjusted_sec = "0"+str(current_sec)
    else:
        adjusted_sec = str(current_sec)
        


    time_string = str.format("{:2}:{:2}:{:2},{}",adjusted_hour,adjusted_min,adjusted_sec,tag)  

    print(time_string)
    print(alarm)
        
    if alarm == time_string:
       
        alarm_snd()
    
    return time_string

def show_time():
    time = gmtnow(alarm)
    #show time
    txt.set(time)
    #triger tick after 1000ms
    root.after(1000,show_time)

def alarm_snd():
    for i in range(5):
        winsound.Beep(750,1000)
        winsound.Beep(1000,500)
        winsound.Beep(750,1000)

def time_input():
        """get the alarm time that you want to set up"""
        ahour = input("what hour?")
        aminute = input("What minute")
        asecond = "00"
        atag = input("AM or PM").upper()
        if len(ahour) < 2:
            ahour = "0"+ahour
        if len(aminute) < 2:
            aminute = "0"+aminute

        alarm = str.format("{:2}:{:2}:{:2},{}",ahour,aminute,asecond,atag)

        return alarm
        

#setting up the gui window
alarm = time_input()
root = Tk()
root.geometry("800x200")
root.configure(background = "black")
root.bind("x",quit)
root.after(1000,show_time) 
fnt = font.Font(family = "Century Gothic",size = 60,weight = "normal")
txt = StringVar()
lbl = ttk.Label(root,textvariable = txt,foreground = "white",background = "black",font = fnt)
lbl.place(relx = 0.5,rely = 0.5,anchor = CENTER)


#running the gui
root.mainloop()
