#!/usr/bin/env python3
class Navig:
    dirs = {"E":(1,0), "S":(0, -1), "W": (-1, 0), "N": (0, 1)}
    caps = {0:"E", 270:"S", 180:"W", 90:"N"}
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.cap = 0

class Way(Navig):
    def path(self, cmd, nb):
        if cmd in Navig.dirs:
            self.x += Navig.dirs[cmd][0] * nb
            self.y += Navig.dirs[cmd][1] * nb
        elif cmd == "L":
            self.turn(nb)
        elif cmd == "R":
            self.turn(-nb)

    def turn(self, nb):
        self.cap += nb
        if self.cap < 0:
            self.cap += 360
        if self.cap >= 360:
            self.cap -= 360

class Boat(Navig):
    def forward(self, way, nb):
        self.x += nb * way.x
        self.y += nb * way.y

def main():
    ll = [(x[0], int(x[1:].strip())) for x in open("test.txt").readlines()]
    way = Way(10, 1)
    boat = Boat(0, 0)
    for cmd, nb in ll:
        print(">", cmd, nb)
        if cmd == "F":
            boat.forward(way, nb)
        else:
            way.path(cmd, nb)
        print("B", boat.x, boat.y)
        print("w", way.x, way.y)

    print("Fin:", boat.x, boat.y, abs(boat.x) + abs(boat.y))

if __name__ == '__main__':
    main()
