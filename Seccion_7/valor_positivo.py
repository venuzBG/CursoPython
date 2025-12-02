# Revision si un valor es positivo

print('Revision de un numero')

numero = int(input("Proporciona un numero:"))

if numero > 0:
    print(f'Es un numero positivo: {numero}')
elif numero < 0:
    print(f'Es negativo: {numero}')
else:
    print(f'Es cero: {numero}')