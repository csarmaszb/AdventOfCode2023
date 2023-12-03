import re
import math

true = True
false = False


def solve_part_1(input_data: str):
    print("solve part 1")
    summa = 0
    splits = input_data.split("\n")
    for row, s in enumerate(splits):
        tmp = ""
        before_row = ""
        after_row = ""
        for i, char in enumerate(s):
            if char != "." and len(re.findall("[0-9]", char)) > 0:
                if i > 0 and tmp == "":
                    tmp = s[i - 1]
                    if row > 0:
                        before_row = before_row + splits[row - 1][i - 1]
                    if row < len(splits) - 1:
                        after_row = after_row + splits[row + 1][i - 1]
                tmp = tmp + char
                if row > 0:
                    before_row = before_row + splits[row - 1][i]
                if row < len(splits) - 1:
                    after_row = after_row + splits[row + 1][i]

                if i == len(s) - 1:
                    if tmp != "":
                        symbols = list(filter(lambda x: x != ".", re.findall("[^0-9]", before_row + after_row + tmp)))
                        if len(symbols) > 0:
                            if len(re.findall("[^0-9]", tmp)) > 0:
                                summa = summa + int(tmp[1:])
                                # print(tmp[1:])
                            else:
                                summa = summa + int(tmp)
                                # print(tmp)
                        tmp = ""
                        before_row = ""
                        after_row = ""
            else:
                if row > 0:
                    before_row = before_row + splits[row - 1][i]
                if row < len(splits) - 1:
                    after_row = after_row + splits[row + 1][i]
                if tmp != "":
                    if char != ".":
                        if len(re.findall("[^0-9]", tmp)) > 0:
                            summa = summa + int(tmp[1:])
                            # print(tmp[1:])
                        else:
                            summa = summa + int(tmp)
                            # print(tmp)
                    else:
                        symbols = list(filter(lambda x: x != ".", re.findall("[^0-9]", before_row + after_row + tmp)))
                        if len(symbols) > 0:
                            if len(re.findall("[^0-9]", tmp)) > 0:
                                summa = summa + int(tmp[1:])
                                # print(tmp[1:])
                            else:
                                summa = summa + int(tmp)
                                # print(tmp)
                tmp = ""
                before_row = ""
                after_row = ""
    print(summa)


def solve_part_2(input_data: str):
    print("solve part 2")
    summa = 0
    splits = input_data.split("\n")
    for row, s in enumerate(splits):
        if s.find("*") != -1:
            for i, char in enumerate(s):
                if char == "*":
                    n1 = math.inf
                    n2 = math.inf

                    if i > 0:
                        tmp = ""
                        k = 1
                        while k <= 3 and i - k >= 0 and s[i - k].isdigit():
                            tmp = tmp + s[i - k]
                            k += 1
                        tmp = tmp[::-1]
                        if tmp != "":
                            n1 = int(tmp)

                    if i < len(s):
                        tmp = ""
                        k = 1
                        while k <= 3 and i + k <= len(s) and s[i + k].isdigit():
                            tmp = tmp + s[i + k]
                            k += 1
                        if tmp != "":
                            if n1 == math.inf:
                                n1 = int(tmp)
                            else:
                                n2 = int(tmp)

                    if n1 != math.inf and n2 != math.inf:
                        summa = summa + n1 * n2
                        # print(n1, " - ", n2)
                        continue
                    else:
                        if row > 0:
                            if splits[row - 1][i].isdigit():
                                begin = i
                                end = i
                                if i > 0 and splits[row - 1][i - 1].isdigit():
                                    begin = i - 1
                                    if i > 1 and splits[row - 1][i - 2].isdigit():
                                        begin = i - 2
                                if i < len(s) and splits[row - 1][i + 1].isdigit():
                                    end = i + 1
                                    if i < len(s) - 1 and splits[row - 1][i + 2].isdigit():
                                        end = i + 2
                                if n1 == math.inf:
                                    n1 = int(splits[row - 1][begin: end + 1])
                                elif n2 == math.inf:
                                    n2 = int(splits[row - 1][begin: end + 1])
                            else:
                                if i > 0:
                                    if splits[row - 1][i - 1].isdigit():
                                        tmp = ""
                                        k = 1
                                        while k <= 3 and i - k >= 0 and splits[row - 1][i - k].isdigit():
                                            tmp = tmp + splits[row - 1][i - k]
                                            k += 1
                                        tmp = tmp[::-1]
                                        if tmp != "":
                                            if n1 == math.inf:
                                                n1 = int(tmp)
                                            elif n2 == math.inf:
                                                n2 = int(tmp)
                                if i < len(s):
                                    if splits[row - 1][i + 1].isdigit():
                                        tmp = ""
                                        k = 1
                                        while k <= 3 and i + k <= len(s) and splits[row - 1][i + k].isdigit():
                                            tmp = tmp + splits[row - 1][i + k]
                                            k += 1
                                        if tmp != "":
                                            if n1 == math.inf:
                                                n1 = int(tmp)
                                            elif n2 == math.inf:
                                                n2 = int(tmp)
                            if n1 != math.inf and n2 != math.inf:
                                summa = summa + n1 * n2
                                # print(n1, " - ", n2)
                                continue

                        if row < len(splits):
                            if splits[row + 1][i].isdigit():
                                begin = i
                                end = i
                                if i > 0 and splits[row + 1][i - 1].isdigit():
                                    begin = i - 1
                                    if i > 1 and splits[row + 1][i - 2].isdigit():
                                        begin = i - 2
                                if i < len(s) and splits[row + 1][i + 1].isdigit():
                                    end = i + 1
                                    if i < len(s) - 1 and splits[row + 1][i + 2].isdigit():
                                        end = i + 2
                                if n1 == math.inf:
                                    n1 = int(splits[row + 1][begin: end + 1])
                                elif n2 == math.inf:
                                    n2 = int(splits[row + 1][begin: end + 1])
                            else:
                                if i > 0:
                                    if splits[row + 1][i - 1].isdigit():
                                        tmp = ""
                                        k = 1
                                        while k <= 3 and i - k >= 0 and splits[row + 1][i - k].isdigit():
                                            tmp = tmp + splits[row + 1][i - k]
                                            k += 1
                                        tmp = tmp[::-1]
                                        if tmp != "":
                                            if n1 == math.inf:
                                                n1 = int(tmp)
                                            elif n2 == math.inf:
                                                n2 = int(tmp)
                                if i < len(s):
                                    if splits[row + 1][i + 1].isdigit():
                                        tmp = ""
                                        k = 1
                                        while k <= 3 and i + k <= len(s) and splits[row + 1][i + k].isdigit():
                                            tmp = tmp + splits[row + 1][i + k]
                                            k += 1
                                        if tmp != "":
                                            if n1 == math.inf:
                                                n1 = int(tmp)
                                            elif n2 == math.inf:
                                                n2 = int(tmp)
                            if n1 != math.inf and n2 != math.inf:
                                summa = summa + n1 * n2
                                # print(n1, " - ", n2)
    print(summa)
