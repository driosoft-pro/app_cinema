from controllers.controlador_usuarios import ControladorUsuarios


class ServicioAutenticacion:
    """
    Servicio para gestionar autenticación y sesión.
    """

    def __init__(self, controlador_usuarios: ControladorUsuarios) -> None:
        self.controlador_usuarios = controlador_usuarios
        self.usuario_actual = None

    def login(self, cedula: int, contrasena: str) -> bool:
        usuario = self.controlador_usuarios.autenticar_usuario(cedula, contrasena)
        if usuario:
            self.usuario_actual = usuario
            return True
        return False

    def logout(self) -> None:
        self.usuario_actual = None

    def es_cliente(self) -> bool:
        from models.usuario import Cliente
        return isinstance(self.usuario_actual, Cliente)

    def es_administrador(self) -> bool:
        from models.usuario import Administrador
        return isinstance(self.usuario_actual, Administrador)

    def get_usuario_actual(self):
        return self.usuario_actual
