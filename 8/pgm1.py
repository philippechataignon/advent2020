#!/usr/bin/env python3
def main():
    with open("input.txt") as f:
        ll = [tuple(x.strip().split()) for x in f.readlines()]

    pc = 0
    acc = 0
    s = set([0])

    while True:
        cmd, val = ll[pc]
        # print(cmd, val)
        val = int(val)
        if cmd == "acc":
            acc += val
            pc += 1
        elif cmd == "jmp":
            pc += val
        elif cmd == "nop":
            pc += 1
        #print(acc, pc)
        if pc in s:
            break
        s.add(pc)

    print(acc, pc)

if __name__ == '__main__':
    main()
