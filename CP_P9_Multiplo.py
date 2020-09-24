# Elaborar un programa que reconozca si un número es múltiplo de otro.

num1 = input('Ingresa el primer número: ')
n = int(num1)
num2 = input('Ingresa el núltiplo: ')
mult = float(num2)
if n % mult == 0:
    print('Es múltiplo')
else:
    print('No es múltiplo')