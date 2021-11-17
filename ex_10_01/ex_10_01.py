fname = input('Enter the name of the file: ')

if(len(fname) < 1) : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

print(di)

tmp = list()
#This gives us a list of the key value pairs:
for k, v in di.items():
    newTuple = (v, k)
    tmp.append(newTuple)

#print('Flipped', tmp)

tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp[:5])

for v,k in tmp[:5]:
    print(v, k)
