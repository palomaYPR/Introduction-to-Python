# Elaborar un programa que pida ingresar la cantidad de sueldos que se pediran, de los cuales debera calcular cual es el mayor.


sueldoMay = 0

message = input('Ingresa el número de sueldos que ingresaras: ')
num = int(message)
for i in range(0,num):
    messa = input('Ingresa el sueldo: ')
    sueldo = float(messa)
    if sueldo > sueldoMay:
        sueldoMay = sueldo
print('El sueldo mayor es: ',sueldoMay)