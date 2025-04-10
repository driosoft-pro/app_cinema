from dataclasses import dataclass
from datetime import datetime
from typing import Literal
import uuid

MetodoPagoLiteral = Literal['efectivo', 'tarjeta', 'transferencia']

@dataclass
class Pago:
    id_pago: str
    metodo: MetodoPagoLiteral
    monto: float
    valor_pagado: float
    cambio: float
    fecha_pago: str

    @classmethod
    def crear_pago(cls, metodo: MetodoPagoLiteral, monto: float, valor_pagado: float) -> 'Pago':
        """Crea un nuevo objeto Pago con los datos calculados"""
        cambio = round(valor_pagado - monto, 2) if metodo == 'efectivo' else 0.0
        return cls(
            id_pago=str(uuid.uuid4()),
            metodo=metodo,
            monto=monto,
            valor_pagado=valor_pagado,
            cambio=cambio,
            fecha_pago=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

    def a_diccionario(self) -> dict:
        return {
            'id_pago': self.id_pago,
            'metodo': self.metodo,
            'monto': self.monto,
            'valor_pagado': self.valor_pagado,
            'cambio': self.cambio,
            'fecha_pago': self.fecha_pago
        }

    @staticmethod
    def desde_diccionario(data: dict) -> 'Pago':
        return Pago(
            id_pago=data['id_pago'],
            metodo=data['metodo'],
            monto=data['monto'],
            valor_pagado=data['valor_pagado'],
            cambio=data['cambio'],
            fecha_pago=data['fecha_pago']
        )
