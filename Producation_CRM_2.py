
from Producation_CRM_3_Module_Imports import *



# Producation Page 1.1.0

#def Producation_1_1_0(value):
window_1_1_0 = tk.Tk()

window_1_1_0.geometry("300x700")
disabler_count=0
def disabler():
    global disabler_count
    
    if disabler_count == 0:
        for i in window_01_01_01.winfo_children():
            i.configure(state="disable")
        disabler_count=1
    else: 
        if disabler_count == 1:
            for i in window_01_01_01.winfo_children():
                    i.configure(state="normal")
            disabler_count=0
tk.Button(window_1_1_0, text="Distabler", command=disabler).pack()
window_01_01_01 = tk.Frame(window_1_1_0)
tk.Label(window_01_01_01, text="Old_Name",font='Bahnschrift 12 bold', command=None).pack()   
tk.Button(window_01_01_01, text="Old_Name", font='Bahnschrift 12 bold', command=None ).pack()
tk.Entry(window_01_01_01, textvariable="Old_Name", font='Bahnschrift 12 bold').pack()
tk.Button(window_01_01_01, text="Destry", command=lambda: window_1_1_0.destroy()).pack()

tk.Label(window_1_1_0,text="value").pack()

window_01_01_01.pack()

window_1_1_0.mainloop()