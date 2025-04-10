from models.pelicula import Pelicula
from datetime import datetime, timedelta

class ControladorPeliculas:
    def __init__(self):
        self.peliculas = []
        self.cargar_peliculas_predeterminadas()

    def agregar_pelicula(self, pelicula: Pelicula):
        self.peliculas.append(pelicula)

    def eliminar_pelicula(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                self.peliculas.remove(pelicula)
                return True
        return False
    
    def editar_pelicula(self, titulo_original, pelicula_editada):
        for i, pelicula in enumerate(self.peliculas):
            if pelicula.titulo == titulo_original:
                self.peliculas[i] = pelicula_editada
                return True
        return False

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

    def obtener_peliculas_activas(self):
        return [p for p in self.peliculas if p.estado == 1]   
