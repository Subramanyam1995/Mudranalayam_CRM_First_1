import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import datetime
import random
import os
import json
import time
from pprint import pprint




with open("Data_Base_0.json","r") as data:
    source = json.load(data)
with open("Data_Base.json","w") as data1 :
    json.dump(source,data1,indent=2)

list1 = ['01_Old_Name',
 '02_Owner_Names',
 '03_Location',
 '04_Visiting_Card_Pic',       
 '05_Fraud',
 '06_Personal_Data',
 '07_Sales_Report',
 '08_Recording',
 '09_Customer_Links',
 '10_Anydesk_Deatils',
 '11_FollowUps_Request',       
 '12_Customer_Update_Required',
 '13_Gold_Mine',
 '14_Date_of_Database_Creation',
 '15_Database_Deactiver',
 '16_Caution']

"""for i in range(16):
    print(f"tk.Button(window_01_01_{list1[i][:2]}, text={str(list1[i][3:])}, font='Bahnschrift 12 bold', command=None ).pack()")

    print(f"window_01_01_{list1[i][:2]} = tk.Frame(window_1_1_0)")

    print(f"tk.Label(window_01_01_{list1[i][:2]}, text={str(list1[i][3:])},font='Bahnschrift 12 bold', command=None).pack()")

    print(f"tk.Entry(window_01_01_{list1[i][:2]}, variable={str(list1[i][3:])}, font='Bahnschrift 12 bold').pack()")

    print()
    print()

tk.Button(window_01_01_01, text=Old_Name, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_01 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_01, text=Old_Name,font='Bahnschrift 12 bold', command=None).pack()      
tk.Entry(window_01_01_01, variable=Old_Name, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_02, text=Owner_Names, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_02 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_02, text=Owner_Names,font='Bahnschrift 12 bold', command=None).pack()   
tk.Entry(window_01_01_02, variable=Owner_Names, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_03, text=Location, font='Bahnschrift 12 bold', command=None ).pack()   
window_01_01_03 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_03, text=Location,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_03, variable=Location, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_04, text=Visiting_Card_Pic, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_04 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_04, text=Visiting_Card_Pic,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_04, variable=Visiting_Card_Pic, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_05, text=Fraud, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_05 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_05, text=Fraud,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_05, variable=Fraud, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_06, text=Personal_Data, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_06 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_06, text=Personal_Data,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_06, variable=Personal_Data, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_07, text=Sales_Report, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_07 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_07, text=Sales_Report,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_07, variable=Sales_Report, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_08, text=Recording, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_08 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_08, text=Recording,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_08, variable=Recording, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_09, text=Customer_Links, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_09 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_09, text=Customer_Links,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_09, variable=Customer_Links, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_10, text=Anydesk_Deatils, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_10 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_10, text=Anydesk_Deatils,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_10, variable=Anydesk_Deatils, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_11, text=FollowUps_Request, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_11 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_11, text=FollowUps_Request,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_11, variable=FollowUps_Request, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_12, text=Customer_Update_Required, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_12 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_12, text=Customer_Update_Required,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_12, variable=Customer_Update_Required, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_13, text=Gold_Mine, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_13 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_13, text=Gold_Mine,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_13, variable=Gold_Mine, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_14, text=Date_of_Database_Creation, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_14 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_14, text=Date_of_Database_Creation,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_14, variable=Date_of_Database_Creation, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_15, text=Database_Deactiver, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_15 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_15, text=Database_Deactiver,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_15, variable=Database_Deactiver, font='Bahnschrift 12 bold').pack()


tk.Button(window_01_01_16, text=Caution, font='Bahnschrift 12 bold', command=None ).pack()
window_01_01_16 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_16, text=Caution,font='Bahnschrift 12 bold', command=None).pack()
tk.Entry(window_01_01_16, variable=Caution, font='Bahnschrift 12 bold').pack()"""

