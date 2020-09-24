# EUP que pida ingresar y se detenga cuando se ingrese uno postivo. Mostrar cuantos se ingresaron en total y cuantos
# positivos y negativos.

num = []
pos = 0
neg = 0

n = int(input('Ingresa un números (0 para finalizar): '))
while n != 0:
    if n > 0:
        pos += 1
    else:
        neg += 1
    num.append(n)
    n = int(input('Ingresa un números (0 para finalizar): '))

print(f'Se introdujeron: {len(num)} elementos')
print(f'Positivos: {pos} & negativos: {neg}')