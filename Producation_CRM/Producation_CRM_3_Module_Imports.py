import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import datetime
import random
import os
import json
import time
from pprint import pprint

# Funcation To All

Set_of_Printing_Company = {
                            "Keshav": {"Registed_date":None
                                       
                                       },
                            "BOP":{"Registed_date":None},
                            

                            }

# Funcation To All

def disabler_window_1_1_0(value,lab):
    if lab["state"] == "normal" : 
        for i in value.winfo_children():
            i.configure(state="disable") 
    else: 
        for i in value.winfo_children():
            i.configure(state="normal") 



