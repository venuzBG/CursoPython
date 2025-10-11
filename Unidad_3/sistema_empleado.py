#Sistema de empleado 
print("Bienvenido al sistema de empleados")
nombre_empleado = input("Introduce el nombre del empleado: \n")
edad_empleado = int(input("Introduce la edad del empleado: \n"))
salario_empleado = float(input("Introduce el salario del empleado: \n"))
es_jefe_departamento = input("¿Es jefe de departamento? (si/no): \n")

#Vamos a convertir en booleano la variable es_jefe_departamento

es_jefe_departamento = es_jefe_departamento.lower() == "si"

print("\n---Datos del empleado---")
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
print(f"Salario: {salario_empleado:.2f}")
print(f"Es jefe de departamento: {es_jefe_departamento}")
# Entrada de datos por consola