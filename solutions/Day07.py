true = True
false = False

import re


def solve_part_1(input_data: str):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    cards.reverse()

    print("solve part 1")
    splits = input_data.split("\n")
    hands = list()
    for i, s in enumerate(splits):
        hands.append(s.split(" "))

    sorting(hands, cards)
    hands.reverse()

    summa = 0
    for i, h in enumerate(hands):
        summa += (i + 1) * int(h[1])

    print(summa)


def solve_part_2(input_data: str):
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    cards.reverse()

    print("solve part 2")
    splits = input_data.split("\n")
    hands = list()
    for i, s in enumerate(splits):
        hands.append(s.split(" "))

    sorting_v2(hands, cards)
    hands.reverse()

    summa = 0
    for i, h in enumerate(hands):
        # print(h)
        summa += (i + 1) * int(h[1])

    print(summa)


def sorting(h, cards):
    for i in range(len(h)):
        cs = list()
        for c in cards:
            cs.append(len(re.findall(c, h[i][0])))
        cs = list(filter(lambda x: x > 0, cs))
        cs.sort(reverse=true)
        h[i].append(cs)

    for i in range(len(h) - 1):
        max = i
        for j in range(i + 1, len(h)):
            if len(h[max][2]) > len(h[j][2]):
                max = j
            elif len(h[max][2]) == len(h[j][2]):
                if len(h[max][2]) == 1:
                    if cards.index(h[max][0][0]) < cards.index(h[j][0][0]):
                        max = j

                if len(h[max][2]) == 2:
                    if h[max][2][0] < h[j][2][0]:
                        max = j
                        continue

                    if h[max][2][0] == h[j][2][0]:
                        k = 0
                        while h[max][0][k] == h[j][0][k]:
                            k += 1
                        if cards.index(h[max][0][k]) < cards.index(h[j][0][k]):
                            max = j

                if len(h[max][2]) == 3:
                    if h[max][2][0] < h[j][2][0]:
                        max = j
                        continue

                    if h[max][2][0] == h[j][2][0]:
                        k = 0
                        while h[max][0][k] == h[j][0][k]:
                            k += 1
                        if cards.index(h[max][0][k]) < cards.index(h[j][0][k]):
                            max = j

                if len(h[max][2]) == 4:
                    k = 0
                    while h[max][0][k] == h[j][0][k]:
                        k += 1
                    if cards.index(h[max][0][k]) < cards.index(h[j][0][k]):
                        max = j

                if len(h[max][2]) == 5:
                    k = 0
                    while h[max][0][k] == h[j][0][k]:
                        k += 1
                    if cards.index(h[max][0][k]) < cards.index(h[j][0][k]):
                        max = j

        if i != max:
            tmp = h[i]
            h[i] = h[max]
            h[max] = tmp


def sorting_v2(h, cards):
    for i in range(len(h)):
        cs = list()
        d = {}
        for c in cards:
            count = len(re.findall(c, h[i][0]))
            if count > 0:
                cs.append(count)
                d[c] = count

        cs.sort(reverse=true)
        backup = None
        if "J" in d.keys():
            if d["J"] == 5:
                backup = h[i][0]
                h[i][0] = h[i][0].replace("J", "A")
            else:
                tmpmax = -1
                tmphigh = None
                for k in d.keys():
                    if k != "J":
                        if tmpmax < d[k]:
                            tmpmax = d[k]
                            tmphigh = k
                        elif tmpmax == d[k]:
                            if cards.index(tmphigh) < cards.index(k):
                                tmpmax = d[k]
                                tmphigh = k
                backup = h[i][0]
                h[i][0] = h[i][0].replace("J", tmphigh)
        else:
            backup = h[i][0]

        cs.clear()
        for c in cards:
            count = len(re.findall(c, h[i][0]))
            if count > 0:
                cs.append(count)
        cs.sort(reverse=true)
        h[i].append(cs)
        h[i].append(backup)

    for i in range(len(h) - 1):
        max = i
        for j in range(i + 1, len(h)):
            if len(h[max][2]) > len(h[j][2]):
                max = j
            elif len(h[max][2]) == len(h[j][2]):
                if len(h[max][2]) == 1:
                    k = 0
                    while h[max][3][k] == h[j][3][k]:
                        k += 1
                    if cards.index(h[max][3][k]) < cards.index(h[j][3][k]):
                        max = j

                if len(h[max][2]) == 2:
                    if h[max][2][0] < h[j][2][0]:
                        max = j
                        continue

                    if h[max][2][0] == h[j][2][0]:
                        k = 0
                        while h[max][3][k] == h[j][3][k]:
                            k += 1
                        if cards.index(h[max][3][k]) < cards.index(h[j][3][k]):
                            max = j

                if len(h[max][2]) == 3:
                    if h[max][2][0] < h[j][2][0]:
                        max = j
                        continue

                    if h[max][2][0] == h[j][2][0]:
                        k = 0
                        while h[max][3][k] == h[j][3][k]:
                            k += 1
                        if cards.index(h[max][3][k]) < cards.index(h[j][3][k]):
                            max = j

                if len(h[max][2]) == 4:
                    k = 0
                    while h[max][3][k] == h[j][3][k]:
                        k += 1
                    if cards.index(h[max][3][k]) < cards.index(h[j][3][k]):
                        max = j

                if len(h[max][2]) == 5:
                    k = 0
                    while h[max][3][k] == h[j][3][k]:
                        k += 1
                    if cards.index(h[max][3][k]) < cards.index(h[j][3][k]):
                        max = j

        if i != max:
            tmp = h[i]
            h[i] = h[max]
            h[max] = tmp