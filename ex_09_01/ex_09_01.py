fname = input('Enter the name of the file: ')

if(len(fname) < 1) : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        ##if not there, the count is zero
        ##if it is there, just add + 1
        di[w] = di.get(w, 0) + 1
        ##All the code below in a single line in the code above
        '''
        if w in di:
            di[w] = di[w] + 1
            print('***EXISTING***')
        else:
            di[w] = 1
            print('***NEW***')
        '''
print(di)

#Finding the most common word:
bigCount = None
bigWord = None

for k, v in di.items():
    if(bigCount == None or v > bigCount):
        bigCount = v
        bigWord = k
        print('bigCount: ', bigCount)
        print('bigWord: ', bigWord)
