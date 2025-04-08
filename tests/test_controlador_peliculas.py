import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.controlador_peliculas import ControladorPeliculas
from models.pelicula import Pelicula

def test_agregar_y_listar_peliculas():
    controlador = ControladorPeliculas()
    peli = Pelicula("Avatar 2", "Ciencia ficción", "PG-13", 160, "Español", True)
    controlador.agregar_pelicula(peli)
    assert peli in controlador.listar_peliculas()

def test_carga_peliculas_predeterminadas():
    controlador = ControladorPeliculas()
    controlador.cargar_peliculas_predeterminadas()
    assert len(controlador.listar_peliculas()) == 20

if __name__ == "__main__":
    test_agregar_y_listar_peliculas()
    test_carga_peliculas_predeterminadas()
    print("✅ Test de películas (agregar + carga predeterminada) pasaron correctamente.")