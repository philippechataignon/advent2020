#!/usr/bin/env python3

def findall(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def genx(adr, xpos):
    # convertit adr en chaine binaire
    adrbit = f'{adr:036b}'
    # lch = adr en liste de char 0 ou 1
    lch = list(adrbit)
    # nb de position float
    n = len(xpos)
    ret = []
    # v parcourt toute les valeurs possibles
    for v in range(1 << n):
        # version binaire limitée à n char de v
        s = f'{v:036b}'[-n:]
        # qu'on vient mettre dans lch=adrbit
        for i, pos in enumerate(xpos):
            lch[pos] = s[i]
        # ajoute le résultat en décimal
        ret.append(int("".join(lch), 2))
    return ret

m = {}
f = open("input.txt")
for l in f:
    if l[:4] == "mask":
        mask = l[7:]
        mask_or = int(mask.replace("X", "1"), 2)
        xpos = findall(mask, "X")
    elif l[:4] == "mem[":
        adr = int(l[4:].split("]")[0]) | mask_or
        val = int(l[6:-1].split("=")[1])
        for a in genx(adr, xpos):
            m[a] = val

print(sum(m.values()))
