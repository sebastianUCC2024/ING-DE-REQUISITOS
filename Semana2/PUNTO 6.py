print("PRIMER VALAOR")
primer_valor = input("Digite el primer numero: ")
print("SEGUNDO VALOR")
segundo_valor = input("Digite el segundo numero: ")

if primer_valor == segundo_valor:
    print(f'los numeros son iguales')

elif primer_valor >= segundo_valor:
    print(f'{primer_valor} es mayor que {segundo_valor}')

elif segundo_valor >= primer_valor:
    print(f'{primer_valor} es menor que {segundo_valor}')

