# EUP que pida ingresar 10 numeros decimales que se almacenaran en una lista, despues realizar un busqueda de
# algun número y mostrar la posicion en la que se encuentra.

num = []

n = float(input('Ingresa un número: '))
for i in range(0,10):
    num.append(n)
    n = float(input('Ingresa un número: '))

print('\nBusqueda')
search = float(input('Ingresa el número a buscar: '))
for i in range(len(num)):
    if num[i] == search:
        print(f'EL número se encuentra en la posicion: {i}')
        break

