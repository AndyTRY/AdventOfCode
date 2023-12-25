from enum import Enum

class TileTypes(Enum):
    DIGIT = "digit"
    PERIOD = "period"
    SYMBOL = "symbol"
    GEAR = "gear"

class Tile:
    def __init__(self, char) -> None:
        if char == '.': self.type = TileTypes.PERIOD
        elif char.isdigit(): self.type = TileTypes.DIGIT
        elif char == "*": self.type = TileTypes.GEAR
        else:               self.type = TileTypes.SYMBOL

        self.char = char
        self.neighNumbers = []

    @classmethod
    def convertStringToTiles(cls, string):
        return list(map(Tile, string))

class Number:
    def __init__(self, rowNum, start, end, value) -> None:
        self.rowNum = rowNum
        self.start = start
        self.end = end
        self.value = value
    
    def NeighboorTiles(self):

        def isInBounds(x, y):
            if x < 0 or x >= len(board): return False
            if y < 0 or y >= len(board[0]): return False
            return True

        startRow = self.rowNum - 1
        startCol = self.start - 1
        endRow = self.rowNum + 1
        endCol = self.end + 1

        neighTiles = []
        for i in range(startRow, endRow + 1):
            for j in range(startCol, endCol):
                if isInBounds(i,j): neighTiles.append(board[i][j])

        return neighTiles
    
    def contribution(self):
        neighTiles = self.NeighboorTiles()
        for tile in neighTiles:
            if tile.type == TileTypes.SYMBOL: return self.value
        
        return 0

    def markNeighboorGears(self):
        neighTiles = self.NeighboorTiles()
        for tile in neighTiles:
            if tile.type == TileTypes.GEAR: tile.neighNumbers.append(self)

board = []
with open('Day3/Day3.txt', 'r') as file:
    for line in file:
        line = line.strip()
        tiles = Tile.convertStringToTiles(line)
        board.append(tiles)


print(board)


def detectNumbers(tiles, rowNum):

    def extractNumber(start, tiles, rowNum):
        numStr = ""
        i = start
        while(i < len(tiles) and tiles[i].type == TileTypes.DIGIT ):
            numStr += tiles[i].char
            i+=1

        return Number(rowNum,start,i,int(numStr))
    
    def fastForwardI(i, tiles):
        while(i < len(tiles) and tiles[i].type == TileTypes.DIGIT): i+=1
        return i

    numbers = []
    i = 0
    while (i != len(tiles)):
        if (tiles[i].type == TileTypes.DIGIT):
            number = extractNumber(i, tiles, rowNum)
            i = fastForwardI(i, tiles)
            numbers.append(number)
        else:
            i+=1
    
    return numbers

runningCount = 0
for i,tiles in enumerate(board):
    numbers = detectNumbers(tiles, i)
    for number in numbers:
        number.markNeighboorGears()
    

for tiles in board:
    for tile in tiles:
        if tile.type == TileTypes.GEAR:
            if len(tile.neighNumbers) == 2:
                runningCount += tile.neighNumbers[0].value * tile.neighNumbers[1].value

print(runningCount)





