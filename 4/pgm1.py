#!/usr/bin/env python3

import re

m_hgt = re.compile(r'^(\d+)(cm|in)$')
m_hcl = re.compile(r'^#[0-9a-f]{6}$')
m_ecl = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
m_pid = re.compile(r'^\d{9}$')

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

n = 0
for p in out:
    ok = "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p \
        and "hcl" in p and "ecl" in p and "pid" in p

    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    #hgt (Height) - a number followed by either cm or in:
    #    If cm, the number must be at least 150 and at most 193.
    #    If in, the number must be at least 59 and at most 76.
    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    #cid (Country ID) - ignored, missing or not.

    try:
        byr = int(p.get("byr"))
        ok = ok and 1920 <= byr <= 2002
    except (ValueError, TypeError):
        ok = False

    try:
        iyr = int(p.get("iyr"))
        ok = ok and 2010 <= iyr <= 2020
    except (ValueError, TypeError):
        ok = False

    try:
        eyr = int(p.get("eyr"))
        ok = ok and 2020 <= eyr <= 2030
    except (ValueError, TypeError):
        ok = False

    m = m_hgt.match(p.get("hgt", ""))
    if m:
        hgt = int(m.group(1))
        if m.group(2) == "cm":
            ok = ok and 150 <= hgt <= 193
        elif m.group(2) == "in":
            ok = ok and 59 <= hgt <= 76
    else:
        ok = False

    m = m_hcl.match(p.get("hcl", ""))
    if not m:
        ok = False

    m = m_ecl.match(p.get("ecl", ""))
    if not m:
        ok = False

    m = m_pid.match(p.get("pid", ""))
    if not m:
        ok = False

    if ok:
        n += 1

print(n)


