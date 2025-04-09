import unittest
from controllers.controlador_peliculas import ControladorPeliculas
from models.pelicula import Pelicula
from datetime import datetime, timedelta

class TestControladorPeliculas(unittest.TestCase):

    def setUp(self):
        self.controlador = ControladorPeliculas()

    def test_agregar_y_listar_peliculas(self):
        fechas = [{
            "fecha": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"),
            "hora": "18:00",
            "jornada": "noche"
        }]
        pelicula = Pelicula("Interstellar", "Ciencia ficción", "PG-13", fechas, 169, "Inglés", True)
        self.controlador.agregar_pelicula(pelicula)
        peliculas = self.controlador.listar_peliculas()
        self.assertEqual(len(peliculas), 1)
        self.assertEqual(peliculas[0].titulo, "Interstellar")

    def test_buscar_por_titulo(self):
        self.controlador.cargar_peliculas_predeterminadas()
        resultados = self.controlador.buscar_por_titulo("avatar")
        self.assertEqual(len(resultados), 1)
        self.assertIn("Avatar", resultados[0].titulo)

    def test_cargar_peliculas_predeterminadas(self):
        self.controlador.cargar_peliculas_predeterminadas()
        peliculas = self.controlador.listar_peliculas()
        self.assertEqual(len(peliculas), 3)

if __name__ == "__main__":
    unittest.main()
