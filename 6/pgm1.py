#!/usr/bin/env python3

with open("input.txt") as f:
    ll = f.read().split("\n\n")

print(sum([len(set(x.replace("\n", ""))) for x in ll]))
