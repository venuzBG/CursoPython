print("Combinacion de listas y tuplas")

productos = [
    ("P001", "Camiseta", 20.00),
    ("P002", "Jeans", 30.00),
    ("P003", "Sudadera", 40.00)
]

# Imprimir la informacion de cada producto
# y tambien calcular el precio total

precio_total = 0
print ("Informacion de los productos")

for producto in productos:
    # print(producto)
    id, descripcion, precio = producto
    print(f"Producto: {id}, Descripcion: {descripcion}, Precio: ${precio}")
    precio_total += precio # productos[2] sino esta desempaquetado
    

print(f"Precio total: $ {precio_total}")