import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import datetime  
import time
import random
import json

names = ["0010 Arkalgud Vinayaka Printers Arkalgud","0013 Arsikere SIDDUSHREE PRINTERS ARASIKERE","0045 Bagalkot CHOWDESHWARI PRINTERS MANVI","0072 Bagalkot OM OFFSET PRINTERS MAHALINGAPURA",
"0076 Bagalkot PRAVEEN PRINTERS GULEDGUDA","0152 Bellary Anoop Offset Bellary","0158 Bellary DHARMASRI MUDRANA KAMPLI","0177 Bellary MALLESHWARA PRINTERS KURUGODU",
"0179 Bellary MR FLEX BELLARY","0188 Bellary PRAKASH BAGALKOTE","0222 Belur Adarsh Printer Belur","0233 Bhadravati NADIG PRINTERS BHADRAVATI","0266 Bidar SRI SAI CARD HOUSE BIDAR",
"0298 Bijapur Neela Ganga Flex Talikote","0303 Bijapur Rani Digital Bijapur","0322 Bijapur TOLANUR PRINTS BIJAPUR","0340 Challakere NAAZ CHALLAKERE","0381 Chikkaballapura GRAPHIC VISION CHIKBALAPURA",
"0408 Chikmagalur Geetha sticke digital CKM","0435 Chikmagalur SRI RAMA PRINT"]

contact = ["9632899014","9900663058","9886070106","9880833679","9482002865","9964478822","9611931339","8904463811","9742459224","9448234416","9141713121","9448416986","9448947616",
"9743015210","9008637444","7760957343","9902780408","9886473862","9353182008","9449917416"]

with open("Data_Base.json","r") as database:
    data_entry = json.load(database)


print()
print(data_entry)
print()


for i in range(10):
    data_entry["Mudranalayam_Database"][names[i]]=contact[i]
    data_entry["Mudranalayam_Database"][f"Contacts{i}"]=[data_entry["Mudranalayam_Database"][f"Contacts{i}"],contact[i]+"999999999999999999999999999999"]

print()
print(data_entry)
print()

with open("Data_Base.json","w") as database1:
   json.dump(data_entry,database1,indent=4)




"""
window_1 = tk.Tk()
list_names  = ( "Name", "Office_Name" ,"Phone_Number")

Table = ttk.Treeview(window_1, columns=list_names,show="headings")
Table.heading(list_names[0],text=list_names[0])
Table.heading(list_names[1],text=list_names[1])
Table.heading(list_names[2],text=list_names[2])

Table.pack()
window_1.mainloop()
"""


