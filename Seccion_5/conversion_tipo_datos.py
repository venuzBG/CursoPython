#Conversion de tipos de datos

#Convertir de cadena a numero 

numero_cadena = "1000"
numero_entero = int(numero_cadena)
print(f"Valor numerico en cadena: {numero_cadena}")
print(f"Valor numerico en entero: {numero_entero}\n")

#Convertir de cadena a flotante

numero_cadena = "1000.50"
numero_flotante = float(numero_cadena)
print(f"Valor numerico en cadena: {numero_cadena}")
print(f"Valor numerico en flotante: {numero_flotante}\n")

#Convertir de numero a cadena
numero = 1500
numero_cadena = str(numero)
print(f"Valor numerico: {numero}")
print(f"Valor numerico en cadena: {numero_cadena}\n")

#Convertir a booleano
#Tipo de bool es falso para los siguientes casos
#Si el valor es 0, cadena vacio, o NONE, entonces regresa False
#Regresa verdadero, si el valor es distinto de 0, si es distinto de cadena vacio, o distinto de NONE

numero_entero = 0
booleano = bool(numero_entero)
print(f"Valor booleano entero o: {booleano}\n")

numero_entero = 15
booleano = bool(numero_entero)
print(f"Valor booleano entero diferente de 0: {booleano}\n")

cadena = ""
booleano = bool(cadena)
print(f"Valor booleano cadena vacia: {booleano}\n")

cadena = "Valor de cadena"
booleano = bool(cadena)
print(f"Valor booleano cadena no vacia: {booleano}\n")

variable = None
booleano = bool(variable)
print(f"Valor booleano de una variable None: {booleano}")