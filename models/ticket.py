from dataclasses import dataclass
from typing import Optional, Literal
from datetime import datetime

EstadoTicketLiteral = Literal["activa", "cancelada"]
TipoTransaccionLiteral = Literal["reserva", "compra"]

@dataclass
class Ticket:
    """Representa una boleta de cine (ticket) para una función"""
    codigo: str  # Código único
    id_usuario: str  # ID del cliente que reservó o compró
    id_pelicula: str  # ID de la película
    sala: str  # Sala 2D o 3D
    fecha_funcion: str  # formato: 'YYYY-MM-DD'
    hora_funcion: str  # formato: 'HH:MM'
    jornada: str  # Mañana, tarde, noche
    id_silla: str  # ID de la silla asignada
    tipo_transaccion: TipoTransaccionLiteral  # compra o reserva
    estado: EstadoTicketLiteral = "activa"
    id_pago: Optional[str] = None  # Solo si es compra
    precio_total: Optional[float] = 0.0

    def a_diccionario(self) -> dict:
        """Convierte el ticket a diccionario para serialización"""
        return {
            "codigo": self.codigo,
            "id_usuario": self.id_usuario,
            "id_pelicula": self.id_pelicula,
            "sala": self.sala,
            "fecha_funcion": self.fecha_funcion,
            "hora_funcion": self.hora_funcion,
            "jornada": self.jornada,
            "id_silla": self.id_silla,
            "tipo_transaccion": self.tipo_transaccion,
            "estado": self.estado,
            "id_pago": self.id_pago,
            "precio_total": self.precio_total
        }
