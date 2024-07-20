import customtkinter as ctk
from app.utils.helpers import eliminar_paginas, cargar_imagen, volver_login
from app.controllers.pelicula_controllers import traer_peliculas, traer_horarios
from app.gui.entradas_peliculas import entradas_movies

def cartelera_movies(root):
    eliminar_paginas(root)
    print("...Cartelera")

    frame_header = ctk.CTkFrame(root, corner_radius=0, fg_color="#333333", height=50)
    frame_header.pack(fill="x", side="top")

    btn_logout = ctk.CTkButton(frame_header, text="Logout", font=("Helvetica", 12), command=lambda: volver_login(root))
    btn_logout.pack(side="left", padx=10, pady=10)
    
    header_label = ctk.CTkLabel(frame_header, text="Cartelera", text_color="white", font=("Helvetica", 20))
    header_label.pack(pady=10, padx=10, side="top")
    
    frame_cartelera = ctk.CTkScrollableFrame(master=root)
    frame_cartelera.pack(pady="25", fill="both", expand=True)

    ancho_imagen, alto_imagen = 253, 363
    num_columnas = 6

    peliculas = traer_peliculas()
    for i, pelicula in enumerate(peliculas):
        fila = i // num_columnas + 1
        columna = i % num_columnas

        ruta_imagen = pelicula['imagen_url']
        nombre_pelicula = pelicula['nombre']
        pelicula_id = pelicula['id']

        ruta_imagen = ruta_imagen.replace("\\", "/")

        imagen = cargar_imagen(ruta_imagen, (ancho_imagen, alto_imagen))

        if imagen:
            frame = ctk.CTkFrame(frame_cartelera)
            frame.grid(row=fila, column=columna, padx=20, pady=(30, 20))

            boton = ctk.CTkButton(frame, border_color="#264747", hover_color="#153448", fg_color="#2E3329", image=imagen, text="", 
                                    command=lambda ruta=ruta_imagen, pel=pelicula: entradas_movies(root, pel, ruta))
            boton.grid(row=0, column=0)

            label_nombre = ctk.CTkLabel(frame, text=nombre_pelicula, font=("Helvetica", 12))
            label_nombre.grid(row=1, column=0, pady=(5, 0))
            
            frame_horarios = ctk.CTkFrame(frame)
            frame_horarios.grid(row=2, column=0, pady=(5, 0))
            
            horarios = traer_horarios(pelicula_id)
            for j, (horario_id, horario, sala_id) in enumerate(horarios):
                horario_str = horario.strftime("%H:%M")
                label_horario = ctk.CTkLabel(frame_horarios, text=horario_str, font=("Helvetica", 11), fg_color="#405D72", corner_radius=5, width=60, height=25)
                label_horario.grid(row=0, column=j, padx=5)          
        else:
            label = ctk.CTkLabel(frame_cartelera, text="Error al cargar imagen")
            label.grid(row=fila, column=columna, padx=15, pady=15)
