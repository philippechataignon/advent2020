#!/usr/bin/env python3
class Navig:
    dirs = {"E":(1,0), "S":(0, -1), "W": (-1, 0), "N": (0, 1)}
    caps = {0:"E", 270:"S", 180:"W", 90:"N"}
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cap = 0

    def path(self, cmd, nb):
        if cmd in Navig.dirs:
            self.x += Navig.dirs[cmd][0] * nb
            self.y += Navig.dirs[cmd][1] * nb
        elif cmd == "L":
            self.turn(nb)
        elif cmd == "R":
            self.turn(-nb)
        elif cmd == "F":
            self.forward(nb)

    def turn(self, nb):
        self.cap += nb
        if self.cap < 0:
            self.cap += 360
        if self.cap >= 360:
            self.cap -= 360

    def forward(self, nb):
        self.x += Navig.dirs[Navig.caps[self.cap]][0] * nb
        self.y += Navig.dirs[Navig.caps[self.cap]][1] * nb

def main():
    ll = [(x[0], int(x[1:].strip())) for x in open("input.txt").readlines()]
    nav = Navig()
    for l in ll:
        nav.path(*l)
    print(nav.x, nav.y, abs(nav.x) + abs(nav.y))

if __name__ == '__main__':
    main()
