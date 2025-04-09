import sys
import os
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.controlador_reservacion import ReservacionControlador
from models.sala import Sala2D

# Mock de base de datos
class DBMock:
    def __init__(self):
        self._reservas = []
        self._salas = {}

    def obtener_todas_las_reservas(self):
        return self._reservas

    def guardar_reserva(self, reserva):
        self._reservas.append(reserva)

    def obtener_reserva(self, id_reserva):
        return next((r for r in self._reservas if r.id_reserva == id_reserva), None)

    def actualizar_reserva(self, reserva):
        pass

    def actualizar_sala(self, sala):
        self._salas[sala.get_nombre()] = sala

    def obtener_sala(self, nombre):
        return self._salas.get(nombre)

def test_crear_reserva_valida():
    db = DBMock()
    sala = Sala2D("Sala Test")
    db.actualizar_sala(sala)
    controlador = ReservacionControlador(db)

    fecha = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
    reserva = controlador.crear_reserva(1, 10, sala, "G001", fecha, "18:00")
    assert reserva is not None
    assert reserva._id_silla == "G001"
    print("✅ test_crear_reserva_valida pasó correctamente")

def test_cancelar_reserva_valida():
    db = DBMock()
    sala = Sala2D("Sala Cancelación")
    db.actualizar_sala(sala)
    controlador = ReservacionControlador(db)

    fecha = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d")
    reserva = controlador.crear_reserva(2, 20, sala, "G002", fecha, "20:00")
    assert reserva is not None

    resultado = controlador.cancelar_reserva(reserva.id_reserva)
    assert resultado is True
    print("✅ test_cancelar_reserva_valida pasó correctamente")

if __name__ == "__main__":
    test_crear_reserva_valida()
    test_cancelar_reserva_valida()