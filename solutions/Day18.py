import re
import math

true = True
false = False

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

def solve_part_1(input_data: str):
    print("solve part 1")
    # directions = input_data.split("\n")
    # now = (0, 0)
    # points = [(0, 0)]
    # for r in directions:
    #     d, m, c = r.split(" ")
    #     if d == "R":
    #         for i in range(int(m)):
    #             now = (now[0] + right[0], now[1] + right[1])
    #             points.append(now)
    #     if d == "U":
    #         for i in range(int(m)):
    #             now = (now[0] + up[0], now[1] + up[1])
    #             points.append(now)
    #     if d == "D":
    #         for i in range(int(m)):
    #             now = (now[0] + down[0], now[1] + down[1])
    #             points.append(now)
    #     if d == "L":
    #         for i in range(int(m)):
    #             now = (now[0] + left[0], now[1] + left[1])
    #             points.append(now)
    #
    # minx = min(map(lambda x: x[0], points))
    # maxx = max(map(lambda x: x[0], points))
    # miny = min(map(lambda x: x[1], points))
    # maxy = max(map(lambda x: x[1], points))
    #
    # grid = []
    # for i in range(minx - 1, maxx + 2):
    #     tmpr = []
    #     for j in range(miny - 1, maxy + 2):
    #         if (i, j) in points:
    #             tmpr.append("#")
    #         else:
    #             tmpr.append(".")
    #     grid.append(tmpr)
    #
    # visited = []
    # next = [(0, 0)]
    # while len(next) > 0:
    #     now = next.pop(0)
    #     for d in [left, up, right, down]:
    #         n = (now[0] + d[0], now[1] + d[1])
    #         if n[0] in range(0, len(grid)) and n[1] in range(0, len(grid[0])) and n not in visited and n not in next:
    #             if grid[n[0]][n[1]] == ".":
    #                 next.append(n)
    #     visited.append(now)
    #     grid[now[0]][now[1]] = "X"
    #
    # summa = 0
    # for r in grid:
    #     summa += len(list(filter(lambda x: x == "#" or x == ".", r)))
    #
    # print(summa)

    directions = input_data.split("\n")
    now = (0, 0)
    # points = [(0, 0)]
    maxes = {}
    for r in directions:
        d, m, c = r.split(" ")
        if d == "R":
            for i in range(int(m)):
                now = (now[0] + right[0], now[1] + right[1])
                # points.append(now)

            if now[0] in maxes.keys():
                if maxes[now[0]][1] < now[1]:
                    maxes[now[0]][1] = now[1]
            else:
                maxes[now[0]] = [now[1] - int(m), now[1]]

        if d == "U":
            for i in range(int(m)):
                now = (now[0] + up[0], now[1] + up[1])
                # points.append(now)

                if now[0] in maxes.keys():
                    if maxes[now[0]][1] < now[1]:
                        maxes[now[0]][1] = now[1]
                    if maxes[now[0]][0] > now[1]:
                        maxes[now[0]][0] = now[1]
                else:
                    maxes[now[0]] = [now[1], now[1]]

        if d == "D":
            for i in range(int(m)):
                now = (now[0] + down[0], now[1] + down[1])
                # points.append(now)

                if now[0] in maxes.keys():
                    if maxes[now[0]][1] < now[1]:
                        maxes[now[0]][1] = now[1]
                    if maxes[now[0]][0] > now[1]:
                        maxes[now[0]][0] = now[1]
                else:
                    maxes[now[0]] = [now[1], now[1]]

        if d == "L":
            for i in range(int(m)):
                now = (now[0] + left[0], now[1] + left[1])
                # points.append(now)

            if now[0] in maxes.keys():
                if maxes[now[0]][0] > now[1]:
                    maxes[now[0]][0] = now[1]
            else:
                maxes[now[0]] = [now[1], now[1] + int(m)]

    summa = 0
    for i in maxes.keys():
        summa += maxes[i][1] - maxes[i][0] + 1
    print(summa)

