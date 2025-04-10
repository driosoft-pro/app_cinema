from models.usuario import Cliente, Administrador
from datetime import datetime
from typing import List, Union

class ControladorUsuarios:
    """
    Controlador para gestionar usuarios.
    """

    def __init__(self) -> None:
        self.usuarios: List[Union[Cliente, Administrador]] = []

    def registrar_usuario(
        self,
        cedula: int,
        nombre: str,
        fecha_nacimiento_str: str,
        correo: str,
        contrasena: str,
        es_admin: bool = False
    ) -> Union[Cliente, Administrador]:

        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Usa AAAA-MM-DD")

        if self.buscar_usuario(cedula):
            raise ValueError("Ya existe un usuario con esta cédula")

        if es_admin:
            nuevo_usuario = Administrador(cedula, nombre, fecha_nacimiento, correo, contrasena)
        else:
            nuevo_usuario = Cliente(cedula, nombre, fecha_nacimiento, correo, contrasena)

        self.usuarios.append(nuevo_usuario)
        return nuevo_usuario

    def buscar_usuario(self, cedula: int) -> Union[Cliente, Administrador, None]:
        for usuario in self.usuarios:
            if usuario.get_cedula() == cedula:
                return usuario
        return None

    def autenticar_usuario(self, cedula: int, contrasena: str) -> Union[Cliente, Administrador, None]:
        usuario = self.buscar_usuario(cedula)
        if usuario and usuario.verificar_contrasena(contrasena):
            return usuario
        return None

    def listar_usuarios(self) -> List[Union[Cliente, Administrador]]:
        return self.usuarios
    
    def convertir_a_admin(self, cedula: int) -> bool:
        usuario = self.buscar_usuario(cedula)
        if usuario and not isinstance(usuario, Administrador):
            nuevo_admin = Administrador(
                usuario.get_cedula(),
                usuario.get_nombre(),
                usuario.get_fecha_nacimiento(),
                usuario.get_correo(),
                usuario._Usuario__contrasena  # Acceso al atributo privado
            )
            self.usuarios.remove(usuario)
            self.usuarios.append(nuevo_admin)
            return True
        return False
