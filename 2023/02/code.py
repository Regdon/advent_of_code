#Advent of Code 2023 Day 2
#Part 1: Which games are possible if there are 12 red, 13 green and 14 blue balls. Add up possible game ids.
#Park 2: What is the minimum red, green and blue to make each game possible? Multiple r, g and b for each row and add the results.


class game:
    def __init__(self, data):
        #Extract game id
        data = data.split(": ")
        self.gameID = int(data[0].replace("Game ", ""))
        self.tests = []

        #Extract test data
        data = data[1].split("; ")
        for t in data:
            self.tests.append(test(t))

    def isPossible(self, red, green, blue):
        for test in self.tests:
            if test.isPossible(red, green, blue) == 0:
                return 0
        return 1
    
    def power(self):
        #Max red, green and blue from all tests multiplied together
        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        for test in self.tests:
            if test.red > maxRed:
                maxRed = test.red
            if test.green > maxGreen:
                maxGreen = test.green
            if test.blue > maxBlue:
                maxBlue = test.blue

        return maxRed * maxGreen * maxBlue
    
    def __str__(self):
        result =  "Game: " + str(self.gameID)
        result = result + " Possible?: " + str(self.isPossible(12, 13, 14))
        result = result + " Data: "
        for test in self.tests:
            result = result + str(test)
        return result

class test:
    def __init__(self, data):
        self.green = 0
        self.blue = 0
        self.red = 0

        colours = data.split(", ")
        for colour in colours:
            pair = colour.split()
            if pair[1] == "green":
                self.green = int(pair[0])
            if pair[1] == "blue":
                self.blue = int(pair[0])
            if pair[1] == "red":
                self.red = int(pair[0])

    def isPossible(self, maxRed, maxGreen, maxBlue):
        if self.red <= maxRed and self.green <= maxGreen and self.blue <= maxBlue:
            return 1
        return 0     

    def __str__(self):
        return "[Red: " + str(self.red) + ", Green: " + str(self.green) + ", Blue: " + str(self.blue) + "]"  


games = []

with open('2023/02/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        games.append(game(line))

    possibleGameIDs = 0
    for game in games:
        if game.isPossible(12, 13, 14) == 1:
            possibleGameIDs += game.gameID

    print("Part1: Sum of possible game IDs:", possibleGameIDs)

    sumPower = 0
    for game in games:
        sumPower += game.power()

    print("Part2: Sum of all game power: ", sumPower)