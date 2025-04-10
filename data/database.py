import json
from pathlib import Path
from typing import Any

# Ruta al archivo JSON
RUTA_BASE_DATOS = Path(__file__).parent / "data.json"

# Si no existe el archivo, se inicializa con estructura vacía
def cargar_base_datos() -> dict[str, Any]:
    if not RUTA_BASE_DATOS.exists():
        datos_iniciales = {
            "usuarios": [],
            "peliculas": [],
            "tickets": [],
            "pagos": [],
            "salas": [],
            "comidas": []
        }
        guardar_base_datos(datos_iniciales)
    with open(RUTA_BASE_DATOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_base_datos(datos: dict[str, Any]) -> None:
    with open(RUTA_BASE_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

# Carga única de datos
base_datos = cargar_base_datos()
