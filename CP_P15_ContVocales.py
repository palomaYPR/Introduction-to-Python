# Elaborar un programa que pida ingresar vocales y al final muestre cuentas se ingresaron de cada uno. (Mediante un for de 10 vueltas)

a = 0
e = 0
ii = 0
o = 0
u = 0

for i in range(0,5):
    message = input('Ingresa un vocal: ')
    v = str(message)
    if v == 'a':
        a += 1
    elif v == 'e':
        e += 1
    elif v == 'i':
        ii += 1
    elif v == 'o':
        o += 1
    else:
        u += 1
print('A: ',a, '\nE: ',e, '\nI: ',ii, '\nO: ',o, '\nU: ',u)
