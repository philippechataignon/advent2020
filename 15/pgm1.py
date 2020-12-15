#!/usr/bin/env python3

rindex = lambda l, item: l[::-1].index(item) + 1

l = [1,0,18,10,19,6]
v = 0

for i in range(2020 - len(l)):
    if v in l:
        n = rindex(l, v)
    else:
        n = 0
    l.append(v)
    # print(n, l)
    v = n

print(l[-1])






