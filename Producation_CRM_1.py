from Producation_CRM_3_Module_Imports import *
from Producation_CRM_2 import *

# Opening Page Funcations 1.0
Window = tk.Tk()

Window.geometry("400x600")

# Opening Page Funcations 1.1
# Funcations 1.1
def Producation_1_1_0_Sender():
    value = Entry_var_Customer_Data_Updater.get()
    if value.isnumeric():
        Producation_1_1_0(value)
    else: 
        tk.Label(window_1_1, text="Invaild_Input").pack()
        

# Tkinter File
window_1_1 = tk.Frame(Window)
ttk.Label(window_1_1, text= "  ", font="Bahnschrift 12 bold").pack(pady=15)
ttk.Label(window_1_1, text= "Customer_Data_Updater", font="Bahnschrift 12 bold").pack(pady=5)
Entry_var_Customer_Data_Updater = tk.StringVar(window_1_1)
ttk.Entry(window_1_1, textvariable=Entry_var_Customer_Data_Updater, font="Bahnschrift 12 bold").pack()
tk.Button(window_1_1, text= "Click To Update", font="Bahnschrift 12 bold",command=Producation_1_1_0_Sender).pack(pady=5)
window_1_1.pack()



Window.mainloop()