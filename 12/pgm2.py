#!/usr/bin/env python3
class Navig:
    dirs = {"E":(1,0), "S":(0, -1), "W": (-1, 0), "N": (0, 1)}
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Way(Navig):
    def path(self, cmd, nb):
        if cmd in Navig.dirs:
            self.x += Navig.dirs[cmd][0] * nb
            self.y += Navig.dirs[cmd][1] * nb
        elif cmd == "L":
            if nb == 90:
                self.turn(1)
            elif nb == 180:
                self.turn(2)
            elif nb == 270:
                self.turn(3)
        elif cmd == "R":
            if nb == 90:
                self.turn(3)
            elif nb == 180:
                self.turn(2)
            elif nb == 270:
                self.turn(1)

    def turn(self, nb):
        for i in range(nb):
            self.x, self.y = -self.y, self.x

class Boat(Navig):
    def forward(self, way, nb):
        self.x += nb * way.x
        self.y += nb * way.y

def main():
    ll = [(x[0], int(x[1:].strip())) for x in open("input.txt").readlines()]
    way = Way(10, 1)
    boat = Boat(0, 0)
    for cmd, nb in ll:
        if cmd == "F":
            boat.forward(way, nb)
        else:
            way.path(cmd, nb)
    print(boat.x, boat.y, abs(boat.x) + abs(boat.y))

if __name__ == '__main__':
    main()
