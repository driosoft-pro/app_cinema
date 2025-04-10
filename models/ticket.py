from dataclasses import dataclass
from typing import Optional, Literal

EstadoTicketLiteral = Literal["activa", "cancelada"]
TipoTransaccionLiteral = Literal["reserva", "compra"]

@dataclass
class Ticket:
    codigo: str
    id_usuario: str
    id_pelicula: str
    sala: str
    fecha_funcion: str
    hora_funcion: str
    jornada: str
    id_silla: str
    tipo_transaccion: TipoTransaccionLiteral
    estado: EstadoTicketLiteral = "activa"
    id_pago: Optional[str] = None
    precio_total: Optional[float] = 0.0

    # --- Métodos de acceso (getters) ---
    def get_codigo(self) -> str:
        return self.codigo

    def get_id_usuario(self) -> str:
        return self.id_usuario

    def get_id_pelicula(self) -> str:
        return self.id_pelicula

    def get_sala(self) -> str:
        return self.sala

    def get_fecha_funcion(self) -> str:
        return self.fecha_funcion

    def get_hora_funcion(self) -> str:
        return self.hora_funcion

    def get_jornada(self) -> str:
        return self.jornada

    def get_id_silla(self) -> str:
        return self.id_silla

    def get_tipo_transaccion(self) -> str:
        return self.tipo_transaccion

    def get_estado(self) -> str:
        return self.estado

    def get_id_pago(self) -> Optional[str]:
        return self.id_pago

    def get_precio_total(self) -> Optional[float]:
        return self.precio_total

    # --- Métodos de modificación (setters) ---
    def set_estado(self, nuevo_estado: EstadoTicketLiteral) -> None:
        self.estado = nuevo_estado

    def set_id_pago(self, nuevo_id_pago: str) -> None:
        self.id_pago = nuevo_id_pago

    def set_precio_total(self, nuevo_precio: float) -> None:
        self.precio_total = nuevo_precio

    def set_silla(self, nueva_silla: str) -> None:
        self.id_silla = nueva_silla

    # --- Diccionario para serialización ---
    def a_diccionario(self) -> dict:
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
    
    def __str__(self) -> str:
        return (
            f"🎟️ Ticket #{self.codigo}\n"
            f"👤 Usuario: {self.id_usuario}\n"
            f"🎬 Película: {self.id_pelicula}\n"
            f"🛋️ Sala: {self.sala}\n"
            f"📅 Fecha: {self.fecha_funcion} | 🕒 Hora: {self.hora_funcion}\n"
            f"🪑 Silla: {self.id_silla} | 🕹 Jornada: {self.jornada}\n"
            f"💳 Tipo: {self.tipo_transaccion} | 💰 Total: ${self.precio_total}\n"
            f"📦 Estado: {self.estado}\n"
        )