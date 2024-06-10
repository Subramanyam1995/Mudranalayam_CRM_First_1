import json
import pprint
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
#from Test__python2 import Main_selection_page
from pprint import pprint



"""window = tk.Tk()

window.title("CRM_1")

def Main_selection_page():


    Button_destroy = ctk.CTkButton(window, text="Destroy" , command=lambda : window.destroy())
    Button_destroy.pack()



window.geometry("800x900")

Button = ctk.CTkButton(window, text="call_one", command=Main_selection_page)
Button.pack()

window.mainloop()


with open("Data_Base_Test.json","r") as database:
    a = json.load(database)
with open("Data_Base_0.json","r") as database_0:
    databases = json.load(database_0)
for i in range(10):
    main_name = str(chr(65+i))
    #loaded_database=main_name

with open("Data_Base_Test.json","w") as database:
    a = json.dump(loaded_database,database)

olf = databases["00001AAAAA"], indent=4
"""
a={"a1":1,"b1":2}

a["c1"]=21

print(a)