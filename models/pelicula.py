from typing import Literal, List
from datetime import datetime, timedelta

class Pelicula:
    def __init__(self, titulo: str, genero: str, clasificacion: str, fecha: List[dict], duracion: int, idioma: str, subtitulada: Literal[True, False] = False, estado: Literal[0,1] = 1):
        self.__titulo = titulo
        self.__genero = genero
        self.__clasificacion = clasificacion  # G, PG, PG-13, R, C
        self.__fecha = fecha
        self.__duracion = duracion  # en minutos
        self.__idioma = idioma
        self.__subtitulada = subtitulada  # True o False
        self.__estado = estado

    def __str__(self):
        return f"{self.titulo} ({self.clasificacion}) - {self.duracion} min"