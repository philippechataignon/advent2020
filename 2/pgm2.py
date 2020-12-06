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
                nc = sum([s[a-1] == c, s[b-1] == c])
                print(a,b,c,s,nc)
                if nc == 1:
                    n += 1
        print(n)


if __name__ == '__main__':
    main()
