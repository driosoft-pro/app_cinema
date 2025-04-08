from typing import Optional, List
from datetime import date

class Usuario:
    """
    Clase base para usuarios del sistema.
    """

    def __init__(
        self,
        cedula: Optional[int] = None,
        nombre: Optional[str] = None,
        fecha_nacimiento: Optional[date] = None,
        correo: Optional[str] = None,
        contrasena: Optional[str] = None
    ) -> None:
        self.__cedula = cedula
        self.__nombre = nombre
        self.__fecha_nacimiento = fecha_nacimiento
        self.__correo = correo
        self.__contrasena = contrasena

    def get_cedula(self) -> Optional[int]:
        return self.__cedula

    def get_nombre(self) -> Optional[str]:
        return self.__nombre

    def get_correo(self) -> Optional[str]:
        return self.__correo

    def get_fecha_nacimiento(self) -> Optional[date]:
        return self.__fecha_nacimiento

    def get_edad(self) -> Optional[int]:
        if self.__fecha_nacimiento:
            today = date.today()
            return today.year - self.__fecha_nacimiento.year - (
                (today.month, today.day) < (self.__fecha_nacimiento.month, self.__fecha_nacimiento.day)
            )
        return None

    def verificar_contrasena(self, contrasena: str) -> bool:
        return self.__contrasena == contrasena

    def set_contrasena(self, nueva_contrasena: str) -> None:
        self.__contrasena = nueva_contrasena

    def __str__(self) -> str:
        return f"{self.__nombre} ({self.__cedula})"


class Cliente(Usuario):
    """
    Cliente: puede comprar, reservar, cancelar.
    """

    def __init__(
        self,
        cedula: Optional[int] = None,
        nombre: Optional[str] = None,
        fecha_nacimiento: Optional[date] = None,
        correo: Optional[str] = None,
        contrasena: Optional[str] = None
    ) -> None:
        super().__init__(cedula, nombre, fecha_nacimiento, correo, contrasena)
        self.__reservas: List = []
        self.__compras: List = []

    def agregar_reserva(self, reserva) -> None:
        self.__reservas.append(reserva)

    def agregar_compra(self, compra) -> None:
        self.__compras.append(compra)

    def get_reservas(self) -> List:
        return self.__reservas

    def get_compras(self) -> List:
        return self.__compras


class Administrador(Usuario):
    """
    Administrador: gestiona usuarios, películas, ventas, etc.
    """

    def __init__(
        self,
        cedula: Optional[int] = None,
        nombre: Optional[str] = None,
        fecha_nacimiento: Optional[date] = None,
        correo: Optional[str] = None,
        contrasena: Optional[str] = None
    ) -> None:
        super().__init__(cedula, nombre, fecha_nacimiento, correo, contrasena)

    def es_admin(self) -> bool:
        return True