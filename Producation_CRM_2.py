
from Producation_CRM_3_Module_Imports import *



# Producation Page 1.1.0

#def Producation_1_1_0(value):
window_1_1_0 = tk.Tk()

window_1_1_0.geometry("300x700")

def disabler():
    for i in window_01_01_01.winfo_children():
        i.configure(state="disable")

window_01_01_01 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_01, text="Old_Name",font='Bahnschrift 12 bold', command=None).pack()   
tk.Button(window_01_01_01, text="Old_Name", font='Bahnschrift 12 bold', command=None ).pack()
tk.Entry(window_01_01_01, textvariable="Old_Name", font='Bahnschrift 12 bold').pack()
tk.Button(window_01_01_01, text="Destry", command=lambda: window_1_1_0.destroy()).pack()

tk.Label(window_1_1_0,text="value").pack()

window_01_01_01.pack()

window_1_1_0.mainloop()