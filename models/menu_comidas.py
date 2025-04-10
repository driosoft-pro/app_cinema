from typing import Literal
from dataclasses import dataclass

EstadoLiteral = Literal['activo', 'inactivo']

@dataclass
class ItemMenu:
    """Clase base para ítems del menú"""
    id_item: int
    codigo: str
    categoria: str
    producto: str
    tamano: str
    precio: float
    estado: EstadoLiteral = 'activo'
    
    def a_diccionario(self) -> dict:
        """Convierte el objeto a diccionario para serialización"""
        return {
            'id_item': self.id_item,
            'codigo': self.codigo,
            'categoria': self.categoria,
            'producto': self.producto,
            'tamano': self.tamano,
            'precio': self.precio,
            'estado': self.estado,
            'tipo': 'base'
        }

class Combo(ItemMenu):
    """Clase para combos especiales"""
    def __init__(self, id_item: int, codigo: str, producto: str, 
                tamano: str, precio: float, items_incluidos: list,
                estado: EstadoLiteral = 'activo'):
        super().__init__(id_item, codigo, 'combo', producto, tamano, precio, estado)
        self.items_incluidos = items_incluidos
        
    def a_diccionario(self) -> dict:
        """Convierte el objeto a diccionario para serialización"""
        datos = super().a_diccionario()
        datos.update({
            'items_incluidos': self.items_incluidos,
            'tipo': 'combo'
        })
        return datos

class Snack(ItemMenu):
    """Clase para snacks individuales"""
    def __init__(self, id_item: int, codigo: str, producto: str, 
                tamano: str, precio: float, 
                estado: EstadoLiteral = 'activo'):
        super().__init__(id_item, codigo, 'snack', producto, tamano, precio, estado)

class Bebida(ItemMenu):
    """Clase para bebidas"""
    def __init__(self, id_item: int, codigo: str, producto: str, 
                tamano: str, precio: float, 
                estado: EstadoLiteral = 'activo'):
        super().__init__(id_item, codigo, 'bebida', producto, tamano, precio, estado)

class Dulce(ItemMenu):
    """Clase para dulces"""
    def __init__(self, id_item: int, codigo: str, producto: str, 
                precio: float, 
                estado: EstadoLiteral = 'activo'):
        super().__init__(id_item, codigo, 'dulce', producto, 'Único', precio, estado)