count = 0
total = 0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('bad data!')
        continue #!!!
    count = count + 1
    total = total + fval

print('Total: ', total)

try:
    print('Average: ', total/count)
except:
    print('No values entered, cannot divide by 0')


#sval : string value
#fval: floating value
