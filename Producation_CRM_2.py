
from Producation_CRM_3_Module_Imports import *




# Funcation To All

def disabler_window_1_1_0(value,lab):
    if lab["state"] == "normal" : 
        for i in value.winfo_children():
            i.configure(state="disable") 
    else: 
        for i in value.winfo_children():
            i.configure(state="normal") 

def Pusher_grid_0():
    window_pusher = tk.Tk()
    tk.Label(window_pusher,text = "Heading",font='Bahnschrift 20 bold').pack()
    window_pusher.mainloop()


def grid_0():
    global value_inputed

    window_01_01_01 = tk.Frame(window_1_1_0)
    
    # Heading Name Stage_1//2
    Heading = tk.Label(window_01_01_01, text="Heading",font='Bahnschrift 20 bold', command=None)
    Heading.grid(row=0,column=0,columnspan=2)    
    
    
    # Stage 01_01
    # Key : Labels 
    
    Old_Serial_Name = tk.StringVar(value=f"{value_inputed}___01_Old_Serial_Name")
    Old_Serial_Name_010101 = tk.Label(window_01_01_01, text=Old_Serial_Name.get(),font='Bahnschrift 20 bold')
    Old_Serial_Name_010101.grid(row=1,column=0,columnspan=2) 

    Name = tk.StringVar(value=f"{value_inputed}___010101__Name")
    tk.Label(window_01_01_01, text= Name.get(),font='Bahnschrift 12 bold', command=None).grid(row=2,column=0)

    OfficeName = tk.StringVar(value=f"{value_inputed}___01021__OfficeName")
    tk.Label(window_01_01_01, text=OfficeName.get(),font='Bahnschrift 12 bold', command=None).grid(row=3,column=0)
    
    # Value : Entrys

    Name__010101 = tk.StringVar(window_01_01_01)
    tk.Entry(window_01_01_01, textvariable=Name__010101, font='Bahnschrift 12 bold').grid(row=2,column=1)  

    OfficeName__01021 = tk.StringVar(window_01_01_01)
    tk.Entry(window_01_01_01, textvariable=OfficeName__01021, font='Bahnschrift 12 bold').grid(row=3,column=1)    


    tk.Button(window_01_01_01, text="Pusher", font='Bahnschrift 12 bold', command=Pusher_grid_0).grid(row=7,columnspan=2,column=0)  
    
   
    Disabler_1 = tk.Checkbutton(window_1_1_0, text= "Disabler", command=lambda : disabler_window_1_1_0(window_01_01_01,Heading))
    Disabler_1.pack(anchor="ne",side="top")

    window_01_01_01.pack()

# Secific Funcation

# Producation Page 1.1.0

################def Producation_1_1_0(value_inputed):


DataBase = {}
value_inputed = 100
window_1_1_0 = tk.Tk()

window_1_1_0.geometry("500x700")
            
# Frame_window_01_01_01           
window_01_01_01 = tk.Frame(window_1_1_0,)

tk.Label(window_1_1_0, text=value_inputed,font='Bahnschrift 20 bold', command=None).pack()


grid_0()






tk.Button(window_1_1_0, text="Destroy", command=lambda: window_1_1_0.destroy()).pack(side="bottom")
window_1_1_0.mainloop()