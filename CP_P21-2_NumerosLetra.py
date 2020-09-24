#EUP que pida ingresar números del 1-10 y te regrese ese numero en letra. Si el número se sale del rango debera mandar
# un mensaje advirtiendo esto.

number = int(input('Ingresa un número entre 1-10: '))

if number == 1:
    print('Uno')
elif number == 2:
    print('Dos')
elif number == 3:
    print('Tres')
elif number == 4:
    print('Cuatro')
elif number == 5:
    print('Cinco')
elif number == 6:
    print('Seis')
elif number == 7:
    print('Siete')
elif number == 8:
    print('Ocho')
elif number == 9:
    print('Nueve')
elif number == 10:
    print('Diez')
else:
    print('El número se encuentra fuera del rango')