# EUP que genere un numero random de 1 a 100, el usuario debera adivinar el numero ingresando uno, esto a
# traves de un ciclo do-while y comparara si el que se ingresa es menor o mayor al que se genero
# en el random, hasta que sea igual.

import random

print('::: Adivina el número :::')
ran = random.randint(1,100)

num = int(input('Ingresa un número:'))
while num != ran:
    if num > ran:
        print('Te pasaste')
        num = int(input('Ingresa un número:'))
    else:
        print('Estas lejos')
        num = int(input('Ingresa un número:'))
print('FELIDIDADES')