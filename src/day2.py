import re


def solveday2_1(input,green_lim, blue_lim, red_lim):
    gameArr = input.split("\n")
    sum = 0
    for game in gameArr:
        setArr = game.split(";")
        possible = True

        for set in setArr:
            green = re.finditer('\d+(?=( green))', set)
            green = [matcher.group(0) for matcher in green]
            blue = re.finditer('(\d+(?=( blue)))', set)
            blue = [matcher.group(0) for matcher in blue]
            red = re.finditer('(\d+(?=( red)))', set)
            red = [matcher.group(0) for matcher in red]

            if len(green) == 0:
                green.append(0)

            if len(blue) == 0:
                blue.append(0)

            if len(red) == 0:
                red.append(0)

            if int(green[0]) > green_lim or int(blue[0]) > blue_lim or int(red[0]) > red_lim:
                possible = False

        if possible:
            id = re.finditer(r'(?<=(Game ))\d+', game)
            id = [matcher.group(0) for matcher in id]
            sum += int(id[0])
    return sum


def solveday2_2(input):
    gameArr = input.split("\n")
    sum = 0
    for game in gameArr:
        setArr = game.split(";")
        red_min = 0
        blue_min = 0
        green_min = 0

        for set in setArr:
            green = re.finditer('\d+(?=( green))', set)
            green = [matcher.group(0) for matcher in green]
            blue = re.finditer('(\d+(?=( blue)))', set)
            blue = [matcher.group(0) for matcher in blue]
            red = re.finditer('(\d+(?=( red)))', set)
            red = [matcher.group(0) for matcher in red]

            if len(green) == 0:
                green.append(0)

            if len(blue) == 0:
                blue.append(0)

            if len(red) == 0:
                red.append(0)

            if green_min < int(green[0]):
                green_min = int(green[0])

            if blue_min < int(blue[0]):
                blue_min = int(blue[0])

            if red_min < int(red[0]):
                red_min = int(red[0])

        sum += green_min * blue_min * red_min

    return sum


if __name__ == '__main__':
    red = 12
    green = 13
    blue = 14

    data = open('../data/day2.txt', 'r').read()
    print("The solution to day 2 part 1 is:", solveday2_1(data, green, blue, red))
    print("The solution to day 2 part 2 is:", solveday2_2(data))

