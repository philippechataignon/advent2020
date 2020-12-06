#!/usr/bin/env python3


with open("input.txt") as f:
    ll = f.read().splitlines()
ll = [x.split() for x in ll]
il = iter(ll)

out = []
d = {}
while True:
    try:
        l = next(il)
    except StopIteration:
        out.append(d)
        break

    if l == []:
        out.append(d)
        d = {}
    else:
        for e in l:
            k,v = e.split(":")
            d[k] = v

print(len(out))

n = 0
for p in out:
    ok = "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p \
        and "hcl" in p and "ecl" in p and "pid" in p
    if ok:
        n += 1
    else:
        print(p)

print(n)


