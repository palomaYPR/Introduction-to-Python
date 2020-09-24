# Elaborar un programa que permita calcular si un
# número es par o impar

number = input('Ingresa un número: ')
n = int(number)
if n % 2 == 0:
    print('Es par')
else:
    print('Es impar')