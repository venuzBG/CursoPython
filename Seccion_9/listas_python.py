print("Manejo de listas")

mi_lista = [1,2,3,4,5,6,7]

print(f"{mi_lista} -> lista orignial")

#largo de la lista

print(f"Largo de la lista: {len(mi_lista)}")

# Acceder  a los elemtos por el indice

print(f"Indice 4: {mi_lista[2]}")
print(f"Indice final: {mi_lista[-1]}") # si usas negativos va al reves

###############

# Modificar los elementos de una lista

mi_lista[2] = 10

print(f"Modificamos el valor del indice 2: {mi_lista[2]}")

# Agregar elementos al final de la lista 

mi_lista.append(24)
print(f"{mi_lista} -> Se agrego el 24 al final de la lista")

# Añadir un elemento en un indice especifico

mi_lista.insert(2, 15) # el primer numero es el indice y el segundo el elemnto a agregar
# Todos los demas elementos se mueven un indice a la derecha

###############
# Eliminar elemento de una lista

mi_lista.remove(5) # 

print(f"{mi_lista} -> se removio el valor 5 de la lista")

# Eliminar un elemento con el indice

mi_lista.pop(1) # al eleminar el valor, los elemtos despues recoren un pusto a la izquierda
print(f"{mi_lista} se elimino el indice 1")

# Eliminar usando la palabra del

del mi_lista[2]
print(f"{mi_lista} -> se elmino el indice 2")

# Obtener sublistas

sublista = mi_lista[1:3] # Se crea una sublista desde el indice 1 al 2 (el 3 no se incluye para la nuva sublista)
print(f"Sblista [1:3]: {sublista}")