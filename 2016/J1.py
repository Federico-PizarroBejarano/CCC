c = 0

g1 = raw_input()
if g1 == "W":
    c += 1
g2 = raw_input()
if g2 == "W":
    c += 1
g3 = raw_input()
if g3 == "W":
    c += 1
g4 = raw_input()
if g4 == "W":
    c += 1
g5 = raw_input()
if g5 == "W":
    c += 1
g6 = raw_input()
if g6 == "W":
    c += 1

if c in [5, 6]:
    print 1
elif c in [3, 4]:
    print 2
elif c in [1, 2]:
    print 3
else:
    print -1
