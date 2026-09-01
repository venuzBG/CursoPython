# print(" Cajero automatico ")

# saldo_inicial = 1000

# salir = False

# while not salir:
#     print(f'''Menu:
#           1. Consultar saldo
#           2. Retirar dinero
#           3. Depositar dinero
#           4. Salir''')
    
#     opcion = int(input("Ingrese una opcion: "))
#     if opcion == 1:
#         print(f"Su saldo actual es: {saldo_inicial} \n")
    
#     elif opcion == 2:
#         monto_retirar = float(input("Ingrese el monto a retirar: "))
#         if monto_retirar <= saldo_inicial:
#             saldo_inicial -= monto_retirar
#             print(f"Retiro exitoso. \nSu nuevo saldo es: {saldo_inicial} \n")
#         else:
#             print("Saldo insuficiente para realizar el retiro \n")
            
#     elif opcion == 3:
#         monto_depositar = float(input("Ingrese el monto a depositar: "))
#         saldo_inicial += monto_depositar
#         print(f"Deposito exitoso. \nSu nuevo saldo es: {saldo_inicial} \n")
        
#     elif opcion == 4:
#         salir = True
#         print("Gracias por usar el cajero automatico \n")

# Reto de calculadora



# print("Calculadora")

# salir = False

# while not salir:
#     print(f'''Menu: 
#           1. Suma
#           2. Resta
#           3. Multiplicacion
#           4. Division
#           5. Salir''')
    
#     opcion = int(input("Ingrese una opcion:"))    
    
#     if opcion == 1:
#         num1 = float(input("Ingrese el primer numero: "))
#         num2 = float(input("Ingrese el segundo numero: "))
#         resultado = num1 + num2
#         print(f"El resultado de la suma es: {resultado:.2f} \n")
        

#     elif opcion == 2:
#         num1 = float(input("Ingrese el primer numero: "))
#         num2 = float(input("Ingrese el segundo numero: "))
#         resultado = num1 - num2
#         print(f"El resultado de la resta es: {resultado:.2f} \n")
        

#     elif opcion == 3:
#         num1 = float(input("Ingrese el primer numero: "))
#         num2 = float(input("Ingrese el segundo numero: "))
#         resultado = num1 * num2
#         print(f"El resultado de la multiplicacion es: {resultado:.2f} \n")
        

#     elif opcion == 4:
#         num1 = float(input("Ingrese el primer numero: "))
#         num2 = float(input("Ingrese el segundo numero: "))
#         if num2 != 0:
#             resultado = num1 / num2
#             print(f"El resultado de la division es: {resultado:.2f} \n")
#         else:
#             print("Error: No se puede dividir entre cero \n")
            
#     elif opcion == 5:
#         salir = True
#         print("Gracias por usar la calculadora \n")
         
#     else:
#         print("Opcion no valida \n")

# Reto de contraseña 

# valido = False

# print("creacion de contraseña")

# while not valido:
#     contrasena = input("Ingrese una contraseña: ")
#     if len(contrasena) == 6:
#         print("Contrsaeña valida \n")
#         valido = True
#     else:
#         print("Contrsaeña invalida, intente nuevamente \n")

# ingrese = input("Ingrese una contresa de 6 caracteres: ")

# while len(ingrese) != 6:
#     print("Contraseña invalida, intente nuevamente \n")
#     ingrese = input("Ingrese una contresa de 6 caracteres: ")
    
# else:
#     print("Contraseña valida \n")

# Juego de adivinar el numero

# import random

# numero_secreto = random.randint(1, 50)

# numero_intentos = 0
# numero_maximo_intentos = 10

# while numero_intentos < numero_maximo_intentos: 
#     intento = int(input("Adivina el numero entre 1 y 50: "))
#     numero_intentos += 1
    
#     if intento < numero_secreto:
#         print("El numero secreto es mayor \n")
#     elif intento > numero_secreto:
#         print("El numero secreto es menor \n")
#     else:
#         print(f"Felicidades! Adivinaste el numero secreto {numero_secreto} en {numero_intentos} intentos \n")
#         break
    
# print(f"Funcion de rango")

# print("Imprimir numero del 0 al 4")

# for i in range(5):
#     print(i, end = " ")


# # Imprimir del 10 al 20
# print("\n\nImprimir del 10 al 20")
# for i in range(10, 21):
#     print(i, end = " ")
    
    
# print("\n\nSecuencia del 20 al 30 con inncremento de 2")
# for i in range(20, 31, 2):
#     print(i, end = " ")

# Impresion de mensaje

# mensaje = input("Proporciona un mensaje: ")
# numero_repeticiones = int(input("Proprciona el numero de repeticiones: "))

# # iterar sobre las repeticiones

# for i in range(numero_repeticiones):
#     print(f"{i+1} -> {mensaje}")

# Dibujar un triangulo

# print("##Dibujar un triangulo##")

# numero_fila = int(input("Proporciona el numero de filas: "))

# for fila in range(1, numero_fila+1):
#     espacion_blanco = " " * (numero_fila - fila)
#     asteriscos = "*" * (2 * fila - 1)
#     print(f"{espacion_blanco}{asteriscos}")

# Break y continue

# Ejemplo break
print("Palabra break: ")

for numero in range(1,10):
    if numero % 2 == 0:
        print(numero)
        break  # Salimos del ciclo inmediatamente
    
# Ejemplo de continue

print("\n\nPalabra continue: ")
for numero in range(1,10):
    if numero % 2 == 1:
        continue # si llega a esta linea va a la siguiente iteracion desde ese punto
    print(numero)