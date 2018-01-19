n = input()
x = []
y = []

poss = 0

xs = []
ys = []
xIDs = []
yIDs = []

for i in xrange(n):
    xi, yi = map(int, raw_input().split())
    x.append(xi)
    y.append(yi)

for i in xrange(n):
    idx = []
    idy = []
    if x[i] not in xs:
        for j in xrange(n):
            if x[j] == x[i]:
                idx.append(y[j])
        idx.sort()
        xs.append(x[i])
        xIDs.append(idx)
    else:
        idx = xIDs[xs.index(x[i])]

    if y[i] not in ys:
        for j in xrange(n):
            if y[j] == y[i]:
                idy.append(x[j])
        idy.sort()
        ys.append(y[i])
        yIDs.append(idy)
    else:
        idy = yIDs[ys.index(y[i])]

    if len(idx) > 1 and len(idy) > 1 and min(idx) < y[i] and max(idx) > y[i] and min(idy) < x[i] and max(idy) > x[i]:
        #print x[i], y[i]
        k = 0
        #idx.sort()
        #idy.sort()
        while k < len(idx):
            if idx[k] == y[i]:
                idx.remove(y[i])
            else:
                k += 1
        k = 0
        while k < len(idy):
            if idy[k] == x[i]:
                idy.remove(x[i])
            else:
                k += 1
    
        for k in xrange(len(idx)):
            if idx[k] > y[i]:
                maxy = k
                break
        for k in xrange(len(idy)):
            if idy[k] >= x[i]:
                maxx = k
                break
        
        poss += 2*len(idx[0: maxy])*len(idx[maxy:])*len(idy[0: maxx])*len(idy[maxx:])

print poss            
