jer = int(raw_input())
ath = int(raw_input())
ljer = []
fin = []
d = {"S":1, "M":2, "L":3}
count = 0

for i in xrange(jer):
    ljer.append(raw_input())

for i in xrange(ath):
    a = raw_input()
    if len(fin) == jer:
        break
    elif int(a[2:]) not in fin:
        if d[a[0]] <= d[ljer[int(a[2:])-1]]:
            count += 1
            fin.append(int(a[2:]))
        
print count
