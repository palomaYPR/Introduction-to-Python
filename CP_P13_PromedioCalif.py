# Elaborar un programa que pida introducir 10 calificaciones de las cuales se calcula el promedio general.

sum = 0
pro = 0

for i in range(0,10):
    number = input('Ingresa una calificación: ')
    n = float(number)
    sum = sum + n
pro = sum / 10
print('El promedio general es: ',pro)