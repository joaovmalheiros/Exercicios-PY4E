str = 'X-DSPAM-Confidence: 0.8475  '

colonposition = str.find(':')
fval = float(str[colonposition+1:])
print(fval)
