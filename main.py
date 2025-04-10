from controllers.controlador_usuarios import ControladorUsuarios
from controllers.controlador_peliculas import ControladorPeliculas
from controllers.controlador_ticket import ControladorTicket
from controllers.controlador_pagos import ControladorPagos
from controllers.controlador_salas import ControladorSalas
from controllers.controlador_menu_comidas import ControladorMenuComidas
from services.auth_services import ServicioAutenticacion
from models.usuario import Administrador, Cliente
from views.peliculas_views import mostrar_peliculas
from views.menu_cliente import menu_cliente
from views.menu_admin import menu_admin

def mostrar_menu_principal():
    print("\n==== BIENVENIDO A APP CINEMA ====")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")

def mostrar_menu_admin():
    print("\n--- Menú Administrador ---")
    print("1. Gestionar películas")
    print("2. Gestionar usuarios")
    print("3. Ver todas las ventas")
    print("4. Ver todas las reservas")
    print("5. Asignar privilegios de administrador")
    print("6. Cerrar sesión")

def main():
    # Bases de datos en memoria (listas)
    bd_tickets = []

    # Inicialización de controladores con sus "bd"
    controlador_usuarios = ControladorUsuarios()
    controlador_peliculas = ControladorPeliculas()
    controlador_tickets = ControladorTicket(bd_tickets)
    controlador_pagos = ControladorPagos()
    controlador_salas = ControladorSalas()
    controlador_menu_comidas = ControladorMenuComidas()
    servicio_auth = ServicioAutenticacion(controlador_usuarios)

    # Crear administrador por defecto si no existe
    if not any(isinstance(u, Administrador) for u in controlador_usuarios.usuarios):
        controlador_usuarios.registrar_usuario(
            cedula=9999,
            nombre="Admin",
            fecha_nacimiento_str="1980-01-01",
            correo="sam@admin.com",
            contrasena="admin",
            es_admin=True
        )
        print("Administrador por defecto creado: cédula 9999, contraseña 'admin'")
    
        # Crear cliente por defecto si no existe
    if not any(isinstance(u, Cliente) for u in controlador_usuarios.usuarios):
        controlador_usuarios.registrar_usuario(
            cedula=1111,
            nombre="Cliente",
            fecha_nacimiento_str="1980-01-01",
            correo="sam@cliente.com",
            contrasena="cliente",
            es_admin=False
        )
        print("Cliente por defecto creado: cédula 1111, contraseña 'cliente'")

    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            cedula = int(input("Cédula: "))
            contrasena = input("Contraseña: ")
            if servicio_auth.login(cedula, contrasena):
                print("Inicio de sesión exitoso.")
                while True:
                    if servicio_auth.es_cliente():
                        menu_cliente(
                            servicio_auth.usuario_actual,
                            controlador_tickets,
                            controlador_pagos,
                            controlador_salas,
                            controlador_peliculas,
                            controlador_menu_comidas
                        )
                        break
                    elif servicio_auth.es_administrador():
                        from views.menu_admin import menu_admin
                        menu_admin(
                            controlador_usuarios,
                            controlador_peliculas,
                            controlador_tickets,
                            controlador_pagos,
                            servicio_auth
                        )
                        break
            else:
                print("Credenciales inválidas.")

        elif opcion == "2":
            try:
                cedula = int(input("Cédula: "))
                nombre = input("Nombre: ")
                fecha_nacimiento = input("Fecha de nacimiento (AAAA-MM-DD): ")
                correo = input("Correo: ")
                contrasena = input("Contraseña: ")

                controlador_usuarios.registrar_usuario(
                    cedula, nombre, fecha_nacimiento, correo, contrasena
                )
                print("Usuario registrado con éxito.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            print("Gracias por usar App Cinema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
