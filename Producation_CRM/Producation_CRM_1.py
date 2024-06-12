from Producation_CRM.Producation_CRM_3_Module_Imports import *
from Producation_CRM.Producation_CRM_2 import *

# Opening Page Funcations 1.0
Window = tk.Tk()

Window.geometry("400x600")



# Funcations 1.1 
def Producation_01_01_00_Sender():
    value = Entry_var_Customer_Data_Updater.get()
    if value.isnumeric():
        Producation_1_1_0(value)
    else: 
        tk.Label(window_01_01, text="Invaild_Input").pack()

        

# Tkinter File

# Opening Page Funcations 1.1 - Entering to DataBase
window_01_01 = tk.Frame(Window)
ttk.Label(window_01_01, text= "  ", font="Bahnschrift 12 bold").pack(pady=15)
ttk.Label(window_01_01, text= "Customer_Data_Updater", font="Bahnschrift 12 bold").pack(pady=5)
Entry_var_Customer_Data_Updater = tk.StringVar(window_01_01)
ttk.Entry(window_01_01, textvariable=Entry_var_Customer_Data_Updater, font="Bahnschrift 12 bold").pack()
tk.Button(window_01_01, text= "Click To Update", font="Bahnschrift 12 bold",command=Producation_01_01_00_Sender).pack(pady=5)
window_01_01.pack()


# Opening Page Funcations 1.2 - Entering to New_DataBase





Window.mainloop()