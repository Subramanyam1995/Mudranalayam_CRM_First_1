
# test_values
#from Producation_CRM.Producation_CRM_3_Module_Imports import *
import json

def Push_To_CRM_Database_First_Time_Grid_0(value_inputed, Phone_Saved_Name_0101,Source_of_Collection_010102, Updated_Office_Name_0102):
    #with open("CRM_Database.json","r") as CRM_Main:
    #   Database = json.load(CRM_Main)
    Database     = {}   
    Database[f"00_{value_inputed}"]={f"01__First_Phone_Saved_Name":{f"0101__Name":f"{Phone_Saved_Name_0101}",
                                                                                     f"0102__Source":f"{Source_of_Collection_010102}",
                                                                                     f"0103__OfficeName" : f"{Updated_Office_Name_0102}",
                                                                                     f"0104__Datetime.now()" : str(datetime.datetime.now()),
                                                                                     f"0105__Number_Of_Time_Corrected" : 0
                                                                                     },
                                       
                                       
                                       f"02__Owner_Names":{ f"0201__First_Reg_Name" : { f"020101__name" :{
                                                                                                          f"02010101__Name": None,
                                                                                                          f"02010102__Datetime.now()": None,
                                                                                                          f"02010103__Number_Of_Time_Corrected": None,
                                                                                                          f"0201010D__DumpYard": [["02010101","02010102","02010103"]]
                                                                                                      },
                                                                        f"020102__PhoneNo's"           : {   f"02010201__Phone_1":   
                                                                                                                                {
                                                                                                                                 f"0201020101__Number1": None,
                                                                                                                                 f"0201020102__Datetime.now()": None,
                                                                                                                                 f"0201020103__Number_Of_Time_Corrected": None,
                                                                                                                                 f"0201020104__if_invaild(True/False)":None,
                                                                                                                                 f"020102010D__DumpYard": [["0201020101","0201020102","0201020103","0201020104"]]
                                                                                                                                },
                                                                                                            f"02010202__Phone_2": None
                                                                                                        }
                                                                                                      ,
                                                                        f"020103__Position_In_Office"  :{
                                                                                                        f"02010301__Position": None,
                                                                                                        f"02010302__Datetime.now()": None,
                                                                                                        f"02010303__Number_Of_Time_Updated": None,
                                                                                                        f"0201030D__DumpYard": [["02010301","02010302","02010303"]]
                                                                                                      },
                                                                        f"020104Relation_With_Other_Conatact":{
                                                                                                        f"02010401__RelationType": [["Name","Relation"]],
                                                                                                        f"02010402__Datetime.now()": None,
                                                                                                        f"02010403__Number_Of_Time_Updated": None,
                                                                                                        f"0201040D__DumpYard": [["02010401","02010402","02010403"]]
                                                                                                        }
                                                                    },

                                             "0202__second_Reg_Name": None
                                            }}
                          
    #with open("CRM_Database.json","w") as push:
    #    json.dump(Database,push,indent=15)
    print(Database)


def Pusher_grid_0(value,Phone_Saved_Name_0101,Source_of_Collection,Updated_Office_Name_0102):

    window_pusher = tk.Tk()
    window_pusher.title("Publishing Name_Reg")
    tk.Label(window_pusher,text = value ,font='Bahnschrift 20 bold').grid(row=0,column=0,columnspan=2)

    tk.Label(window_pusher,text = "0101_Phone_Saved_Name", font='Bahnschrift 12 bold').grid(row=1,column=0)
    tk.Label(window_pusher,text= f": {Phone_Saved_Name_0101}",font='Bahnschrift 12 bold').grid(row=1,column=1)

    tk.Label(window_pusher,text = "010102_Source", font='Bahnschrift 12 bold').grid(row=2,column=0)
    tk.Label(window_pusher,text= f": {Source_of_Collection}",font='Bahnschrift 12 bold').grid(row=2,column=1)

    tk.Label(window_pusher,text = "010201_OfficeName", font='Bahnschrift 12 bold').grid(row=3,column=0)
    tk.Label(window_pusher,text= f": {Updated_Office_Name_0102}",font='Bahnschrift 12 bold').grid(row=3,column=1)

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


# ---------------------
window_01_01_01 = tk.Frame(window)

# Heading 01_1
Heading = tk.Label(window_01_01_01, text="Heading",font='Bahnschrift 20 bold', command=None)
Heading.grid(row=0,column=1,columnspan=2)    


# 02_01_Heading : Label
Old_Serial_Name = tk.StringVar(value=f"{value_inputed}_01_Old_Serial_Name")
Old_Serial_Name_010101 = tk.Label(window_01_01_01, text=Old_Serial_Name.get(),font='Bahnschrift 20 bold')
Old_Serial_Name_010101.grid(row=1,column=1,columnspan=2) 
# 02_02_Serial_No : Label
tk.Label(window_01_01_01, text="1 :",font='Bahnschrift 12 bold', command=None).grid(row=2,column=0)
# 02_03_Key : Label 
tk.Label(window_01_01_01, text = f"{value_inputed}_010101_Name",font='Bahnschrift 12 bold', command=None).grid(row=2,column=1)
# 02_04_Value : Entrys
Name_010101 = tk.StringVar(window_01_01_01)
tk.Entry(window_01_01_01, textvariable=Name_010101, font='Bahnschrift 12 bold').grid(row=2,column=2)  


