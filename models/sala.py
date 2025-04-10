from models.silla import Silla

class Sala:
    """
    Clase base para representar una sala de cine.
    """

    def __init__(self, nombre):
        self._nombre = nombre
        self._sillas = []
        self._funciones = []

    def agregar_funcion(self, fecha: str, hora: str) -> bool:
        for f in self._funciones:
            if f["fecha"] == fecha and f["hora"] == hora:
                return False
        self._funciones.append({"fecha": fecha, "hora": hora})
        return True

    def esta_disponible(self, fecha: str, hora: str) -> bool:
        return all(f["fecha"] != fecha or f["hora"] != hora for f in self._funciones)

    def obtener_funciones(self):
        return self._funciones

    def obtener_sillas_disponibles(self):
        return [silla for silla in self._sillas if not silla.esta_ocupada()]

    def obtener_sillas(self):
        return self._sillas

    def buscar_silla_por_id(self, id):
        for silla in self._sillas:
            if silla.obtener_id() == id:
                return silla
        return None

    def mostrar_disponibilidad(self):
        for silla in self._sillas:
            print(silla)

    def get_nombre(self):
        return self._nombre


class Sala2D(Sala):
    """
    Sala 2D: 100 sillas generales.
    """
    def __init__(self, nombre="Sala 2D"):
        super().__init__(nombre)
        self.crear_sillas()

    def crear_sillas(self):
        for i in range(1, 101):
            id_silla = f"G{i:03}"
            self._sillas.append(Silla(id_silla, 'general'))

    @property
    def tipo(self):
        return "2D"


class Sala3D(Sala):
    """
    Sala 3D: 80 sillas generales, 20 preferenciales.
    """
    def __init__(self, nombre="Sala 3D"):
        super().__init__(nombre)
        self.crear_sillas()

    def crear_sillas(self):
        for i in range(1, 81):
            id_silla = f"G{i:03}"
            self._sillas.append(Silla(id_silla, 'general'))
        for i in range(81, 101):
            id_silla = f"P{i:03}"
            self._sillas.append(Silla(id_silla, 'preferencial'))

    @property
    def tipo(self):
        return "3D"
