from controllers.controlador_salas import ControladorSalas

def test_creacion_y_disponibilidad_de_salas():
    controlador = ControladorSalas()
    sala_2d = controlador.obtener_sala("2D")
    sala_3d = controlador.obtener_sala("3D")

    assert sala_2d is not None
    assert sala_3d is not None
    assert len(sala_2d.obtener_sillas()) == 100
    assert len(sala_3d.obtener_sillas()) == 100

def test_ocupar_y_liberar_silla():
    controlador = ControladorSalas()
    id_silla = "G001"
    tipo_sala = "2D"

    # Verifica que la silla esté libre inicialmente
    silla = controlador.buscar_silla_en_sala(tipo_sala, id_silla)
    assert silla is not None
    assert not silla.esta_ocupada()

    # Ocupar la silla
    resultado_ocupar = controlador.ocupar_silla(tipo_sala, id_silla)
    assert resultado_ocupar
    assert silla.esta_ocupada()

    # Intentar ocuparla nuevamente (debe fallar)
    resultado_ocupar_nuevamente = controlador.ocupar_silla(tipo_sala, id_silla)
    assert not resultado_ocupar_nuevamente

    # Liberar la silla
    resultado_liberar = controlador.liberar_silla(tipo_sala, id_silla)
    assert resultado_liberar
    assert not silla.esta_ocupada()

    # Intentar liberarla nuevamente (debe fallar)
    resultado_liberar_nuevamente = controlador.liberar_silla(tipo_sala, id_silla)
    assert not resultado_liberar_nuevamente