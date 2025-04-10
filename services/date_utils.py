from datetime import datetime, timedelta
from typing import Optional


def calcular_edad(fecha_nacimiento: str) -> Optional[int]:
    """Calcula la edad a partir de una fecha de nacimiento en formato YYYY-MM-DD."""
    try:
        nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
        hoy = datetime.today().date()
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        return edad
    except ValueError:
        return None


def es_fecha_reserva_valida(fecha: str) -> bool:
    """Verifica si una fecha es válida para reserva (entre 2 y 7 días desde hoy)."""
    try:
        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
        hoy = datetime.today().date()
        return hoy + timedelta(days=2) <= fecha_obj <= hoy + timedelta(days=7)
    except ValueError:
        return False


def es_fecha_cancelacion_valida(fecha_funcion: str) -> bool:
    """Verifica si se puede cancelar una reserva (entre 1 y 2 días antes de la función)."""
    try:
        fecha_funcion_obj = datetime.strptime(fecha_funcion, "%Y-%m-%d").date()
        hoy = datetime.today().date()
        dias_restantes = (fecha_funcion_obj - hoy).days
        return 1 <= dias_restantes <= 2
    except ValueError:
        return False


def validar_formato_fecha(fecha: str) -> bool:
    """Valida el formato de una fecha como YYYY-MM-DD."""
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validar_formato_hora(hora: str) -> bool:
    """Valida el formato de una hora como HH:MM (24h)."""
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False
from datetime import datetime, timedelta

def validar_fecha_reserva(fecha_str: str) -> bool:
    """
    Valida si la fecha de reserva está entre 2 y 7 días a partir de hoy.
    """
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        hoy = datetime.today().date()
        return hoy + timedelta(days=2) <= fecha <= hoy + timedelta(days=7)
    except ValueError:
        return False

def validar_fecha_funcion(fecha_str: str) -> bool:
    """
    Valida que la fecha de función no sea anterior a hoy.
    """
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        return fecha >= datetime.today().date()
    except ValueError:
        return False
