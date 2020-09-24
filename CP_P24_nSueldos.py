# Elaborar un programa que pida ingresar la cantidad de sueldos que se pediran, realizar la sumatoria de
# estos y mostrar cuantos son mayores $85 000

sueldoMay = 0
sumS = 0

message = input('Ingresa el número de sueldos que ingresaras: ')
num = int(message)
for i in range(0,num):
    messa = input('Ingresa el sueldo: ')
    sueldo = float(messa)
    if sueldo > 85000:
        sueldoMay += 1
        sumS += sueldo
print('El total de sueldos es: ',sumS,'\nLos sueldos mayores a $85000 son: ',sueldoMay)
