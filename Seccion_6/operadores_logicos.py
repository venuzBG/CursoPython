# Operadores logicos

# Operador AND (y)

condicion1 = True
condicion2 = False

resultado = condicion1 and condicion2
print(f'El resultado de {condicion1} and {condicion2} es: {resultado}')

a, b = 5, 3
print(f'Valores iniciales: a={a}, b={b}')
operacion = (a > 2) and (b < 5)
print(f'El resultado de (a > 2) and (b < 5) es: {operacion}')


# Operador OR (o) 

condicion1 = True
condicion2 = False

resultado = condicion1 or condicion2
print(f'El resultado de {condicion1} or {condicion2} es: {resultado}')

# Operador NOT (no)
condicion = True
resultado = not condicion
print(f'El resultado de not {condicion} es: {resultado}')

# Revisar si es una cadena vacia

nombre = ""
es_vacio = not nombre
print(f'El variable no tiene nungun valor: {es_vacio}')

# Revisar si una varibale no tiene ningun valor asignado (NONE)
variable = None
no_tiene_valor = not variable
print(f'La variable no tiene ningun valor asignado: {no_tiene_valor}')

variable = 10
no_tiene_valor = not variable
print(f'La variable no tiene ningun valor asignado: {no_tiene_valor}')