import re

true = True
false = False


def solve_part_1(input_data: str):
    print("solve part 1")
    splits = input_data.split("\n")
    summa = 0
    for s in splits:
        numbers = list(map(lambda x: int(x), re.findall("-?\\d+", s)))
        sequences = list()
        sequences.append(get_sequence(numbers))
        while len(sequences[-1]) != len(list(filter(lambda x: x == 0, sequences[-1]))):
            sequences.append(get_sequence(sequences[-1]))
        tmp = 0
        for i in range(len(sequences) - 2, -1, -1):
            tmp = tmp + sequences[i][-1]
        summa += numbers[-1] + tmp
    print(summa)


def solve_part_2(input_data: str):
    print("solve part 2")
    splits = input_data.split("\n")
    summa = 0
    for s in splits:
        numbers = list(map(lambda x: int(x), re.findall("-?\\d+", s)))
        sequences = list()
        sequences.append(get_sequence(numbers))
        while len(sequences[-1]) != len(list(filter(lambda x: x == 0, sequences[-1]))):
            sequences.append(get_sequence(sequences[-1]))
        tmp = 0
        for i in range(len(sequences) - 2, -1, -1):
            tmp = sequences[i][0] - tmp
        summa += numbers[0] - tmp
    print(summa)


def get_sequence(numbers):
    tmp = list()
    for i in range(1, len(numbers)):
        tmp.append(numbers[i] - numbers[i - 1])
    return tmp
