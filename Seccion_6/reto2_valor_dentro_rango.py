# Valor dentro de un rango

# Solicitar al usuario un valor entre 0 y 5

VALOR_MINIMO , VALOR_MAXIMO = 0 , 5

valor_usurio = int(input(f'Ingrese un valor entre {VALOR_MINIMO} y {VALOR_MAXIMO}: '))

# Verificar si el valor ingresado por el usuario esta dentro del rango

esta_dentro_rango = VALOR_MINIMO <= valor_usurio <= VALOR_MAXIMO

# Otra forma

# esta_dentro_rango = (valor_usurio >= VALOR_MINIMO) and (valor_usurio <= VALOR_MAXIMO)

print(f'El valor {valor_usurio} esta dentro del rango: {esta_dentro_rango}')