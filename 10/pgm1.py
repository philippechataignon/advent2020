#!/usr/bin/env python3

from collections import Counter

def main():
    pass

def main():
    ll = [int(x.strip()) for x in open("test2.txt").readlines()]
    ll.insert(0, 0)
    ll = sorted(ll)
    print(ll)

    dd = [ll[i+1] - ll[i] for i in range(len(ll) - 1)]
    print(dd)

    cc = Counter(dd)
    print(dd)
    print(cc)
    print(cc[1] * (cc[3] + 1))

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()

