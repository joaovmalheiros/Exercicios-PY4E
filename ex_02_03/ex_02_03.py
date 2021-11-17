#Exercício 3: Escreva um programa que solicite ao usuário as horas e o
#valor da taxa por horas para calcular o valor a ser pago por horas de
#serviço.

hours = input('Enter hours: ')
rate = input('Enter rate: ')

try:
    fhours = float(hours)
    frate = float(rate)
except:
    print('Enter only numeric values!')
    quit()

pay = float(hours) * float(rate)
print(f'{pay:.2f}')
