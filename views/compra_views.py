from datetime import datetime
from controllers.controlador_ticket import ControladorTicket
from controllers.controlador_pagos import ControladorPagos
from controllers.controlador_salas import ControladorSalas
from controllers.controlador_peliculas import ControladorPeliculas
from controllers.controlador_menu_comidas import ControladorMenuComidas
from services.date_utils import validar_fecha_reserva, validar_fecha_funcion
from models.usuario import Cliente

def mostrar_menu_comida(controlador_menu: ControladorMenuComidas):
    print("\n--- MENÚ DE COMIDAS DISPONIBLES ---")
    items = controlador_menu.obtener_items_activos()
    for item in items:
        print(f"{item.id_item} - {item.producto} ({item.categoria}) - ${item.precio}")
    return items

def seleccionar_comidas(controlador_menu: ControladorMenuComidas):
    items_disponibles = mostrar_menu_comida(controlador_menu)
    seleccion = []
    while True:
        opcion = input("Ingrese el ID del producto que desea agregar (Enter para finalizar): ")
        if not opcion:
            break
        try:
            id_producto = int(opcion)
            item = next((i for i in items_disponibles if i.id_item == id_producto), None)
            if item:
                seleccion.append(item)
                print(f"Agregado: {item.producto} - ${item.precio}")
            else:
                print("ID no válido.")
        except ValueError:
            print("Ingrese un número válido.")
    return seleccion

def realizar_compra_o_reserva(
    cliente: Cliente,
    controlador_tickets: ControladorTicket,
    controlador_pagos: ControladorPagos,
    controlador_salas: ControladorSalas,
    controlador_peliculas: ControladorPeliculas,
    controlador_menu: ControladorMenuComidas,
    tipo_transaccion: str = "compra"
):
    print(f"\n--- {'COMPRA' if tipo_transaccion == 'compra' else 'RESERVA'} DE ENTRADAS ---")

    peliculas = controlador_peliculas.obtener_peliculas_activas()
    if not peliculas:
        print("No hay películas disponibles.")
        return

    for idx, peli in enumerate(peliculas, 1):
        print(f"{idx}. {peli.titulo} - {peli.genero} - {peli.duracion} min")

    try:
        opcion_peli = int(input("Seleccione una película por número: ")) - 1
        pelicula = peliculas[opcion_peli]
    except (ValueError, IndexError):
        print("Selección inválida.")
        return

    print(f"\n🎬 Fechas disponibles para {pelicula.titulo}:")
    for i, funcion in enumerate(pelicula.fecha, start=1):
        print(f"{i}. 📅 {funcion['fecha']} 🕒 {funcion['hora']} ({funcion['jornada'].capitalize()})")

    while True:
        try:
            seleccion = int(input("\nIngrese el número de la función deseada: "))
            if 1 <= seleccion <= len(pelicula.fecha):
                funcion_seleccionada = pelicula.fecha[seleccion - 1]
                fecha_funcion = funcion_seleccionada['fecha']
                jornada = funcion_seleccionada['jornada']
                hora = funcion_seleccionada['hora']
                print(f"\n✅ Has seleccionado: 📅 {fecha_funcion} 🕒 {hora} ({jornada.capitalize()})")
                break
            else:
                print("❌ Número fuera de rango. Intenta nuevamente.")
        except ValueError:
            print("❌ Entrada inválida. Por favor ingresa un número.")

    if tipo_transaccion == "reserva" and not validar_fecha_reserva(fecha_funcion):
        print("Fecha inválida para reserva. Debe ser entre 2 y 7 días antes de la función.")
        return

    if tipo_transaccion == "compra" and not validar_fecha_funcion(fecha_funcion):
        print("Fecha inválida para compra. Debe ser para hoy o mañana.")
        return

    print("\n🎟️ Tipos de sala disponibles:")
    print("1. 2D")
    print("2. 3D")
    opcion_sala = input("Seleccione tipo de sala (1 o 2): ")
    tipo_sala = "2D" if opcion_sala == "1" else "3D" if opcion_sala == "2" else None

    if not tipo_sala:
        print("Tipo de sala inválido.")
        return

    sala = controlador_salas.obtener_sala(tipo_sala)
    if not sala:
        print("Sala no válida.")
        return

    if not controlador_salas.asignar_funcion_a_sala(tipo_sala, fecha_funcion, hora):
        print("❌ Esta sala ya tiene una función en ese horario. Seleccione otra sala u horario.")
        return

    sillas_disponibles = sala.obtener_sillas_disponibles()
    print("\n--- 💺 SILLAS DISPONIBLES ---")
    for silla in sillas_disponibles:
        print(f"{silla.obtener_id()} - {silla.obtener_tipo()}")

    id_silla = input("Ingrese el ID de la silla que desea: ")
    silla = sala.buscar_silla_por_id(id_silla)
    if not silla or silla.esta_ocupada():
        print("Silla no disponible.")
        return

    print("\n--- 🍿 MENÚ DE COMIDA ---")
    comida_seleccionada = seleccionar_comidas(controlador_menu)
    total_comida = sum(item.precio for item in comida_seleccionada)

    precio_base = 10000 if silla.obtener_tipo() == "general" else 15000
    precio_total = precio_base + total_comida

    print(f"\n💰 Total a pagar: ${precio_total}")
    print("Métodos de pago disponibles:")
    print("1. Efectivo\n2. Tarjeta\n3. Transferencia")
    metodo = input("Seleccione método de pago (1/2/3): ")
    metodo_pago = {"1": "efectivo", "2": "tarjeta", "3": "transferencia"}.get(metodo)

    if not metodo_pago:
        print("Método inválido.")
        return

    monto_pagado = float(input("Ingrese monto entregado: ")) if metodo_pago == "efectivo" else precio_total
    cambio = monto_pagado - precio_total if metodo_pago == "efectivo" else 0
    if metodo_pago == "efectivo" and cambio < 0:
        print("Monto insuficiente.")
        return

    pago = controlador_pagos.registrar_pago(metodo_pago, precio_total, monto_pagado)

    ticket = controlador_tickets.registrar_ticket(
        cliente,
        pelicula,
        sala,
        fecha_funcion,
        jornada,
        id_silla,
        tipo_transaccion,
        pago.id_pago,
        precio_total
    )

    controlador_salas.ocupar_silla(tipo_sala, id_silla)
    controlador_salas.actualizar_sala(sala)

    if tipo_transaccion == "compra":
        cliente.agregar_compra(ticket)
    else:
        cliente.agregar_reserva(ticket)

    print(f"\n✅ {'COMPRA' if tipo_transaccion == 'compra' else 'RESERVA'} registrada con éxito.")
    print(f"🎟️ Código de ticket: {ticket.codigo}")
    print(f"💳 Pago registrado. ID transacción: {pago.id_pago}")
    if metodo_pago == "efectivo":
        print(f"💵 Cambio: ${cambio}")