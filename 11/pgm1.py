#!/usr/bin/env python3
import copy

class Grille:
    def __init__(self, gr=None):
        if gr is None:
            self.gr = [list(x.strip()) for x in open("input.txt").readlines()]
        else:
            self.gr = gr
        self.ncol = len(self.gr[0])
        self.nrow = len(self.gr)

    def case(self, r, c):
        if 0 <= r < self.nrow and 0 <= c < self.ncol:
            ret = self.gr[r][c]
        else:
            ret = "."
        return ret

    def __repr__(self):
        return "\n".join(["".join(x) for x in self.gr])

    __str__ = __repr__

    def voisin(self, r, c, char):
        return \
            int(self.case(r-1, c-1) == char) + \
            int(self.case(r-1, c) == char) + \
            int(self.case(r-1, c+1) == char) + \
            int(self.case(r, c-1) == char) + \
            int(self.case(r, c+1) == char) + \
            int(self.case(r+1, c-1) == char) + \
            int(self.case(r+1, c) == char) + \
            int(self.case(r+1, c+1) == char)

    def count(self, char):
        n = 0
        for r in range(self.nrow):
            for c in range(self.ncol):
                if self.case(r, c) == char:
                    n += 1
        return n

    def gen(self):
        new_gr = copy.deepcopy(self.gr)
        for r in range(self.nrow):
            for c in range(self.ncol):
                v = self.voisin(r, c, "#")
                if self.case(r, c) == "L" and v == 0:
                    new_gr[r][c] = "#"
                elif self.case(r, c) == "#" and v >= 4:
                    new_gr[r][c] = "L"
        return new_gr

if __name__ == '__main__':
    g = Grille()
    first = True
    while True:
        g = Grille(g.gen())
        if not first and repr(g) == repr(prevg):
            break
        prevg = g
        first = False
    print(g.count("#"))
