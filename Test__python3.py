
import json
import pprint
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pprint

data_filds = {"01AAAAA":{ "01_Old_Name":      {
                                                 "0101__Old_Reg_Name"        : { "010101__Name"   :  "dileep printer",
                                                                                 "01012__Source"  : None
                                                                             },
                                                 "0102__Updated_Office_Name" : {
                                                                                "01021__OfficeName": None,
                                                                                "01022__Datetime.now()":None,
                                                                                "01023__Number_Of_Time_Corrected":None,
                                                                                "01029__DumpYard": []


                                                                         },
                                              },

                          "02_Owner_Names":{ "0201First_Reg_Name" : { "020101__name"                 :{ "02010101__Name": None,
                                                                                                        "02010102__Datetime.now()": None,
                                                                                                        "02010103__Number_Of_Time_Corrected": 0,
                                                                                                        "02010109__DumpYard": []
                                                                                                      },
                                                                  "020102__PhoneNo's"                 :{
                                                                                                        "02010201__Number1": None,
                                                                                                        "02010202__Datetime.now()": None,
                                                                                                        "02010203__Number_Of_Time_Corrected": None,
                                                                                                        "02010209__DumpYard": []
                                                                                                      },
                                                                  "020103__Position_In_Office"        :{
                                                                                                        "02010301__Position": None,
                                                                                                        "02010302__Datetime.now()": None,
                                                                                                        "02010303__Number_Of_Time_Updated": None,
                                                                                                        "02010309__DumpYard": []
                                                                                                      },
                                                                  "Relation_With_Other_Conatact":[[None],[]]
                                                                },
                                             "second_Reg_Name": None,                                   
                                            },
                          "03_Location"   :  {
                                                "0301__Address_Mention_In_Visiting_Card":{              "030101__Address": None,
                                                                                                        "030102__Datetime.now()": None,
                                                                                                        "030103__Number_Of_Time_Corrected": 0,
                                                                                                        "030109__DumpYard": []
                                                                                        },
                                                "0302__District":                        {              "030201__District": None,
                                                                                                        "030202__Datetime.now()": None,
                                                                                                        "030203__Number_Of_Time_Corrected": 0,
                                                                                                        "030209__DumpYard": []
                                                                                        },
                                                "0303__Taluks":                           {             "030301__Taluks": None,
                                                                                                        "030302__Datetime.now()": None,
                                                                                                        "030303__Number_Of_Time_Corrected": 0,
                                                                                                        "030309__DumpYard": []
                                                                                        },
                                                "0304__Other_Address_Below_Taluks":None
                                             },
                          "04_Visiting_Card_Pic":     {   "0401__Upload_1":        {"040101__Address" : None,
                                                                                    "040102__Datetime.now()" : None,
                                                                                    "040103__Number_Of_Time_Corrected": 0,
                                                                                    "040109__DumpYard": []
                                                                                   },
                                                          "0402__Upload_2":          None
                                                        },
                          "05_Fraud":{ "0501__Fraud": None, # True or False
                                     "0502__Type_Of_Fraud":{    "050201__Fraud_Type": None,
                                                                "030302__Datetime.now()": None,
                                                                "030303__Number_Of_Time_Fruad": 0,
                                                                "030304__Explanation_Reason": None,
                                                                "030305__Attachment":None,
                                                                "030309__DumpYard": []
                                                           }
                                     },
                          "06_Personal_Data":{  "Caste": None,
                                                "Political_Party": None,
                                                "OtherThing": None
                                            },
                          "07_Sales_Report":{

                                                },
                          "08_Recording":       { "Call_Rec"   :  {"File_Link": None},
                                                  "Video_Rec"  :  {"File_Link":None}
                                                },
                          "09_Customer_Links":{ "Update" : None,
                                                "Friends_In_the_Industry": None,
                                                "Refered_By":None,
                                                "Hate_In_The_Industry":None,
                                                "Don't_Ask_Thinks": None
                                              },
                          "10_Anydesk_Deatils":{"Collection_1": {
                                                                 "Anydesk_No": None,
                                                                 "Datetime.now()":None,
                                                                 },
                                                "Collection_2": {"Anydesk_No": None,
                                                                 "Datetime.now()":None
                                                                 }
                                                },
                          "11_FollowUps":None,
                          "12_Customer_Update_Required":None,
                          "13_Gold_Mine":None,


                        
                        },
              
              }





def printing(var01_name):
    print(var01_name.get())


def Name_data_upload():

    window = tk.Tk()

    window.geometry("300x800")

    ttk.Label(window, text="Name Registry",font="Bahnschrift 24 bold", ).pack(pady=30)


    # Name
    ttk.Label(window, text= "Name Of The Client",font="Bahnschrift 14").pack()
    var01_name = tk.StringVar(window)
    ttk.Entry(window, textvariable=var01_name,width=40).pack()
    ttk.Label(window, textvariable=var01_name, font="Bahnschrift 12").pack()

    ttk.Button(window, text=" Click ME", command= lambda : printing(var01_name)).pack()

    window.mainloop()

window = tk.Tk()

window.geometry("300x800")

ttk.Button(window, text=" Click ME", command=Name_data_upload).pack()

window.mainloop()