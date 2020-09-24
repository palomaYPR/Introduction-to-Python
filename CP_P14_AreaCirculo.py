# Elabora un programa que calcule el area de un circulo
# Nota: Tome en cuenta que la formula es A = (pi * r^2)

import math

message = input('Ingresa el radio del circulo: ')
r = int(message)
area = math.pi * r**2
#area = math.pi * math.pow(r,2)
print('El area es: ',area)