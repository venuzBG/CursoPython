# Ejercicio 4: Venta de Tickets

precio_leche = float(input('Ingrese el precio de la leche: '))
precio_pan = float(input('Ingrese el precio del pan: '))
precio_lechuga = float(input('Ingrese el precio de la lechuga: '))
precio_platano = float(input('Ingrese el precio del platano: '))
descuento_cupon = int(input('Desea aplicar un descuentio en %: '))

# Calculo del subtotal(sin impuestos)

subtotal = precio_leche + precio_pan + precio_lechuga + precio_platano

# Aplicar el decuento

descuento = subtotal * (descuento_cupon / 100)

# Subtotal con descuento

subtotal_con_descuento = subtotal - descuento

# calculo del impuesto (13%)

impuesto = subtotal_con_descuento * 0.13

# Calculo total de compra (con impuestos)

costo_total = subtotal_con_descuento + impuesto

print(f'''El subtotal de la compra es: ${subtotal:.2f}
        \n El descuento es: {descuento:.2f} {descuento_cupon}%
        \n El subtotal con descuento es: {subtotal_con_descuento:.2f}
        \n El impuesto (13%) es: {impuesto:.2f}
        \n El costo total de la compra es: {costo_total:.2f}
        ''')
