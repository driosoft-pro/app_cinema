from models.pelicula import Pelicula

class ControladorPeliculas:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def listar_peliculas(self):
        return self.peliculas

    def buscar_por_titulo(self, titulo):
        return [p for p in self.peliculas if titulo.lower() in p.titulo.lower()]
    
    def cargar_peliculas_predeterminadas(self):
        predeterminadas = [
            Pelicula("Avatar 2", "Ciencia ficción", "PG-13", 160, "Español", True),
            Pelicula("Mario Bros", "Animación", "G", 90, "Español", False),
            Pelicula("John Wick 4", "Acción", "R", 140, "Inglés", True),
            Pelicula("Barbie", "Comedia", "PG", 115, "Español", False),
            Pelicula("Oppenheimer", "Drama", "R", 180, "Inglés", True),
            Pelicula("Paw Patrol", "Infantil", "G", 88, "Español", False),
            Pelicula("La Monja 2", "Terror", "C", 110, "Inglés", True),
            Pelicula("Los Juegos del Hambre", "Acción", "PG-13", 130, "Español", True),
            Pelicula("Rapidos y Furiosos X", "Acción", "PG-13", 145, "Español", False),
            Pelicula("Titanic", "Romance", "PG-13", 195, "Inglés", True),
            Pelicula("Frozen II", "Animación", "G", 103, "Español", False),
            Pelicula("El Exorcista", "Terror", "C", 122, "Español", True),
            Pelicula("Shrek", "Animación", "G", 93, "Español", False),
            Pelicula("La La Land", "Musical", "PG-13", 128, "Inglés", True),
            Pelicula("Dune", "Ciencia ficción", "PG-13", 156, "Inglés", True),
            Pelicula("Spider-Man: No Way Home", "Acción", "PG-13", 148, "Español", True),
            Pelicula("Coco", "Animación", "G", 105, "Español", False),
            Pelicula("IT", "Terror", "C", 135, "Inglés", True),
            Pelicula("La Sirenita", "Musical", "PG", 125, "Español", True),
            Pelicula("Elemental", "Animación", "G", 101, "Español", False),
        ]
        self.peliculas.extend(predeterminadas)