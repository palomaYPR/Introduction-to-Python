# Elaborar un programa que calcule el promedio de 10 calificaciones,
# y 10 edades ingresadas por el usuario, además de decir
# cuantos alumnos son mayores a 18 años.

may = 0
sumC = 0
sumE = 0
proC = 0
proE = 0

for i in range(0,10):
    message = input('Ingresa la calificación del alumno ',i)
    calif = float(message)
    message1 = input('Ingresa la edad del alumno ',i)
    edad = float(message1)
    if edad > 18:
        may += 1
    sumC = sumC + calif
    sumE = sumE + edad

proC = sumC / 10
proE = sumE / 10
print('El promedio de las calificaciones es: ',proC,
      'El promedio de las edades es: ', proE)