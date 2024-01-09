#Advent of Code 2023 Day 5
#Part 1:
#Part 2:

class cRange:
    def __init__(self, start, length) -> None:
        self.start = int(start)
        self.end = int(start) + int(length) - 1
        self.length = int(length)

    def compareRange(self, mapRange, source, destination):
        if self.start <= mapRange.sourceEnd and self.end >= mapRange.sourceStart:
            # if self.start == 53 and self.end == 56:
            #     pass

            matchingStart = max(self.start, mapRange.sourceStart)
            matchingEnd = min(self.end, mapRange.sourceEnd)
            matchingLength = matchingEnd - matchingStart + 1

            matchingStartPos = matchingStart - mapRange.sourceStart
            matchingDestStart = mapRange.destinationStart + matchingStartPos
            matchingDestLength = matchingLength

            dest = cRange(matchingDestStart, matchingDestLength)
            destination.append(dest)
            #sss += ' becomes '
            
            if matchingStart > self.start:
                s = cRange(self.start, matchingStart - self.start)
                source.append(s)

            if matchingEnd < self.end:
                s = cRange(matchingEnd + 1, self.end - matchingEnd)
                source.append(s)

            return 1
        return 0
    
    def __str__(self) -> str:
        return '[' + str(self.start) + '-' + str(self.end) + ']'


class cMap:
    def __init__(self, name, mapNumber) -> None:
        self.name = name
        self.mapNumber = mapNumber
        self.ranges = []

    def addRange(self, data):
        r = cMapRange(data)
        self.ranges.append(r)

class cMapRange:
    def __init__(self, data) -> None:
        data = data.split(' ')
        #destination, source, length
        self.sourceStart = int(data[1])
        self.sourceEnd = int(data[1]) + int(data[2]) - 1
        self.destinationStart = int(data[0])
        self.destinationEnd = int(data[0]) + int(data[2]) - 1
        self.length = int(data[2])

source = []
destination = []
maps = []
currentReadMap = -1

with open('2023/05/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line.find('seeds') != -1:
            line = line.replace('seeds: ', '')
            ss = line.split(' ')
            i = 0
            while i < len(ss) / 2:
                r = cRange(ss[2*i], ss[2*i + 1])
                source.append(r)
                i += 1
            
        ##
        
        elif line.find('map') != -1:
            line = line.replace(' map:', '')
            currentReadMap += 1
            mp = cMap(line, currentReadMap)
            maps.append(mp)

        ##
        
        elif len(line) > 1:
            maps[currentReadMap].addRange(line)

        else:
            pass

for map in maps:

    sss = ''
    for s in source:
        sss += str(s) + ', '
    print(sss)

    i = 0
    while i < len(source):
        s = source[i]
        rangeFound = 0

        for r in map.ranges:
            if s.compareRange(r, source, destination) == 1:
                rangeFound = 1
                break
            else:
                continue

        if rangeFound == 0:
            destination.append(s)

        i += 1

    source = destination
    destination = []



sss = ''
result = 0
for s in source:
    sss += str(s) + ', '
    if result == 0:
        result = s.start
    elif s.start < result:
        result = s.start
print(sss)
print('Part 2: ', result)
