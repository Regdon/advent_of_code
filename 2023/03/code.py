#Advent of Code 2023 Day 3
#Part 1: Add up numbers which are next to a symbol (including diagonally). '.' doesn't count
#Part 2: When two numbers are next to a '*' symbol, multiple them together and add the results

symbols = '*#$+/%@=&-'
symbolsTwo = '*'

with open('2023/03/input.txt') as f:
    lines = f.readlines()

class starObj:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = 1
        self.count = 0

    def addNumber(self, val):
        self.value = self.value * val
        self.count = self.count + 1


def searchSymbolAround(lastX, lastY, length):
    startX = max(0, lastX - length - 1)
    endX = min(len(lines[0]), lastX + 1)
    startY = max(0, lastY - 1)
    endY = min(len(lines)-1, lastY + 1)

    currentY = startY
    while currentY < endY + 1:
        currentX = startX
        while currentX < endX + 1:
            if symbols.find(lines[currentY][currentX]) != -1:
                return [currentX, currentY]
            currentX += 1
        currentY += 1
    return 0

sequence = ''
total = 0
stars = []
starExists = 0
x = 0
y = 0
for line in lines:
    x = 0
    if y == 0:
        pass
    for char in line:
        if ord(char) >= 48 and ord(char) <= 57:
            sequence += char
        else:
            if sequence == '':
                x += 1
                continue

            # if sequence == '35':
            #     pass

            symbolLocation = searchSymbolAround(x-1, y, len(sequence) - 1)
            if symbolLocation != 0:
                total = total + int(sequence)
                if symbolsTwo.find(lines[symbolLocation[1]][symbolLocation[0]]) != -1:
                    for star in stars:
                        if star.x == symbolLocation[0] and star.y == symbolLocation[1]:
                            star.addNumber(int(sequence))
                            print('Star Object Updated at x=', star.x, 'y=',star.y,'value=',star.value)
                            starExists = 1
                    
                    if starExists == 0:
                        s = starObj(symbolLocation[0], symbolLocation[1])
                        s.addNumber(int(sequence))
                        stars.append(s)
                        print('Star Object Created at x=', s.x, 'y=',s.y,'value=',sequence)
                
                    starExists = 0
                print('Number:', sequence, 'Running Total:', total)
            else:
                print('Number:', sequence, 'Skipped', 'Running Total:', total)
            sequence = ''
        x += 1
    y += 1

starTotal = 0
for star in stars:
    if star.count == 2:
        starTotal += star.value

print('Star Total:', starTotal)
