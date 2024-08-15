print("Precio del producto")
precio = input("Porfavor ingrese el precio del producto: ")

if int(precio) >= float(2500.00):
    descuento = int(precio)*0.15
    print(f'Se aplico un descueto {descuento}')

elif int(precio) <= float(2500.00):
    descuento = int(precio)*0.08
    descuento = int(descuento)
    print(f'Se aplico un descueto {descuento}')
