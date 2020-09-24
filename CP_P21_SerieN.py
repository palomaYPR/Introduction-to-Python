# Elaborar un programa que pida ingresar un número n e imprima desde 1 a n.

message = input('Ingresa el número hasta el cuál termina la serie: ')
n = int(message)

for i in range(1,n+1):
    print(i)