# EUP que pida ingresar un número de 0-99 y lo muestre escrito.

num = str(input('Ingresa un número (0 a 99): '))

if num.startswith('0'):
    print('')
elif num.startswith('1'):
    print('diez')
elif num.startswith('2'):
    print()
elif num.startswith('3'):
    print('treinta')
elif num.startswith('4'):
    print('cuarenta')
elif num.startswith('5'):
    print('cincuenta')
elif num.startswith('6'):
    print('sesenta')
elif num.startswith('7'):
    print('setenta')
elif num.startswith('8'):
    print('ochenta')
elif num.startswith('9'):
    print('noventa')

print(' y ')

if num.endswith('0'):
    print('')
elif num.endswith('1'):
    print('uno')
elif num.endswith('2'):
    print('dos')
elif num.endswith('3'):
    print('tres')
elif num.endswith('4'):
    print('cuatro')
elif num.endswith('5'):
    print('cinco')
elif num.endswith('6'):
    print('seis')
elif num.endswith('7'):
    print('siete')
elif num.endswith('8'):
    print('ocho')
elif num.endswith('9'):
    print('nueve')
