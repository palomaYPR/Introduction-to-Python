# Elaborar un programa que calcule los radianes de una cantidad de grados ingresada por el usuario.

import math

grados = input('Ingresa los grados: ')
g = float(grados)
radianes = g / 360.0 * 2 *  math.pi
print(math.sin(radianes))