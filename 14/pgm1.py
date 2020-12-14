#!/usr/bin/env python3

m = {}
f = open("input.txt")
for l in f:
    if l[:4] == "mask":
        mask = l[7:]
        mask_and = int(mask.replace("X", "1"), 2)
        mask_or = int(mask.replace("X", "0"), 2)
    elif l[:4] == "mem[":
        adr = int(l[4:].split("]")[0])
        val = int(l[6:-1].split("=")[1])
        val = (val & mask_and) | mask_or
        m[adr] = val

print(sum(m.values()))
