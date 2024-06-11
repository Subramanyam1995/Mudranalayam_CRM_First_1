
from Producation_CRM_3_Module_Imports import *




# Funcation To All

def disabler_window_1_1_0(value,lab):
    if lab["state"]=="normal" : 
        for i in value.winfo_children():
            i.configure(state="disable") 
    else: 
        for i in value.winfo_children():
            i.configure(state="normal") 

# Secific Funcation

# Producation Page 1.1.0

def Producation_1_1_0(value_inputed):

#    with open("Data_Base_0.json","r") as dat:
 #       DataBase = json.loads(dat)

    window_1_1_0 = tk.Tk()

    window_1_1_0.geometry("300x700")
                
    # Frame_window_01_01_01           
    window_01_01_01 = tk.Frame(window_1_1_0,)
    
    tk.Label(window_1_1_0, text=value_inputed,font='Bahnschrift 20 bold', command=None)  .pack(anchor="nw",side="left")
    tk.Checkbutton(window_1_1_0,text= "Disabler",command=lambda : disabler_window_1_1_0(window_01_01_01,lab)).pack(anchor="ne",side="top")
    
    # Key Values 
    window_01_01_01_01 = tk.Frame(window_01_01_01,highlightbackground="blue", highlightthickness=1, width=600, height=100, bd=0)#

    #DataBase["01_Old_Name"] = str(value_inputed)

    tk.Button(window_01_01_01_01, text="Old_Name", font='Bahnschrift 12 bold', command=None).pack()
    window_01_01_01 = tk.Frame(window_1_1_0)
    tk.Label(window_01_01_01_01, text="Old_Name",font='Bahnschrift 12 bold', command=None).pack()      
    tk.Entry(window_01_01_01_01, variable=None, font='Bahnschrift 12 bold').pack()


    window_01_01_01_01.pack()
 
    # Entry Values
    window_01_01_01_02 = tk.Frame(window_01_01_01)



    window_01_01_01_02.pack()
 

    lab = tk.Label(window_01_01_01, text="Old_Name",font='Bahnschrift 12 bold', command=None)  
    lab.pack() 
    tk.Button(window_01_01_01, text="Old_Name", font='Bahnschrift 12 bold', command=None ).pack()
    tk.Entry(window_01_01_01, textvariable=None, font='Bahnschrift 12 bold').pack()
    tk.Button(window_01_01_01, text="Destry", command=lambda: window_1_1_0.destroy()).pack()

    tk.Label(window_1_1_0,text="value").pack()
    
    window_01_01_01.pack()
    
    window_1_1_0.mainloop()