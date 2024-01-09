#Advent of Code 2023 Day 5
#Part 1:
#Part 2:

class seed:
    def __init__(self, seedID) -> None:
        self.properties = []
        self.properties.append(int(seedID))

    def applyMap(self, currentMap):
        source = self.properties[currentMap.mapNumber]
        destination = currentMap.applyMap(source)
        self.properties.append(destination)

    def finalValue(self):
        return self.properties[len(self.properties) - 1]


class map:
    def __init__(self, name, mapNumber) -> None:
        self.name = name
        self.mapNumber = mapNumber
        self.ranges = []

    def addRange(self, data):
        r = range(data)
        self.ranges.append(r)

    def applyMap(self, source):
        for r in self.ranges:
            if r.inRange(source):
                pos = source - r.sourceStart
                return r.destinationStart + pos
            else:
                pass
        return source

class range:
    def __init__(self, data) -> None:
        data = data.split(' ')
        #destination, source, length
        self.sourceStart = int(data[1])
        self.sourceEnd = int(data[1]) + int(data[2]) - 1
        self.destinationStart = int(data[0])
        self.length = int(data[2])

    def inRange(self, source):
        if source >= self.sourceStart and source <= self.sourceEnd:
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
            for s in line.split(' '):
                sd = seed(s)
                seeds.append(sd)
            
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

for currentReadMap in maps:
    for s in seeds:
        s.applyMap(currentReadMap)

minLocation = 0

for s in seeds:
    if minLocation == 0:
        minLocation = s.finalValue()
    elif s.finalValue() < minLocation:
        minLocation = s.finalValue()
    else:
        pass

print('Part 1: Lowest location =', minLocation)
