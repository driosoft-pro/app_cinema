from typing import List, Optional, Dict
from models.menu_comidas import ItemMenu, Combo, Snack, Bebida, Dulce

class ControladorMenuComidas:
    def __init__(self, bd):
        self.bd = bd
    
    def obtener_siguiente_id_item(self) -> int:
        """Obtiene el próximo ID autoincremental"""
        items = self.bd.obtener_todos_los_items_comida()
        return max(item.id_item for item in items) + 1 if items else 1
    
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
                
            self.bd.guardar_item_comida(item)
            return item
            
        except Exception as e:
            print(f"Error al crear el ítem del menú: {e}")
            return None
    
    def obtener_todos_los_items(self) -> List[ItemMenu]:
        """Obtiene todos los ítems del menú"""
        return self.bd.obtener_todos_los_items_comida()
    
    def obtener_items_por_categoria(self, categoria: str) -> List[ItemMenu]:
        """Obtiene ítems por categoría"""
        return [item for item in self.bd.obtener_todos_los_items_comida() 
                if item.categoria.lower() == categoria.lower()]
    
    def obtener_items_activos(self) -> List[ItemMenu]:
        """Obtiene ítems activos"""
        return [item for item in self.bd.obtener_todos_los_items_comida() 
                if item.estado == 'activo']
    
    def actualizar_item(self, id_item: int, datos_actualizados: Dict) -> bool:
        """Actualiza un ítem del menú"""
        item = self.bd.obtener_item_comida(id_item)
        if not item:
            return False
            
        for clave, valor in datos_actualizados.items():
            if hasattr(item, clave):
                setattr(item, clave, valor)
                
        return self.bd.guardar_item_comida(item)
    
    def cambiar_estado_item(self, id_item: int, estado: str) -> bool:
        """Cambia el estado de un ítem"""
        item = self.bd.obtener_item_comida(id_item)
        if not item:
            return False
            
        item.estado = estado
        return self.bd.guardar_item_comida(item)
