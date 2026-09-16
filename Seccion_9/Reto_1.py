# Reto de sistema de inventario

inventario = []
print("Sistema de inventario")
elementos_nuevos = int(input("Cuantos productos desean ingresar:  "))

for numeros in range(elementos_nuevos):
    
    print(f"Proporciona los valores del producto {numeros + 1}")
    
    num = len(inventario)
    nombre_nuevo = input("Producto : ")
    precio_nuevo = float(input("Precio : "))
    cantidad_nuevo = float(input("Cantidad : "))
    
    inventario.append({ "id" : num , "nombre" : nombre_nuevo, "precio" : precio_nuevo, "cantidad" : cantidad_nuevo })
    
print(inventario)    

id_encontrar = int(input("Ingrese el ID del producto a buscar : "))

if id_encontrar != len(inventario): 
    print(f'''
            ID = {inventario[id_encontrar].get("id")}
            Producto = {inventario[id_encontrar].get("nombre")}
            Precio = {inventario[id_encontrar].get("precio")}
            Cantidad = {inventario[id_encontrar].get("cantidad")}
        ''')
else :
    print(f"Producto con id {id_encontrar} NO encontrado")   

print("\nInventario Actualizado")

for i in range(len(inventario)):
    print(f'''
        ID = {inventario[i].get("id")}
        Producto = {inventario[i].get("nombre")}
        Precio = {inventario[i].get("precio")}
        Cantidad = {inventario[i].get("cantidad")}
      ''')
