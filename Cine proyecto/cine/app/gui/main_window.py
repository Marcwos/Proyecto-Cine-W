import customtkinter as ctk
from app.gui.login import create_login

def MainWindow():
    root = ctk.CTk()
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')
    root.geometry("800x600")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    create_login(root)
    
    return root