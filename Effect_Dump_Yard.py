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




# Dumpyard Button and Entry

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import datetime
import time
import random
import json
import random


window_0_1 = tk.Tk()

window_0_1.geometry("800x800")


def funcation_1():
    root = tk.Tk()
    frame1 = tk.Frame(root, highlightbackground="blue", highlightthickness=1, width=600, height=100, bd=0)
    frame1.pack()

    root.mainloop()
window_0_1_1 = tk.Frame(window_0_1, )


Label_1_Varible_Customer_Name = tk.StringVar(value="Customer_Name:")
Label_1_Customer_Name = ttk.Label(window_0_1_1, textvariable=Label_1_Varible_Customer_Name)
Label_1_Customer_Name.pack( padx=10, pady=10, anchor="e")

Label_2_Varible_Contact_Number = tk.StringVar(value="Contact_Number")
Label_2_Contact_Number = ttk.Label(window_0_1_1, textvariable=Label_2_Varible_Contact_Number)
Label_2_Contact_Number.pack( padx=10, pady=10, anchor="e")

Label_3_Varible_Followup_date = tk.StringVar(value="Followup_date")
Label_3_Followup_date = ttk.Label(window_0_1_1, textvariable=Label_3_Varible_Followup_date)
Label_3_Followup_date.pack( padx=10, pady=10, anchor="e")

Label_4_Varible_Followup_date = tk.StringVar(value="Followup_date")
Label_4_Followup_date = ttk.Label(window_0_1_1, textvariable=Label_4_Varible_Followup_date)
Label_4_Followup_date.pack( padx=10, pady=10, anchor="e")






window_0_1_1.grid(row=0,column=0, padx=10, pady=10)







window_0_1_2 = tk.Frame(window_0_1)

Text_1_Varible_Customer_Name = tk.StringVar(value=123154165423154165423154165465432)
Text_1_Customer_Name = tk.Entry( window_0_1_2, textvariable = Text_1_Varible_Customer_Name )
Text_1_Customer_Name.pack( padx=10, pady=10)


Text_2_Varible_Contact_Number = tk.StringVar()
Text_2_Contact_Number = tk.Entry(window_0_1_2, textvariable=Text_2_Varible_Contact_Number)
Text_2_Contact_Number.pack( padx=10, pady=10)

Text_3_Varible_Followup_date = tk.StringVar()
Text_3_Followup_date = tk.Entry(window_0_1_2, textvariable=Text_3_Varible_Followup_date)
Text_3_Followup_date.pack( padx=10, pady=10)

Text_4_Varible_Followup_date = tk.StringVar()
Text_4_Followup_date = tk.Entry(window_0_1_2, textvariable=Text_4_Varible_Followup_date)
Text_4_Followup_date.pack( padx=10, pady=10)


window_0_1_2.grid(row=0,column=1,padx=10, pady=10)




window_0_1_3 = tk.Frame(window_0_1)

Button_1_Customer_Name = ttk.Button(window_0_1_3, text="Customer_Name_Push",command=funcation_1)
Button_1_Customer_Name.pack( padx=10, pady=10)
window_0_1_3.grid(row=0,column=3,padx=10, pady=10)

window_0_1.mainloop()


# Table
def loader():
    for i in range(30):
        if a[i]=="a":
            table_1.insert(parent="", index=0, values=(f"a{i}"))
        if a[i]=="b":
            table_2.insert(parent="", index=0, values=(f"b{i}"))
        if a[i]=="c":
            table_3.insert(parent="", index=0, values=(f"c{i}"))
window = tk.Tk()
a= []
for i in range(30):
    a.append(random.choices(("a","b","c"))[0])
print(len(a))
window1=tk.Frame(window)
listss = ("a")
table_1 = ttk.Treeview(window1, columns=listss, show="headings" )
table_1.heading(listss[0], text=listss[0])
table_1.pack(fill="both",expand=True)

listss = ("b")
table_2 = ttk.Treeview(window1, columns=listss, show="headings" )

table_2.heading(listss[0], text=listss[0])
table_2.pack(fill="both",expand=True)

listss = ("c")
table_3 = ttk.Treeview(window1, columns=listss, show="headings" )
table_3.heading(listss[0], text=listss[0])
table_3.pack(fill="both",expand=True)
loader()

window1.pack()

window.mainloop()