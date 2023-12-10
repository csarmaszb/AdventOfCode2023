import re
import math

true = True
false = False


def solve_part_1(input_data: str):
    print("solve part 1")
    grid = input_data.split("\n")
    start = None
    for i, r in enumerate(grid):
        if "S" in r:
            start = (i, r.find("S"))
            break
    steps = []
    while start not in steps:
        if start[0] > 0:
            if grid[start[0] - 1][start[1]] != "." and (grid[start[0] - 1][start[1]] == "|" or grid[start[0] - 1][start[1]] == "7" or grid[start[0] - 1][start[1]] == "F"):
                steps.append(start)
                next_step = (start[0] - 1, start[1])
                while next_step is not None and (next_step != start or next_step != "."):
                    tmp = next_step
                    next_step = get_next_step(grid, next_step[0], next_step[1], steps[-1][0], steps[-1][1])
                    steps.append(tmp)
                if next_step == start:
                    break

        steps = []
        if start[0] < len(grid[0]):
            steps = []
            if grid[start[0] + 1][start[1]] != "." and (grid[start[0] + 1][start[1]] == "|" or grid[start[0] + 1][start[1]] == "J" or grid[start[0] + 1][start[1]] == "L"):
                steps.append(start)
                next_step = (start[0] + 1, start[1])
                while next_step is not None and next_step != start:
                    tmp = next_step
                    next_step = get_next_step(grid, next_step[0], next_step[1], steps[-1][0], steps[-1][1])
                    steps.append(tmp)
                if next_step == start:
                    break

        steps = []
        if start[1] > 0:
            steps = []
            if grid[start[0]][start[1] - 1] != "." and (grid[start[0]][start[1] - 1] == "-" or grid[start[0]][start[1] - 1] == "L" or grid[start[0]][start[1] - 1] == "7"):
                steps.append(start)
                next_step = (start[0], start[1] - 1)
                while next_step is not None and (next_step != start or next_step != "."):
                    tmp = next_step
                    steps.append(next_step)
                    steps.append(tmp)
                if next_step == start:
                    break

        steps = []
        if start[1] < len(grid[0]):
            steps = []
            if grid[start[0]][start[1] + 1] != "." and (grid[start[0]][start[1] + 1] == "-" or grid[start[0]][start[1] + 1] == "7" or grid[start[0]][start[1] + 1] == "J"):
                steps.append(start)
                next_step = (start[0], start[1] + 1)
                while next_step is not None and (next_step != start or next_step != "."):
                    tmp = next_step
                    next_step = get_next_step(grid, next_step[0], next_step[1], steps[-1][0], steps[-1][1])
                    steps.append(tmp)
                if next_step == start:
                    break

    # print(steps)
    print(int(len(steps) / 2))


