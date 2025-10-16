import requests

URLBASE = "http://127.0.0.1:8000"

# Solución del mini ejercicio
def get_estudiantes():
    respuesta = requests.get(URLBASE + "/estudiantes")
    print(respuesta.json())

def get_estudiante_por_id():
    respuesta = requests.get(URLBASE + "/estudiante/1")
    print(respuesta.json())

def get_estudiante_por_id_mayusculas():
    """
    En este caso vemos que no es necesario pasar true
    como un booleano de Python (True) sino como una cadena
    de caracteres simple.
    Si no le damos true o false, sería como hacer una petición
    a la ruta de arriba.
    """
    respuesta = requests.get(URLBASE + "/estudiante/1/true")
    print(respuesta.json())

def get_estudiante_por_id_query():
    """
    Los parámetros que queremos que se manden como parámetros de petición
    los ponemos después del signo ? con su nombre, un igual (=) y su valor
    """
    respuesta = requests.get(URLBASE + "/estudiante-query?estudiante_id=1")
    print(respuesta.json())

def get_estudiante_por_id_query_v2():
    """
    En ocasiones no queremos construir la cadena de caracteres a mano, por lo que requests
    nos da chance de definir este tipo de parámetros como un diccionario
    """
    respuesta = requests.get(URLBASE + "/estudiante-query", params={"estudiante_id": 1})
    print(respuesta.json())

def get_estudiante_por_id_ruta_y_peticion():
    respuesta = requests.get(URLBASE + "/estudiante-query/1", params={"conversion": "minusculas"})
    print(respuesta.json())

get_estudiante_por_id_ruta_y_peticion()