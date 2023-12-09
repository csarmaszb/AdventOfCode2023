true = True
false = False

import math

def solve_part_1(input_data: str):
    print("solve part 1")
    splits = input_data.split("\n\n")
    steps = 0
    map = {}
    inst = splits[0]
    curr = "AAA"
    for s in splits[1].split("\n"):
        tmp = s.split(" = ")
        map[tmp[0]] = tmp[1][1:len(tmp[1]) - 1].split(", ")

    while curr != "ZZZ":
        if inst[steps % len(inst)] == "L":
            curr = map[curr][0]
        if inst[steps % len(inst)] == "R":
            curr = map[curr][1]
        steps += 1

    print(steps)

maps = {}

def solve_part_2(input_data: str):
    print("solve part 2")
    splits = input_data.split("\n\n")
    steps = list()
    inst = splits[0]
    currs = list()

    for s in splits[1].split("\n"):
        tmp = s.split(" = ")
        maps[tmp[0]] = tmp[1][1:len(tmp[1]) - 1].split(", ")
        if tmp[0][-1] == "A":
            currs.append(tmp[0])

    for c in currs:
        step = 0
        while c[-1] != "Z":
            if inst[step % len(inst)] == "L":
                c = maps[c][0]
            if inst[step % len(inst)] == "R":
                c = maps[c][1]
            step += 1
        steps.append(step)

    print(math.lcm(*steps))