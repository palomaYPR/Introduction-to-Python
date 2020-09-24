# Elaborar un programa que reconozca si un número es mayor,
# menor o igual a otro.

num1 = input('Ingresa el primer número: ')
n1 = int(num1)
num2 = input('Ingresa el segundo núemro: ')
n2 = int(num2)
if num1 < num2:
    print(num2,' es el mayor')
elif num1 > num2:
    print(num1,' es el mayor')
else:
    print('Son iguales')