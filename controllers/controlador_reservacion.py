from typing import Optional
from models.reservacion import Reserva
from models.sala import Sala
from datetime import datetime

class ReservacionControlador:
    """Controlador que gestiona las reservas en salas de cine."""

    def __init__(self, db):
        self.db = db

    def obtener_proximo_id_reserva(self) -> int:
        reservas = self.db.obtener_todas_las_reservas()
        return max(r.id_reserva for r in reservas) + 1 if reservas else 1

    def _esta_en_rango_para_reserva(self, fecha_funcion: str) -> bool:
        fecha = datetime.strptime(fecha_funcion, "%Y-%m-%d")
        hoy = datetime.now()
        diferencia = (fecha - hoy).days
        return 2 <= diferencia <= 7

    def _se_puede_cancelar_reserva(self, fecha_funcion: str) -> bool:
        fecha = datetime.strptime(fecha_funcion, "%Y-%m-%d")
        hoy = datetime.now()
        diferencia = (fecha - hoy).days
        return diferencia >= 2

    def crear_reserva(self, id_usuario: int, id_pelicula: int, sala: Sala,
                    id_silla: str, fecha_funcion: str, hora_funcion: str) -> Optional[Reserva]:
        """
        Crea una reserva si la silla está disponible y la fecha es válida.
        """
        try:
            if not self._esta_en_rango_para_reserva(fecha_funcion):
                print("La fecha de la función debe estar entre 2 y 7 días desde hoy.")
                return None

            silla = sala.buscar_silla_por_id(id_silla)
            if not silla or silla.esta_ocupada():
                print("La silla no está disponible.")
                return None

            silla.ocupar()
            self.db.actualizar_sala(sala)

            id_reserva = self.obtener_proximo_id_reserva()
            reserva = Reserva(
                id_reserva=id_reserva,
                id_usuario=id_usuario,
                id_sala=sala.get_nombre(),
                id_silla=id_silla,
                id_pelicula=id_pelicula,
                fecha_funcion=fecha_funcion,
                hora_funcion=hora_funcion
            )
            self.db.guardar_reserva(reserva)
            return reserva

        except Exception as e:
            print(f"Error al crear la reserva: {e}")
            return None

    def cancelar_reserva(self, id_reserva: int) -> bool:
        reserva = self.db.obtener_reserva(id_reserva)
        if not reserva or reserva.estado != 'activa':
            print("La reserva no existe o ya está cancelada.")
            return False

        if not self._se_puede_cancelar_reserva(reserva._fecha_funcion):
            print("La reserva solo se puede cancelar hasta 2 días antes de la función.")
            return False

        sala = self.db.obtener_sala(reserva._id_sala)
        silla = sala.buscar_silla_por_id(reserva._id_silla)
        if silla:
            silla.liberar()
            self.db.actualizar_sala(sala)

        reserva.cancelar()
        self.db.actualizar_reserva(reserva)
        return True

