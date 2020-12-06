#!/usr/bin/env python3

import re

m = re.compile(r'(\d+)-(\d+) (.): (.*)')

def main():
    with open("input.txt") as f:
        n = 0
        for l in f:
            if mm := m.findall(l):
                a, b, c, s = mm[0]
                a = int(a)
                b = int(b)
                nc = sum([x == c for x in s])
                print(a,b,c,s,nc)
                if a <= nc and nc <= b:
                    n += 1
        print(n)


if __name__ == '__main__':
    main()
