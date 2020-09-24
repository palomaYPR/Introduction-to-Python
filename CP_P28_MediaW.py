# EUP que pida un digito, el cual sera el numero de numeros que se introducieran de los cuales se calculara la
# media mediante un ciclo while.

sum = 0
i = 0
number = int(input('Ingresa la cantidad de números: '))

while i != number:
    n = int(input(f'Ingresa el número {i}: '))
    sum += n
    i += 1

media = float(sum / i)
print(f'La media es: {media}')