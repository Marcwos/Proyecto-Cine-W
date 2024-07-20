import customtkinter as ctk
from PIL import Image
from app.utils.helpers import eliminar_paginas, ir_a_peliculas_admin, ir_a_salas_admin, volver_login
from app.controllers.pelicula_controllers import crear_horario

def interfaz_admin(root):
    eliminar_paginas(root)

    frame_header = ctk.CTkFrame(root, corner_radius=0, fg_color="#333333", height=50)
    frame_header.pack(fill="x", side="top")

    btn_logout = ctk.CTkButton(frame_header, text="Logout", font=("Helvetica", 12), command=lambda: volver_login(root))
    btn_logout.pack(side="left", padx=10, pady=10)
    
    header_label = ctk.CTkLabel(frame_header, text="CINE W ADMIN", text_color="white", font=("Helvetica", 20))
    header_label.pack(pady=10, padx=10, side="top")

    frame_main = ctk.CTkFrame(root, corner_radius=0)
    frame_main.pack(fill="both", expand=True, pady=20, padx=20)

    img_peliculas = ctk.CTkImage(Image.open("cine/app/images/logo_peliculas.jpg"), size=(400,400))
    img_salas = ctk.CTkImage(Image.open("cine/app/images/logo_salas.jpg"), size=(400,400))
    img_horarios = ctk.CTkImage(Image.open("cine/app/images/logo_horarios.jpg"), size=(400,400))

    frame_buttons = ctk.CTkFrame(frame_main)
    frame_buttons.pack(pady=20, padx=20, fill="both", expand=True)

    frame_buttons.grid_rowconfigure(0, weight=1)
    frame_buttons.grid_columnconfigure(0, weight=1)
    frame_buttons.grid_columnconfigure(1, weight=1)
    frame_buttons.grid_columnconfigure(2, weight=1)

    button_peliculas = ctk.CTkButton(frame_buttons, image=img_peliculas, text="", command=lambda: ir_a_peliculas_admin(root) )
    button_peliculas.grid(row=0, column=0, padx=5, pady=20)
    
    label_peliculas = ctk.CTkLabel(frame_buttons, text="Películas")
    label_peliculas.grid(row=1, column=0, padx=20, pady=10)

    button_salas = ctk.CTkButton(frame_buttons, image=img_salas, text="", command=lambda: ir_a_salas_admin(root))
    button_salas.grid(row=0, column=1, padx=5, pady=20)
    
    label_salas = ctk.CTkLabel(frame_buttons, text="Salas")
    label_salas.grid(row=1, column=1, padx=20, pady=10)

    button_horarios = ctk.CTkButton(frame_buttons, image=img_horarios, text="", command=lambda: crear_ventana_anadir_horario(root))
    button_horarios.grid(row=0, column=2, padx=20, pady=20)
    
    label_horarios = ctk.CTkLabel(frame_buttons, text="Horarios")
    label_horarios.grid(row=1, column=2, padx=5, pady=10)

def crear_ventana_anadir_horario(parent):
    ventana = ctk.CTkToplevel(parent)
    ventana.title("Añadir Nuevo Horario")
    ventana.geometry("400x400")
    ventana.transient(parent) 
    ventana.grab_set() 

    label_info = ctk.CTkLabel(ventana, text="Ingrese los datos para crear un nuevo horario", text_color="white", font=("Helvetica", 14))
    label_info.pack(pady=10, padx=10)

    campos = ["ID Película", "ID Sala", "Horario"]
    entries = {}

    for campo in campos:
        label = ctk.CTkLabel(ventana, text=campo, text_color="white", font=("Helvetica", 12))
        label.pack(pady=5, padx=10)
        entry = ctk.CTkEntry(ventana, width=300)
        entry.pack(pady=5, padx=10)
        entries[campo] = entry

    def guardar():
        datos = {campo: entries[campo].get() for campo in campos}
        if crear_horario(datos['ID Película'], datos['ID Sala'], datos['Horario']):
            print("Horario guardado exitosamente.")
        else:
            print("Error al guardar el horario.")
        ventana.destroy()

    def cancelar():
        ventana.destroy()

    btn_guardar = ctk.CTkButton(ventana, text="Guardar", command=guardar)
    btn_guardar.pack(pady=10, padx=10, side="left", expand=True)

    btn_cancelar = ctk.CTkButton(ventana, text="Cancelar", command=cancelar)
    btn_cancelar.pack(pady=10, padx=10, side="right", expand=True)
