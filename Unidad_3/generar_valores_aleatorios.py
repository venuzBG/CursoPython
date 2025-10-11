# Valores aleatorios con la funcion randint()

# import random 
from random import randint

# Generar un numero aleatorio entre 1 y 10
# numero_aleatorio = random.randint(1, 10) esto si ponemos la opcion import random
numero_aleatorio = randint(1, 10)

print("Numero aleatorio entre 1 y 10:", numero_aleatorio)

# Generar un numero de 1 al 6

#dado = random.randint(1, 6) esto si ponemos la opcion import random
dado = randint(1, 6)
print(f"Numero aleatorio de un dado: {dado}")
