# print("Iterar listas")

# lista = ["Carlos", "Juan", "Sebas"]

# for nombres in lista:
#     print(nombres)
    
# lista_heterogenea = [1, 12.4, "Carlos"]

# print()

# for elemtos in lista_heterogenea:
#     print(elemtos)

#Ejercicio una play list de canciones

print("Lista de canciones")

# Creamos una lista vacia

lista_reproducciones = []
numero_canciones = int(input("Cuantas canciones desea agregar: "))

# Iterar cada elemento en la lista para agregar cada elemento

for indice in numero_canciones:
    cancion = input(f"Proporciona la cancion {indice + 1}: ")
    lista_reproducciones.append(cancion)

# Agregar canciones 

# lista_reproducciones.append("Hotel california - Eagles")
# lista_reproducciones.append("Sugar - Harry Styles")
# lista_reproducciones.append("If could fly - One Direction")

# Ordenar la lista alfabeticamente 

# lista_reproducciones.sort(reverse=True) # Sirve para ordenar en modo ascendente
lista_reproducciones.sort()

# Mostrar la lista

print("\n Lista de reproduccion en orden alfabetica")
print(lista_reproducciones)

# Iterar cada cancion
print()
for cancion in lista_reproducciones:
    print(f"- {cancion}")