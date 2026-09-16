# print("Lista de suscriptores")

# suscriptores = {"luisa@gamil.com", "marcos@gmail.com", "elena@gmail.com"}
# print(f"Lista de suscriptores inicial: {suscriptores}")

# nuevo_suscriptor = "Sebas@gmail.com"

# if nuevo_suscriptor in suscriptores:
#     print("Ya existe esa cuenta")
# else:
#     suscriptores.add(nuevo_suscriptor)
#     print(f"El nuevo suscrptor se ha agregado a la lista {nuevo_suscriptor}")

# print(f"Lista de suscriptores: {suscriptores}")

# # Eliminamos a un sucriptor

# suscrptor_eliminado = "elena@gmail.com"

# suscriptores.remove(suscrptor_eliminado)

# print(f"El suscriptor {suscrptor_eliminado} ha sido eliminado de la lista ")
# print(f"Lista de suscriptores: {suscriptores}")

# # Verificamos la cantidad total de suscriptores

# print(f"Cantidad total de suscriptores: {len(suscriptores)}")

# print("--- Lista de suscriptores ---")

# for suscriptor in suscriptores:
#     print(f"- {suscriptor   }")

# Ahora mas dinamico

# Definimos un set vacio

# suscriptores = {} no es la forma corecta de declarar una set vaio esa sintaxis es para un diccionario

suscriptores = set() # Definir un set vacio

numero_suscriptor = int(input("Proporciona el  numero de suscriptores: "))

for i in range(numero_suscriptor):
    suscriptores.add(input("Nuevo suscriptor (email): "))
    
print(f"Lista de suscriptores inicial: {suscriptores}")


nuevo_suscriptor = input("Ingrese el nuevo suscriptor: ")

if nuevo_suscriptor in suscriptores:
    print("Ya existe esa cuenta")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"El nuevo suscrptor se ha agregado a la lista {nuevo_suscriptor}")

print(f"Lista de suscriptores: {suscriptores}")

# Eliminamos a un sucriptor

suscrptor_eliminado = input("Ingrese el suscriptor a remover: ")

suscriptores.remove(suscrptor_eliminado)

print(f"El suscriptor {suscrptor_eliminado} ha sido eliminado de la lista ")
print(f"Lista de suscriptores: {suscriptores}")

# Verificamos la cantidad total de suscriptores

print(f"Cantidad total de suscriptores: {len(suscriptores)}")

print("--- Lista de suscriptores ---")

for suscriptor in suscriptores:
    print(f"- {suscriptor   }")