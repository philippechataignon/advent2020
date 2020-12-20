#!/usr/bin/env python3
import re

def test_ticket(liste_t, d):
    ret = []
    for t in liste_t:
        for s1, e1, s2, e2 in d.values():
            for e in t:
                print(e, s1, e1, s2, e2)
                if not (s1 <= e <= e1 or s2 <= e <= e2):
                    ret.append(e)
    return ret

hdr = re.compile(r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$')

with open("test.txt") as f:
    ll = f.read()[0:-1].split("\n\n")

d = {}
for l in ll[0].split("\n"):
    m = hdr.findall(l)
    if m:
        m = m[0]
        d[m[0]] = (int(m[1]), int(m[2]), int(m[3]), int(m[4]))

my = eval("[" + ll[1].split(":")[1].strip() + "]")
near = [eval("[" + e.strip() + "]") for e in ll[2].split("\n")[1:]]

t = test_ticket(near, d)
print(t)
print(sum(t))

