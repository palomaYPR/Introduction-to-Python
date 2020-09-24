# Elaborar un programa que calcule la potencia de un número elevado a otro distinto
# Nota: El primero debera ser entero y la potencia decimal.

import math
number = input('Ingrese un número: ')
n = int(number)
potencia = input('Ingrese la potencia: ')
pot = float(potencia)
resu = n ** pot
# ó
resu = math.pow(n,pot)
print(resu)
