#!/usr/bin/env python3
from collections import deque

def main():
    ll = [int(x.strip()) for x in open("input.txt").readlines()]
    f = ll.copy()

    d = deque(f[:25], maxlen=25)
    f = f[25:]

    while True:
        l = f.pop(0)
        p = set()
        for d1 in list(d)[:-1]:
            for d2 in list(d)[1:]:
                p.add(d1 + d2)
        if l not in p:
            break
        d.append(l)
    t = l
    print(t)

    found = False
    for i in range(2, len(ll)):
        l = ll.copy()
        d = deque(l[:i], maxlen=i)
        l = l[i:]
        while l:
            if sum(d) == t:
                found = True
                break
            d.append(l.pop(0))
        if found:
            break

    if found:
        print(min(d) + max(d))

if __name__ == '__main__':
    main()

