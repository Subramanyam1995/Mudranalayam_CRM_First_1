import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import datetime  
import time
import random
import json
import random


window = tk.Tk()
a= []
for i in range(30):
    a.append(random.choices(("a","b","c","d"))[0])
window1=tk.Frame(window)
listss = ("a")
table_1 = ttk.Treeview(window1, columns=listss, show="headings" )
table_1.heading(listss[0], text=listss[0])
table_1.pack(side="left")

listss = ("b")
table_1 = ttk.Treeview(window1, columns=listss, show="headings" )
table_1.heading(listss[0], text=listss[0])
table_1.pack(side="left")

listss = ("c")
table_1 = ttk.Treeview(window1, columns=listss, show="headings" )
table_1.heading(listss[0], text=listss[0])
table_1.pack(side="left")

window1.pack()

"""for i in range(10):
    if a[i]=="a":
        table.insert(parent="", index=0,values=("a","0","0"))
    if a[i]=="b":
        table.insert(parent="", index=0,values=("0","b","0"))
    if a[i]=="c":
        table.insert(parent="", index=0,values=("0","0","c"))"""
window.mainloop()