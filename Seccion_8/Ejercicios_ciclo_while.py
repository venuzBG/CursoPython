print (" Ciclo while ")

# Imprimir valores del 1 al 5

# contador = 1
# while contador <= 5:
#     print(contador, end=" ") # con end nos oermite modificar como se imprime el resultado
#     contador += 1


# Ejercicio de suma acumulativa de numeros del 1 al 5

# MAXIMO = 5
# numero = 1
# suma = 0

# while numero <= MAXIMO:
    
#     print(f"Acumulador + suma -> {suma} + {numero}")
    
#     suma += numero
#     print(f"El resultado de la suma es: {suma} \n")
#     numero += 1


# Menu uterativo con while

print("Sistema de adminitracion de cuentas")

salir = False

while not salir:
    print(f'''Menu: 
          1. Crear cuenta
          2. Eliminar cuenta
          3. Salir''')
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print("Crear cuenta \n")
    elif opcion == 2:
        print("Eliminar cuenta \n")
    elif opcion == 3:
        salir = True
        print("Gracias por usar el sistema \n")
    else:
        print("Opcion no valida")