print("HORAS TRABAJADAS")
horas_semanales = int(input(" Digite la cantidad de horas semanales trabajadas: "))

print ("VALOR DE LA HORA")
pago = int(input(" Digite el valor de la hora: "))

print("SUELDO")
sueldo = horas_semanales * pago
print(f'El sueldo del trabajador es de ${sueldo}')