print("VOLUMEN DE LA ALBERCA")
altura_alberca = float(input("ingrese la altura: "))
ancho_alberca = float(input("ingrese la ancho: "))
volumen_cubo = altura_alberca * ancho_alberca
valor_metro = int(input("ingrese el valor del metro cubico: "))
#COSUMO POR LA PERSONA
consumo = int(volumen_cubo * valor_metro)

print(f'El valor a pagar es de {consumo}')