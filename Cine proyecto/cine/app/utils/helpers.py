import customtkinter as ctk
from PIL import Image

def eliminar_paginas(root):
    for widget in root.winfo_children():
        widget.destroy()

def cargar_imagen(ruta, tamaño):
    try:
        imagen = Image.open(ruta)
        imagen = imagen.resize(tamaño, Image.Resampling.LANCZOS)
        return ctk.CTkImage(light_image=imagen, size=tamaño)
    except Exception as e:
        print(f"Error al cargar la imagen {ruta}: {e}")
        return None
    
def volver_login(root):
    from app.gui.login import create_login
    eliminar_paginas(root)
    create_login(root)

def ir_a_asientos(root, pelicula, ruta, horario_seleccionado, sala_id, cantidad_boletos):
    from app.gui.asientos import mostrar_asientos
    mostrar_asientos(root, pelicula, ruta, horario_seleccionado, sala_id, cantidad_boletos)

def volver_a_entradas(root, pelicula, ruta):
    from app.gui.entradas_peliculas import entradas_movies
    entradas_movies(root, pelicula, ruta)
    print("Volviendo ha entradas")

def volver_a_cartelera(root):
    from app.gui.cartelera import cartelera_movies
    cartelera_movies(root)
    print("Volviendo a cartelera")

def incrementar_valor(value, step=1, max_value=None):
    try:
        value = int(value)
        if max_value is not None and value >= max_value:
            return value
        return value + step
    except ValueError:
        return value

def decrementar_valor(value, step=1, min_value=None):
    try:
        value = int(value)
        if min_value is not None and value <= min_value:
            return value
        return value - step
    except ValueError:
        return value
    
def mostrar_mensaje(titulo, mensaje, parent):
    ventana_mensaje = ctk.CTkToplevel(parent)
    ventana_mensaje.title(titulo)
    ventana_mensaje.geometry("300x150")
    ventana_mensaje.transient(parent)  # Hace que la ventana de mensaje aparezca encima del programa
    ventana_mensaje.grab_set()  # Bloquea la interacción con la ventana principal

    label_mensaje = ctk.CTkLabel(ventana_mensaje, text=mensaje, font=("Helvetica", 14))
    label_mensaje.pack(pady=20, padx=20)

    boton_ok = ctk.CTkButton(ventana_mensaje, text="OK", command=ventana_mensaje.destroy)
    boton_ok.pack(pady=10)

COLORES_ASIENTOS = {
    "disponible": "grey",
    "reservado": "black",
    "tu_asiento": "lightblue",
    "recomendado": "orange"
}

def toggle_asiento_color(asiento, asientos_seleccionados, cantidad_boletos):
    if asiento.cget("fg_color") == COLORES_ASIENTOS["reservado"]:
        return

    if asiento.cget("fg_color") == COLORES_ASIENTOS["recomendado"]:
        if asiento in asientos_seleccionados:
            asiento.configure(fg_color=COLORES_ASIENTOS["disponible"])
            asientos_seleccionados.remove(asiento)
        elif len(asientos_seleccionados) < cantidad_boletos:
            asiento.configure(fg_color=COLORES_ASIENTOS["tu_asiento"])
            asientos_seleccionados.append(asiento)
    else:
        if asiento in asientos_seleccionados:
            asiento.configure(fg_color=COLORES_ASIENTOS["disponible"])
            asientos_seleccionados.remove(asiento)
        elif len(asientos_seleccionados) < cantidad_boletos:
            asiento.configure(fg_color=COLORES_ASIENTOS["tu_asiento"])
            asientos_seleccionados.append(asiento)

def ir_a_peliculas_admin(root):
    from app.gui.admin.peliculas_admin import peliculas_admin
    peliculas_admin(root)

def ir_a_salas_admin(root):
    from app.gui.admin.salas_admin import salas_admin
    salas_admin(root)

def volver_administrador(root):
    from app.gui.admin.administrador import interfaz_admin
    interfaz_admin(root)