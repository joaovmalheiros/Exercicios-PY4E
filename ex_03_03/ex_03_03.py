pont = input('Digite uma pontuacao entre 0 e 1:')
pont = float(pont)

while pont < 0.0 or pont > 1.0:
    pont = input('Pontuacao Invalida! Digite uma pontuacao entre 0 e 1:')
    pont = float(pont)

if(pont >= 0.9):
    print('Nota: A')
elif(pont >= 0.8):
    print('Nota: B')
elif(pont >= 0.7):
    print('Nota: C')
elif(pont >= 0.6):
    print('Nota: D')
else:
    print('Nota: F')
