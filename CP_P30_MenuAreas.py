# EUP que muestre un menu para calcular areas. Tome en cuenta que las figuras en el menu serán: Cuadrado, circulo, triangulo,
# Trapecio y Elipse.
## FORMULAS:
# Cuadrado L^2 ----- Rectangulo b*h
# Circulo pi * r^2 ----- Elipse a*b*pi
# Triangulo h*h / 2 ----- Trapecio (B+b)*h / 2
import math

print('Calcular Áreas de figuras Geométricas.\n')
print('1.Cuadrado.\n2.Circulo.\n3.Triangulo.\n4.Trapecio.\n5.Rectangulo.\n6.Elipse ')

op = int(input('Escoje una figura: '))

if op == 1:
    print('Cuadrado')
    L = int(input('Ingresa el lado: '))
    a = math.pow(L,2)
    print(f'El area del cuadrado: {a}')
elif op == 2:
    print('Circulo')
    R = int(input('Ingresa el radio del circulo: '))
    a = math.pi*R**2
    print(f'El area del circulo: {a}')
elif op == 3:
    print('Triangulo')
    b = int(input('Ingresa la base: '))
    h = int(input('Ingresa la altura: '))
    a = b*h/2
    print(f'El area del triangulo: {a}')
elif op == 4:
    print('Trapecio')
    B = int(input('Ingresa la base mayor: '))
    b = int(input('Ingresa la base menor: '))
    h = int(input('Ingresa la altura: '))
    a = (B+b)*h/2
    print(f'El area del trapecio: {a}')
elif op == 5:
    print('Rectangulo')
    b = int(input('Ingresa la base: '))
    h = int(input('Ingresa la altura: '))
    a = b*h
    print(f'El area del rectangulo: {a}')
elif op == 6:
    print('Elipse')
    a = int(input('Ingresa el eje menor: '))
    b = int(input('Ingresa el eje mayor: '))
    a = a*b*math.pi
    print(f'El area del eclipse: {a}')
else:
    print('La opción no existe')