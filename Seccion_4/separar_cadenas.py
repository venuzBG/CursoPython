# Seporar cadenas

datos = "Hola Mundo"

lista = datos.split() #Por defecto separa por espacios en blanco, ve que hay un espacio en blanco y spara la cadena en ese punto.
print(lista)

datos = "Juan,30,Mexico"
lista = datos.split(",") #Separa la cadena en cada coma. Le indicamos que queremos que separe dentro de las "" comillas dobles.
print(lista)
