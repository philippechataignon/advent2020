#!/usr/bin/env python3
with open("input.txt") as f:
    ll = f.read()[0:-1].split("\n\n")

ll = [x.split("\n") for x in ll]
ll = [[set(x) for x in l] for l in ll]
ll = [x[0].intersection(*x) for x in ll]
print(sum([len(x) for x in ll]))
