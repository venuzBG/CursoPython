# Ejercicios de dicc

print("Diccionarios")

persona = {
    "nombre" : "Sergio",
    "edad"  : "18",
    "pais"  : "Mexico"
}

print(f"Diccionario de persona: {persona}")

# Acceder a los elementos del diccionario

print(f"Nombre: {persona["nombre"]}")
print(f"edad: {persona.get("edad")}")
print(f"pais: {persona.get("pais")}")

# Modificar el valor del diccionario

persona["edad"] = 30

print(f"Diccionario persona: {persona}")

# Agregar elemento

persona["profesion"] = "Ingeniero"
print(f"Diccionario persona: {persona}")

# Eliminar elementos 

del persona["pais"]
print(f"Diccionario persona: {persona}")

persona.pop("profesion")
print(f"Diccionario persona: {persona}")

# Iterar los elementos de un dic(llave, valor)

print("Valores de diccionario: ")
for llave, valor in persona.items():
    print(f"La llave: {llave}, valor: {valor}")

# Imprimir solo los valores del diccionario

print("Imprimir los valores del diccionaario: ")
for valor in persona.values():
    print(f"- Valor : {valor}")

# Imprimir solo las claves del diccionario

print(f"Imprimir las claves del diccionario: ")
for clave in persona.keys():
    print(f"- Clave : {clave}")