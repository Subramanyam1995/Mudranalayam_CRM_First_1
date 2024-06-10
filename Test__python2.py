import json
import pprint
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from Test__python3 import *
import datetime
def update_viewer(link):
    window = tk.Tk()
    Name_011 = data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["011Name"]
    Datetime_012 = data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["012Datetime.now()"]
    NumberOfTimeCorrected_013 = data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["013Number_Of_Time_Corrected"]

    window.title("Update_Viewer")

    ttk.Label(window, text= Name_011).pack()
    ttk.Label(window, text=Datetime_012).pack()
    ttk.Label(window, text=NumberOfTimeCorrected_013).pack()


    window.mainloop()
    
def Name_Updater():
    Name_011 = data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["011Name"]
    Datetime_012 = data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["012Datetime.now()"]
    NumberOfTimeCorrected_013 = data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["013Number_Of_Time_Corrected"]
    if Name_011 == None and NumberOfTimeCorrected_013 == 0 and Datetime_012==None:
        data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["011Name"] = var01_name.get()
        data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["012Datetime.now()"] = datetime.datetime.now()
        data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["013Number_Of_Time_Corrected"]=1
    else:
        data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["019DumpYard"].insert(0, [{ "011Name":Name_011, "012Datetime.now()":Datetime_012, "013Number_Of_Time_Corrected":NumberOfTimeCorrected_013,"Date_Created": datetime.datetime.now()} ])
        data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["011Name"] = var01_name.get()
        data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["012Datetime.now()"] = datetime.datetime.now()
        data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"]["013Number_Of_Time_Corrected"] += 1

    update_viewer(data_filds["01Name"]["01_list_of_Name"]["First_reg_Name"])
def Name_data_upload(Value):
    global  var01_name
    window = tk.Tk()

    window.geometry("300x800")

    ttk.Label(window, text="Name Registry",font="Bahnschrift 24 bold", ).pack(pady=30)


    # Name
    ttk.Label(window, text= "Name Of The Client",font="Bahnschrift 14").pack()
    var01_name = tk.StringVar(window)
    ttk.Entry(window, textvariable=var01_name,width=40).pack()
    ttk.Label(window, textvariable=var01_name, font="Bahnschrift 12").pack()



    ttk.Button(window, text=" Click ME", command= Name_Updater ).pack()

    ttk.Button(window, text="Destroy", command=lambda : window.destroy()).pack()

    window.mainloop()



