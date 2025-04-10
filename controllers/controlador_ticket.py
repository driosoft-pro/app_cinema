from typing import List, Optional, Literal
from models.ticket import Ticket
import uuid

class ControladorTicket:
    def __init__(self, bd: List[Ticket]):
        self.bd = bd  # Lista simple como base de datos

    def generar_codigo_ticket(self) -> str:
        return str(uuid.uuid4())

    def crear_ticket(
        self,
        id_usuario: str,
        id_pelicula: str,   
        sala: str,
        fecha_funcion: str,
        hora_funcion: str,
        jornada: str,
        id_silla: str,
        tipo_transaccion: str,
        precio_total: float,
        id_pago: Optional[str] = None
    ) -> Optional[Ticket]:
        try:
            codigo = self.generar_codigo_ticket()
            ticket = Ticket(
                codigo=codigo,
                id_usuario=id_usuario,
                id_pelicula=id_pelicula,
                sala=sala,
                fecha_funcion=fecha_funcion,
                hora_funcion=hora_funcion,
                jornada=jornada,
                id_silla=id_silla,
                tipo_transaccion=tipo_transaccion,
                id_pago=id_pago,
                precio_total=precio_total
            )
            self.bd.append(ticket)
            return ticket
        except Exception as e:
            print(f"Error al crear ticket: {e}")
            return None

    def obtener_ticket_por_codigo(self, codigo: str) -> Optional[Ticket]:
        for t in self.bd:
            if t.codigo == codigo:
                return t
        return None

    def obtener_tickets_por_usuario(self, id_usuario: str) -> List[Ticket]:
        return [t for t in self.bd if t.id_usuario == id_usuario]

    def cancelar_ticket(self, codigo: str) -> bool:
        for ticket in self.bd:
            if ticket.codigo == codigo:
                ticket.estado = "cancelada"
                return True
        return False

    def listar_todos_los_tickets(self) -> List[Ticket]:
        return self.bd

    def silla_disponible(self, sala: str, fecha: str, hora: str, jornada: str, id_silla: str) -> bool:
        for ticket in self.bd:
            if (
                ticket.sala == sala and
                ticket.fecha_funcion == fecha and
                ticket.hora_funcion == hora and
                ticket.jornada == jornada and
                ticket.id_silla == id_silla and
                ticket.estado == "activa"
            ):
                return False
        return True

    def registrar_ticket(
        self,
        id_usuario: str,
        id_pelicula: str,
        sala: str,
        fecha: str,
        hora: str,
        jornada: str,
        id_silla: str,
        tipo_transaccion: Literal["reserva", "compra"],
        precio_total: float,
        id_pago: Optional[str] = None
    ) -> Optional[Ticket]:
        if not self.silla_disponible(sala, fecha, hora, jornada, id_silla):
            return None

        codigo_ticket = self.generar_codigo_ticket()
        ticket = Ticket(
            codigo=codigo_ticket,
            id_usuario=id_usuario,
            id_pelicula=id_pelicula,
            sala=sala,
            fecha_funcion=fecha,
            hora_funcion=hora,
            jornada=jornada,
            id_silla=id_silla,
            tipo_transaccion=tipo_transaccion,
            precio_total=precio_total,
            id_pago=id_pago
        )
        self.bd.append(ticket)
        return ticket
