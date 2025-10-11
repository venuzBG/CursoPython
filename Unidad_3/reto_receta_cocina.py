# Reto de cocina
print("Bienvenido al sistema de recetas de cocina")
nombre_receta = input("Introduce el nombre de la receta: \n")
nombre_ingredientes = input("Introduce los nombres de los ingredientes: \n")
tiempo_preparacion = int(input("Introduce el tiempo de preparación en minutos: \n"))
dificultad_receta = input("Introduce la dificultad de la receta (fácil, medio, difícil): \n")

print("\n---Datos de la receta---")
print(f"Nombre de la receta: {nombre_receta}")
print(f"Número de ingredientes: {nombre_ingredientes}")
print(f"Tiempo de preparación: {tiempo_preparacion} minutos")
print(f"Dificultad de la receta: {dificultad_receta}")
