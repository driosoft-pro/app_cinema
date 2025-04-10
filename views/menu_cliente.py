from models.usuario import Cliente
from controllers.controlador_ticket import ControladorTicket
from controllers.controlador_pagos import ControladorPagos
from controllers.controlador_salas import ControladorSalas
from controllers.controlador_peliculas import ControladorPeliculas
from controllers.controlador_menu_comidas import ControladorMenuComidas
from views.compra_views import realizar_compra_o_reserva


def menu_cliente(
    cliente: Cliente,
    controlador_tickets: ControladorTicket,
    controlador_pagos: ControladorPagos,
    controlador_salas: ControladorSalas,
    controlador_peliculas: ControladorPeliculas,
    controlador_menu_comidas: ControladorMenuComidas
):
    while True:
        print("\n==== MENÚ CLIENTE ====")
        print("1. Comprar entrada")
        print("2. Reservar entrada")
        print("3. Ver mis compras")
        print("4. Ver mis reservas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            realizar_compra_o_reserva(
                cliente,
                controlador_tickets,
                controlador_pagos,
                controlador_salas,
                controlador_peliculas,
                controlador_menu_comidas,
                tipo_transaccion="compra"
            )
        elif opcion == "2":
            realizar_compra_o_reserva(
                cliente,
                controlador_tickets,
                controlador_pagos,
                controlador_salas,
                controlador_peliculas,
                controlador_menu_comidas,
                tipo_transaccion="reserva"
            )
        elif opcion == "3":
            print("\n--- MIS COMPRAS ---")
            compras = cliente.get_compras()
            if not compras:
                print("No tienes compras registradas.")
            else:
                for c in compras:
                    print(c)
        elif opcion == "4":
            print("\n--- MIS RESERVAS ---")
            reservas = cliente.get_reservas()
            if not reservas:
                print("No tienes reservas registradas.")
            else:
                for r in reservas:
                    print(r)
        elif opcion == "0":
            print("Saliendo del menú cliente...")
            break
        else:
            print("Opción inválida.")
