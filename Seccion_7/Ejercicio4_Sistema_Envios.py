# Sistema de envios 

Lugar = input("El paquete es para (Nacional/Internacional): ")
Peso = float(input("Ingrese el peso del paquete en kg: "))

if Lugar.lower() == "nacional": 
    pago = 10 * Peso
    
    print(f"El costo del envio nacional es: ${pago:.2f}")
    
elif Lugar.lower() == "internacional":
    pago = 20 * Peso
    
    print(f"El costo del envio internacional es: ${pago:.2f}")
    
else:
    print("Lugar de envio no valido. Por favor ingrese 'Nacional' o 'Internacional'.")
    