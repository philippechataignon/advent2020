#!/usr/bin/env python3

class Grille:
    def __init__(self):
        with open("input.txt") as f:
            self.gr = f.read().splitlines()
            self.size = len(self.gr[0])
            self.nb = len(self.gr)

    def is_tree(self, r, c):
        return self.gr[r][c % self.size] == "#"

    def slope(self, dr, dc):
        n = 0
        for i in range(self.nb):
            r = dr * i
            if r >= self.nb:
                break
            c = dc * i
            if self.is_tree(r, c):
                n += 1
        return n

def main():
    g = Grille()
    print(g.slope(1, 3))
    print(g.slope(1, 1) * g.slope(1, 3) * g.slope(1, 5) * g.slope(1, 7) * g.slope(2, 1))

if __name__ == '__main__':
    main()
