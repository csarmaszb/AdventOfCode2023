import math

true = True
false = False


def solve_part_1(input_data: str):
    print("solve part 1")
    splits = input_data.split("\n\n")
    seeds = splits[0].split("seeds: ")[1].split(" ")
    maps = {
        'seed-to-soil map:': 1,
        'soil-to-fertilizer map:': 2,
        'fertilizer-to-water map:': 3,
        'water-to-light map:': 4,
        'light-to-temperature map:': 5,
        'temperature-to-humidity map:': 6,
        'humidity-to-location map:': 7
    }

    seed_map = {}

    tmp = splits[1:]
    splits.clear()
    for s in tmp:
        for t in s.split("\n"):
            splits.append(t)

    seed_to_soil = list()
    soil_to_fertilizer = list()
    fertilizer_to_water = list()
    water_to_light = list()
    light_to_temperature = list()
    temperature_to_humidity = list()
    humidity_to_location = list()

    next = 0
    for i in range(len(splits)):
        if splits[i] in maps.keys():
            next = maps[splits[i]]

        if next == 1 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            seed_to_soil.append(tmp)

        if next == 2 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            soil_to_fertilizer.append(tmp)

        if next == 3 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            fertilizer_to_water.append(tmp)

        if next == 4 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            water_to_light.append(tmp)

        if next == 5 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            light_to_temperature.append(tmp)

        if next == 6 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            temperature_to_humidity.append(tmp)

        if next == 7 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            humidity_to_location.append(tmp)

    for k in range(7):
        for s in seeds:
            if k == 0:
                seed_map[int(s)] = list()
                found = false
                for n in range(len(seed_to_soil)):
                    if int(s) in range(seed_to_soil[n][1], seed_to_soil[n][1] + seed_to_soil[n][2]) and not found:
                        seed_map[int(s)].append(int(s) - seed_to_soil[n][1] + seed_to_soil[n][0])
                        found = true
                if not found:
                    seed_map[int(s)].append(int(s))

            if k == 1:
                found = false
                for n in range(len(soil_to_fertilizer)):
                    if seed_map[int(s)][-1] in range(soil_to_fertilizer[n][1], soil_to_fertilizer[n][1] + soil_to_fertilizer[n][2]) and not found:
                        seed_map[int(s)].append(seed_map[int(s)][-1] - soil_to_fertilizer[n][1] + soil_to_fertilizer[n][0])
                        found = true
                if not found:
                    seed_map[int(s)].append(seed_map[int(s)][-1])

            if k == 2:
                found = false
                for n in range(len(fertilizer_to_water)):
                    if seed_map[int(s)][-1] in range(fertilizer_to_water[n][1], fertilizer_to_water[n][1] + fertilizer_to_water[n][2]) and not found:
                        seed_map[int(s)].append(seed_map[int(s)][-1] - fertilizer_to_water[n][1] + fertilizer_to_water[n][0])
                        found = true
                if not found:
                    seed_map[int(s)].append(seed_map[int(s)][-1])

            if k == 3:
                found = false
                for n in range(len(water_to_light)):
                    if seed_map[int(s)][-1] in range(water_to_light[n][1], water_to_light[n][1] + water_to_light[n][2]) and not found:
                        seed_map[int(s)].append(seed_map[int(s)][-1] - water_to_light[n][1] + water_to_light[n][0])
                        found = true
                if not found:
                    seed_map[int(s)].append(seed_map[int(s)][-1])

            if k == 4:
                found = false
                for n in range(len(light_to_temperature)):
                    if seed_map[int(s)][-1] in range(light_to_temperature[n][1], light_to_temperature[n][1] + light_to_temperature[n][2]) and not found:
                        seed_map[int(s)].append(seed_map[int(s)][-1] - light_to_temperature[n][1] + light_to_temperature[n][0])
                        found = true
                if not found:
                    seed_map[int(s)].append(seed_map[int(s)][-1])

            if k == 5:
                found = false
                for n in range(len(temperature_to_humidity)):
                    if seed_map[int(s)][-1] in range(temperature_to_humidity[n][1], temperature_to_humidity[n][1] + temperature_to_humidity[n][2]) and not found:
                        seed_map[int(s)].append(seed_map[int(s)][-1] - temperature_to_humidity[n][1] + temperature_to_humidity[n][0])
                        found = true
                if not found:
                    seed_map[int(s)].append(seed_map[int(s)][-1])

            if k == 6:
                found = false
                for n in range(len(humidity_to_location)):
                    if seed_map[int(s)][-1] in range(humidity_to_location[n][1], humidity_to_location[n][1] + humidity_to_location[n][2]) and not found:
                        seed_map[int(s)].append(seed_map[int(s)][-1] - humidity_to_location[n][1] + humidity_to_location[n][0])
                        found = true
                if not found:
                    seed_map[int(s)].append(seed_map[int(s)][-1])

    min = math.inf
    for k in seed_map.keys():
        if seed_map[k][-1] < min:
            min = seed_map[k][-1]
    print(min)


