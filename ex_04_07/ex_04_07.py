def computarNotas(vnota):
    if(vnota >= 0.9):
        snota = 'A'
    elif(vnota >= 0.8):
        snota = 'B'
    elif(vnota >= 0.7):
        snota = 'C'
    elif(vnota >= 0.6):
        snota = 'D'
    else:
        snota = 'F'

    return snota

while True:

    rawstr = input('Insira a pontuacao ou -1 para finalizar:')

    try:
        fstr = float(rawstr)
    except:
        print('Pontuacao invalida!')
        continue

    if(fstr == -1):
        quit()

    print(computarNotas(fstr))
