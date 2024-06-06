from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import customtkinter as ctk
import datetime  
import time
import random
import json
import random

root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar
def calenders():
    root = Tk()

    # Set geometry
    root.geometry("400x400")
    cal = Calendar(root, selectmode='day', year=2020, month=5, day=22)

    cal.pack(pady=20)


    def grad_date():
        date.config(text="Selected Date is: " + cal.get_date())


    # Add Button and Label
    Button(root, text="Get Date",
           command=grad_date).pack(pady=20)

    date = Label(root, text="")
    date.pack(pady=20)
    root.mainloop()


button = Button(root, text= "Button", command=calenders)
button.pack()

# Execute Tkinter
root.mainloop()
