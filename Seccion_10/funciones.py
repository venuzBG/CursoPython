# Definir una funcion para mandar a llamar

def saludar(): # Firma del metodo
    # Cuerpo de la funcion
    print("Saludos desde una funcion.....")
    
# Programa principal, llamamos a la funcion

saludar()


# Definir una funcion para mandar a saludar

# def saludar(mensaje):
    
#     print(f"Mensaje recibido: {mensaje}")
    
# saludar("saludar a todos")

# Definir la funcion de sumar

# Llamar la funcion 
#import modulos_funcion

from modulos_funcion import sumar


# resultado_funcion = modulos_funcion.sumar(8, 5) solo si uso el import y no con from
resultado_funcion = sumar(8, 5) # Con from ya no es necesario poner el nombre del archivo 

print(f"Resultado de sumar: {resultado_funcion}")

# resultado_funcion = sumar(9, 15)

# print(f"Resultado de sumar: {resultado_funcion}")