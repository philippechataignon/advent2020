#!/usr/bin/env python3
import numpy as np

N = 30_000_000
# N = 2020
d = np.zeros(N, np.int32)

l = [1,0,18,10,19,6]
# l = [0, 3, 6]
for i, v in enumerate(l):
    d[v] = len(l) - i
print(d[:9])

v = 0
s = set(l)

for i in range(N - len(l)):
    n = d[v]
    d[v] = 0
    s.add(v)
    d[list(s)] += 1
    lv = v
    v = n
    # print(i, v, n)
    if i % 10000 == 0:
        print(i // 10000)
print(lv)
