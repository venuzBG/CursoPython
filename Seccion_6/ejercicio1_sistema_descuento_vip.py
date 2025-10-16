# Sistema de descuebnto para clientes VIP

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input("Ingrese la cantidad de productos que lleva: "))
tiene_membresia_vip = input("Es usted miembro VIP (si/no): ")

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO and 
                        tiene_membresia_vip.strip().lower() == 'si')

print(f'Es elegible para descuento: {es_elegible_descuento}')