n = int(input("Ingrese la cantidad de empleados de la empresa: "))
empleados = [0]*n

for i in range(n):
  empleado = input(f"Ingresa el nombre del trabajador {i+1}: ")
  empleados[i] = empleado

print(empleados)

print("\nDías de la semana:")
print("1. Lunes 2. Martes 3. Miercoles 4. Jueves 5. Viernes 6. Sabado 7. Domingo")

m = int(input("Ingrese hasta qué día de la semana desea administrar (1-7): "))

todos_los_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

dias = [0] * m

for i in range(m):
    dias[i] = todos_los_dias[i]

print(dias)

matriz = [[[] for _ in range(m)] for _ in range(n)]

for i in range(n):

    print(f"\n========== Agenda de {empleados[i]} ==========")

    for j in range(m):

        print(f"\n--- {dias[j]} ---")

        cantidad = int(input("¿Cuántos servicios tiene este día?: "))

        for k in range(cantidad):

            print(f"\nServicio {k + 1}")

            cliente = input("Ingrese el nombre del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            servicio = input("Ingrese el servicio: ")
            hora = input("Ingrese la hora: ")
            direccion = input("Ingrese la dirección: ")

            matriz[i][j].append([
                cliente,
                telefono,
                servicio,
                hora,
                direccion
            ])


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

                print(f"\n  Servicio {k + 1}")
                print(f"    Cliente: {matriz[i][j][k][0]}")
                print(f"    Teléfono: {matriz[i][j][k][1]}")
                print(f"    Servicio: {matriz[i][j][k][2]}")
                print(f"    Hora: {matriz[i][j][k][3]}")
                print(f"    Dirección: {matriz[i][j][k][4]}")

    print("-" * 70)
