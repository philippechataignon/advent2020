#!/usr/bin/env python3
time = 1001612
slignes = "19,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,821,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,463,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23"
lignes = [int(x) for x in slignes.split(",") if x != "x"]
print(lignes)

class Ligne:
    def __init__(self, freq):
        self.freq = freq

    def next(self, stamp):
        return (stamp // self.freq + 1) * self.freq

    def __repr__(self):
        return "L%s" % self.freq

if __name__ == '__main__':
    ll = [Ligne(x) for x in lignes]
    print(ll)
    ml = [(x, x.next(time)) for x in ll if x.next(time) == min([x.next(time) for x in ll])][0]
    print(ml)
    print(ml[0].freq * (ml[1] - time))

