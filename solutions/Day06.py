true = True
false = False


def solve_part_1(input_data: str):
    print("solve part 1")
    splits = input_data.split("\n")
    times = list()
    distances = list()
    for s in splits[0].split(" "):
        if s.isdigit():
            times.append(int(s))
    for s in splits[1].split(" "):
        if s.isdigit():
            distances.append(int(s))

    ways = 1
    for i, t in enumerate(times):
        tmp = 0
        for k in range(t + 1):
            if k * (t - k) > distances[i]:
                tmp += 1
        ways *= tmp

    print(ways)


def solve_part_2(input_data: str):
    print("solve part 2")
    splits = input_data.split("\n")
    times = list()
    distances = list()
    for s in splits[0].split(" "):
        if s.isdigit():
            times.append(s)
    for s in splits[1].split(" "):
        if s.isdigit():
            distances.append(s)

    tmp = "".join(times)
    times.clear()
    times.append(int(tmp))

    tmp = "".join(distances)
    distances.clear()
    distances.append(int(tmp))

    ways = 1
    for i, t in enumerate(times):
        tmp = 0
        for k in range(t + 1):
            if k * (t - k) > distances[i]:
                tmp += 1
        ways *= tmp

    print(ways)