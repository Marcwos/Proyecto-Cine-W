import customtkinter as ctk
from app.utils.helpers import eliminar_paginas, volver_a_entradas, cargar_imagen, COLORES_ASIENTOS, mostrar_mensaje, toggle_asiento_color
from app.controllers.pelicula_controllers import traer_sala
from app.controllers.reserva_controllers import obtener_asientos_reservados, guardar_reserva

def mostrar_asientos(root, pelicula, ruta, horario_id, sala_id, cantidad_boletos):
    eliminar_paginas(root)
    print(horario_id, "sala ", sala_id, " boletos ", cantidad_boletos)
    
    frame_principal = ctk.CTkFrame(master=root)
    frame_principal.pack(pady=20, padx=40, fill="both", expand=True)

    frame_izquierdo = ctk.CTkFrame(master=frame_principal)
    frame_izquierdo.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    frame_derecho = ctk.CTkFrame(master=frame_principal)
    frame_derecho.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    frame_principal.columnconfigure(0, weight=2)
    frame_principal.columnconfigure(1, weight=1)

    frame_volver = ctk.CTkFrame(master=frame_principal)
    frame_volver.pack(anchor="nw", padx=10, pady=10)

    boton_volver = ctk.CTkButton(master=frame_volver, text="Volver", command=lambda: volver_a_entradas(root, pelicula, ruta))
    boton_volver.pack()

    imagen = cargar_imagen(ruta, (280, 400))

    frame_imagen = ctk.CTkFrame(master=frame_derecho)
    frame_imagen.pack(pady=15, padx=30, anchor="nw")

    nombre = ctk.CTkLabel(frame_imagen, text=pelicula['nombre'], font=("Helvetica", 20))
    nombre.pack(side="top", pady=5)

    label_imagen = ctk.CTkLabel(frame_imagen, image=imagen, text="")
    label_imagen.pack(pady=10, padx=10)

    frame_colores = ctk.CTkFrame(master=frame_izquierdo)
    frame_colores.pack(padx=10, pady=10, fill="both")

    frame_colores.grid_columnconfigure(0, weight=1)
    frame_colores.grid_columnconfigure(1, weight=1)

    colores = [
        ("Disponible", COLORES_ASIENTOS["disponible"]),
        ("Reservado", COLORES_ASIENTOS["reservado"]),
        ("Tu asiento", COLORES_ASIENTOS["tu_asiento"]),
        ("Recomendado", COLORES_ASIENTOS["recomendado"])
    ]

    for i, (texto, color) in enumerate(colores):
        fila = i // 2
        columna = i % 2

        frame_color = ctk.CTkFrame(master=frame_colores)
        frame_color.grid(row=fila, column=columna, padx=10, pady=10)

        borde = ctk.CTkFrame(master=frame_color, width=20, height=20, fg_color=color, border_width=2, corner_radius=0)
        borde.pack(side="left", padx=5)

        etiqueta = ctk.CTkLabel(master=frame_color, text=texto)
        etiqueta.pack(side="left", padx=5)

    filas, columnas = traer_sala(sala_id)

    asientos_seleccionados = []
    asientos_reservados = obtener_asientos_reservados(horario_id)
    
    if filas and columnas:
        frame_asientos = ctk.CTkFrame(master=frame_izquierdo)
        frame_asientos.pack(pady=10, padx=10)

        frame_pantalla = ctk.CTkFrame(master=frame_asientos, height=30, fg_color="black")
        frame_pantalla.grid(row=0, column=1, columnspan=columnas, pady=(0, 10), sticky="ew")

        label_pantalla = ctk.CTkLabel(master=frame_pantalla, text="Pantalla", text_color="white")
        label_pantalla.pack(expand=True)

        for i in range(filas):
            label_fila = ctk.CTkLabel(master=frame_asientos, text=chr(65 + i))
            label_fila.grid(row=i+1, column=0, padx=5, pady=5)

        for j in range(columnas):
            label_columna = ctk.CTkLabel(master=frame_asientos, text=str(j+1))
            label_columna.grid(row=filas+1, column=j+1, padx=5, pady=5)

        # Calcular la fila inicial para las recomendaciones
        fila_inicial_recomendacion = filas // 2
        asientos_recomendados = []

        # Seleccionar los asientos recomendados desde la mitad y expandirse por los lados
        for i in range(fila_inicial_recomendacion, -1, -1):
            for j in range(columnas):
                col_central = columnas // 2
                izquierda = col_central - (j // 2 + 1)
                derecha = col_central + (j // 2)

                if izquierda >= 0 and len(asientos_recomendados) < cantidad_boletos and (i+1, izquierda+1) not in asientos_reservados:
                    asientos_recomendados.append((i+1, izquierda+1))

                if derecha < columnas and len(asientos_recomendados) < cantidad_boletos and (i+1, derecha+1) not in asientos_reservados:
                    asientos_recomendados.append((i+1, derecha+1))

                if len(asientos_recomendados) >= cantidad_boletos:
                    break
            if len(asientos_recomendados) >= cantidad_boletos:
                break

        for i in range(filas):
            for j in range(columnas):
                if (i+1, j+1) in asientos_reservados:
                    color = COLORES_ASIENTOS["reservado"]
                elif (i+1, j+1) in asientos_recomendados:
                    color = COLORES_ASIENTOS["recomendado"]
                else:
                    color = COLORES_ASIENTOS["disponible"]
                asiento = ctk.CTkButton(
                    master=frame_asientos, width=60, height=60, text=f"{i+1}-{j+1}", fg_color=color
                )
                asiento.grid(row=i+1, column=j+1, padx=2, pady=2)
                asiento.configure(command=lambda a=asiento: toggle_asiento_color(a, asientos_seleccionados, cantidad_boletos))

    frame_continuar = ctk.CTkFrame(master=frame_derecho)
    frame_continuar.pack(padx=10, pady=10, side="bottom", anchor="se")

    def validar_asientos():
        if len(asientos_seleccionados) != cantidad_boletos:
            mostrar_mensaje("Error", f"Debes seleccionar exactamente {cantidad_boletos} asientos.", root)
            return False
        return True

    def guardar_asientos(asientos_seleccionados, horario_id):
        if validar_asientos():
            for asiento in asientos_seleccionados:
                fila, columna = map(int, asiento.cget("text").split('-'))
                exito = guardar_reserva(horario_id, fila, columna)
                if not exito:
                    print(f"Error al guardar el asiento en fila {fila}, columna {columna}")
                else:
                    print(f"Asiento en fila {fila}, columna {columna} guardado exitosamente")

    boton_continuar = ctk.CTkButton(master=frame_continuar, text="Guardar", command=lambda: guardar_asientos(asientos_seleccionados, horario_id))
    boton_continuar.pack(side="right")