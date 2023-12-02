import re


def reforminputtostringarray(input: str):
    stringArr = input.split("\n")
    return stringArr


def getnumbers(string):
    print("String:", string)
    numberArr = re.finditer('(?=(\d|one|two|three|four|five|six|seven|eight|nine))', string)
    numberArr = [number.group(1) for number in numberArr]
    for i in range(0, len(numberArr)):
        numberArr[i] = convertletternumbers(numberArr[i])
    print(numberArr)
    finalNumber = 0
    if (numberArr):
        finalNumber = int(numberArr[0] + numberArr[len(numberArr) - 1])
    print(finalNumber)
    return finalNumber


def convertletternumbers(value):
    helplist = {'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9'}

    return helplist.get(value, value)


def solveday1(input):
    stringarr = reforminputtostringarray(input)
    numbers = []
    for item in stringarr:
        number = getnumbers(item)
        numbers.append(number)

    sum = 0
    for number in numbers:
        sum += number

    return sum


if __name__ == '__main__':
    data = open('../data/day1.txt', 'r').read()
    print("The solution to day 1 is:", solveday1(data))
