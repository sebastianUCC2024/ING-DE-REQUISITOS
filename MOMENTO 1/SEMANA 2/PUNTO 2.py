print("PRODUCCION DE LECHE EN UN DIA")
litros_leche = int(input(" digite la cantidad de leche: "))
print(f'la cantidad de leche producida en este dia fue de {litros_leche}litros')

print("CONVERSION DE LITROS A GALONES DE LECHE")
conversion = litros_leche * float(3.785)
print(f'la cantidad producida de leche en galones es de {conversion}')

print("VALOR DEL GALON")
valor = int(input("Digite el valor: "))

print(" PAGO POR PRODUCIDO ")
pago = valor * conversion
print(f'El pago que resivio el productor por el dia producido es {pago}')

