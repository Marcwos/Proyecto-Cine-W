# Cine W

## Dependencias utilizadas:
1. CustomTkinter
2. psycopg2
3. bcrypt
4. Pillow

## Instalar dependencias:
```sh
pip3 install -r requirements.txt
```

## Uso del backup para la base de datos:
Para restaurar los datos del backup, utiliza el archivo `BASESQL.sql` que se encuentra en `app/controllers/BASESQL.sql`.

La configuración de la conexión a la base de datos PostgreSQL se encuentra en el archivo `pelicula_controllers.py` ubicado en `app/controllers/pelicula_controllers.py`. Para ajustar la conexión, debes cambiar los parámetros en la función `conectar_base_de_datos`:

```python
def conectar_base_de_datos():
    try:
        conexion = psycopg2.connect(
            user='tu_usuario',
            password='tu_contraseña',
            host='tu_host##',
            port='tu_puerto##',
            database='nombre_de_base'
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
```
## Ejecutar programa:
Para ejecutar el programa, debes ejecutar el archivo main.py ubicado fuera de la carpeta cine.

```
python3 main.py
