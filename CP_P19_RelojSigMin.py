# Pedir una hora de la forma hora, minutos y segundos, y mostrar la hora en el segundo siguiente.



hrs = input('Ingresa la hora: ')
h = int(hrs)
min = input('Ingresa los minutos: ')
m = int(min)
seg = input('Ingresa el segundo: ')
s = int(seg)

#Suponiendo que la hora es la correcta, aumentamos los segundos
s += 1

if s >= 60:
    s = 0
    m += 1
    if m >= 60:
        m = 0
        if h >= 24:
            h = 0
print('La hora es: ',h,':',m,':',s)