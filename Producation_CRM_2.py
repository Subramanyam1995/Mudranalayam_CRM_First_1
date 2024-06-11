
from Producation_CRM_3_Module_Imports import *




# Funcation To All

def disabler_window_1_1_0(value,lab):
    if lab["state"]=="normal" : 
        for i in value.winfo_children():
            i.configure(state="disable") 
    else: 
        for i in value.winfo_children():
            i.configure(state="normal") 

def grid_0():
    window_01_01_01 = tk.Frame(window_1_1_0)
    global value_inputed
    # Heading Name Stage_1//2
    Heading = tk.Label(window_01_01_01, text="Heading",font='Bahnschrift 20 bold', command=None)
    Heading.grid(row=0,column=0,columnspan=2)    
    # Stage 01_01
    # Key  Labels 
    #DataBase["01_Old_Name"] = str(value_inputed)

    Old_Serial_Name = tk.StringVar(value=f"{value_inputed}01_Old_Serial_Name")
    tk.Label(window_01_01_01, text=Old_Serial_Name,font='Bahnschrift 20 bold', command=None).grid(row=1,column=0,columnspan=2) 

    Name = tk.StringVar(value=f"{value_inputed}___010101__Name")
    tk.Label(window_01_01_01, text= Name,font='Bahnschrift 12 bold', command=None).grid(row=2,column=0)

    OfficeName = tk.StringVar(value=f"{value_inputed}___01021__OfficeName")
    tk.Label(window_01_01_01, text=OfficeName,font='Bahnschrift 12 bold', command=None).grid(row=3,column=0)

    Name__010101 = tk.StringVar(window_01_01_01)
    tk.Entry(window_01_01_01, textvariable=Name__010101, font='Bahnschrift 12 bold').grid(row=2,column=1)  

    OfficeName__01021 = tk.StringVar(window_01_01_01)
    tk.Entry(window_01_01_01, textvariable=OfficeName__01021, font='Bahnschrift 12 bold').grid(row=3,column=1)    


    tk.Button(window_01_01_01, text="Old_Name", font='Bahnschrift 12 bold', command=None).grid(row=7,column=0)  





    # Value Entrys


    #tk.Label(window_01_01_01, text="Old_Name",font='Bahnschrift 12 bold', command=None).grid(row=2,column=0)
    #tk.Button(window_01_01_01, text="Old_Name", font='Bahnschrift 12 bold', command=None ).grid(row=3,column=0)  
    #tk.Entry(window_01_01_01, textvariable=None, font='Bahnschrift 12 bold').grid(row=2,column=1)  
    
    Disabler_1 = tk.Checkbutton(window_1_1_0, text= "Disabler", command=lambda : disabler_window_1_1_0(window_01_01_01,Heading))
    Disabler_1.pack(anchor="ne",side="top")

    window_01_01_01.pack()

# Secific Funcation

# Producation Page 1.1.0

################def Producation_1_1_0(value_inputed):


DataBase = {}
value_inputed = 100
window_1_1_0 = tk.Tk()

#window_1_1_0.geometry("300x700")
            
# Frame_window_01_01_01           
window_01_01_01 = tk.Frame(window_1_1_0,)

tk.Label(window_1_1_0, text=value_inputed,font='Bahnschrift 20 bold', command=None).pack(anchor="nw",side="left")


grid_0()






tk.Button(window_1_1_0, text="Destroy", command=lambda: window_1_1_0.destroy()).pack(side="bottom")
window_1_1_0.mainloop()