true = True
false = False


def solve_part_1(input_data: str):
    print("solve part 1")
    splits = input_data.split("\n")
    summa = 0
    for s in splits:
        winning_numbers = list(filter(lambda x: x.isdigit(), s.split(": ")[1].split("|")[0].split(" ")))
        numbers = list(filter(lambda x: x.isdigit(), s.split(": ")[1].split("|")[1].split(" ")))
        points = 0
        for n in numbers:
            if n in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        summa += points
    print(summa)


def solve_part_2(input_data: str):
    print("solve part 2")
    splits = input_data.split("\n")
    mapping = {}
    for i in range(len(splits)):
        mapping[i + 1] = 1
    for i, s in enumerate(splits):
        winning_numbers = list(filter(lambda x: x.isdigit(), s.split(": ")[1].split("|")[0].split(" ")))
        numbers = list(filter(lambda x: x.isdigit(), s.split(": ")[1].split("|")[1].split(" ")))
        points = 0
        for n in numbers:
            if n in winning_numbers:
                points += 1
        for k in range(points):
            mapping[i + 1 + k + 1] = mapping[i + 1 + k + 1] + mapping[i + 1]
    print(sum(mapping.values()))