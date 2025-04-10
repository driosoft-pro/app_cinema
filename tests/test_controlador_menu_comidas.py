import unittest
from controllers.controlador_menu_comidas import ControladorMenuComidas
from models.menu_comidas import Dulce

class FakeBD:
    def __init__(self):
        self.items = []
        self.siguiente_id = 1

    def obtener_todos_los_items_comida(self):
        return self.items

    def obtener_item_comida(self, id_item):
        for item in self.items:
            if item.id_item == id_item:
                return item
        return None

    def guardar_item_comida(self, item):
        for i, actual in enumerate(self.items):
            if actual.id_item == item.id_item:
                self.items[i] = item
                return True
        self.items.append(item)
        return True

class TestControladorMenuComidas(unittest.TestCase):
    def setUp(self):
        self.bd = FakeBD()
        self.controlador = ControladorMenuComidas(self.bd)

    def test_crear_item_dulce(self):
        datos_dulce = {
            'tipo': 'dulce',
            'codigo': 'D1',
            'producto': 'Gomitas',
            'precio': 3000
        }

        item = self.controlador.crear_item(datos_dulce)

        self.assertIsNotNone(item)
        self.assertEqual(item.codigo, 'D1')
        self.assertEqual(item.producto, 'Gomitas')
        self.assertEqual(item.precio, 3000)
        self.assertEqual(item.categoria, 'dulce')

if __name__ == '__main__':
    unittest.main()
