# Sentencia if

print(f"Sentencia if")

edad = 14
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad}')

else:
    print(f'Eres menor de edad. Tienes {edad}')


edad = 12
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad}')
elif 13 <= edad < 18:
    print(f'Eres un adolscente. Tienes {edad}')
else:
    print(f'Eres un niñ@. Tienes {edad}')