red = 12
green = 13
blue = 14


def solve_part_1(input: str):
    print("solve part 1")
    sum = 0
    splits = input.split("\n")
    gameid = 0
    for s in splits:
        gameid = gameid + 1
        tmp = s.split(f"Game {gameid}: ")
        games = tmp[1].split(";")
        possible = True
        for g in games:
            colors = g.split(", ")
            for i, c in enumerate(colors):
                colors[i] = c.strip()

            for c in colors:
                tmp = c.split(" red")
                if len(tmp) == 2:
                    if int(tmp[0]) > red:
                        possible = False
                tmp = c.split(" blue")
                if len(tmp) == 2:
                    if int(tmp[0]) > blue:
                        possible = False
                tmp = c.split(" green")
                if len(tmp) == 2:
                    if int(tmp[0]) > green:
                        possible = False
        if possible:
            sum += gameid
    print(sum)


def solve_part_2(input: str):
    print("solve part 2")
    sum = 0
    splits = input.split("\n")
    gameid = 0
    for s in splits:
        gameid = gameid + 1
        tmp = s.split(f"Game {gameid}: ")
        games = tmp[1].split(";")
        maxred = -1
        maxblue = -1
        maxgreen = -1
        for g in games:
            colors = g.split(", ")
            for i, c in enumerate(colors):
                colors[i] = c.strip()

            for c in colors:
                tmp = c.split(" red")
                if len(tmp) == 2:
                    if int(tmp[0]) > maxred:
                        maxred = int(tmp[0])
                tmp = c.split(" blue")
                if len(tmp) == 2:
                    if int(tmp[0]) > maxblue:
                        maxblue = int(tmp[0])
                tmp = c.split(" green")
                if len(tmp) == 2:
                    if int(tmp[0]) > maxgreen:
                        maxgreen = int(tmp[0])
        sum += maxred * maxblue * maxgreen
    print(sum)