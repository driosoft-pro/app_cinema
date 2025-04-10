from controllers.controlador_usuarios import ControladorUsuarios
from controllers.controlador_peliculas import ControladorPeliculas
from controllers.controlador_ticket import ControladorTicket
from controllers.controlador_salas import ControladorSalas
from models.pagos import Pago

# Inicialización del sistema
usuarios_controller = ControladorUsuarios()
peliculas_controller = ControladorPeliculas()
salas_controller = ControladorSalas()
tickets_guardados = []
pagos = []

# Carga de películas por defecto
peliculas_controller.cargar_peliculas_predeterminadas()

# Configuración del controlador de tickets con almacenamiento simulado
tickets_controller = ControladorTicket(bd=None)
tickets_controller.bd = type('FakeDB', (), {
    'guardar_ticket': lambda self, t: tickets_guardados.append(t),
    'obtener_ticket': lambda self, c: next((t for t in tickets_guardados if t.codigo == c), None),
    'obtener_todos_los_tickets': lambda self: tickets_guardados,
    'guardar_pago': lambda self, p: pagos.append(p),
    'obtener_pago': lambda self, pid: next((p for p in pagos if p.id_pago == pid), None)
})()

# Menú principal del sistema
def menu_principal():
    while True:
        print("\n🎬 Bienvenido al Sistema de Cine")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = login_usuario()
            if usuario:
                if hasattr(usuario, 'es_admin') and usuario.es_admin():
                    menu_admin(usuario)
                else:
                    menu_cliente(usuario)
        elif opcion == "3":
            print("Gracias por usar el sistema. Hasta pronto!")
            break
        else:
            print("Opcion inválida. Intente nuevamente.")

def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    try:
        cedula = int(input("Cédula: "))
        nombre = input("Nombre completo: ")
        correo = input("Correo electrónico: ")
        fecha = input("Fecha de nacimiento (YYYY-MM-DD): ")
        contrasena = input("Contraseña: ")
        es_admin = input("Es administrador? (s/n): ").lower() == 's'
        usuarios_controller.registrar_usuario(cedula, nombre, fecha, correo, contrasena, es_admin)
        print("Registro exitoso ✅")
    except Exception as e:
        print(f"Ocurrió un error durante el registro: {e}")

def login_usuario():
    print("\n--- Iniciar Sesión ---")
    cedula = int(input("Cédula: "))
    contrasena = input("Contraseña: ")
    usuario = usuarios_controller.autenticar_usuario(cedula, contrasena)
    if usuario:
        print(f"Bienvenido {usuario.get_nombre()}!")
        return usuario
    else:
        print("Cédula o contraseña incorrecta")
    return None

def menu_cliente(cliente):
    while True:
        print("\n--- Menú Cliente ---")
        print("1. Ver Cartelera")
        print("2. Reservar Silla")
        print("3. Comprar Entrada")
        print("4. Ver Mis Tickets")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for peli in peliculas_controller.listar_peliculas():
                print(f"🎞️ {peli}")
        elif opcion in ["2", "3"]:
            reservar_o_comprar(cliente, tipo='reserva' if opcion == "2" else 'compra')
        elif opcion == "4":
            tickets = tickets_controller.obtener_tickets_por_usuario(str(cliente.get_cedula()))
            for t in tickets:
                print(t.a_diccionario())
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

def reservar_o_comprar(cliente, tipo='reserva'):
    print("\n--- Selección de Película ---")
    pelis = peliculas_controller.listar_peliculas()
    for i, p in enumerate(pelis):
        print(f"{i+1}. {p.titulo}")
    idx = int(input("Seleccione película: ")) - 1
    peli = pelis[idx]

    funciones = peli.fecha
    for i, f in enumerate(funciones):
        print(f"{i+1}. {f['fecha']} {f['hora']} ({f['jornada']})")
    idx_funcion = int(input("Seleccione función: ")) - 1
    funcion = funciones[idx_funcion]

    sala = input("Sala (2D/3D): ").upper()
    salas_controller.mostrar_disponibilidad_sala(sala)
    silla = input("ID de la silla: ")

    if not tickets_controller.silla_disponible(sala, funcion['fecha'], funcion['hora'], funcion['jornada'], silla):
        print("Silla ocupada ❌")
        return

    precio = 18000 if tipo == 'reserva' else 25000
    id_pago = None
    if tipo == 'compra':
        metodo = input("Método de pago (efectivo/tarjeta/transferencia): ")
        pagado = float(input("Valor pagado: "))
        pago = Pago.crear_pago(metodo, precio, pagado)
        pagos.append(pago)
        id_pago = pago.id_pago

    ticket = tickets_controller.registrar_ticket(
        id_usuario=str(cliente.get_cedula()),
        id_pelicula=peli.titulo,
        sala=sala,
        fecha=funcion['fecha'],
        hora=funcion['hora'],
        jornada=funcion['jornada'],
        id_silla=silla,
        tipo_transaccion=tipo,
        precio_total=precio,
        id_pago=id_pago
    )
    if ticket:
        print("✅ Ticket generado correctamente: ", ticket.codigo)
    else:
        print("No se pudo generar el ticket")

def menu_admin(admin):
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Ver usuarios registrados")
        print("2. Ver cartelera")
        print("3. Ver todos los tickets")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for u in usuarios_controller.listar_usuarios():
                print(f"👤 {u}")
        elif opcion == "2":
            for p in peliculas_controller.listar_peliculas():
                print(f"🎬 {p}")
        elif opcion == "3":
            for t in tickets_controller.listar_todos_los_tickets():
                print(t.a_diccionario())
        elif opcion == "4":
            break
        else:
            print("Opcion no válida")

if __name__ == '__main__':
    menu_principal()