# EUP que pida al usuario ingresar 10 vocales
# de las cuales nos dira cuantas son a,e,i,o,u.

contA = 0
contE = 0
contI = 0
contO = 0
contU = 0

for i in range(0,10):
    v = str(input('Ingresa un vocal: '))
    if v == 'a':
        contA += 1
    elif v == 'e':
        contE += 1
    elif v == 'i':
        contI += 1
    elif v == 'o':
        contO += 1
    else:
        contU += 1
print('Fueron ',contA,' a ')
print('Fueron ',contE,' e ')
print('Fueron ',contI,' i ')
print('Fueron ',contO,' o ')
print('Fueron ',contU,' u ')

