#!/usr/bin/env python3

import re

def to_bin(s):
    l = ['1' if c in ('B', 'R') else '0' for c in s]
    n = int("".join(l), 2)
    return n


if __name__ == "__main__":
    #print(to_bin("RLR"))
    #print(to_bin("FBFBBFF"))
    #print(to_bin("FBFBBFFRLR"))
    #print(to_bin("BFFFBBFRRR"))
    #print(to_bin("FFFBBBFRRR"))
    #print(to_bin("BBFFBBFRLL"))
    m = 0
    with open("input.txt") as f:
        for l in f:
            l = l.rstrip()
            n = to_bin(l)
            if n > m:
                m = n
                mm = l
    print(mm, m)
