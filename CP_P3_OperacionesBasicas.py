# Elaborar un programa el cual tenga la capacidad de realizar las
# cuatro operaciones básicas: suma, resta, multiplicación, división.

number = input('Ingresa el primer número:')
n1 = float(number)
number1 = input('Ingresa el segundo número:')
n2 = float(number1)
multi = n1 * n2
divi = n1 /n2
sum = n1 + n2
res = n1 - n2

print('M: ',multi,'\nD: ',divi,'\nS: ',sum,'\nR: ',res)