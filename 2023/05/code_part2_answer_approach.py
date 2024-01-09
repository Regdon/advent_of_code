#Advent of Code 2023 Day 5
#Part 1:
#Part 2:

class seedRange:
    def __init__(self, seedStart, seedLength) -> None:
        self.seedStart = int(seedStart)
        self.seedEnd = int(seedStart) + int(seedLength) - 1
        self.seedLength = int(seedLength)

    def inRange(self, value):
        if value >= self.seedStart and value <= self.seedEnd:
            return 1
        else:
            return 0


class map:
    def __init__(self, name, mapNumber) -> None:
        self.name = name
        self.mapNumber = mapNumber
        self.ranges = []

    def addRange(self, data):
        r = range(data)
        self.ranges.append(r)

    def applyInvert(self, destination):
        for r in self.ranges:
            if r.inRangeInvert(destination):
                pos = destination - r.destinationStart
                return r.sourceStart + pos
            else:
                pass
        return destination


class range:
    def __init__(self, data) -> None:
        data = data.split(' ')
        #destination, source, length
        self.sourceStart = int(data[1])
        self.sourceEnd = int(data[1]) + int(data[2]) - 1
        self.destinationStart = int(data[0])
        self.destinationEnd = int(data[0]) + int(data[2]) - 1
        self.length = int(data[2])

    def inRange(self, source):
        if source >= self.sourceStart and source <= self.sourceEnd:
            return 1
        else:
            return 0
        
    def inRangeInvert(self, destination):
        if destination >= self.destinationStart and destination <= self.destinationEnd:
            return 1
        else:
            return 0
    

seeds = []
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
                sr = seedRange(ss[2*i], ss[2*i + 1])
                seeds.append(sr)
                i += 1
            
        ##
        
        elif line.find('map') != -1:
            line = line.replace(' map:', '')
            currentReadMap += 1
            mp = map(line, currentReadMap)
            maps.append(mp)

        ##
        
        elif len(line) > 1:
            maps[currentReadMap].addRange(line)

        else:
            pass

i = 1
valid = 0
c = 0
cc = 0

while valid == 0:
    m = len(maps) - 1
    dest = i



    while m >= 0:
        dest = maps[m].applyInvert(dest)
        m -= 1


    for sr in seeds:
        if sr.inRange(dest) == 1:
            valid = 1

    i += 1
    c += 1

    if c == 10000:
        c = 0
        cc += 1
        print(str(cc * 10000))

print("Lowest Location = ", i - 1, "from seed = ", dest)