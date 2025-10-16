# Sistema de préstamo de libros

print("Bienvenido al sistema de préstamo de libros")

DISTANCIA_PERMITIDA_KM = 3
tiene_credencial_estudiante = input("¿Tiene credencial de estudiante? (si/no): ").strip().lower() == 'si'
distancia_km = int(input("Ingrese la distancia en kilómetros a la biblioteca: "))

es_elegible_prestamo = tiene_credencial_estudiante or distancia_km <= DISTANCIA_PERMITIDA_KM

print(f'Es elegible para préstamo: {es_elegible_prestamo}')