#Advent of Code 2023 Day 4
#Part 1: For each card how many numbers are on the left and right hand side. Calculate 2^n-1 for each card. Add up result.
#Part 2:

class card:
    def __init__(self, data):
        self.cardNumber = 0
        self.winningNumbers = set()
        self.ourNumbers = set()

        data = data.split(':')
        self.cardNumber = int(data[0].replace('Card', ''))

        data = data[1].split('|')

        #Winning Numbers
        winning = data[0].split(' ')
        for win in winning:
            if win != '':
                self.winningNumbers.add(int(win))

        #Our Numbers
        our = data[1].split(' ')
        for o in our:
            if o != '':
                self.ourNumbers.add(int(o))

    def points(self):
        wins = self.winningNumbers.intersection(self.ourNumbers)
        if len(wins) == 0:
            return 0
        else:
            return pow(2, len(wins) - 1)


cards = []
totalPoints = 0

with open('2023/04/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        currentCard = card(line)
        cards.append(currentCard)
        totalPoints += currentCard.points()

    print('Part 1: Toatal Points =', totalPoints)