import uuid
from datetime import datetime
from typing import Literal, Optional
from models.pagos import Pago

# Tipos válidos de métodos de pago
MetodoPagoLiteral = Literal["efectivo", "tarjeta", "transferencia"]

class ControladorPagos:
    def __init__(self):
        self.pagos = []  # Lista local para pruebas, luego se conecta al JSON

    def generar_id_pago(self) -> str:
        """Genera un ID único para el pago"""
        return str(uuid.uuid4())

    def registrar_pago(self, metodo: MetodoPagoLiteral, monto: float, 
                    valor_pagado: Optional[float] = None) -> Pago:
        """Registra un nuevo pago y retorna el objeto"""
        if metodo not in ["efectivo", "tarjeta", "transferencia"]:
            raise ValueError("Método de pago no válido")

        if metodo == "efectivo":
            if valor_pagado is None or valor_pagado < monto:
                raise ValueError("El valor pagado debe ser mayor o igual al monto para pagos en efectivo")
        else:
            valor_pagado = monto  # Para tarjeta o transferencia

        nuevo_pago = Pago.crear_pago(metodo=metodo, monto=monto, valor_pagado=valor_pagado)
        self.pagos.append(nuevo_pago)
        return nuevo_pago


    def obtener_pago_por_id(self, id_pago: str) -> Optional[Pago]:
        """Consulta un pago por su ID"""
        for pago in self.pagos:
            if pago.id_pago == id_pago:
                return pago
        return None

    def listar_pagos(self) -> list[Pago]:
        """Lista todos los pagos registrados"""
        return self.pagos
