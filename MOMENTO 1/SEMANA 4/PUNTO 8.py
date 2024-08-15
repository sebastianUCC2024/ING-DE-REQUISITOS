print("PRECIO DEL PRODUCTO")
precio = int(input("Porfavor ingrese el precio del producto: "))

if precio >= float(2500.00):
    descuento = precio*0.15
    print(f'Se aplico un descueto {descuento}')

elif precio <= float(2500.00):
    descuento = round(precio * 0.08)
    print(f'Se aplico un descueto {descuento}')
