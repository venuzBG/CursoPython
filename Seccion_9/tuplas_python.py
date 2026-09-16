# Tuplas

# my_tupla = (1, 2, 3, 4, 5)

# print(my_tupla)

# for elementos in my_tupla:
#     print(elementos, end = " ")
    
# # tupla de un elemento

# tupla_1 = 10,
# print(tupla_1)

# # tupla anidada

# tupla_anidada = (1, 2, (3,5), [24,5], 6)

# print(f"Segundo elemento: {tupla_anidada[2]}")

# Desempaquetado de tuplas

producto = ("P001", "Camisa", 20.00)

# Desempaquetado
id, descripcion, precio = producto

print(f"Tupla completa: {producto}")

# Valores independientes

print(f"Producto: id = {id}, descripcion = {descripcion}, precio = {precio}")
