
from tkinter import *
import datetime
import time
import win32api
import random

def playsound():
    for i in range(2):
        win32api.Beep(random.randint(37,10000), random.randint(750,3000))

    x=37
    y=2500
    for i in range(6):
        win32api.Beep(x,y)
        x+=100
        y-=120

def alarm():
    while True:
       
        set_alarm_time = f"{hour.get()}:{min.get()}:{sec.get()}"
 
        time.sleep(1)
 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        if current_time == set_alarm_time:
            print("Time to Wake up")
            playsound()
            
            break


clock = Tk()

clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = alarm).place(x =110,y=70)

clock.mainloop()