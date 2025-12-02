# Ejemplo 2

print(' Bienvenidos a la casa de los espejos')

edad = int(input('Cual es tu edad? '))
tienes_miedo_oscuridad = input('Tienes miedo a la oscuridad (si/no)? ').strip().lower() == "si"

if not tienes_miedo_oscuridad and edad >= 10:
    print('Puedes entrar a la casa de los espejos:')
else:
    print('Lo siento, la Casa de los espejos podria darte miedo')
