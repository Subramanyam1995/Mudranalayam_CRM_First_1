
from Producation_CRM.Producation_CRM_3_Module_Imports import *
from Producation_CRM_2_SideFiles.Grid_0 import grid_0



# Funcation To All

def disabler_window_1_1_0(value,lab):
    if lab["state"] == "normal" : 
        for i in value.winfo_children():
            i.configure(state="disable") 
    else: 
        for i in value.winfo_children():
            i.configure(state="normal") 


# Secific Funcation

# Producation Page 1.1.0

def Producation_1_1_0(value_inputed):

    window_1_1_0 = tk.Tk()

    window_1_1_0.geometry("500x700")
                
    # Frame_window_01_01_01           
    window_01_01_01 = tk.Frame(window_1_1_0,)

    tk.Label(window_1_1_0, text=value_inputed,font='Bahnschrift 20 bold', command=None).pack()

    grid_0(window_1_1_0,value_inputed)

    tk.Button(window_1_1_0, text="Destroy", command=lambda: window_1_1_0.destroy()).pack(side="bottom")
    window_1_1_0.mainloop()