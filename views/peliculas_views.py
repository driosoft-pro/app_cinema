from models.pelicula import Pelicula

def mostrar_peliculas(peliculas):
    peliculas_activas = [p for p in peliculas if p.estado == 1]
    if not peliculas_activas:
        print("No hay películas activas disponibles.")
    else:
        print("\n--- Cartelera ---")
        for i, peli in enumerate(peliculas_activas, 1):
            print(f"{i}. {peli} (Estado: Activa)")

def mostrar_peliculas_filtradas(peliculas):
    if not peliculas:
        print("No hay películas registradas.")
    else:
        print("\n--- Lista de Películas (Filtradas por Estado) ---")
        for i, peli in enumerate(peliculas, 1):
            estado = "Activa" if peli.estado == 1 else "Inactiva"
            print(f"{i}. {peli} (Estado: {estado})")

def gestionar_peliculas(controlador_peliculas):
    while True:
        print("\n--- Gestión de Películas ---")
        print("1. Ver todas las películas")
        print("2. Agregar nueva película")
        print("3. Editar una película")
        print("4. Eliminar una película")
        print("5. Volver")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_peliculas_filtradas(controlador_peliculas.listar_peliculas())

        elif opcion == "2":
            try:
                titulo = input("Título: ")
                genero = input("Género: ")
                clasificacion = input("Clasificación (G, PG, PG-13, R, C): ")
                duracion = int(input("Duración en minutos: "))
                idioma = input("Idioma: ")
                subtitulada = input("¿Está subtitulada? (s/n): ").lower() == "s"
                fechas = []
                while True:
                    agregar_fecha = input("¿Desea agregar una función? (s/n): ").lower()
                    if agregar_fecha != "s":
                        break
                    fecha = input("Fecha (YYYY-MM-DD): ")
                    hora = input("Hora (HH:MM): ")
                    jornada = input("Jornada (mañana/tarde/noche): ")
                    fechas.append({"fecha": fecha, "hora": hora, "jornada": jornada})

                nueva_pelicula = Pelicula(titulo, genero, clasificacion, fechas, duracion, idioma, subtitulada)
                controlador_peliculas.agregar_pelicula(nueva_pelicula)
                print("Película agregada con éxito.")

            except ValueError:
                print("Error en los datos ingresados.")

        elif opcion == "3":
            peliculas = controlador_peliculas.listar_peliculas()
            mostrar_peliculas_filtradas(peliculas)
            try:
                indice = int(input("Ingrese el número de la película a editar: ")) - 1
                if 0 <= indice < len(peliculas):
                    pelicula = peliculas[indice]
                    print("Deje en blanco si no desea modificar un campo.")
                    nuevo_titulo = input(f"Nuevo título ({pelicula.titulo}): ") or pelicula.titulo
                    nuevo_genero = input(f"Nuevo género ({pelicula.genero}): ") or pelicula.genero
                    nuevo_clasificacion = input(f"Nueva clasificación ({pelicula.clasificacion}): ") or pelicula.clasificacion
                    nuevo_duracion = input(f"Nueva duración ({pelicula.duracion}): ") or str(pelicula.duracion)
                    nuevo_idioma = input(f"Nuevo idioma ({pelicula.idioma}): ") or pelicula.idioma
                    nueva_subtitulada = input(f"¿Está subtitulada? ({'sí' if pelicula.subtitulada else 'no'}): ").lower()
                    subtitulada = pelicula.subtitulada if nueva_subtitulada not in ["s", "n"] else nueva_subtitulada == "s"

                    nuevo_estado = input(f"¿Desea cambiar el estado de la película? (actual: {'activa' if pelicula.estado == 1 else 'inactiva'}) (s/n): ").lower()
                    if nuevo_estado == "s":
                        estado = 0 if pelicula.estado == 1 else 1
                    else:
                        estado = pelicula.estado

                    pelicula_editada = Pelicula(
                        nuevo_titulo,
                        nuevo_genero,
                        nuevo_clasificacion,
                        pelicula.fecha,
                        int(nuevo_duracion),
                        nuevo_idioma,
                        subtitulada,
                        estado
                    )
                    controlador_peliculas.editar_pelicula(pelicula.titulo, pelicula_editada)
                    print("Película editada exitosamente.")
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "4":
            peliculas = controlador_peliculas.listar_peliculas()
            mostrar_peliculas_filtradas(peliculas)
            try:
                indice = int(input("Ingrese el número de la película a eliminar: ")) - 1
                if 0 <= indice < len(peliculas):
                    titulo = peliculas[indice].titulo
                    confirmado = input(f"¿Está seguro de que desea eliminar '{titulo}'? (s/n): ").lower()
                    if confirmado == "s":
                        if controlador_peliculas.eliminar_pelicula(titulo):
                            print("Película eliminada exitosamente.")
                        else:
                            print("No se pudo eliminar la película.")
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "5":
            break

        else:
            print("Opción inválida.")
