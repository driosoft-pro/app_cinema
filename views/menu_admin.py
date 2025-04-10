from views.peliculas_views import mostrar_peliculas, gestionar_peliculas
from models.pelicula import Pelicula

def menu_admin(
    controlador_usuarios,
    controlador_peliculas,
    controlador_tickets,
    controlador_pagos,
    servicio_auth
):
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Gestionar películas")
        print("2. Gestionar usuarios")
        print("3. Ver todas las ventas")
        print("4. Ver todas las reservas")
        print("5. Asignar privilegios de administrador")
        print("6. Cerrar sesión")

        opcion = input("Selecciona una opción: ")

        if opcion == "6":
            servicio_auth.logout()
            print("Sesión cerrada.")
            break

        elif opcion == "1":
            gestionar_peliculas(controlador_peliculas)

        elif opcion == "5":
            try:
                cedula_objetivo = int(input("Ingrese la cédula del usuario a convertir en administrador: "))
                if controlador_usuarios.convertir_a_admin(cedula_objetivo):
                    print("El usuario ahora tiene privilegios de administrador.")
                else:
                    print("No se pudo convertir. ¿El usuario existe y no es ya administrador?")
            except ValueError:
                print("Cédula inválida.")

        else:
            print("Funcionalidad en desarrollo...")
