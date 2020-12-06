#!/usr/bin/env python3

class Grille:
    def __init__(self):
        with open("input.txt") as f:
            self.gr = f.read().splitlines()
            self.size = len(self.gr[0])
            self.nb = len(self.gr)

    def is_tree(self, r, c):
        return self.gr[r][c % self.size] == "#"

def main():
    g = Grille()
    n = 0
    for i in range(g.nb):
        r = i
        c = 3 * i
        if g.is_tree(r, c):
            n += 1
        print(r, c, n)

if __name__ == '__main__':
    main()
