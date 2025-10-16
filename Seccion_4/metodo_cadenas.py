# metodos en python para cadenas

cadena1 = 'Hola Mundo'

print(f'Cadena original: {cadena1}')

mayusculas = cadena1.upper()

print(f'Cadena en mayusculas: {mayusculas}')
print(f'Cadena en minusculas: {cadena1.lower()}') #Concertir a minusculas

cadena2 = '   Hola Mundo   '

print(f'Cadena 2 original: "{cadena2}"')
print(f'Cadena 2 sin espacios: "{cadena2.strip()}"') #Eliminar espacios al inicio y al final
print(f'Cadena 2 sin espacios a la izquierda: "{cadena2.lstrip()}"') #Eliminar espacios a la izquierda
print(f'Cadena 2 sin espacios a la derecha: "{cadena2.rstrip()}"') #Eliminar espacios a la derecha

print(f'Cadena dividida: {cadena1.split()}') #Dividir cadena en una lista
print(f'Cadena reemplazada: {cadena1.replace("Mundo", "Python")}') #Reemplazar una subcadena por otra
print(f'Cadena contiene "Hola": {"Hola" in cadena1}') #Verificar si una subcadena está en la cadena