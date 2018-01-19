from sys import stdin
gates = int(raw_input())
planes = int(raw_input())
taken = []
count = 0
for i in xrange(planes):
    poss = int(raw_input())
    while poss != 0:
        if poss not in taken:
            taken.append(poss)
            count += 1
            break
        else:
            poss -= 1
    if poss == 0:
        break

print count
rest = stdin.read()


