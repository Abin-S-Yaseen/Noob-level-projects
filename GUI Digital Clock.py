#GUI Digital Clock

from tkinter import Tk
from tkinter import Label
import time
import sys

screen = Tk()
screen.title('Digital Clock')

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

clock = Label(screen,font=("calibri",90),bg="#E0FFFF",fg="#666362")
clock.pack()

get_time()

screen.mainloop()
