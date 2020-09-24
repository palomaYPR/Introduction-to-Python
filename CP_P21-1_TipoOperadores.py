# EUP que permita ingresar dos números y un operador, de acuerdo al operador ingresado se realizara la debida
# operacion.

num1 = int(input('Ingresa el 1er número: '))
num2 = int(input('Ingresa el 2do número: '))
ope = str(input('Ingresa el operador: '))

if ope == '*':
    res = num1 + num2
elif ope == '/':
    res = num1 / num2
elif ope == '+':
    res = num1 + num2
else:
    res = num1 - num2
