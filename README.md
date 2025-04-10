# 🎟️ Sistema de Venta de Entradas para un Cinema

Este proyecto es una aplicación en consola desarrollada en Python que permite gestionar la venta y reserva de entradas para un cinema con dos salas (2D y 3D), además de integrar funcionalidades para la gestión de usuarios, películas, menú de comida y métodos de pago.

## 🧩 Características principales

- **Salas de cine:**  
  - Sala 2D: todas las boletas son generales.  
  - Sala 3D: boletas generales y preferenciales.  
  - Cada sala tiene 100 sillas: 80 generales, 20 preferenciales.

- **Precios de entradas:**  
  - Estándar: $18.000  
  - Preferencial: $25.000  
  - Niño (menor de 12): $15.000  
  - Adulto mayor (mayor de 60): $16.000  
  - **Promoción 2x1:** Martes y jueves en la tarde para sillas preferenciales.

- **Usuarios:**  
  - Cliente: puede registrarse, comprar, reservar, cancelar, ver sus datos y consultar películas y menú de comida.  
  - Administrador: puede gestionar usuarios, películas, menú, reservas, ventas y trazabilidad completa del sistema.  

- **Películas:**  
  - Clasificación por edad (G, PG, PG-13, R, C).  
  - Atributos: título, director, sinopsis, duración, idioma, origen, fechas, horarios, jornada, estado.  
  - Mínimo 20 películas disponibles durante 15 días.

- **Reservas:**  
  - Permitidas de 2 a 7 días antes.  
  - Cancelaciones permitidas de 1 a 2 días antes.

- **Pagos:**  
  - Reservas: efectivo, tarjeta, transferencia.  
  - Compras: efectivo, tarjeta (con cálculo de cambio).

- **Menú de comida:**  
  - Combos, snacks, bebidas y dulces con sus respectivos precios.  
  - Clientes y administradores pueden consultar; solo el administrador puede gestionar.

## 🛠️ Tecnologías utilizadas

- **Python 3.11+**
- **Programación orientada a objetos (POO):**  
  - Herencia, encapsulamiento, polimorfismo (sobrecarga y sobreescritura).
- **Rich** y **Pyfiglet** para la interfaz en consola.
- **Entorno virtual** para la gestión de dependencias.
- **PEP8** para la documentación y comentarios del código.

---

## 🗃️ Estructura del proyecto

```bash
app_cinema/
│
├── main.py
├── .gitignore
├── README.md
│
├── doc/
│   ├── diagramaClaseSistemaVentaCinema.png
│   ├── diagramaFlujoSistemaVentaCinema.png
│   ├── requerimientos.txt
│   └── requerimientosDetallados.txt
│
├── img/
│   └── imagenes de aplicacion en funcionamiento .jpg
│
├── pseudocodigo/
│   ├── calculo_precios.md
│   ├── comprar_entrada.md
│   ├── estructura_principal.md
│   ├── gestion_peliculas.md
│   ├── registro_usuario.md
│   └── validaciones.md
│
├── controllers/
│   ├── __init__.py
│   ├── controlador_menu_comidas.py
│   ├── controlador_pagos.py
│   ├── controlador_peliculas.py
│   ├── controlador_reservacion.py
│   ├── controlador_salas.py
│   ├── controlador_ticket.py
│   └── controlador_usuarios.py
│
├── models/
│   ├── __init__.py
│   ├── menu_comidas.py
│   ├── pagos.py
│   ├── pelicula.py
│   ├── reservacion.py
│   ├── sala.py
│   ├── silla.py
│   ├── ticket.py
│   └── usuario.py
│
├── services/
│   ├── auth_services.py
│   └── date_utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_controlador_menu_comidas.py
│   ├── test_controlador_pagos.py
│   ├── test_controlador_peliculas.py
│   ├── test_controlador_reservacion.py
│   ├── test_controlador_sala.py
│   ├── test_controlador_ticket.py
│   └── test_controlador_usuarios.py
│
└── views/
    ├── compra_views.py
    ├── menu_admin.py
    ├── menu_cliente.py
    └── peliculas_views.py
```

---

## Autor
📌 **By:** Deyton Riascos Ortiz
            Dana Isabella Mosquera Mosquera
            Samuel Izquierdo Bonilla 