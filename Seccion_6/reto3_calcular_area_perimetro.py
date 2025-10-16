# Calcular el area y perimetro de un rectangulo

base = float(input('Ingrese la base del rectangulo: '))
altura = float(input('Ingrese la altura del rectangulo: '))

area = base * altura
perimetro = 2 * (base + altura) # Si no ponemos entre parentesis la suma, primero se multiplicara

print(f'El area del rectangulo es: {area}:.2f')
print(f'El perimetro del rectangulo es: {perimetro}:.2f')