r1 = map(int, raw_input().split())
r2 = map(int, raw_input().split())
r3 = map(int, raw_input().split())
r4 = map(int, raw_input().split())

c = sum(r1)

if sum(r2) == c and sum(r3) == c and sum(r4) == c:
    b = True
    for i in range(4):
        a = r1[i] + r2[i] + r3[i] + r4[i]
        if a != c:
            b = False
    if b == True:
        print "magic"
    else:
        print "not magic"
else:
    print "not magic"
        
