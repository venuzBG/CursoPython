# Revisar si una variable no es un rango (not range)

dato = int(input("Ingrese un numero: "))

# Revisar si el numero no esta en el rango de 1 a 10
dentro_rango = (1 <= dato <= 10)

print(f'El numero {dato} esta dentro del rango de 1 a 10: {dentro_rango}')

# Revisar la logica inversa, esta fuera de rango

esta_fuera_rango = not (1 <= dato <= 10)

print(f'El numero {dato} esta fuera del rango de 1 a 10: {esta_fuera_rango}')