import customtkinter as ctk
from app.gui.cartelera import cartelera_movies
from app.gui.admin.administrador import interfaz_admin
from app.controllers.pelicula_controllers import obtener_usuario
import bcrypt

def create_login(root):
    print("...Login")
    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Bienvenido a CINE W")
    label.pack(pady=12, padx=10)

    entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)

    entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    button_login = ctk.CTkButton(master=frame, text="Login", command=lambda: authenticate_user(entry1.get(), entry2.get(), root))
    button_login.pack(pady=12, padx=10)

def authenticate_user(username, password, root):
    user_record = obtener_usuario(username)
    if user_record and bcrypt.checkpw(password.encode('utf-8'), user_record[0].encode('utf-8')):
        role = user_record[1]
        if role == "admin":
            open_admin_dashboard(root)
        else:
            cartelera_movies(root)
    else:
        print("Credenciales inválidas")

def open_admin_dashboard(root):
    interfaz_admin(root)