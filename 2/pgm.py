#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        n1 = 0
        n2 = 0
        for l in f:
            r, c, s = l.strip().split()
            a, b = r.split("-")
            a = int(a)
            b = int(b)
            c = c[:-1]

            nc = sum([x == c for x in s])
            if a <= nc <= b:
                n1 += 1
            nd = sum([s[a-1] == c, s[b-1] == c])
            if nd == 1:
                n2 += 1

    print(n1, n2)

if __name__ == '__main__':
    main()
