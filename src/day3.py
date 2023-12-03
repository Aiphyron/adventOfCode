import re

def solveday3_1(input):
    symbols = {'*',
               '$',
               '@',
               '/',
               '+',
               '&',
               '#',
               '=',
               '%',
               '-'}
    lines = input.split("\n")
    sum = 0

    for i in range(0, len(lines)):
        numbers = re.findall(r'\d+', lines[i])
        for number in numbers:
            isfirstline = False
            isleftcolumn = False
            isrightcolumn = False
            islastline = False

            if number == '2':
                print("idgaf")
            numberStart = lines[i].find(number)
            numberEnd = numberStart
            numbertemp = int(int(number) / 10)
            while numbertemp != 0:
                numberEnd += 1
                numbertemp = int(numbertemp / 10)


            if i == 0:
                isfirstline = True

            if i == len(lines)-1:
                islastline = True

            if numberStart == 0:
                isleftcolumn = True

            if numberEnd == len(lines[i])-1:
                isrightcolumn = True

            rowabove = ''
            if not isfirstline:
                if isleftcolumn:
                    rowabove = lines[i - 1][numberStart:numberEnd + 2]
                elif isrightcolumn:
                    rowabove = lines[i - 1][numberStart - 1:numberEnd+1]
                else:
                    rowabove = lines[i - 1][numberStart - 1:numberEnd + 2]

            leftslot = ''
            if not isleftcolumn:
                leftslot = lines[i][numberStart-1]

            rightslot = ''
            if not isrightcolumn:
                rightslot = lines[i][numberEnd+1]

            rowunder = ''
            if not islastline:
                if isleftcolumn:
                    rowunder = lines[i + 1][numberStart:numberEnd + 2]
                elif isrightcolumn:
                    rowunder = lines[i + 1][numberStart - 1:numberEnd+1]
                else:
                    rowunder = lines[i + 1][numberStart - 1:numberEnd + 2]

            print("Number:", number)
            if number == '2':
                print("wakawaka")
            print("NumberStart:", numberStart)
            print("NumberEnd:", numberEnd)
            for symbol in symbols:
                added = False
                if not added:
                    if symbol in rowabove or symbol in rowunder or symbol in leftslot or symbol in rightslot:
                        print("Number added")
                        print("Found Symbol:",symbol)
                        sum += int(number)
                        added = True

    return sum
def solveday3_2(input):
    a = 1


if __name__ == '__main__':
    data = open('../data/day3.txt', 'r').read()
    print("The solution to day 3 part 1 is:", solveday3_1(data))
    #print("The solution to day 3 part 2 is:", solveday2_2(data))