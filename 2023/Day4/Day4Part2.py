class Card():

    def __init__(self, id, cardLine) -> None:

        self.id = id
        parts = cardLine.split("|")
        
        self.winNums = parts[0].strip()
        self.winNums = self.winNums.split()
        self.winNums = list(map(int,self.winNums))

        self.cardNums = parts[1].strip()
        self.cardNums = self.cardNums.split()
        self.cardNums = list(map(int,self.cardNums))

    def calculateScore(self):
        runningMatches = 0
        for cardNum in self.cardNums:
            if cardNum in self.winNums:
                runningMatches += 1

        if runningMatches == 0: return 0
        return pow(2, runningMatches - 1)

    def cardWinCopies(self):
        runningMatches = 0
        for cardNum in self.cardNums:
            if cardNum in self.winNums:
                runningMatches += 1
        
        return [idx for idx in range(self.id + 1, self.id + runningMatches + 1)]

class CardInstanceCount():
    def __init__(self) -> None:
        self.cardCounts = {}
    
    def increment(self, i, k):
        if i not in self.cardCounts: self.cardCounts[i] = 0
        self.cardCounts[i]+=k
    
    def getCount(self, i):
        return self.cardCounts[i]


runningCount = 0
cardCounts = CardInstanceCount()
with open('Day4/Day4.txt', 'r') as file:
    for cardLine in file:
        
        cardLine = cardLine.split(":")
        cardId = int(cardLine[0].split()[1])
        cardValues = cardLine[1]

        card = Card(cardId, cardValues)
        cardCounts.increment(cardId, 1)

        mutiplyer = cardCounts.getCount(cardId)
        runningCount += mutiplyer

        for cardId2 in card.cardWinCopies():
            cardCounts.increment(cardId2, mutiplyer)
        




print(runningCount)
