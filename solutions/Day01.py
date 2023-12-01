import re
import math

strDigits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def solvePart1(input: str):
    print("solve part 1")
    splits = input.split("\n")
    numbers = list()
    for s in splits:
        n = re.findall("\d", s)
        if len(n) == 1:
            numbers.append(int(n[0] + n[0]))
        else:
            numbers.append(int(n[0] + n[-1]))
    print(sum(numbers))


def solvePart2(input: str):
    print("solve part 2")
    splits = input.split("\n")
    numbers = list()
    for s in splits:
        min, smin, max, smax = minMaxSearch(s)
        if max == min + len(smin) - 1 and len(re.findall("\d", s[:max])) > 0:
            if smax != "":
                s = s[:max] + mapping[smax] + s[max + len(smax):]
            min, smin, max, smax = minMaxSearch(s)
            if smin != "":
                s = s.replace(smin, mapping[smin], 1)
        else:
            if smin != "":
                s = s.replace(smin, mapping[smin], 1)
            min, smin, max, smax = minMaxSearch(s)
            if smax != "":
                s = s[:max] + mapping[smax] + s[max + len(smax):]

        n = re.findall("\d", s)
        # print(n)
        if len(n) == 1:
            numbers.append(int(n[0] + n[0]))
        else:
            numbers.append(int(n[0] + n[-1]))
    print(sum(numbers))


def minMaxSearch(s: str) -> [int, str, int, str]:
    min = math.inf
    smin = ""
    for d in strDigits:
        if s.find(d) < min and s.find(d) != -1:
            min = s.find(d)
            smin = d

    max = -1
    smax = ""
    for d in strDigits:
        if s.rfind(d) > max and s.rfind(d) != -1:
            max = s.rfind(d)
            smax = d
    return [min, smin, max, smax]
