# Inventarios

print("Sistemas de inventarios")

inventario = []

numero_productos = int(input("Cuantos productos deseas agregar:"))

for indice in range(numero_productos):
    print(f"Proporciona los valores del producto {indice+1}")
    
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    #Creamos el diccionario
    
    prducto = {"id": indice, "nombre": nombre, "precio": precio, "cantidad": cantidad}
    
    #Agregamos el nuevo producto al inventario
    
    inventario.append(prducto)
    
# Mostrar el inventario inicial

print(f"\nInventario inicial: {inventario}")

# Buscar un producto id

id_buscar = int(input("\nIngrese el ID del producto: "))

producto_encontrado = None

for producto in inventario:
    if producto.get("id") == id_buscar:
        producto_encontrado = producto
        break
    
if producto_encontrado is not None:
    print("Informacion del producto encontrado: ")
    print(f'''Id: {producto_encontrado.get("id")}
          Nombre: {producto_encontrado.get("nombre")}
          Precio: {producto_encontrado.get("precio")}
          Cantidad: {producto_encontrado.get("cantidad")}        
          ''')
else:
    print(f"Producto con id {id_buscar} NO encontrado")   
    
# Mostrar el inventario detallado

print(f"\nInventario Detallado")    

for producto in inventario:
    print(f'''ID : {producto.get("id")}
          Nombre : {producto.get("nombre")}
          Precio : {producto.get("precio")}
          Cantidad : {producto.get("cantidad")}
          ''')
    
    
    
