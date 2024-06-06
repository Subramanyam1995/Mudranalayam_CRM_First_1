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

window_0_1_1 = tk.Frame(window_0_1, width=100, height=100, background="bisque")

Label_1_Varible_Customer_Name = tk.StringVar(value="Customer_Name")
Label_1_Customer_Name = ttk.Label(window_0_1_1, textvariable=Label_1_Varible_Customer_Name)
Label_1_Customer_Name.pack()

Label_2_Varible_Contact_Number = tk.StringVar(value="Contact_Number")
Label_2_Contact_Number = ttk.Label(window_0_1_1, textvariable=Label_2_Varible_Contact_Number)
Label_2_Contact_Number.pack()

Label_3_Varible_Followup_date = tk.StringVar(value="Followup_date")
Label_3_Followup_date = ttk.Label(window_0_1_1, textvariable=Label_3_Varible_Followup_date)
Label_3_Followup_date.pack()

window_0_1_1.grid(row=0,column=0, padx=100, pady=100)

window_0_1_2 = tk.Frame(window_0_1) 

Text_1_Varible_Customer_Name = tk.StringVar()
Text_1_Customer_Name = tk.Entry( window_0_1_2, textvariable = Text_1_Varible_Customer_Name )
Text_1_Customer_Name.pack()


Text_2_Varible_Contact_Number = tk.StringVar()
Text_2_Contact_Number = tk.Entry(window_0_1_2, textvariable=Text_2_Varible_Contact_Number)
Text_2_Contact_Number.pack()

Text_3_Varible_Followup_date = tk.StringVar()
Text_3_Followup_date = tk.Entry(window_0_1_2, textvariable=Text_3_Varible_Followup_date)
Text_3_Followup_date.pack()

window_0_1_2.grid(row=0,column=1,padx=10, pady=10)

def botton_press():
    root = tk.Tk()
    frame1 = tk.Frame(root, width=100, height=100, background="bisque")
    frame2 = tk.Frame(root, width=50, height = 50, background="#b22222")

    frame1.pack(fill=None, expand=False)
    frame2.place(relx=.2, rely=.5, anchor="c")

    root.mainloop()
Button_1 = tk.Button(window_0_1, text="click", command= botton_press)
Button_1.grid(row=1,column=1,padx=10, pady=10)

window_0_1.mainloop()