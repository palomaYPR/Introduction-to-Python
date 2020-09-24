# EUP que pida un número y calcule su factorial.

fac = 1

message = input('Ingresa un número: ')
n = float(message)

while n >= 1:
    fac = fac * n
    n = n - 1
print(f'El factorial es: {fac}')