def solve_part_2(input_data: str):
    print("solve part 2")
    directions = input_data.split("\n")
    now = (0, 0)
    points = [(0, 0)]
    asd = [["."] * 15_000_000 for i in range(15_000_000)]
    print("Read")
    for r in directions:
        d, m, c = r.split(" ")
        c = c[2: len(c) - 1]
        print(c, int(c[:len(c) - 1], base=16))
        if c[-1] == "0":
            for i in range(int(c[:len(c) - 1], base=16)):
                now = (now[0] + right[0], now[1] + right[1])
                points.append(now)
        if c[-1] == "3":
            for i in range(int(c[:len(c) - 1], base=16)):
                now = (now[0] + up[0], now[1] + up[1])
                points.append(now)
        if c[-1] == "1":
            for i in range(int(c[:len(c) - 1], base=16)):
                now = (now[0] + down[0], now[1] + down[1])
                points.append(now)
        if c[-1] == "2":
            for i in range(int(c[:len(c) - 1], base=16)):
                now = (now[0] + left[0], now[1] + left[1])
                points.append(now)

    minx = min(map(lambda x: x[0], points))
    maxx = max(map(lambda x: x[0], points))
    miny = min(map(lambda x: x[1], points))
    maxy = max(map(lambda x: x[1], points))

    print("Making grid", minx, maxx, miny, maxy)
    grid = []
    for i in range(minx - 1, maxx + 2):
        if i % 10 == 0:
            print(i)
        tmpr = []
        for j in range(miny - 1, maxy + 2):
            if j % 10 == 0:
                print(i, j)
            if (i, j) in points:
                tmpr.append("#")
            else:
                tmpr.append(".")
        grid.append(tmpr)

    print("Clear points")
    points.clear()
    visited = []
    next = [(0, 0)]
    while len(next) > 0:
        now = next.pop(0)
        for d in [left, up, right, down]:
            n = (now[0] + d[0], now[1] + d[1])
            if n[0] in range(0, len(grid)) and n[1] in range(0, len(grid[0])) and n not in visited and n not in next:
                if grid[n[0]][n[1]] == ".":
                    next.append(n)
        visited.append(now)
        grid[now[0]][now[1]] = "X"

    summa = 0
    for r in grid:
        summa += len(list(filter(lambda x: x == "#" or x == ".", r)))

    print(summa)
    # directions = input_data.split("\n")
    # now = (0, 0)
    # ranges = {}
    # for r in directions:
    #     d, m, c = r.split(" ")
    #     c = c[2 : len(c) - 1]
    #     # print(c, int(c[:len(c) - 1], base=16))
    #     if c[-1] == "0":
    #         for i in range(int(c[:len(c) - 1], base=16)):
    #             now = (now[0] + right[0], now[1] + right[1])
    #
    #         if now[0] in ranges.keys():
    #             if ranges[now[0]][1] < now[1]:
    #                 ranges[now[0]][1] = now[1]
    #         else:
    #             ranges[now[0]] = [now[1] - int(c[:len(c) - 1], base=16), now[1]]
    #
    #     if c[-1] == "3":
    #         for i in range(int(c[:len(c) - 1], base=16)):
    #             now = (now[0] + up[0], now[1] + up[1])
    #
    #             if now[0] in ranges.keys():
    #                 if ranges[now[0]][1] < now[1]:
    #                     ranges[now[0]][1] = now[1]
    #                 if ranges[now[0]][0] > now[1]:
    #                     ranges[now[0]][0] = now[1]
    #             else:
    #                 ranges[now[0]] = [now[1], now[1]]
    #
    #     if c[-1] == "1":
    #         for i in range(int(c[:len(c) - 1], base=16)):
    #             now = (now[0] + down[0], now[1] + down[1])
    #
    #             if now[0] in ranges.keys():
    #                 if ranges[now[0]][1] < now[1]:
    #                     ranges[now[0]][1] = now[1]
    #                 if ranges[now[0]][0] > now[1]:
    #                     ranges[now[0]][0] = now[1]
    #             else:
    #                 ranges[now[0]] = [now[1], now[1]]
    #
    #     if c[-1] == "2":
    #         for i in range(int(c[:len(c) - 1], base=16)):
    #             now = (now[0] + left[0], now[1] + left[1])
    #
    #         if now[0] in ranges.keys():
    #             if ranges[now[0]][0] > now[1]:
    #                 ranges[now[0]][0] = now[1]
    #         else:
    #             ranges[now[0]] = [now[1], now[1] + int(c[:len(c) - 1], base=16)]
    #
    # summa = 0
    # for i in ranges.keys():
    #     summa += ranges[i][1] - ranges[i][0] + 1
    #
    # print(summa)