def solve_part_2(input_data: str):
    print("solve part 2")
    splits = input_data.split("\n\n")

    seeds = splits[0].split("seeds: ")[1].split(" ")
    for i, s in enumerate(seeds):
        if i % 2 == 1:
            seeds[i] = str(int(seeds[i - 1]) + int(seeds[i]) - 1)

    maps = {
        'seed-to-soil map:': 1,
        'soil-to-fertilizer map:': 2,
        'fertilizer-to-water map:': 3,
        'water-to-light map:': 4,
        'light-to-temperature map:': 5,
        'temperature-to-humidity map:': 6,
        'humidity-to-location map:': 7
    }

    tmp = splits[1:]
    splits.clear()
    for s in tmp:
        for t in s.split("\n"):
            splits.append(t)

    seed_to_soil = list()
    soil_to_fertilizer = list()
    fertilizer_to_water = list()
    water_to_light = list()
    light_to_temperature = list()
    temperature_to_humidity = list()
    humidity_to_location = list()

    next = 0
    for i in range(len(splits)):
        if splits[i] in maps.keys():
            next = maps[splits[i]]

        if next == 1 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            seed_to_soil.append(tmp)

        if next == 2 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            soil_to_fertilizer.append(tmp)

        if next == 3 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            fertilizer_to_water.append(tmp)

        if next == 4 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            water_to_light.append(tmp)

        if next == 5 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            light_to_temperature.append(tmp)

        if next == 6 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            temperature_to_humidity.append(tmp)

        if next == 7 and splits[i] not in maps.keys():
            tmp = list()
            tmp.append(int(splits[i].split(" ")[0]))
            tmp.append(int(splits[i].split(" ")[1]))
            tmp.append(int(splits[i].split(" ")[2]))
            humidity_to_location.append(tmp)

    iteration = 0
    minimum = math.inf
    for i in range(0, len(seeds), 2):
        print("Range: ", int(seeds[i]), " ", int(seeds[i + 1]), " ", iteration)

        for k in range(int(seeds[i]), int(seeds[i + 1])):
            iteration += 1

            if k % 1000000 == 0:
                print(k)

            tmp = k
            for n in range(len(seed_to_soil)):
                if tmp in range(seed_to_soil[n][1], seed_to_soil[n][1] + seed_to_soil[n][2]):
                    tmp = tmp - seed_to_soil[n][1] + seed_to_soil[n][0]
                    break

            for n in range(len(soil_to_fertilizer)):
                if tmp in range(soil_to_fertilizer[n][1], soil_to_fertilizer[n][1] + soil_to_fertilizer[n][2]):
                    tmp = tmp - soil_to_fertilizer[n][1] + soil_to_fertilizer[n][0]
                    break

            for n in range(len(fertilizer_to_water)):
                if tmp in range(fertilizer_to_water[n][1], fertilizer_to_water[n][1] + fertilizer_to_water[n][2]):
                    tmp = tmp - fertilizer_to_water[n][1] + fertilizer_to_water[n][0]
                    break

            for n in range(len(water_to_light)):
                if tmp in range(water_to_light[n][1], water_to_light[n][1] + water_to_light[n][2]):
                    tmp = tmp - water_to_light[n][1] + water_to_light[n][0]
                    break

            for n in range(len(light_to_temperature)):
                if tmp in range(light_to_temperature[n][1], light_to_temperature[n][1] + light_to_temperature[n][2]):
                    tmp = tmp - light_to_temperature[n][1] + light_to_temperature[n][0]
                    break

            for n in range(len(temperature_to_humidity)):
                if tmp in range(temperature_to_humidity[n][1], temperature_to_humidity[n][1] + temperature_to_humidity[n][2]):
                    tmp = tmp - temperature_to_humidity[n][1] + temperature_to_humidity[n][0]
                    break

            for n in range(len(humidity_to_location)):
                if tmp in range(humidity_to_location[n][1], humidity_to_location[n][1] + humidity_to_location[n][2]):
                    tmp = tmp - humidity_to_location[n][1] + humidity_to_location[n][0]
                    break

            if minimum > tmp:
                minimum = tmp

    print(minimum)