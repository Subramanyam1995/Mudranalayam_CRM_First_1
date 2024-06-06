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

window_0_1_1 = tk.Frame(window_0_1, width=10, height=10)


Label_1_Varible_Customer_Name = tk.StringVar(value="Customer_Name:")
Label_1_Customer_Name = ttk.Label(window_0_1_1, textvariable=Label_1_Varible_Customer_Name)
Label_1_Customer_Name.pack( padx=10, pady=10, anchor="e")

Label_2_Varible_Contact_Number = tk.StringVar(value="Contact_Number")
Label_2_Contact_Number = ttk.Label(window_0_1_1, textvariable=Label_2_Varible_Contact_Number)
Label_2_Contact_Number.pack( padx=10, pady=10, anchor="e")

Label_3_Varible_Followup_date = tk.StringVar(value="Followup_date")
Label_3_Followup_date = ttk.Label(window_0_1_1, textvariable=Label_3_Varible_Followup_date)
Label_3_Followup_date.pack( padx=10, pady=10, anchor="e")

Label_3_Varible_Followup_date = tk.StringVar(value="Followup_date")
Label_3_Followup_date = ttk.Label(window_0_1_1, textvariable=Label_3_Varible_Followup_date)
Label_3_Followup_date.pack( padx=10, pady=10, anchor="e")






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

window_0_1_2.grid(row=0,column=1,padx=10, pady=10)




window_0_1_3 = tk.Frame(window_0_1) 

Button_1_Customer_Name = ttk.Button(window_0_1_3, text="Customer_Name_Push")
Button_1_Customer_Name.pack( padx=10, pady=10)
window_0_1_3.grid(row=0,column=3,padx=10, pady=10)

window_0_1.mainloop()