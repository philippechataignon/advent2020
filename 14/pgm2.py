#!/usr/bin/env python3

def findall(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def genx(ch, xpos):
    lch = list(ch)
    n = len(xpos)
    ret = []
    for v in range(2 ** n):
        s = f'{v:036b}'[-n:]
        for i, pos in enumerate(xpos):
            lch[pos] = s[i]
        ret.append("". join(lch))
    # print(ch, xpos, ret, [int(x, 2) for x in ret])
    return ret

m = {}
f = open("input.txt")
for l in f:
    if l[:4] == "mask":
        mask = l[7:]
        mask_or = int(mask.replace("X", "1"), 2)
        xpos = findall(mask, "X")
    elif l[:4] == "mem[":
        adr = l[4:].split("]")[0]
        adrnum = int(adr) | mask_or
        adrbit = f'{adrnum:036b}'
        val = int(l[6:-1].split("=")[1])
        adrs = genx(adrbit, xpos)
        for adr in  adrs:
            m[int(adr, 2)] = val

print(sum(m.values()))
