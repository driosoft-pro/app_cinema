import unittest
from models.ticket import Ticket
from controllers.controlador_ticket import ControladorTicket

class BaseDatosFalsa:
    def __init__(self):
        self.tickets = {}

    def guardar_ticket(self, ticket: Ticket):
        self.tickets[ticket.codigo] = ticket
        return True

    def obtener_ticket(self, codigo: str):
        return self.tickets.get(codigo)

    def obtener_todos_los_tickets(self):
        return list(self.tickets.values())

class TestControladorTicket(unittest.TestCase):
    def setUp(self):
        self.bd_falsa = BaseDatosFalsa()
        self.controlador = ControladorTicket(self.bd_falsa)

    def test_crear_ticket(self):
        ticket = self.controlador.crear_ticket(
            id_usuario="123",
            id_pelicula="456",
            sala="Sala2D",
            fecha_funcion="2025-04-15",
            hora_funcion="19:00",
            jornada="noche",
            id_silla="A1",
            tipo_transaccion="compra",
            precio_total=15000,
            id_pago="pago123"
        )

        self.assertIsNotNone(ticket)
        self.assertEqual(ticket.id_usuario, "123")
        self.assertEqual(ticket.tipo_transaccion, "compra")
        self.assertEqual(self.bd_falsa.obtener_ticket(ticket.codigo), ticket)

if __name__ == "__main__":
    unittest.main()
