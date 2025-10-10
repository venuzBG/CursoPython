# Buscar subcadenas

cadena = 'Hola, Mundo!'
indice = cadena.find('Mundo') #Devuelve el indice de la primera ocurrencia de la subcadena ose aque el indice de M es 6, ese es el numero que devuelve.
print(f'La subcadena "Mundo" se encuentra en el indice: {indice}')

# Si la subcadena no se encuentra, devuelve -1
indice_no_encontrado = cadena.find('hola')
print(f'La subcadena "hola" se encuentra en el indice: {indice_no_encontrado}')

