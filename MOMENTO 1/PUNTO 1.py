
print("AREA DEL RECTANGULO ")
baseRectangulo = int(input(" Ingrese la longitud de la base : "))
alturaRectangulo = int(input(" Ingrese la altura : "))
areaRenctangulo = baseRectangulo * alturaRectangulo
print(f'La area del rectangulo es de {areaRenctangulo} metros')


print("AREA DEL TRIANGULO")
baseTriangulo = int(input(" Ingrese la longitud de la base : "))
alturaTriangulo = int(input(" Ingrese la altura : "))
areaTriangulo = baseTriangulo * alturaRectangulo/2
print(f'La area del triangulo es de {areaTriangulo} metros')



print("AREA DEL TERRENO")
Area = areaTriangulo + areaRenctangulo
print(f'La area del terreno es de {Area} metros')

