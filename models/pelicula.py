from typing import Literal, List, Dict
from datetime import datetime

class Pelicula:
    def __init__(
        self,
        titulo: str,
        genero: str,
        clasificacion: Literal["G", "PG", "PG-13", "R", "C"],
        fecha: List[Dict[str, str]],
        duracion: int,
        idioma: str,
        subtitulada: bool = False,
        estado: Literal[0, 1] = 1
    ):
        self.__titulo = titulo
        self.__genero = genero
        self.__clasificacion = clasificacion
        self.__fecha = fecha  # [{"fecha": "2025-04-10", "hora": "15:00", "jornada": "tarde"}]
        self.__duracion = duracion
        self.__idioma = idioma
        self.__subtitulada = subtitulada
        self.__estado = estado

    # --------- Propiedades ---------
    @property
    def titulo(self): return self.__titulo
    @property
    def genero(self): return self.__genero
    @property
    def clasificacion(self): return self.__clasificacion
    @property
    def fecha(self): return self.__fecha
    @property
    def duracion(self): return self.__duracion
    @property
    def idioma(self): return self.__idioma
    @property
    def subtitulada(self): return self.__subtitulada
    @property
    def estado(self): return self.__estado

    # --------- Setters opcionales ---------
    @estado.setter
    def estado(self, nuevo_estado: Literal[0, 1]):
        self.__estado = nuevo_estado

    # --------- Métodos ---------
    def a_diccionario(self) -> dict:
        return {
            "titulo": self.__titulo,
            "genero": self.__genero,
            "clasificacion": self.__clasificacion,
            "fecha": self.__fecha,
            "duracion": self.__duracion,
            "idioma": self.__idioma,
            "subtitulada": self.__subtitulada,
            "estado": self.__estado,
        }

    def __str__(self):
        return f"{self.__titulo} ({self.__clasificacion}) - {self.__duracion} min"