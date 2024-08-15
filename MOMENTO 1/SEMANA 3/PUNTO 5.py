print("Caculo del volumen de la alberca")
altura_alberca = input("ingrese la altura: ")
ancho_alberca = input("ingrese la ancho: ")
volumen_cubo = float(altura_alberca)*float(ancho_alberca)
valor_metro = input("ingrese el valor del metro cubico: ")
#COSUMO POR LA PERSONA
consumo = float(volumen_cubo)*int(valor_metro)
consumo = int(consumo)

print(f'El valor a pagar es de {consumo}')