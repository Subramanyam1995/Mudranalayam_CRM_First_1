import tkinter as tk
from tkinter import ttk

value_inputed=1001

def disabler_window_1_1_0(value,lab):
    if lab["state"] == "normal" : 
        for i in value.winfo_children():
            i.configure(state="disable") 
    else: 
        for i in value.winfo_children():
            i.configure(state="normal") 

Set_of_Printing_Company = {
                            "Keshav": {
                                "Registed_date":None  
                            },
                            "BOP":{
                                "Registed_date":None
                            },
                            "Other":{

                            }
}



def First_Line(windows_link, value_inputed):
    window_01 = tk.Frame(window)

    Heading = tk.Label(window_01, text="Heading",font='Bahnschrift 20 bold', command=None)
    Heading.grid(row=0,column=1,columnspan=2)  

    window_01.pack()

def Second_Line(windows_link, value_inputed):
    
    window_02 = tk.Frame(windows_link)
    
    # 02_01_Heading : Label
    Old_Serial_Name = tk.StringVar(value=f"{value_inputed}_01_Old_Serial_Name")
    Old_Serial_Name_010101 = tk.Label(window_02, text=Old_Serial_Name.get(),font='Bahnschrift 20 bold')
    Old_Serial_Name_010101.grid(row=1,column=1,columnspan=2) 
    # 02_02_Serial_No : Label
    tk.Label(window_02, text="1.1 :",font='Bahnschrift 12 bold', command=None).grid(row=2,column=0)
    # 02_03_Key : Label 
    tk.Label(window_02, text = f"{value_inputed}_010101_Name",font='Bahnschrift 12 bold', command=None).grid(row=2,column=1)
    # 02_04_Value : Entrys
    Name_010101 = tk.StringVar(window_02)
    tk.Entry(window_02, textvariable=Name_010101, font='Bahnschrift 12 bold').grid(row=2,column=2)  
    
    window_02.pack()

def Thrid_Line(windows_link, value_inputed):
    
    window_03 = tk.Frame(windows_link)
    
    # 03_01_Serial_No : Label
    tk.Label(window_03, text="1.2 :",font='Bahnschrift 12 bold', command=None).grid(row=3,column=0)
    # 03_02_Key : Label 
    tk.Label(window_03, text = f"{value_inputed}_010102_Source" ,font='Bahnschrift 12 bold', command=None).grid(row=3,column=1)
    # 03_03_Value : Entrys
    Source_010102 = tk.StringVar(window_03,value="Not_selected")    
    ttk.Combobox(window_03, textvariable=Source_010102, value = tuple(Set_of_Printing_Company.keys())).grid(row=3, column=2)
    
    window_03.pack()

def Fourth_Line(windows_link, value_inputed):
    
    window_04 = tk.Frame(windows_link)
    
    # 04_01_Serial_No : Label
    tk.Label(window_04, text="1.3 :",font='Bahnschrift 12 bold', command=None).grid(row=4,column=0)
    # 04_02_Key : Label 
    tk.Label(window_04, text = f"{value_inputed}_01021_OfficeName", font='Bahnschrift 12 bold', command=None).grid(row=4,column=1)
    # 04_03_Value : Entrys
    OfficeName_01021 = tk.StringVar(window_04)
    tk.Entry(window_04, textvariable=OfficeName_01021, font='Bahnschrift 12 bold').grid(row=4,column=2)    
    
    window_04.pack()

def checker():
    pass




# Start_of_Tkinter_Map

window = tk.Tk()

# Heading 01_1
"""First_Line(window,value_inputed)
Second_Line(window,value_inputed)
Thrid_Line(window,value_inputed)
Fourth_Line(window,value_inputed)"""

tk.Label(window, text="Hello1").grid(row=1, column=0)
tk.Label(window, text="Hello2").grid(row=2, column=0)
tk.Label(window, text="Hello3").grid(row=3, column=0)

checkbox = tk.IntVar(window)

ttk.Checkbutton(
                window, 
                text="CheckBox",
                onvalue=1, 
                offvalue=0,
                variable=checkbox,
                #command = lambda: tk.Label(window, text="Number_1").grid(row=5+j, column=0) for j in range(10) if checkbox.get() == 1 else None,
                ).grid(row=4, column=0)


tk.Label(window, text="Hello4").grid(row=6, column=0)
tk.Label(window, text="Hello5").grid(row=7, column=0)





window.mainloop()