# EUP que permita introducir un serie de palabras y las alamacene una lista, se dejara de pedir palabras cuando
# se ingrese la palabra 'listo', a continuacion se debera busqueda una palabra en esa lista y mostrar si se
# encuentra en ella o no, ademas debera de introducir la posicion en la que se encuentra.

palabras = []

print(':::Llenado del array:::')
word = str(input('Ingresa una palabra: '))
while word != 'listo':
    palabras.append(word)
    word = str(input('Ingresa una palabra: '))

print('\n:::Busqueda de la palabras:::')
search = str(input('Ingresa la palabra a buscar: '))
for i in range(len(palabras)):
    if palabras[i] == search:
        print(f'Existe en la lista, con la posición: {i}')
        break
