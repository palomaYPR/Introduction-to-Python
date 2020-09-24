# Elaborar un programa que pida 10 números mediante un ciclo for, deberá mostrar cuantos fueron positivos y cuantos negativos.

pos = 0
neg = 0

for i in range(0, 10):
    number = input('Ingresa un número: ')
    n = int(number)
    if n > 0:
        pos += 1
    else:
        neg += 1
print('Positivos: ',pos,'\nNegativos: ',neg)
