#!/usr/bin/env python3
from collections import deque

def main():
    d = deque(maxlen=25)
    f = open("input.txt")

    for i in range(25):
        ll = f.readline()
        l = int(ll.strip())
        d.append(l)

    while True:
        ll = f.readline()
        l = int(ll.strip())
        p = set()
        for d1 in list(d)[:-1]:
            for d2 in list(d)[1:]:
                p.add(d1 + d2)
        if l not in p:
            break
        d.append(l)
    t = l
    print(t)

    ll = [int(x.strip()) for x in open("input.txt").readlines()]

    found = False
    for i in range(2, len(ll)):
        l = ll.copy()
        d = deque(maxlen=i)
        for j in range(i-1):
            d.append(l.pop(0))
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

