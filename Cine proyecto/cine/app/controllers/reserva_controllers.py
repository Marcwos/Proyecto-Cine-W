from app.controllers.pelicula_controllers import realizar_consulta, conectar_base_de_datos

def guardar_reserva(horario_id, fila, columna):
    conexion = conectar_base_de_datos()
    if conexion is None:
        return False
    try:
        cursor = conexion.cursor()
        sql = f"INSERT INTO reservas (horario_id, fila, columna) VALUES (%s, %s, %s)"
        cursor.execute(sql, (horario_id, fila, columna))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al guardar la reserva: {e}")
        return False

def obtener_asientos_reservados(horario_id):
    sql = f'SELECT fila, columna FROM reservas WHERE horario_id = {horario_id}'
    registros = realizar_consulta(sql)
    asientos_reservados = [(registro[0], registro[1]) for registro in registros]
    return asientos_reservados

