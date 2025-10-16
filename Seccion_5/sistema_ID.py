# Generar un ID unico

from random import randint

nombre = input("Ingrese su nombre: \n")
apellido = input("Ingrese su apellido: \n")
año_nacimiento = input("Ingrese su año de nacimiento: \n")
numero_aleatorio = randint(1000, 9999)

subcadena_nombre = nombre[0:2].upper().strip()
subcadena_apellido = apellido[0:2].upper().strip()
subcadena_año = año_nacimiento[2:4].strip() # Funcion strip para eliminar espacios en blanco


print(f"Su ID unico es: {subcadena_nombre}{subcadena_apellido}{subcadena_año}{numero_aleatorio}")