# EUP que pida 10 números. Mostrar la media de
# los números positivos, la media de los números
# negativos y la cantidad de ceros

ceros = 0
pos = 0
neg = 0
sumPos = 0
sumNeg = 0

for i in range(1,10):
    message = input('Ingresa el número: ')
    n = int(message)
    if n == 0:
        ceros += 1
    else:
        if n > 0:
            pos += 1
            sumPos += n
        else:
            neg += 1
            sumNeg += n

print('Número de ceros: ',ceros)

##Positivos
if pos == 0:
    print('No se puede hacer la media de los positivos')
else:
    mediaPos = float(sumPos / pos)
    print('Media de los positivos: ',mediaPos)

##Negativos
if neg == 0:
    print('No se puede hacer la media de los negativos')
else:
    mediaNeg = float(sumNeg /neg)
    print('Media de los negativos: ', mediaNeg)
