def crear_vector():
    """Crea y devuelve un vector (lista) vacío de servicios."""
    return []


def siguiente_codigo(servicios):
    """Calcula el siguiente código disponible para un nuevo servicio."""
    if len(servicios) == 0:
        return 1
    return max(servicio[0] for servicio in servicios) + 1


def registrar_servicio(servicios):
    """Pide los datos de un nuevo servicio y lo agrega al vector."""
    print("\n--- Registrar nuevo servicio ---")
    codigo = siguiente_codigo(servicios)
    nombre = input("Ingrese el nombre del servicio: ")
    descripcion = input("Ingrese la descripción del servicio: ")

    while True:
        try:
            precio = float(input("Ingrese el precio del servicio: "))
            break
        except ValueError:
            print("Precio inválido, ingrese solo números.")

    while True:
        try:
            duracion = int(input("Ingrese la duración del servicio (minutos): "))
            break
        except ValueError:
            print("Duración inválida, ingrese solo números enteros.")

    servicios.append([codigo, nombre, descripcion, precio, duracion])
    print(f"\nServicio '{nombre}' registrado con código {codigo}.")
    return servicios


def mostrar_servicios(servicios):
    """Imprime todos los servicios registrados en el vector."""
    print("\n" + "=" * 70)
    print("                    CATÁLOGO DE SERVICIOS")
    print("=" * 70)

    if len(servicios) == 0:
        print("No hay servicios registrados.")
    else:
        for servicio in servicios:
            print(f"\nCódigo     : {servicio[0]}")
            print(f"Nombre     : {servicio[1]}")
            print(f"Descripción: {servicio[2]}")
            print(f"Precio     : ${servicio[3]:.2f}")
            print(f"Duración   : {servicio[4]} min")
            print("-" * 70)

    print("=" * 70)


def buscar_servicio_por_codigo(servicios, codigo):
    """
    Búsqueda interna usada por la matriz: recibe un código y
    devuelve el servicio completo [codigo, nombre, descripcion,
    precio, duracion], o None si no existe.
    """
    for servicio in servicios:
        if servicio[0] == codigo:
            return servicio
    return None


def buscar_servicio(servicios):
    """Búsqueda interactiva (menú) por código o por nombre."""
    print("\n--- Buscar servicio ---")
    print("1. Buscar por código")
    print("2. Buscar por nombre")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo = int(input("Ingrese el código del servicio: "))
        resultado = buscar_servicio_por_codigo(servicios, codigo)
        if resultado:
            print("\nServicio encontrado:", resultado)
            return resultado
    elif opcion == "2":
        nombre = input("Ingrese el nombre del servicio: ")
        for servicio in servicios:
            if servicio[1].lower() == nombre.lower():
                print("\nServicio encontrado:", servicio)
                return servicio
    else:
        print("Opción inválida.")
        return None

    print("No se encontró ningún servicio con esos datos.")
    return None


def modificar_servicio(servicios):
    """Busca un servicio por código y permite modificar sus datos."""
    print("\n--- Modificar servicio ---")
    codigo = int(input("Ingrese el código del servicio a modificar: "))

    for servicio in servicios:
        if servicio[0] == codigo:
            print("Datos actuales:", servicio)
            print("(Presione ENTER para dejar un campo sin cambios)")

            nombre = input(f"Nuevo nombre [{servicio[1]}]: ")
            descripcion = input(f"Nueva descripción [{servicio[2]}]: ")
            precio = input(f"Nuevo precio [{servicio[3]}]: ")
            duracion = input(f"Nueva duración [{servicio[4]}]: ")

            if nombre != "":
                servicio[1] = nombre
            if descripcion != "":
                servicio[2] = descripcion
            if precio != "":
                servicio[3] = float(precio)
            if duracion != "":
                servicio[4] = int(duracion)

            print("\nServicio actualizado:", servicio)
            return servicios

    print("No se encontró ningún servicio con ese código.")
    return servicios


def eliminar_servicio(servicios):
    """Busca un servicio por código y lo elimina del vector."""
    print("\n--- Eliminar servicio ---")
    codigo = int(input("Ingrese el código del servicio a eliminar: "))

    for i in range(len(servicios)):
        if servicios[i][0] == codigo:
            eliminado = servicios.pop(i)
            print(f"\nServicio '{eliminado[1]}' eliminado correctamente.")
            return servicios

    print("No se encontró ningún servicio con ese código.")
    return servicios




