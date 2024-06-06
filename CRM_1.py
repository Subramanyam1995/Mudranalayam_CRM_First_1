import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import datetime  
import time
import random
import json
import random

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