n = int(input("Ingrese la cantidad de empleados de la empresa: "))
empleado = 0
empleados = [0]*n

for i in n:
  empleado = string(input(f"Ingresa el nombre del trabajador {i+1}: "))
  empleados[i] = empleado
print(empleados)
