import tkinter as tk
window = tk.Tk()
window.title('GFG')

A =  tk.Label(window, text="flat", width=10, height=2, borderwidth=5, relief="flat")
B =  tk.Label(window, text="solid", width=10, height=2, borderwidth=5, relief="solid")
C =  tk.Label(window, text="raised", width=10, height=2, borderwidth=5, relief="raised")
D =  tk.Label(window, text="sunken", width=10, height=2, borderwidth=5, relief="sunken")
E =  tk.Label(window, text="ridge", width=10, height=2, borderwidth=5, relief="ridge")
F =  tk.Label(window, text="groove", width=10, height=2, borderwidth=5, relief="groove")

A.grid(column=0, row=1, padx=100, pady=10)
B.grid(column=0, row=2, padx=100, pady=10)
C.grid(column=0, row=3, padx=100, pady=10)
D.grid(column=0, row=4, padx=100, pady=10)
E.grid(column=0, row=5, padx=100, pady=10)
F.grid(column=0, row=6, padx=100, pady=10)

window.mainloop()


# Calender Code
from tkinter import *
from tkcalendar import Calendar
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
