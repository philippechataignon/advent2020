#!/usr/bin/env python3
import re

# plaid green bags contain 3 dark red bags, 1 wavy crimson bag, 4 light coral bags, 4 striped indigo bags.
motif4 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?, (\d+) (.*) bags?, (\d+) (.*) bags?, (\d+) (.*) bags?\.$')
motif3 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?, (\d+) (.*) bags?, (\d+) (.*) bags?\.$')
motif2 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?, (\d+) (.*) bags?\.$')
motif1 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?\.$')
motif0 = re.compile(r'^(.*) bags contain no other bags\.$')

s = set()


def peres(enf):
    lp = set([p[0] for p in pere if p[1] in enf])
    return lp

if __name__ == "__main__":
    global pere
    pere = []
    with open("input.txt") as f:
        for l in f:
            l = l.rstrip()
            m4 = motif4.findall(l)
            m3 = motif3.findall(l)
            m2 = motif2.findall(l)
            m1 = motif1.findall(l)
            m0 = motif0.findall(l)
            if m4:
                m = m4[0]
                for i in range(2, len(m), 2):
                    pere.append((m[0], m[i]))
            elif m3:
                m = m3[0]
                for i in range(2, len(m), 2):
                    pere.append((m[0], m[i]))
            elif m2:
                m = m2[0]
                for i in range(2, len(m), 2):
                    pere.append((m[0], m[i]))
            elif m1:
                m = m1[0]
                pere.append((m[0], m[2]))
            elif m0:
                #m = m0[0]
                pere.append((m[0], ""))

    print(pere)

    p0 = ["shiny gold"]
    s = set()
    while True:
        p = peres(p0)
        if not p:
            break
        s = s.union(p)
        p0 = p
    print(s)
    print(len(s))


