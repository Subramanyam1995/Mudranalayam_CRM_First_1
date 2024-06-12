
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
                                                                                     },
                                       "02__{value_inputed}__Owner_Names":{ "0201__{value_inputed}__First_Reg_Name" : { "020101__{value_inputed}__name" :{
                                                                                                                                                            "02010101__Name": None,
                                                                                                                                                            "02010102__Datetime.now()": None,
                                                                                                                                                            "02010103__Number_Of_Time_Corrected": None,
                                                                                                                                                            "0201010D__DumpYard": [["02010101","02010102","02010103"]]
                                                                                                                                                        },
                                                                        "020102__PhoneNo's"           : {   "02010201__Phone_1":   
                                                                                                                                {
                                                                                                                                 "0201020101__Number1": None,
                                                                                                                                 "0201020102__Datetime.now()": None,
                                                                                                                                 "0201020103__Number_Of_Time_Corrected": None,
                                                                                                                                 "0201020104__if_invaild(True/False)":None,
                                                                                                                                 "020102010D__DumpYard": [["0201020101","0201020102","0201020103","0201020104"]]
                                                                                                                                },
                                                                                                            "02010202__Phone_2": None
                                                                                                        }
                                                                                                      ,
                                                                        "020103__Position_In_Office"  :{
                                                                                                        "02010301__Position": None,
                                                                                                        "02010302__Datetime.now()": None,
                                                                                                        "02010303__Number_Of_Time_Updated": None,
                                                                                                        "0201030D__DumpYard": [["02010301","02010302","02010303"]]
                                                                                                      },
                                                                        "020104Relation_With_Other_Conatact":{
                                                                                                        "02010401__RelationType": [["Name","Relation"]],
                                                                                                        "02010402__Datetime.now()": None,
                                                                                                        "02010403__Number_Of_Time_Updated": None,
                                                                                                        "0201040D__DumpYard": [["02010401","02010402","02010403"]]
                                                                                                        }
                                                                    },

                                             "0202__second_Reg_Name": None
                                            },
                          "03_Location"   :{
                                                "0301__Address_Mention_In_Visiting_Card":{              "030101__Address": None,
                                                                                                        "030102__Datetime.now()": None,
                                                                                                        "030103__Number_Of_Time_Upgraded": 0,
                                                                                                        "03010D__DumpYard": [["030101","030102","030103"]]
                                                                                        },
                                                "0302__District":                        {              "030201__District": None,
                                                                                                        "030202__Datetime.now()": None,
                                                                                                        "030203__Number_Of_Time_Corrected": 0,
                                                                                                        "030204__List_of_District":"Get_the_Link_from_Database",
                                                                                                        "03020D__DumpYard": [["030201","030202","030203"]]
                                                                                        },
                                                "0303__Taluks":                           {             "030301__Taluks": None,
                                                                                                        "030302__Datetime.now()": None,
                                                                                                        "030303__Number_Of_Time_Corrected": 0,
                                                                                                        "030304__List_of_Taluks":"Get_the_Link_from_Database",
                                                                                                        "03030D__DumpYard": [["030301","030302","030303"]]
                                                                                        },
                                                "0304__Other_Address_Below_Taluks":None,

                                                "0305__double_office": None
                                             },
                          "04_Visiting_Card_Pic":     {   "0401__Upload_1":        {"040101__Upload_link" : None,
                                                                                    "040102__Datetime.now()" : None,
                                                                                    "040103__Number_Of_Time_Corrected": 0,
                                                                                    "040104__if_invaild(True/False)":None,
                                                                                    "04010D__DumpYard": [["040101","040102","040103","040104"]]
                                                                                   },
                                                          "0402__Upload_2":          None
                                                        },
                          "05_Fraud":{ "0501__Fraud": None,
                                       "0502__Type_Of_Fraud":{  "050201__Fraud_Type": None,
                                                                "050302__Datetime.now()": None,
                                                                "050303__Number_Of_Time_Fruad": 0,
                                                                "050304__Explanation_Reason": None,
                                                                "050305__Proff_files_attachment":None,
                                                                "05030D__DumpYard": []
                                                              }
                                     },
                          "06_Personal_Data":{  "0601__Caste": None,
                                                "0602__Political_Party": None,
                                                "0603__OtherThing": None,
                                                "0604__Heavy_Drama":None
                                             },
                          "07_Sales_Report": {
                                              "0701Product": None
                            
                                               
                                             },
                          "08_Recording":       { "0801__Call_Rec"   :  {"080101__File_Link": [None]},
                                                  "0802__Video_Rec"  :  {"080101__File_Link": [None]}
                                                },
                          "09_Customer_Links":{ "0901__Update" : None,
                                                "0902__Friends_In_the_Industry": None,
                                                "0903__Refered_By":None,
                                                "0904__Hate_In_The_Industry":None,
                                                "0905__Don't_Ask_Thinks": None
                                              },
                          "10_Anydesk_Deatils":{"1001__Collection_1": {
                                                                        "100101__Anydesk_No": None,
                                                                        "100102__Datetime.now()":None,
                                                                        "100103__if_invaild(True/False)":None
                                                                      },
                                                "1002__Collection_2": None
                                                },
                          "11_FollowUps_Request":{
                                                  "1101__Floowup":["feild_to_follow"],
                                                  "1102__Datetime.Datetime.now()":None,
                                                  "110D__DumpYard": []
                                                 },
                          "12_Customer_Update_Required":[None],
                          "13_Gold_Mine":[None],
                          "14_Date_of_Database_Creation": "Datetime.Datetime.now()",
                          "15_Database_Deactiver" : { 
                                                      "1501__Deactive": false,
                                                      "1502__Deactive_Reason":None,
                                                      "1503__Datetime.Datetime.now()":None,
                                                      "150D__DumpYard": []
                                                    },
                          "16_Caution" :{     "1601__Caution" :{        "160101__Caution":None,
                                                                        "160102__Datetime.Datetime.now()":None,
                                                                        "160103__if_invaild(True/False)":None,
                                                                        "16010D__DumpYard": []
                                                               },
                                              "1602__Caution": None
                                        },
                          "17_Printing_Office_Known" :{"1701__Office_Name": {"170101Customer_From (datetime)": None,
                                                                             "170102__Datetime.Datetime.now()":None,
                                                                             "17010D__DumpYard": []
                                                                            },
                                                        "add":None
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


# ---------------------
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
tk.Label(window_01_01_01, textvariable=OfficeName, font='Bahnschrift 12 bold', command=None).grid(row=4,column=0)

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