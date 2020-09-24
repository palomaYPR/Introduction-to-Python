# EUP que pida ingresar 10 numero enteros los cuales seran almacenados en un array, al final se deberan de mostrar.

num = []
for i in range(0,10):
    num.append(int(input('Ingresa un número: ')))

for i in range(len(num)):
    print(num[i])
