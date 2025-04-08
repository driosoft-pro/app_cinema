from controllers.controlador_usuarios import ControladorUsuarios
from models.usuario import Cliente, Administrador
from datetime import datetime
import unittest

def calcular_edad_test(fecha_str):
    fecha_nac = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    hoy = datetime.today().date()
    edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
    return edad

class TestControladorUsuarios(unittest.TestCase):

    def test_registro_y_autenticacion_cliente(self):
        controlador = ControladorUsuarios()

        cedula = 12345678
        nombre = "Carlos"
        fecha_nacimiento = "2000-05-15"
        correo = "carlos@example.com"
        contrasena = "clave123"

        cliente = controlador.registrar_usuario(
            cedula, nombre, fecha_nacimiento, correo, contrasena, es_admin=False
        )

        self.assertIsInstance(cliente, Cliente)
        self.assertEqual(cliente.get_nombre(), nombre)
        self.assertEqual(cliente.get_cedula(), cedula)
        self.assertEqual(cliente.get_correo(), correo)
        self.assertTrue(cliente.verificar_contrasena(contrasena))
        self.assertEqual(cliente.get_edad(), calcular_edad_test(fecha_nacimiento))

        usuario_autenticado = controlador.autenticar_usuario(cedula, contrasena)
        self.assertIsNotNone(usuario_autenticado)
        self.assertIsInstance(usuario_autenticado, Cliente)

    def test_registro_administrador(self):
        controlador = ControladorUsuarios()

        cedula = 98765432
        nombre = "Laura"
        fecha_nacimiento = "1985-03-20"
        correo = "laura@example.com"
        contrasena = "adminpass"

        admin = controlador.registrar_usuario(
            cedula, nombre, fecha_nacimiento, correo, contrasena, es_admin=True
        )

        self.assertIsInstance(admin, Administrador)
        self.assertEqual(admin.get_nombre(), nombre)
        self.assertEqual(admin.get_edad(), calcular_edad_test(fecha_nacimiento))

if __name__ == "__main__":
    unittest.main()
