import re
import math

true = True
false = False


def solve_part_1(input_data: str):
    print("solve part 1")
    splits = input_data.split("\n")
    indeces = []
    for i, s in enumerate(splits):
        if s.find("#") == -1:
            indeces.append(i)
    for i in range(len(indeces)):
        splits.insert(indeces[i] + i, "".join(["."] * len(splits[0])))

    indeces = []
    for j in range(len(splits[0])):
        tmpc = ""
        for i in range(len(splits)):
            tmpc += splits[i][j]
        if tmpc.find("#") == -1:
            indeces.append(j)
    for j in range(len(indeces)):
        for i in range(len(splits)):
            splits[i] = splits[i][0 : indeces[j] + j] + "." + splits[i][indeces[j] + j:]

    galaxies = []
    for i, s in enumerate(splits):
        for j in range(len(s)):
            if splits[i][j] == "#":
                galaxies.append((i, j))

    distances = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            distances += (abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]))

    print(distances)


def solve_part_2(input_data: str):
    print("solve part 2")
    grow = 999999
    splits = input_data.split("\n")
    rows = []
    for i, s in enumerate(splits):
        if s.find("#") == -1:
            rows.append(i)

    columns = []
    for j in range(len(splits[0])):
        tmpc = ""
        for i in range(len(splits)):
            tmpc += splits[i][j]
        if tmpc.find("#") == -1:
            columns.append(j)

    galaxies = []
    for i, s in enumerate(splits):
        for j in range(len(s)):
            if splits[i][j] == "#":
                galaxies.append((i, j))

    distances = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            empty_rows_between = list(filter(lambda x: galaxies[j][0] > x > galaxies[i][0], rows))
            if galaxies[i][1] > galaxies[j][1]:
                empty_columns_between = list(filter(lambda x: galaxies[j][1] < x < galaxies[i][1], columns))
            else:
                empty_columns_between = list(filter(lambda x: galaxies[j][1] > x > galaxies[i][1], columns))
            distances += (abs(galaxies[i][0] - galaxies[j][0]) + grow * len(empty_rows_between) + abs(galaxies[i][1] - galaxies[j][1]) + grow * len(empty_columns_between))

    print(distances)