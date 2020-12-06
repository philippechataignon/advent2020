#!/usr/bin/env python3

with open("input.txt") as f:
    ll = f.read().splitlines()
il = iter(ll)

out = []
s = set()
n = 0
while True:
    try:
        l = next(il)
    except StopIteration:
        # out.append(s)
        n += len(s)
        break

    if l == "":
        # out.append(s)
        n += len(s)
        s = set()
    else:
        s = s.union(set(l))

print(n)
