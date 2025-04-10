import unittest
from controllers.controlador_pagos import ControladorPagos
from models.pagos import Pago

class TestControladorPagos(unittest.TestCase):
    def setUp(self):
        self.controlador = ControladorPagos()

    def test_registrar_pago_valido_efectivo(self):
        pago = self.controlador.registrar_pago(metodo="efectivo", monto=20000, valor_pagado=25000)
        self.assertIsInstance(pago, Pago)
        self.assertEqual(pago.metodo, "efectivo")
        self.assertEqual(pago.monto, 20000)
        self.assertEqual(pago.valor_pagado, 25000)
        self.assertEqual(pago.cambio, 5000)

    def test_registrar_pago_valido_tarjeta(self):
        pago = self.controlador.registrar_pago(metodo="tarjeta", monto=15000)
        self.assertIsInstance(pago, Pago)
        self.assertEqual(pago.metodo, "tarjeta")
        self.assertEqual(pago.monto, 15000)
        self.assertEqual(pago.valor_pagado, 15000)
        self.assertEqual(pago.cambio, 0)

    def test_registrar_pago_invalido(self):
        with self.assertRaises(ValueError):
            self.controlador.registrar_pago(metodo="cheque", monto=10000, valor_pagado=10000)

    def test_registrar_pago_efectivo_sin_valor_suficiente(self):
        with self.assertRaises(ValueError):
            self.controlador.registrar_pago(metodo="efectivo", monto=10000, valor_pagado=5000)

    def test_obtener_pago_por_id(self):
        pago = self.controlador.registrar_pago(metodo="efectivo", monto=10000, valor_pagado=10000)
        resultado = self.controlador.obtener_pago_por_id(pago.id_pago)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.id_pago, pago.id_pago)

    def test_listar_pagos(self):
        self.controlador.registrar_pago(metodo="efectivo", monto=10000, valor_pagado=10000)
        self.controlador.registrar_pago(metodo="tarjeta", monto=15000)
        pagos = self.controlador.listar_pagos()
        self.assertEqual(len(pagos), 2)

if __name__ == '__main__':
    unittest.main()
