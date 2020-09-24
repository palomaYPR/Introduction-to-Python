# Elaborar un programa que pida ingresar un hora, y se debera evaluar si es correcta, tome en cuenta:
# meses: 12, dias: 31, año entre 1800 - 2019. Introducir con el formato: aaaa-mm-dd

ac = False
mc = False
dc = False


año = input('Ingresa el año: ')
a = int(año)
mes = input('Ingresa el mes: ')
m = int(mes)
dia = input('Ingresa el día: ')
d = int(dia)

if a >= 1800 and a <= 2019:
    ac = True
    if m >= 1 and m <= 12:
        mc = True
        if d >= 1 and d <= 31:
            dc = True

if ac and mc and dc:
    print('Fechas correctas: ', a, ' - ', m, ' - ', d)
else:
    print('Fechas incorrectas.')