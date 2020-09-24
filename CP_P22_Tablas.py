# Elaborar un programa que pida ingresar un número del cual se calculará su tabla de multiplicar.

message = input('Ingresa el número del que quieres tu tabla: ')
n = int(message)

for i in range(1,11):
    print(n,' x ',i,' = ',i*n)