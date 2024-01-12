#Advent of Codr 2023 Day 6
#Part 1:
#Part 2:

import math

times = []
distances = []
totalWays = []

with open('2023/06/input.txt') as f:
    lines = f.read().splitlines()

    #First line, read the times in
    tt = lines[0].split(" ")
    for t in tt:
        if t.isdigit():
            times.append(int(t))

    #Second line, read the distances in
    dd = lines[1].split(" ")
    for d in dd:
        if d.isdigit():
            distances.append(int(d))

#Find possible victories
n = len(times)
i = 0
while i < n:
    time = times[i]
    target = distances[i]
    buttonTime = 1
    ways = 0

    while buttonTime < time:
        result = buttonTime * (time - buttonTime)
        if result > target:
            ways += 1
        buttonTime += 1

    totalWays.append(ways)
    print('iteration:', i, 'time:', time, 'Target Distance:', target, 'Possible Ways:', ways)
    i += 1

answer = 1
for x in totalWays:
    answer = answer * x
print('Part 1 Answer:', answer)

#Part 2. Big numbers!
s = ''
for time in times:
    s += str(time)
raceTime = int(s)
s = ''
for distance in distances:
    s += str(distance)
targetDistance = int(s)

#quadratic
a = -1
b = raceTime
c = 0-targetDistance

root1 = (-b + math.sqrt(b*b - 4*a*c)) / (2 * a)
root2 = (-b - math.sqrt(b*b - 4*a*c)) / (2 * a)

root1 = math.ceil(root1)
root2 = math.floor(root2)

poss = root2 - root1 + 1
print('Part 2 Answer:', poss)
