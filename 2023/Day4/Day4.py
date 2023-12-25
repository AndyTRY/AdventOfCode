class Card():

    def __init__(self, cardLine) -> None:
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
    
runningCount = 0
with open('Day4/Day4.txt', 'r') as file:
    for cardLine in file:
        cardLine = cardLine.split(":")[1]
        card = Card(cardLine)
        runningCount += card.calculateScore()

print(runningCount)
