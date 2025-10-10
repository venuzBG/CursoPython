#Largo de una cadena

cadena = 'Hola, Mundo!'
largo_cadena = len(cadena)
print(f'La cadena "{cadena}" tiene {largo_cadena} caracteres.')
print('El largo de la cadena incluyendo espacios es:', len(cadena))

#Largo de una cadena sin contar espacios
largo_sin_espacios = len(cadena.replace(' ', ''))
print('El largo de la cadena sin contar espacios es:', largo_sin_espacios)
print(f'La cadena contiene {cadena.count("o")} letras "o".')