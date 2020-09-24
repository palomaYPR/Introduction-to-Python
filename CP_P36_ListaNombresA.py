# EUP que permita almacenar nombres hasta que se introduzca la palabra 'listo', despues imprimir unicamente
# aquellos nombres que comincen con A.

palabras = []

print(':::Llenado del array:::')
word = str(input('Ingresa un nombre: '))
while word != 'listo':
    palabras.append(word)
    word = str(input('Ingresa un nombre: '))

print('\n:::Impresión:::')

for i in range(len(palabras)):
    if palabras[i].startswith('a'):
        nombre = palabras[i]
        print(nombre)
