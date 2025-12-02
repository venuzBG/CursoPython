# Reto de crear una tienda en linea

print('*****Tienda en linea******')

MONTO_COMPRA = 1000

valor_compra = float(input("Ingrese el valor de su compra:"))

miembro_vip = (input('Es miembro de la tienda (si/no)?')).strip().lower() == "si"

if (MONTO_COMPRA < valor_compra) and miembro_vip:
    descuento = valor_compra * (10/100)
    valor_pagar = valor_compra - descuento
    print(f'Monto del descuento: {descuento}')
    print(f'Total a pagar: {valor_pagar}')
elif miembro_vip == True:
    descuento = valor_compra * (5/100)
    valor_pagar = valor_compra - descuento
    print(f'Monto del descuento: {descuento}')
    print(f'Total a pagar: {valor_pagar}')
elif MONTO_COMPRA < valor_compra:
    descuento = valor_compra * (3/100)
    valor_pagar = valor_compra - descuento
    print(f'Monto del descuento: {descuento}')
    print(f'Total a pagar: {valor_pagar}')

else:
    print(f'''No obtuviste ningun tipo de descuento
          \n Te invitamos a hacerte miembro
          \n Monto final a pagar: {valor_compra}
          ''')
    
