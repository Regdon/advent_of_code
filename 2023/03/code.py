symbols = '*#$+/%@=&-'

with open('2023/03/input.txt') as f:
    lines = f.readlines()

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
                return 1
            currentX += 1
        currentY += 1
    return 0

sequence = ''
total = 0
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

            if searchSymbolAround(x-1, y, len(sequence) - 1) == 1:
                total = total + int(sequence)
                print('Number:', sequence, 'Running Total:', total)
            else:
                print('Number:', sequence, 'Skipped', 'Running Total:', total)
            sequence = ''
        x += 1
    y += 1