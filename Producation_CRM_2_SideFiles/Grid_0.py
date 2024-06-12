
# test_values
#from Producation_CRM.Producation_CRM_3_Module_Imports import *


def Push_To_CRM_Database_First_Time_Grid_0(value_inputed, Phone_Saved_Name__0101,Source_of_Collection__010102, Updated_Office_Name__0102):
    with open("CRM_Database.json","r") as CRM_Main:
        Database = json.load(CRM_Main)
        
    Database[f"00_{value_inputed}"]={f"01__{value_inputed}__First_Phone_Saved_Name":{f"0101__{value_inputed}__Name":f"{Phone_Saved_Name__0101}",
                                                                                     f"0102__{value_inputed}__Source":f"{Source_of_Collection__010102}",
                                                                                     f"0103__{value_inputed}__OfficeName" : f"{Updated_Office_Name__0102}",
                                                                                     f"0104__{value_inputed}__Datetime.now()" : str(datetime.datetime.now()),
                                                                                     f"0105__{value_inputed}__Number_Of_Time_Corrected" : 0
                                                                                     }
                                     
                                     }
    with open("CRM_Database.json","w") as push:
        json.dump(Database,push,indent=15)
    print("Donea")


def Pusher_grid_0(value,Phone_Saved_Name__0101,Source_of_Collection,Updated_Office_Name__0102):

    window_pusher = tk.Tk()
    window_pusher.title("Publishing Name_Reg")
    tk.Label(window_pusher,text = value ,font='Bahnschrift 20 bold').grid(row=0,column=0,columnspan=2)

    tk.Label(window_pusher,text = "0101__Phone_Saved_Name", font='Bahnschrift 12 bold').grid(row=1,column=0)
    tk.Label(window_pusher,text= f": {Phone_Saved_Name__0101}",font='Bahnschrift 12 bold').grid(row=1,column=1)

    tk.Label(window_pusher,text = "010102__Source", font='Bahnschrift 12 bold').grid(row=2,column=0)
    tk.Label(window_pusher,text= f": {Source_of_Collection}",font='Bahnschrift 12 bold').grid(row=2,column=1)

    tk.Label(window_pusher,text = "010201__OfficeName", font='Bahnschrift 12 bold').grid(row=3,column=0)
    tk.Label(window_pusher,text= f": {Updated_Office_Name__0102}",font='Bahnschrift 12 bold').grid(row=3,column=1)

    tk.Button(window_pusher, text="Publish", command=lambda:Push_To_CRM_Database_First_Time_Grid_0(value,Phone_Saved_Name__0101,Source_of_Collection, Updated_Office_Name__0102)).grid(row=4,column=0,columnspan=2)
    window_pusher.mainloop()


#def grid_0(window,value_inputed):
#------------------------------
#Extend Values
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
value_inputed=1001
Set_of_Printing_Company = {
                            "Keshav": {"Registed_date":None
                                       
                                       },
                            "BOP":{"Registed_date":None},
                            

                            }
def disabler_window_1_1_0(value,lab):
    if lab["state"] == "normal" : 
        for i in value.winfo_children():
            i.configure(state="disable") 
    else: 
        for i in value.winfo_children():
            i.configure(state="normal") 


#---------------------
window_01_01_01 = tk.Frame(window)

# Heading Name Stage_1//2
Heading = tk.Label(window_01_01_01, text="Heading",font='Bahnschrift 20 bold', command=None)
Heading.grid(row=0,column=0,columnspan=2)    


# Stage 01_01
# Key : Labels 

Old_Serial_Name = tk.StringVar(value=f"{value_inputed}___01_Old_Serial_Name")
Old_Serial_Name_010101 = tk.Label(window_01_01_01, text=Old_Serial_Name.get(),font='Bahnschrift 20 bold')
Old_Serial_Name_010101.grid(row=1,column=0,columnspan=2) 

Name = tk.StringVar(window_01_01_01,value=f"{value_inputed}___010101__Name")
tk.Label(window_01_01_01, textvariable= Name,font='Bahnschrift 12 bold', command=None).grid(row=2,column=0)

Source_of_Collection = tk.StringVar(window_01_01_01,value=f"{value_inputed}__010102__Source")
tk.Label(window_01_01_01, textvariable= Source_of_Collection,font='Bahnschrift 12 bold', command=None).grid(row=3,column=0)


OfficeName = tk.StringVar(window_01_01_01, value=f"{value_inputed}___01021__OfficeName")
tk.Label(window_01_01_01, textvariable=OfficeName,font='Bahnschrift 12 bold', command=None).grid(row=4,column=0)

# Value : Entrys

Name__010101 = tk.StringVar(window_01_01_01)
tk.Entry(window_01_01_01, textvariable=Name__010101, font='Bahnschrift 12 bold').grid(row=2,column=1)  
    
Source__010102 = tk.StringVar(window_01_01_01,value="Not_selected")    
ttk.Combobox(window_01_01_01, textvariable=Source__010102, value=tuple(Set_of_Printing_Company.keys())).grid(row=3, column=1)

OfficeName__01021 = tk.StringVar(window_01_01_01)
tk.Entry(window_01_01_01, textvariable=OfficeName__01021, font='Bahnschrift 12 bold').grid(row=4,column=1)    

tk.Button(window_01_01_01, text="Pusher", font='Bahnschrift 12 bold', command=lambda:Pusher_grid_0(value_inputed,Name__010101.get(),Source__010102.get(),OfficeName__01021.get())).grid(row=7,columnspan=2,column=0)  

Disabler_1 = tk.Checkbutton(window, text= "Disabler", command=lambda : disabler_window_1_1_0(window_01_01_01,Heading))
Disabler_1.pack(anchor="ne",side="top")

window_01_01_01.pack()


#Extend Values
tk.Button(window, text="Destroy", command=lambda: window.destroy()).pack(side="bottom")
window.mainloop()