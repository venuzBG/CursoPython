# Promedio de calificaciones

numero_calificaciones = int(input("Numero de calificaciones: "))
lista_calificaciones = []
total_calificaciones = 0

for i in range(numero_calificaciones):
    
    calificacion = float(input(f"Calificacion [{i + 1}]: "))
    lista_calificaciones.append(calificacion)
    total_calificaciones += calificacion

promedio = total_calificaciones / numero_calificaciones

print(f"Calificaiones proporcionadas: {lista_calificaciones}")

print(f"El promedio total es : {promedio:.2f}")


#suma en iterativa en python

# suma_calificaciones = sum(calificacion)
# promedio = total_calificaciones / numero_calificaciones

# print(f"{promedio}")