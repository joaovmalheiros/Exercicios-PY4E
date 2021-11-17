'''
fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    wds = line.split()
    if line == '': ##if line is a blank line
        continue
    if wds[0] != 'From' :
        continue
    print(wds[2])
'''

'''
fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    wds = line.split()
    #Guardian in an compound statement:
    if len(wds) < 3: or if wds[0] != 'From' : ##if we flip this order, it fails. Short circuit evaluation
        continue
    print(wds[2])
'''

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    wds = line.split()
    #Guardian:
    if len(wds) < 3: ##in case of line has no words or has a 'From', but only one word
        continue
    if wds[0] != 'From' :
        continue
    print(wds[2])
