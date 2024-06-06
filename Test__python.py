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

window_0_1_1 = tk.Frame(window_0_1, width=10, height=10,border=1)

Label_1_Varible_Customer_Name = tk.StringVar(value="Customer_Name")
Label_1_Customer_Name = ttk.Label(window_0_1_1, textvariable=Label_1_Varible_Customer_Name)
Label_1_Customer_Name.pack()

Label_2_Varible_Contact_Number = tk.StringVar(value="Contact_Number")
Label_2_Contact_Number = ttk.Label(window_0_1_1, textvariable=Label_2_Varible_Contact_Number)
Label_2_Contact_Number.pack()

Label_3_Varible_Followup_date = tk.StringVar(value="Followup_date")
Label_3_Followup_date = ttk.Label(window_0_1_1, textvariable=Label_3_Varible_Followup_date)
Label_3_Followup_date.pack()

window_0_1_1.grid(row=0,column=0, padx=10, pady=10)



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




  

   

window_0_1.mainloop()