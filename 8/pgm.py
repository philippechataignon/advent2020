#!/usr/bin/env python3

def execute(pgm):
    pc = 0
    acc = 0
    s = set([0])

    while True:
        cmd, val = pgm[pc]
        val = int(val)
        if cmd == "acc":
            acc += val
            pc += 1
        elif cmd == "jmp":
            pc += val
        elif cmd == "nop":
            pc += 1
        if pc == len(pgm):
            return True, acc
        if pc in s:
            return False, acc
        s.add(pc)

def main():
    with open("input.txt") as f:
        pgm = [x.strip().split() for x in f.readlines()]

    _, val = execute(pgm)
    print(val)

    for i in range(len(pgm)):
        cmd, val = pgm[i]
        val = int(val)
        change = False
        if cmd == "jmp":
            l = pgm.copy()
            l[i] = ["nop", val]
            change = True
        elif cmd == "nop":
            l = pgm.copy()
            l[i] = ["jmp", val]
            change = True
        if change:
            e = execute(l)
            if e[0]:
                print(e[1])
                break

if __name__ == '__main__':
    main()