# 03_01_Serial_No : Label
tk.Label(window_01_01_01, text="2 :",font='Bahnschrift 12 bold', command=None).grid(row=3,column=0)
# 03_02_Key : Label 
tk.Label(window_01_01_01, text = f"{value_inputed}_010102_Source" ,font='Bahnschrift 12 bold', command=None).grid(row=3,column=1)
# 03_03_Value : Entrys
Source_010102 = tk.StringVar(window_01_01_01,value="Not_selected")    
ttk.Combobox(window_01_01_01, textvariable=Source_010102, value = tuple(Set_of_Printing_Company.keys())).grid(row=3, column=2)


# 04_01_Serial_No : Label
tk.Label(window_01_01_01, text="3 :",font='Bahnschrift 12 bold', command=None).grid(row=4,column=0)
# 04_02_Key : Label 
tk.Label(window_01_01_01, text = f"{value_inputed}_01021_OfficeName", font='Bahnschrift 12 bold', command=None).grid(row=4,column=1)
# 04_03_Value : Entrys
OfficeName_01021 = tk.StringVar(window_01_01_01)
tk.Entry(window_01_01_01, textvariable=OfficeName_01021, font='Bahnschrift 12 bold').grid(row=4,column=2)    

# 05_01_Heading : Label
Old_Serial_Name_010101 = tk.Label(window_01_01_01, text="02_Owner_Names",font='Bahnschrift 20 bold').grid(row=5,column=1,columnspan=2) 

# 06_01_Serial_No : Label
tk.Label(window_01_01_01, text="4 :",font='Bahnschrift 12 bold', command=None).grid(row=6,column=0)
# 06_02_Key : Label 
tk.Label(window_01_01_01, text = f"{value_inputed}_0201__First_Reg_Name", font='Bahnschrift 12 bold', command=None).grid(row=6,column=1)
# 06_03_Value : Entrys
OfficeName_01021 = tk.StringVar(window_01_01_01)
tk.Entry(window_01_01_01, textvariable=OfficeName_01021, font='Bahnschrift 12 bold').grid(row=6,column=2)  

# 07_01_Serial_No : Label
tk.Label(window_01_01_01, text="5 :",font='Bahnschrift 12 bold', command=None).grid(row=7,column=0)
# 07_02_Key : Label 
tk.Label(window_01_01_01, text = f"{value_inputed}__02010201__Phone_1", font='Bahnschrift 12 bold', command=None).grid(row=7,column=1)
# 07_03_Value : Entrys
OfficeName_01021 = tk.StringVar(window_01_01_01)
tk.Entry(window_01_01_01, textvariable=OfficeName_01021, font='Bahnschrift 12 bold').grid(row=7,column=2)  
# Addable upto 8 numbers bez row given 8 lines
# 07_04_Value : Checkbox
tk.Checkbutton(window_01_01_01, text="More Than On Number", font='Bahnschrift 12 bold', command=None).grid(row=15,column=0, columnspan=3)

# 08_01_Serial_No : Label
tk.Label(window_01_01_01, text="6 :",font='Bahnschrift 12 bold', command=None).grid(row=16,column=0)
# 08_02_Key : Label 
tk.Label(window_01_01_01, text = f"{value_inputed}__020103__Position_In_Office", font='Bahnschrift 12 bold', command=None).grid(row=16,column=1)
# 08_03_Value : Entrys
OfficeName_01021 = tk.StringVar(window_01_01_01)
tk.Entry(window_01_01_01, textvariable=OfficeName_01021, font='Bahnschrift 12 bold').grid(row=16,column=2) 

# 09_01_Serial_No : Label
tk.Label(window_01_01_01, text="7 :",font='Bahnschrift 12 bold', command=None).grid(row=17,column=0)
# 09_02_Key : Label 
tk.Label(window_01_01_01, text = f"{value_inputed}__020103__Position_In_Office", font='Bahnschrift 12 bold', command=None).grid(row=17,column=1)
# 09_03_Value : Entrys
OfficeName_01021 = tk.StringVar(window_01_01_01)
tk.Entry(window_01_01_01, textvariable=OfficeName_01021, font='Bahnschrift 12 bold').grid(row=17,column=2) 

tk.Button(window_01_01_01, text="Pusher", font='Bahnschrift 12 bold', command=lambda:Pusher_grid_0(value_inputed,Name_010101.get(),Source_010102.get(),OfficeName_01021.get())).grid(row=50,column=1, columnspan=2)  

Disabler_1 = tk.Checkbutton(window, text= "Disabler", command=lambda : disabler_window_1_1_0(window_01_01_01,Heading))
Disabler_1.pack(anchor="ne",side="top")

window_01_01_01.pack()

#Extend Values
tk.Button(window, text="Destroy", command=lambda: window.destroy()).pack(side="bottom")
window.mainloop()