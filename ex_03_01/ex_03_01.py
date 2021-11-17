hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))

if(hours < 40):
    pay = hours * rate
else:
    pay = (40 * rate) + (hours - 40) * 1.5 * (rate)
print("Pay: ",pay)
