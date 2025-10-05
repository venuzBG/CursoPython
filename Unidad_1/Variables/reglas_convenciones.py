# Reglas y conveciones

#Ejemplos de reglas estrictas

nombre_usuario = "Juan" # Correcto
#nombre-usuario = "Juan" # Incorrecto, no se permiten guiones
#1nombre = "Juan" # Incorrecto, no puede empezar con numero
#nombre usuario = "Juan" # Incorrecto, no se permiten espacios
#nombre@usuario = "Juan" # Incorrecto, no se permiten caracteres especiales

#No podemos usar palabras reservadas de Python como nombres de variables

#def = "Funcion" # Incorrecto, 'def' es una palabra reservada
#class = "Clase" # Incorrecto, 'class' es una palabra reservada
#if = "Condicional" # Incorrecto, 'if' es una palabra reservada
klass = "Clase" # Correcto, 'klass' no es una palabra reservada
print("Nombre de usuario: ", nombre_usuario)
print("Valor de klass: ", klass)

# Sensible a mayusculas y minusculas

nombre = "Ana"
Nombre = "Pedro"
print("nombre: ", nombre)
print("Nombre: ", Nombre)

# snake case

nombre_completo = "Ana Maria"
print("Nombre completo: ", nombre_completo)

# prefijos y sufijos
contador1 = 10
es_casado = False