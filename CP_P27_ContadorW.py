# EUP que pida ingresar números (positivos/negativos) y se detenga cuando se ingrese un 0. Tambien se debera
# mostrar cuantos números han sido ingresados y la suma de estos.

sum = 0
cont = 0
number = int(input('Ingresa un número: '))

while number != 0:
    sum = sum + number
    number = int(input('Ingresa un número: '))
    cont += 1

print(f'Se introdujerón: {cont} \nLa suma es: {sum}')