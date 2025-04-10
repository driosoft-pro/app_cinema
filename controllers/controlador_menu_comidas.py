from typing import List, Optional, Dict
from models.menu_comidas import ItemMenu, Combo, Snack, Bebida, Dulce

class ControladorMenuComidas:
    def __init__(self):
        self.items: List[ItemMenu] = []
        self._cargar_items_por_defecto()

    def _cargar_items_por_defecto(self):
        """Carga ítems iniciales al menú"""

        # Snacks
        self.items.extend([
            Snack(1, "S001", "Crispetas Pequeñas", "pequeño", 8000),
            Snack(2, "S002", "Crispetas Medianas", "mediano", 15000),
            Snack(3, "S003", "Crispetas Grandes", "grande", 20000),
            Snack(4, "S004", "Nachos con Queso", "único", 18000),
            Snack(5, "S005", "Perro Caliente", "único", 12000),
            Snack(6, "S006", "Hamburguesa Sencilla", "único", 15000),
        ])

        # Bebidas
        self.items.extend([
            Bebida(7, "B001", "Gaseosa Pequeña", "pequeño", 6000),
            Bebida(8, "B002", "Gaseosa Mediana", "mediano", 8000),
            Bebida(9, "B003", "Gaseosa Grande", "grande", 10000),
            Bebida(10, "B004", "Agua Embotellada", "único", 5000),
            Bebida(11, "B005", "Jugo en Caja", "único", 7000),
        ])

        # Dulces
        self.items.extend([
            Dulce(12, "D001", "Chocolatina", 4000),
            Dulce(13, "D002", "Paquete de Dulces", 6000),
        ])

        # Combos
        self.items.extend([
            Combo(14, "C001", "Combo Crispetas Pequeñas + Gaseosa Pequeña", "pequeño", 15000, ["Crispetas Pequeñas", "Gaseosa Pequeña"]),
            Combo(15, "C002", "Combo Crispetas Medianas + Gaseosa Mediana", "mediano", 22000, ["Crispetas Medianas", "Gaseosa Mediana"]),
            Combo(16, "C003", "Combo Crispetas Grandes + Gaseosa Grande", "grande", 28000, ["Crispetas Grandes", "Gaseosa Grande"]),
            Combo(17, "C004", "Combo Crispetas Familiares + 2 Gaseosas Grandes", "familiar", 35000, ["Crispetas Grandes", "Gaseosa Grande", "Gaseosa Grande"]),
        ])

    def obtener_siguiente_id_item(self) -> int:
        """Obtiene el próximo ID autoincremental"""
        return max((item.id_item for item in self.items), default=0) + 1

    def crear_item(self, datos_item: Dict) -> Optional[ItemMenu]:
        """Crea un nuevo ítem en el menú"""
        try:
            id_item = self.obtener_siguiente_id_item()
            tipo_item = datos_item.get('tipo', 'base')

            if tipo_item == 'combo':
                item = Combo(
                    id_item=id_item,
                    codigo=datos_item['codigo'],
                    producto=datos_item['producto'],
                    tamano=datos_item['tamano'],
                    precio=datos_item['precio'],
                    items_incluidos=datos_item['items_incluidos']
                )
            elif tipo_item == 'snack':
                item = Snack(
                    id_item=id_item,
                    codigo=datos_item['codigo'],
                    producto=datos_item['producto'],
                    tamano=datos_item['tamano'],
                    precio=datos_item['precio']
                )
            elif tipo_item == 'bebida':
                item = Bebida(
                    id_item=id_item,
                    codigo=datos_item['codigo'],
                    producto=datos_item['producto'],
                    tamano=datos_item['tamano'],
                    precio=datos_item['precio']
                )
            elif tipo_item == 'dulce':
                item = Dulce(
                    id_item=id_item,
                    codigo=datos_item['codigo'],
                    producto=datos_item['producto'],
                    precio=datos_item['precio']
                )
            else:
                return None

            self.items.append(item)
            return item

        except Exception as e:
            print(f"Error al crear el ítem del menú: {e}")
            return None

    def obtener_todos_los_items(self) -> List[ItemMenu]:
        """Obtiene todos los ítems del menú"""
        return self.items

    def obtener_items_por_categoria(self, categoria: str) -> List[ItemMenu]:
        """Obtiene ítems por categoría"""
        return [item for item in self.items if item.categoria.lower() == categoria.lower()]

    def obtener_items_activos(self) -> List[ItemMenu]:
        """Obtiene ítems activos"""
        return [item for item in self.items if item.estado == 'activo']

    def actualizar_item(self, id_item: int, datos_actualizados: Dict) -> bool:
        """Actualiza un ítem del menú"""
        item = next((i for i in self.items if i.id_item == id_item), None)
        if not item:
            return False

        for clave, valor in datos_actualizados.items():
            if hasattr(item, clave):
                setattr(item, clave, valor)

        return True

    def cambiar_estado_item(self, id_item: int, estado: str) -> bool:
        """Cambia el estado de un ítem"""
        item = next((i for i in self.items if i.id_item == id_item), None)
        if not item:
            return False

        item.estado = estado
        return True
