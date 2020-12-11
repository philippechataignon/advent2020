#!/usr/bin/env python3
from copy import deepcopy

class Grille:
    def __init__(self, gr=None):
        if gr is None:
            self.gr = [list(x.strip()) for x in open("test.txt").readlines()]
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

    def grille(self):
        return self.gr

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

    def gen(self):
        new_gr = deepcopy(self.gr)
        for r in range(self.nrow):
            for c in range(self.ncol):
                v = self.voisin(r, c, "#")
                print(r,c,v)
                if self.case(r, c) == "L" and v == 0:
                    new_gr[r][c] = "#"
                elif self.case(r, c) == "#" and v >= 4:
                    new_gr[r][c] = "L"
        return new_gr

if __name__ == '__main__':
    g = Grille()
    print(g.gen())
