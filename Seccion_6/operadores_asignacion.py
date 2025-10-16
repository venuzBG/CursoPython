# Operadores de asignacion

numero = 5
print(f'Valor inicial: {numero}')
numero = 10
print(f'Nuevo valor: {numero}')

# Asignacion multiple 

x, y, z = 1, 2, 3
print(f'Valores iniciales: x={x}, y={y}, z={z}')


# Asignacion encadenada

a = b = c = 20
print(f'Valores asignados: a={a}, b={b}, c={c}')

# Intercambio de valores de una variable, sin usar una variable temporal

x, y = 5, 4
print(f'Antes del intercambio: x={x}, y={y}')

# Aplicando el concepto de asignacion multiple, intercambiar valores
x, y = y, x
print(f'Despues del intercambio: x={x}, y={y}')

# Podemos recibir multiples valores de entrada del usuario 

nombre, apellido = input('Ingrese su nombre y apellido: ').split()

print(f'Nombre: {nombre}, Apellido: {apellido}')