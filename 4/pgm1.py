#!/usr/bin/env python3

import re

m_hgt = re.compile(r'^(\d+)(cm|in)$')
m_hcl = re.compile(r'^#[0-9a-f]{6}$')
m_ecl = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
m_pid = re.compile(r'^\d{9}$')
m_year = re.compile(r'^(\d{4})$')

with open("input.txt") as f:
    ll = f.read()[0:-1].split("\n\n")

n = 0
for p in (dict([e.split(":") for e in x.replace("\n", " ").split(" ")]) for x in ll):
    ok = "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p \
        and "hcl" in p and "ecl" in p and "pid" in p

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    m = m_year.match(p.get("byr", ""))
    ok = ok and m and 1920 <= int(m.group(1)) <= 2002

    m = m_year.match(p.get("iyr", ""))
    ok = ok and m and 2010 <= int(m.group(1)) <= 2020

    m = m_year.match(p.get("eyr", ""))
    ok = ok and m and 2020 <= int(m.group(1)) <= 2030

    m = m_hgt.match(p.get("hgt", ""))
    ok = ok and m and (
            (m.group(2) == "cm" and 150 <= int(m.group(1)) <= 193) or
            (m.group(2) == "in" and 59 <= int(m.group(1)) <= 76)
        )

    ok = ok and m_hcl.match(p.get("hcl", ""))
    ok = ok and m_ecl.match(p.get("ecl", ""))
    ok = ok and m_pid.match(p.get("pid", ""))

    if ok:
        n += 1

print(n)
