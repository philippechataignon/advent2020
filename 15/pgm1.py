#!/usr/bin/env python3

rindex = lambda l, item: l[::-1].index(item) + 1

l = [1,0,18,10,19,6]
# l = [0, 3, 6]
v = 0
d = {v:len(l) - i for i, v in enumerate(l)}
print(d)
for i in range(30_000_000 - len(l)):
    if v in d:
        n = d[v]
    else:
        n = 0
    d[v] = 0
    d = {k: v+1 for k,v in d.items()}
    # print(n, d)
    lv = v
    v = n

print(lv)
