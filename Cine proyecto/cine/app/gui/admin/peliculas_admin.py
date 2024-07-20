import customtkinter as ctk
from app.utils.helpers import eliminar_paginas, volver_administrador
from app.controllers.pelicula_controllers import traer_peliculas, guardar_pelicula, eliminar_pelicula

def peliculas_admin(root):
    eliminar_paginas(root)

    peliculas = traer_peliculas()

    frame_header = ctk.CTkFrame(root, corner_radius=0, fg_color="#333333", height=50)
    frame_header.pack(fill="x", side="top")

    header_label = ctk.CTkLabel(frame_header, text="CINE W ADMIN Peliculas", text_color="white", font=("Helvetica", 20))
    header_label.pack(pady=10, padx=10, side="top", expand=True)

    frame_main = ctk.CTkScrollableFrame(root, corner_radius=0)
    frame_main.pack(fill="both", expand=True, pady=20, padx=20)

    encabezados = ["ID", "Nombre", "Sinopsis", "Imagen URL", "Duración", "Categoría"]
    for col, encabezado in enumerate(encabezados):
        header_frame = ctk.CTkFrame(frame_main, fg_color="#555555")
        header_frame.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")
        label = ctk.CTkLabel(header_frame, text=encabezado, text_color="white", font=("Helvetica", 12))
        label.pack(padx=5, pady=5, expand=True)

    for row, pelicula in enumerate(peliculas, start=1):
        for col, (key, value) in enumerate(pelicula.items()):
            cell_frame = ctk.CTkFrame(frame_main, fg_color="#444444")
            cell_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            if key == "sinopsis":
                label = ctk.CTkLabel(cell_frame, text=str(value), text_color="white", wraplength=800)
            else:
                label = ctk.CTkLabel(cell_frame, text=str(value), text_color="white")
            label.pack(padx=5, pady=5, expand=True)

    for col in range(len(encabezados)):
        frame_main.grid_columnconfigure(col, weight=1)
    for row in range(1, len(peliculas) + 1):
        frame_main.grid_rowconfigure(row, weight=1)

    # Añadir un espaciador para empujar los botones hacia arriba
    frame_spacer = ctk.CTkFrame(root, corner_radius=0, fg_color="#1E1E1E", height=30)
    frame_spacer.pack(fill=None, side="bottom", pady=10)

    frame_botones = ctk.CTkFrame(root, corner_radius=0, fg_color="#1E1E1E", height=50)
    frame_botones.pack(fill="both", side="bottom", pady=10, padx=20)

    # Añadir un frame interno alineado a la derecha
    frame_botones_interno = ctk.CTkFrame(frame_botones, fg_color="#333333")
    frame_botones_interno.pack(side="right")

    # Botones
    btn_volver = ctk.CTkButton(frame_botones_interno, text="Volver", font=("Helvetica", 12), command= lambda: volver_administrador(root))
    btn_volver.pack(side="right", padx=5, pady=5)

    btn_eliminar = ctk.CTkButton(frame_botones_interno, text="Eliminar", font=("Helvetica", 12), command=lambda: crear_ventana_eliminar_pelicula(root))
    btn_eliminar.pack(side="left", padx=5, pady=5)

    btn_anadir = ctk.CTkButton(frame_botones_interno, text="Añadir", font=("Helvetica", 12), command=lambda: crear_ventana_anadir_pelicula(root))
    btn_anadir.pack(side="left", padx=5, pady=5)

def crear_ventana_anadir_pelicula(parent):
    ventana = ctk.CTkToplevel(parent)
    ventana.title("Añadir Nueva Película")
    ventana.geometry("400x700")
    ventana.transient(parent) 
    ventana.grab_set() 

    label_info = ctk.CTkLabel(ventana, text="Ingrese los datos para crear una nueva película", text_color="white", font=("Helvetica", 14))
    label_info.pack(pady=10, padx=10)

    campos = ["ID", "Nombre", "Sinopsis", "Imagen URL", "Duración", "Categoría"]
    entries = {}

    for campo in campos:
        label = ctk.CTkLabel(ventana, text=campo, text_color="white", font=("Helvetica", 12))
        label.pack(pady=5, padx=10)
        entry = ctk.CTkEntry(ventana, width=300)
        entry.pack(pady=5, padx=10)
        entries[campo] = entry

    def guardar():
        datos = {campo: entries[campo].get() for campo in campos}
        if guardar_pelicula(datos):
            print("Película guardada exitosamente.")
        else:
            print("Error al guardar la película.")
        ventana.destroy()

    def cancelar():
        ventana.destroy()

    btn_guardar = ctk.CTkButton(ventana, text="Guardar", command=guardar)
    btn_guardar.pack(pady=10, padx=10, side="left", expand=True)

    btn_cancelar = ctk.CTkButton(ventana, text="Cancelar", command=cancelar)
    btn_cancelar.pack(pady=10, padx=10, side="right", expand=True)

def crear_ventana_eliminar_pelicula(parent):
    ventana = ctk.CTkToplevel(parent)
    ventana.title("Eliminar Película")
    ventana.geometry("400x200")
    ventana.transient(parent) 
    ventana.grab_set() 

    label_info = ctk.CTkLabel(ventana, text="Ingrese el ID de la película a eliminar", text_color="white", font=("Helvetica", 14))
    label_info.pack(pady=10, padx=10)

    entry_id = ctk.CTkEntry(ventana, width=300)
    entry_id.pack(pady=10, padx=10)

    def eliminar():
        pelicula_id = entry_id.get()
        if eliminar_pelicula(pelicula_id):
            print("Película eliminada exitosamente.")
        else:
            print("Error al eliminar la película.")
        ventana.destroy()

    def cancelar():
        ventana.destroy()

    btn_eliminar = ctk.CTkButton(ventana, text="Eliminar", command=eliminar)
    btn_eliminar.pack(pady=10, padx=10, side="left", expand=True)

    btn_cancelar = ctk.CTkButton(ventana, text="Cancelar", command=cancelar)
    btn_cancelar.pack(pady=10, padx=10, side="right", expand=True)

