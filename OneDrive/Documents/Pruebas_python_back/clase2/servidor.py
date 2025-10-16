from typing import Literal
from fastapi import FastAPI

app = FastAPI()

@app.get("/estudiantes")
def get_estudiantes():
    return ["Pepe", "Toño", "Ana", "Mary"]

SUPER_DB = ["Pepe", "Toño", "Ana", "Mary"]

@app.get("/estudiante/{estudiante_id}")
def get_estudiante_por_id(estudiante_id: int):
    # return estudiante_id --- Verificamos que lo que mandamos, lo regresamos
    """
    En este caso, pensamos que el id es simplemente la posición
    del estudiante en la lista de arriba.
    
    Recordemos que el cliente no sabe cómo está la base de datos
    siempre y cuando obtenga lo que solicita
    """
    return SUPER_DB[estudiante_id]

@app.get("/estudiante/{estudiante_id}/{mayusculas}")
def get_estudiante_por_id_mayusculas(estudiante_id: int, mayusculas: bool):
    estudiante = SUPER_DB[estudiante_id]
    """
    Este condicional está pensado para que si mayusculas es True, entonces
    se devuelve todo en mayúsculas, por otro lado, si es falso, se devuelve
    todo en minúsculas, en caso de que queramos obtener el nombre
    tal cual fue guardado, podemos hacer uso de la función de arriba.
    """
    if mayusculas:
        return estudiante.upper()
    else:
        return estudiante.lower()
    
@app.get("/estudiante-query")
def get_estudiante_por_id_parametro_de_ruta(estudiante_id: int):
    """
    En primer lugar notamos que no ponemos nada en la ruta (lo que va con app.get)
    y lo definimos directamente como argumento de nuestra función.
    
    Esta función hace exactamente lo mismo que get_estudiante_por_id
    pero el id lo recibimos como parámetro de petición
    """
    # return estudiante_id --- Verificamos que lo que mandamos, lo regresamos
    return SUPER_DB[estudiante_id]

@app.get("/estudiante-query/{estudiante_id}")
def get_estudiante_por_id_ruta_y_peticion(estudiante_id: int, conversion: Literal["normal", "mayusculas", "minusculas"]):
    estudiante = SUPER_DB[estudiante_id]
    if conversion == "normal":
        return estudiante
    elif conversion == "mayusculas":
        return estudiante.upper()
    elif conversion == "minusculas":
        return estudiante.lower()