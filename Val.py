import customtkinter 
import hashlib
import os
import platform
import sys
import time
from datetime import datetime
from time import sleep
from keyauth import api

base = customtkinter.CTk()

base.geometry("380x240")
base.title("Nexus Login")
base.resizable(False, False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
Attempt = "Key"

def loginClick():
    global Attempt
    key = entry.get()
    try:
        if keyauthapp.license(key):
            main = customtkinter.CTkToplevel(base)
            main.title("Nexus")
            main.geometry("700x300")
            main.resizable(False, False)
        else:
            entry.placeholder_text = "Invalid"
            Attempt = "Invalid"
    except Exception as e:
        print("Error:", e)

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(__file__, "rb")  # Using __file__ to get the current file path
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

try:
    # Initialize KeyAuth
    keyauthapp = api(
        name="",
        ownerid="",
        secret="",
        version="",
        hash_to_check=getchecksum()
    )
except Exception as e:
    print("Error initializing KeyAuth:", e)

frame = customtkinter.CTkFrame(master=base)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login", font=("Impact", 24))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text=Attempt)
entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=loginClick)
button.pack(pady=12, padx=10)

base.mainloop()
