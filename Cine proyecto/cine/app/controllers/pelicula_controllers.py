import psycopg2

def conectar_base_de_datos():
    try:
        conexion = psycopg2.connect(
            user='postgres',
            password='8881243',
            host='127.0.0.1',
            port='5432',
            database='cine'
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def realizar_consulta(sql, params=None):
    conexion = conectar_base_de_datos()
    if conexion is None:
        return []

    try:
        cursor = conexion.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        return registros
    except Exception as e:
        print(f"Error al realizar la consulta: {e}")
        return []

def traer_peliculas():
    sql = 'SELECT * FROM peliculas'
    registros = realizar_consulta(sql)
    peliculas = [
        {
            'id': registro[0],
            'nombre': registro[1],
            'sinopsis': registro[2],
            'imagen_url': registro[3],
            'duracion': registro[4],
            'categoria': registro[5]
        }
        for registro in registros
    ]
    return peliculas

def traer_horarios(pelicula_id):
    sql = f'SELECT id, horario, sala_id FROM horarios WHERE pelicula_id = {pelicula_id}'
    registros = realizar_consulta(sql)
    horarios = [(registro[0], registro[1], registro[2]) for registro in registros]
    return horarios


def traer_sala(sala_id):
    sql = f'SELECT filas, columnas FROM salas WHERE id = {sala_id}'
    registros = realizar_consulta(sql)
    if registros:
        filas, columnas = registros[0]
        return filas, columnas
    return None, None


def traer_salas_completas():
    sql = 'SELECT * FROM salas'
    registros = realizar_consulta(sql)
    salas = [
        {
            'id': registro[0],
            'nombre': registro[1],
            'filas': registro[2],
            'columnas': registro[3]
        }
        for registro in registros
    ]
    return salas

def obtener_usuario(username):
    sql = 'SELECT password_hash, role FROM usuarios WHERE username = %s'
    registros = realizar_consulta(sql, (username,))
    if registros:
        return registros[0]
    return None

def guardar_pelicula(datos):
    conexion = conectar_base_de_datos()
    if conexion is None:
        return False

    try:
        cursor = conexion.cursor()
        sql = """
        INSERT INTO peliculas (id, nombre, sinopsis, imagen_url, duracion, categoria)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (
            datos['ID'],
            datos['Nombre'],
            datos['Sinopsis'],
            datos['Imagen URL'],
            datos['Duración'],
            datos['Categoría']
        ))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al guardar la película: {e}")
        return False

def crear_sala(id, nombre, filas, columnas):
    conexion = conectar_base_de_datos()
    if conexion is None:
        return False

    try:
        cursor = conexion.cursor()
        consulta = """
        INSERT INTO salas (id, nombre, filas, columnas)
        VALUES (%s, %s, %s, %s);
        """
        valores = (id, nombre, filas, columnas)
        cursor.execute(consulta, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al crear la sala: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def crear_horario(id_pelicula, sala_id, horario):
    conexion = conectar_base_de_datos()
    if conexion is None:
        return False

    try:
        cursor = conexion.cursor()
        consulta = """
        INSERT INTO horarios (pelicula_id, sala_id, horario)
        VALUES (%s, %s, %s);
        """
        valores = (id_pelicula, sala_id, horario)
        cursor.execute(consulta, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al crear el horario: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

def eliminar_pelicula(pelicula_id):
    conexion = conectar_base_de_datos()
    if conexion is None:
        return False

    try:
        cursor = conexion.cursor()
        
        # Eliminar los registros en reservas que referencian los horarios de la película
        consulta_reservas = """
        DELETE FROM reservas
        WHERE horario_id IN (SELECT id FROM horarios WHERE pelicula_id = %s);
        """
        valores_reservas = (pelicula_id,)
        cursor.execute(consulta_reservas, valores_reservas)
        
        # Eliminar los registros en horarios que referencian la película
        consulta_horarios = "DELETE FROM horarios WHERE pelicula_id = %s;"
        valores_horarios = (pelicula_id,)
        cursor.execute(consulta_horarios, valores_horarios)
        
        # Eliminar la película
        consulta_pelicula = "DELETE FROM peliculas WHERE id = %s;"
        valores_pelicula = (pelicula_id,)
        cursor.execute(consulta_pelicula, valores_pelicula)
        
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar la película: {e}")
        if conexion:
            conexion.rollback()
        return False
    finally:
        if conexion:
            conexion.close()

