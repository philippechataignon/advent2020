#!/usr/bin/env python3

from collections import Counter

def main():
    pass

def main():
    ll = [int(x.strip()) for x in open("input.txt").readlines()]
    ll.insert(0, 0)
    ll = sorted(ll)

    dd = [ll[i+1] - ll[i] for i in range(len(ll) - 1)]

    cc = Counter(dd)
    print(cc[1] * (cc[3] + 1))

if __name__ == '__main__':
    main()
