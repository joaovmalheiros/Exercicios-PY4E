try:
    hours = input('Enter hours: ')
    hours = float(hours)
    rate = input('Enter rate: ')
    rate = float(rate)
except:
    hours = -1
    rate = -1
    print('Erro, por favor utilize uma entrada numerica')
    quit() ##do not continue

if(hours < 40):
    pay = hours * rate
else:
    pay = (40 * rate) + (hours - 40) * 1.5 * (rate)
if(hours != -1 and rate != -1):
    print("Pay: ",pay)

##Ver como fazer um while no try para a pessoa continuar digitando as entradas enquanto
##algo estiver errado