def crear_matriz_agenda():
    """
    Pide empleados y días, y crea la matriz vacía
    (empleados x días), donde cada celda es una lista de citas.
    """
    n = int(input("Ingrese la cantidad de empleados de la empresa: "))
    empleados = [0] * n
    for i in range(n):
        empleados[i] = input(f"Ingresa el nombre del trabajador {i + 1}: ")
    print(empleados)

    print("\nDías de la semana:")
    print("1. Lunes 2. Martes 3. Miercoles 4. Jueves 5. Viernes 6. Sabado 7. Domingo")
    m = int(input("Ingrese hasta qué día de la semana desea administrar (1-7): "))
    todos_los_dias = ["Lunes", "Martes", "Miercoles", "Jueves",
                       "Viernes", "Sabado", "Domingo"]
    dias = [0] * m
    for i in range(m):
        dias[i] = todos_los_dias[i]
    print(dias)

    matriz = [[[] for _ in range(m)] for _ in range(n)]
    return empleados, dias, matriz


def llenar_agenda(empleados, dias, matriz, servicios):
    """
    Llena la matriz de citas. Aquí ocurre la INTEGRACIÓN:
    en vez de escribir el servicio como texto libre, se elige
    un código del vector de servicios.
    """
    n = len(empleados)
    m = len(dias)

    if len(servicios) == 0:
        print("\nNo hay servicios registrados en el catálogo todavía.")
        print("Registre al menos un servicio antes de armar la agenda.")
        return matriz

    for i in range(n):
        print(f"\n========== Agenda de {empleados[i]} ==========")
        for j in range(m):
            print(f"\n--- {dias[j]} ---")
            cantidad = int(input("¿Cuántos servicios tiene este día?: "))
            for k in range(cantidad):
                print(f"\nServicio {k + 1}")
                cliente = input("Ingrese el nombre del cliente: ")
                telefono = input("Ingrese el teléfono del cliente: ")

               
                mostrar_servicios(servicios)
                servicio_elegido = None
                while servicio_elegido is None:
                    codigo = int(input("Ingrese el código del servicio a agendar: "))
                    servicio_elegido = buscar_servicio_por_codigo(servicios, codigo)
                    if servicio_elegido is None:
                        print("Código no válido, intente de nuevo.")

                hora = input("Ingrese la hora: ")
                direccion = input("Ingrese la dirección: ")

                matriz[i][j].append([
                    cliente,
                    telefono,
                    servicio_elegido,  
                    hora,
                    direccion
                ])

    return matriz


def mostrar_agenda(empleados, dias, matriz):
    """Imprime la agenda completa, incluyendo los datos del
    servicio tomados desde el vector."""
    n = len(empleados)
    m = len(dias)

    print("\n")
    print("=" * 70)
    print("                    AGENDA DE SERVICIOS")
    print("=" * 70)

    for i in range(n):
        print(f"\nEMPLEADO: {empleados[i]}")
        print("-" * 70)
        for j in range(m):
            print(f"\n{dias[j]}")
            if len(matriz[i][j]) == 0:
                print("  Sin servicios programados")
            else:
                for k in range(len(matriz[i][j])):
                    cita = matriz[i][j][k]
                    servicio_info = cita[2]  
                    print(f"\n  Servicio {k + 1}")
                    print(f"    Cliente     : {cita[0]}")
                    print(f"    Teléfono    : {cita[1]}")
                    print(f"    Servicio    : {servicio_info[1]} (código {servicio_info[0]})")
                    print(f"    Precio      : ${servicio_info[3]:.2f}")
                    print(f"    Duración    : {servicio_info[4]} min")
                    print(f"    Hora        : {cita[3]}")
                    print(f"    Dirección   : {cita[4]}")
        print("-" * 70)




def main():
  
    servicios = crear_vector()

    print("=" * 70)
    print("   PASO 1: REGISTRAR EL CATÁLOGO DE SERVICIOS DE LA EMPRESA")
    print("=" * 70)

    seguir = "s"
    while seguir.lower() == "s":
        servicios = registrar_servicio(servicios)
        seguir = input("\n¿Desea registrar otro servicio? (s/n): ")

    mostrar_servicios(servicios)

  
    print("\n" + "=" * 70)
    print("   PASO 2: ARMAR LA AGENDA (MATRIZ EMPLEADOS x DÍAS)")
    print("=" * 70)

    empleados, dias, matriz = crear_matriz_agenda()

    matriz = llenar_agenda(empleados, dias, matriz, servicios)

   
    mostrar_agenda(empleados, dias, matriz)


if __name__ == "__main__":
    main()
