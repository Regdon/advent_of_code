#Advent of Code 2023 Day 7
#Part 1:
#Part 2:

cardValues = '23456789TJQKA'

class hand:
    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = bid
        self.strength = 0
        self.rank = 0

        self.calcCardCounts()
        self.calcStrenght()

    def calcCardCounts(self):
        self.cardCounts = [0,0,0,0,0,0,0,0,0,0,0,0,0]

        for card in self.cards:
            value = cardValues.find(card)
            self.cardCounts[value] += 1

    def calcStrenght(self):
        strength = 0

        #Five of a kind --- 96
        for cc in self.cardCounts:
            if cc == 5:
                strength = int('600000', 16)
                break

        #Four of a kind --- 80
        if strength == 0:
            for cc in self.cardCounts:
                if cc == 4:
                    strength = int('500000', 16)
                    break


        #Full house --- 64
        if strength == 0:
            matchThree = 0
            matchTwo = 0
            for cc in self.cardCounts:
                if cc == 3:
                    matchThree = 1
                elif cc == 2:
                    matchTwo = 1
            if matchThree == 1 and matchTwo == 1:
                strength = int('400000', 16)

        
        #Three of a kind --- 48
        if strength == 0:
            for cc in self.cardCounts:
                if cc == 3:
                    strength = int('300000', 16)
                    break

        #Two pair --- 32 or One pair --- 16
        if strength == 0:
            matchTwo = 0
            for cc in self.cardCounts:
                if cc == 2:
                    matchTwo += 1
            if matchTwo == 2:
                strength = int('200000', 16)
            elif matchTwo == 1:
                strength = int('100000', 16)

        #High card --- 0
        i = 0
        while i < 5:
            ##print(hex(strength))
            card = self.cards[i]
            val = cardValues.find(card)
            a = val << 4 * (4 - i)
            strength += a
            i += 1

        self.strength = strength
        ##print(hex(self.strength))

    def applyRank(self, rank):
        self.rank = rank
        self.winnings = rank * int(self.bid)

    def __str__(self) -> str:
        return self.cards + ' ' + hex(self.strength)


#-------------------------------------
hands = []

with open('2023/07/input.txt') as f:
    lines = f.read().splitlines()

    for line in lines:
        line = line.split(' ')
        cards = line[0]
        bid = line[1]
        h = hand(cards, bid)
        hands.append(h)

    hands = sorted(hands, key = lambda hand: hand.strength, reverse=False)

    i = 0
    totalWinnings = 0
    while i < len(hands):
        print (hands[i])
        hands[i].applyRank(i + 1)
        totalWinnings += hands[i].winnings
        i += 1

    print('Part1: Total Winnings = ', totalWinnings)

    