def solve_part_2(input_data: str):
    print("solve part 2")
    grid = input_data.split("\n")
    start = None
    for i, r in enumerate(grid):
        if "S" in r:
            start = (i, r.find("S"))
            break
    steps = []
    while start not in steps:
        if start[0] > 0:
            if grid[start[0] - 1][start[1]] != "." and (
                    grid[start[0] - 1][start[1]] == "|" or grid[start[0] - 1][start[1]] == "7" or grid[start[0] - 1][start[1]] == "F"):
                steps.append(start)
                next_step = (start[0] - 1, start[1])
                while next_step is not None and (next_step != start or next_step != "."):
                    tmp = next_step
                    next_step = get_next_step(grid, next_step[0], next_step[1], steps[-1][0], steps[-1][1])
                    steps.append(tmp)
                if next_step == start:
                    break

        steps = []
        if start[0] < len(grid):
            steps = []
            if grid[start[0] + 1][start[1]] != "." and (
                    grid[start[0] + 1][start[1]] == "|" or grid[start[0] + 1][start[1]] == "J" or grid[start[0] + 1][
                start[1]] == "L"):
                steps.append(start)
                next_step = (start[0] + 1, start[1])
                while next_step is not None and next_step != start:
                    tmp = next_step
                    next_step = get_next_step(grid, next_step[0], next_step[1], steps[-1][0], steps[-1][1])
                    steps.append(tmp)
                if next_step == start:
                    break

        steps = []
        if start[1] > 0:
            steps = []
            if grid[start[0]][start[1] - 1] != "." and (
                    grid[start[0]][start[1] - 1] == "-" or grid[start[0]][start[1] - 1] == "L" or grid[start[0]][
                start[1] - 1] == "7"):
                steps.append(start)
                next_step = (start[0], start[1] - 1)
                while next_step is not None and (next_step != start or next_step != "."):
                    tmp = next_step
                    steps.append(next_step)
                    steps.append(tmp)
                if next_step == start:
                    break

        steps = []
        if start[1] < len(grid[0]):
            steps = []
            if grid[start[0]][start[1] + 1] != "." and (
                    grid[start[0]][start[1] + 1] == "-" or grid[start[0]][start[1] + 1] == "7" or grid[start[0]][
                start[1] + 1] == "J"):
                steps.append(start)
                next_step = (start[0], start[1] + 1)
                while next_step is not None and (next_step != start or next_step != "."):
                    tmp = next_step
                    next_step = get_next_step(grid, next_step[0], next_step[1], steps[-1][0], steps[-1][1])
                    steps.append(tmp)
                if next_step == start:
                    break

    grid_v2 = list()

    for i in range(len(grid)):
        tmp = ["", "", ""]
        for j in range(len(grid[0])):
            if (i, j) not in steps:
                grid[i] = grid[i][0:j] + "." + grid[i][j + 1:]
            if grid[i][j] == "|":
                tmp[0] += ".█."
                tmp[1] += ".█."
                tmp[2] += ".█."
            if grid[i][j] == "-":
                tmp[0] += "..."
                tmp[1] += "███"
                tmp[2] += "..."
            if grid[i][j] == "F":
                tmp[0] += "..."
                tmp[1] += ".██"
                tmp[2] += ".█."
            if grid[i][j] == "7":
                tmp[0] += "..."
                tmp[1] += "██."
                tmp[2] += ".█."
            if grid[i][j] == "L":
                tmp[0] += ".█."
                tmp[1] += ".██"
                tmp[2] += "..."
            if grid[i][j] == "J":
                tmp[0] += ".█."
                tmp[1] += "██."
                tmp[2] += "..."
            if grid[i][j] == ".":
                tmp[0] += "..."
                tmp[1] += "..."
                tmp[2] += "..."
            if grid[i][j] == "S":
                tmp[0] += "SSS"
                tmp[1] += "SSS"
                tmp[2] += "SSS"
        grid_v2.append(tmp[0])
        grid_v2.append(tmp[1])
        grid_v2.append(tmp[2])

    now = (0, 0)
    next = [(0, 1), (1, 0)]
    visited = []
    while true:
        if now[0] - 1 >= 0 and (now[0] - 1, now[1]) not in next and (now[0] - 1, now[1]) not in visited and grid_v2[now[0] - 1][now[1]] == ".":
            next.append((now[0] - 1, now[1]))
        if now[0] + 1 < len(grid_v2) and (now[0] + 1, now[1]) not in next and (now[0] + 1, now[1]) not in visited and grid_v2[now[0] + 1][now[1]] == ".":
            next.append((now[0] + 1, now[1]))
        if now[1] - 1 >= 0 and (now[0], now[1] - 1) not in next and (now[0], now[1] - 1) not in visited and grid_v2[now[0]][now[1] - 1] == ".":
            next.append((now[0], now[1] - 1))
        if now[1] + 1 < len(grid_v2[0]) and (now[0], now[1] + 1) not in next and (now[0], now[1] + 1) not in visited and grid_v2[now[0]][now[1] + 1] == ".":
            next.append((now[0], now[1] + 1))

        visited.append(now)
        grid_v2[now[0]] = grid_v2[now[0]][0 : now[1]] + "X" + grid_v2[now[0]][now[1] + 1:]
        if len(next) > 0:
            now = next.pop(0)
        else:
            break

    for g in grid_v2:
        print(g)

    enclosed = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid_v2[i * 3 + 1][j * 3 + 1] == ".":
                # print(i, j)
                enclosed += 1
    print(enclosed)


def get_next_step(g, i, j, bi, bj):
    if g[i][j] == "|":
        return i - (bi - i), j

    if g[i][j] == "-":
        return i, j - (bj - j)

    if g[i][j] == "L":
        if i == bi:
            return i - 1, j
        return i, j + 1

    if g[i][j] == "J":
        if i == bi:
            return i - 1, j
        return i, j - 1

    if g[i][j] == "7":
        if i == bi:
            return i + 1, j
        return i, j - 1

    if g[i][j] == "F":
        if i == bi:
            return i + 1, j
        return i, j + 1

    if g[i][j] == ".":
        return None
