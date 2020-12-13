#!/usr/bin/env python3
import math

slignes = "19,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,821,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,463,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23"
# slignes = "7,13,x,x,59,x,31,19"
# slignes = "67,7,59,61"
lignes = [(int(x), i % int(x)) for i, x in enumerate(slignes.split(",")) if x != "x"]
print(lignes)
# (19, 0), (41, 9), (37, 13), (821, 19), (13, 6), (17, 2), (29, 19), (463, 50), (23, 4)
FIN = 100_000_000_000_000_000
mult = lignes[0][0]

def mink(deb, incr, n, modn):
    "Renvoit le premier entier m qui vérifie la condition m + delta modulo ligne = 0"
    print(deb, incr, n, modn)
    found = False
    for k in range(deb, FIN, incr):
        m = mult * k
        if (m + modn) % n == 0:
            found = True
            break
    if found:
        return k
    else:
        return None

m = 1
k1 = 1
for n, modn in lignes[1:]:
    # plus petit entier
    k1 = mink(k1, m , n, modn)
    # on incrémente le pas en le multipliant pour conserver les modulo existants
    m *= n

n =  mult * k1
print(n)
