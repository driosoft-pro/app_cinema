from models.pelicula import Pelicula
from datetime import datetime, timedelta

class ControladorPeliculas:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula: Pelicula):
        self.peliculas.append(pelicula)

    def listar_peliculas(self):
        return self.peliculas

    def buscar_por_titulo(self, titulo: str):
        return [p for p in self.peliculas if titulo.lower() in p.titulo.lower()]

    def cargar_peliculas_predeterminadas(self):
        hoy = datetime.now()
        jornada = "tarde"
        hora = "15:00"

        def generar_fechas(n=5):
            return [
                {
                    "fecha": (hoy + timedelta(days=i)).strftime("%Y-%m-%d"),
                    "hora": hora,
                    "jornada": jornada
                } for i in range(n)
            ]

        predeterminadas = [
            Pelicula("Avatar 2", "Ciencia ficción", "PG-13", generar_fechas(), 160, "Español", True),
            Pelicula("Mario Bros", "Animación", "G", generar_fechas(), 90, "Español", False),
            Pelicula("Oppenheimer", "Drama", "R", generar_fechas(), 180, "Inglés", True),
        ]

        self.peliculas.extend(predeterminadas)
