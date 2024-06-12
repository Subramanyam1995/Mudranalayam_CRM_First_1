import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import datetime  
import time
import random
import json
import random


from Test__python2 import *

window = tk.Tk()

window.geometry("400x800")

ttk.Label(window, text="Personl Information Updater", font= "Bahnschrift 14 ").pack(pady=10)
Send_Value= tk.StringVar(window)
Value_To_Send = ttk.Entry(window, textvariable= Send_Value,width=10,font= "Bahnschrift 14 ").pack(pady=1)
ttk.Label(window, textvariable=Send_Value , font= "Bahnschrift 14 ").pack(pady=10)
ctk.CTkButton(window, text=" Click ME", command=lambda :Name_data_upload(Send_Value)).pack()

window.mainloop()

