# Inmutabilidad de las cadenas

print("")
print("*** Inmutabilidad de las cadenas ***")

cadena1 = "Hola Mundo"
#cadena1[0] = "h"      # Esto generará un error porque las cadenas son inmutables
cadena2 = cadena1 
cadena1 = "Adios"

print(cadena1)
print(cadena2) # Esto muestra que todos los objetos que aun se esten referenciaand, no se iran en el recolector de basura