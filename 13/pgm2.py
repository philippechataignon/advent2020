#!/usr/bin/env python3
import math

slignes = "19,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,821,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,463,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23"
#slignes = "7,13,x,x,59,x,31,19" = 1068781
#slignes = "67,7,59,61" = 754018
lignes = [(int(x), i % int(x)) for i, x in enumerate(slignes.split(",")) if x != "x"]
print(lignes)
# (19, 0), (41, 9), (37, 13), (821, 19), (13, 6), (17, 2), (29, 19), (463, 50), (23, 4)
FIN = 100_000_000_000_000_000

def mink(deb, incr, n, modn):
    "Renvoit le premier entier k qui vérifie la condition (k + modn) modulo n = 0"
    print(deb, incr, n, modn)
    found = False
    for k in range(deb, FIN, incr):
        if (k + modn) % n == 0:
            found = True
            break
    if found:
        return k
    else:
        # ne doit pas arriver
        return None

k = 1 # début boucle
m = 1 # incrément

for n, modn in lignes:
    # plus petit entier
    k = mink(k, m , n, modn)
    # on incrémente le pas en le multipliant pour conserver les modulo existants
    m *= n

print(k)
