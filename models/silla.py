from typing import Literal

class Silla:
    """
    Clase que representa una silla dentro de una sala de cine.

    Atributos:
        __id: Identificador único de la silla.
        __tipo: Tipo de silla ('general' o 'preferencial').
        __ocupada: Indica si la silla está ocupada.
    """

    def __init__(self, id: int, tipo: Literal["general", "preferencial"] = "general"):
        """
        Constructor de la clase Silla.

        Args:
            id: Identificador único de la silla.
            tipo: Tipo de silla, por defecto 'general'.
        """
        self.__id = id
        self.__tipo = tipo.lower()
        self.__ocupada = False

    def ocupar(self):
        """Marca la silla como ocupada."""
        self.__ocupada = True

    def liberar(self):
        """Libera la silla (disponible)."""
        self.__ocupada = False

    def esta_ocupada(self):
        """Devuelve True si la silla está ocupada."""
        return self.__ocupada

    def obtener_tipo(self):
        """Devuelve el tipo de silla."""
        return self.__tipo

    def obtener_id(self):
        """Devuelve el ID de la silla."""
        return self.__id

    def __str__(self):
        """Representación en texto de la silla."""
        estado = "X" if self.__ocupada else "O"
        return f"[{self.__id} | {self.__tipo.capitalize()} | {'Ocupada' if self.__ocupada else 'Libre'}]"