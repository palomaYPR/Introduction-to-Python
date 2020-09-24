# Elaborar un programa que pida ingresar un score entre un rango de 0.0 y 1.0, de acuerdo al score ingresado
# se asignara una calificación.
# Nota: utiliza try-except

message = input('Enter your score: ')
try:
    score = float(message)
    if  score > 0.0 and score < 1.0:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')
except:
    print('Bad Score')