q = input()
n = input()
dm = map(int, raw_input().split())
pg = map(int, raw_input().split())

s = 0
if q == 2:
    for i in range(n):
        if max(dm) >= max(pg):
            s += max(dm)
            dm.remove(max(dm))
            pg.remove(min(pg))
        else:
            s += max(pg)
            pg.remove(max(pg))
            dm.remove(min(dm))
else:
    for i in range(n):
        if max(dm) >= max(pg):
            s += max(dm)
            dm.remove(max(dm))
            pg.remove(max(pg))
        else:
            s += max(pg)
            pg.remove(max(pg))
            dm.remove(max(dm))

print s
