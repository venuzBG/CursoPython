# Calificaciones de los estudiantes

Calificacion = int(input("Ingrese la nota del estudiante (0-10): "))
Calificacion_letra = ""

if 0 <= Calificacion < 6 :
    Calificacion_letra = "F"
    
elif 6 <= Calificacion < 7 :
    Calificacion_letra = "D"
    
elif 7 <= Calificacion < 8 :
    Calificacion_letra = "C"
    
elif 8 <= Calificacion < 9 :
    Calificacion_letra = "B"

elif 9 <= Calificacion < 10 :
    Calificacion_letra = "A"

else:
    Calificacion_letra = "Calificación inválida"

print(f"La calificación del estudiante es {Calificacion_letra} y la nota es {Calificacion}.")