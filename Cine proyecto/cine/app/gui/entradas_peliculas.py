import customtkinter as ctk
from app.utils.helpers import eliminar_paginas, cargar_imagen, incrementar_valor, decrementar_valor, ir_a_asientos, volver_a_cartelera, mostrar_mensaje
from app.controllers.pelicula_controllers import traer_horarios

def entradas_movies(root, pelicula, ruta):
    eliminar_paginas(root)

    print(f"Entrando a... {pelicula['nombre']}")

    frame_principal = ctk.CTkFrame(master=root)
    frame_principal.pack(pady=20, padx=60, fill="both", expand=True)

    frame_volver = ctk.CTkFrame(master=frame_principal)
    frame_volver.pack(side=None, anchor="nw")

    boton_volver = ctk.CTkButton(master=frame_volver, text="Volver", command=lambda: volver_a_cartelera(root))
    boton_volver.pack(side="left", anchor="nw", padx=10, pady=10)

    imagen = cargar_imagen(ruta, (600, 800))

    frame_imagen = ctk.CTkFrame(master=frame_principal)
    frame_imagen.pack(pady=10, padx=50, side="left")

    label_imagen = ctk.CTkLabel(frame_imagen, image=imagen, text="")
    label_imagen.pack(pady=10, padx=10)

    frame_info_peli = ctk.CTkFrame(master=frame_principal)
    frame_info_peli.pack(pady=40, padx=60, fill="both", expand=True)

    nombre = ctk.CTkLabel(frame_info_peli, text=pelicula['nombre'], font=("Helvetica", 34))
    nombre.pack(side="top", pady=15)

    frame_sinopsis = ctk.CTkFrame(frame_info_peli)
    frame_sinopsis.pack(pady=40, padx=10, fill=None)

    sinopsis = ctk.CTkLabel(frame_sinopsis, text=pelicula['sinopsis'], font=("Helvetica", 24), wraplength=500, justify="left")
    sinopsis.pack(side="left", pady=10, padx=5)

    frame_horarios = ctk.CTkFrame(frame_info_peli)
    frame_horarios.pack(pady=10, padx=10)

    horario_seleccionado = ctk.StringVar(value="")
    horario_id_mapeo = {}

    horarios = traer_horarios(pelicula['id'])

    print(horarios)

    for j, (horario_id, horario, sala_id) in enumerate(horarios):
        horario_str = horario.strftime("%H:%M")
        horario_id_mapeo[horario_str] = (horario_id, sala_id)
        radio_horario = ctk.CTkRadioButton(frame_horarios, text=horario_str, variable=horario_seleccionado, 
                                            value=horario_str, font=("Helvetica", 14), hover_color="#405D72", corner_radius=5, width=60, height=25)
        radio_horario.grid(row=0, column=j, padx=5)

    frame_boletos = ctk.CTkFrame(master=frame_info_peli)
    frame_boletos.pack(pady=10, padx=10, fill=None)

    def actualizar_precio():
        try:
            cantidad = int(entry.get())
            precio_total = cantidad * precio_entrada
            label_precio.configure(text=f" x   ${precio_total:.2f}", font=("Helvetica", 17))
        except ValueError:
            label_precio.configure(text=" x   $0.00", font=("Helvetica", 17))

    def increment():
        current_value = entry.get()
        new_value = incrementar_valor(current_value, step=1, max_value=to_value)
        entry.delete(0, ctk.END)
        entry.insert(0, str(new_value))
        actualizar_precio()

    def decrement():
        current_value = entry.get()
        new_value = decrementar_valor(current_value, step=1, min_value=from_value)
        entry.delete(0, ctk.END)
        entry.insert(0, str(new_value))
        actualizar_precio()

    from_value = 0
    to_value = 10
    precio_entrada = 5.75

    label_boletos = ctk.CTkLabel(frame_boletos, text="Boletos:", font=("Helvetica", 17))
    entry = ctk.CTkEntry(frame_boletos, width=50)
    entry.insert(0, str(from_value))

    increment_button = ctk.CTkButton(frame_boletos, text="+", command=increment, width=30, height=30)
    decrement_button = ctk.CTkButton(frame_boletos, text="-", command=decrement, width=30, height=30)
    label_precio = ctk.CTkLabel(frame_boletos, text=" x   $0.00", font=("Helvetica", 17))

    label_boletos.grid(row=0, column=0, padx=5)
    decrement_button.grid(row=0, column=1)
    entry.grid(row=0, column=2, padx=5)
    increment_button.grid(row=0, column=3)
    label_precio.grid(row=0, column=4, padx=5)

    frame_continuar = ctk.CTkFrame(master=frame_info_peli)
    frame_continuar.pack(side="right", pady=20, padx=10, anchor="sw")

    def validar_seleccion():
        if not horario_seleccionado.get():
            mostrar_mensaje("Error", "Por favor, seleccione un horario.", root)
            return False
        try:
            cantidad_boletos = int(entry.get())
            if cantidad_boletos <= 0:
                mostrar_mensaje("Error", "Por favor, seleccione al menos un boleto.", root)
                return False
        except ValueError:
            mostrar_mensaje("Error", "Por favor, ingrese un número válido de boletos.", root)
            return False
        return True

    def continuar():
        if validar_seleccion():
            cantidad_boletos = int(entry.get())
            horario_id, sala_id = horario_id_mapeo[horario_seleccionado.get()]
            ir_a_asientos(root, pelicula, ruta, horario_id, sala_id, cantidad_boletos)

    boton_continuar = ctk.CTkButton(master=frame_continuar, text="Continuar", command=continuar)
    boton_continuar.pack()


