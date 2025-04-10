from models.sala import Sala2D, Sala3D, Sala
from typing import Union

class ControladorSalas:
    def __init__(self):
        self.__salas: dict[str, Sala] = {}
        self._crear_salas_por_defecto()

    def _crear_salas_por_defecto(self):
        self.__salas["2D"] = Sala2D()
        self.__salas["3D"] = Sala3D()

    def obtener_sala(self, tipo: str) -> Union[Sala2D, Sala3D, None]:
        return self.__salas.get(tipo.upper())

    def obtener_todas_las_salas(self) -> list[Sala]:
        return list(self.__salas.values())

    def mostrar_disponibilidad_sala(self, tipo: str):
        sala = self.obtener_sala(tipo)
        if sala:
            print(f"Disponibilidad en {sala.get_nombre()}:")
            sala.mostrar_disponibilidad()
        else:
            print(f"No se encontró la sala de tipo '{tipo}'.")

    def buscar_silla_en_sala(self, tipo_sala: str, id_silla: str):
        sala = self.obtener_sala(tipo_sala)
        if sala:
            return sala.buscar_silla_por_id(id_silla)
        return None

    def ocupar_silla(self, tipo_sala: str, id_silla: str) -> bool:
        silla = self.buscar_silla_en_sala(tipo_sala, id_silla)
        if silla and not silla.esta_ocupada():
            silla.ocupar()
            return True
        return False

    def liberar_silla(self, tipo_sala: str, id_silla: str) -> bool:
        silla = self.buscar_silla_en_sala(tipo_sala, id_silla)
        if silla and silla.esta_ocupada():
            silla.liberar()
            return True
        return False

    def asignar_funcion_a_sala(self, tipo_sala: str, fecha: str, hora: str) -> bool:
        sala = self.obtener_sala(tipo_sala)
        if sala:
            return sala.agregar_funcion(fecha, hora)
        return False

    def actualizar_sala(self, sala: Sala):
        """Actualiza la sala dentro del diccionario."""
        self.__salas[sala.get_nombre().split()[-1].upper()] = sala
    
    def obtener_sala_por_id(self, id_sala: str) -> Union[Sala2D, Sala3D, None]:
        return self.__salas.get(id_sala.upper())
