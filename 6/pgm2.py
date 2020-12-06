#!/usr/bin/env python3

with open("input.txt") as f:
    ll = f.read().splitlines()
il = iter(ll)

s = set()
n = 0
out = []
first = True
while True:
    try:
        l = next(il)
    except StopIteration:
        out.append(s)
        n += len(s)
        break

    if l == "":
        out.append(s)
        n += len(s)
        s = set()
        first = True
    else:
        if first:
            s = set(l)
            first = False
        else:
            s = s.intersection(set(l))

# print(out)
print(sum([len(x) for x in out]))

