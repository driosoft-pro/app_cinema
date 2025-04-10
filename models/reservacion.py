from datetime import datetime
from typing import Literal

class Reserva:
    """Clase que representa una reserva de entrada para una función."""
    def __init__(self, id_reserva: int, id_usuario: int, id_sala: str, 
                id_silla: str, id_pelicula: int, fecha_funcion: str, hora_funcion: str,
                fecha_reserva: str = None,
                estado: Literal['activa', 'cancelada', 'expirada'] = 'activa'):

        self._id_reserva = id_reserva
        self._id_usuario = id_usuario
        self._id_sala = id_sala
        self._id_silla = id_silla
        self._id_pelicula = id_pelicula
        self._fecha_funcion = fecha_funcion
        self._hora_funcion = hora_funcion
        self._estado = estado
        self._fecha_reserva = fecha_reserva or datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @property
    def id_reserva(self): return self._id_reserva

    @property
    def estado(self): return self._estado

    def cancelar(self):
        self._estado = 'cancelada'

    def expirar(self):
        self._estado = 'expirada'

    def a_diccionario(self):
        return {
            'id_reserva': self._id_reserva,
            'id_usuario': self._id_usuario,
            'id_sala': self._id_sala,
            'id_silla': self._id_silla,
            'id_pelicula': self._id_pelicula,
            'fecha_funcion': self._fecha_funcion,
            'hora_funcion': self._hora_funcion,
            'fecha_reserva': self._fecha_reserva,
            'estado': self._estado
        }
