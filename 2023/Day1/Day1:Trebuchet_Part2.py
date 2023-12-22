def getStringDigit(str, i, map):
    for key in map:
        if i + len(key) > len(str): continue
        if str[i: i + len(key)] == key: return map[key]
    return -1


def getFirstDigit(string, digitsMap):
    for i,char in enumerate(string):
        if char.isdigit(): return char
        digit = getStringDigit(string, i, digitsMap)
        if digit != -1: return str(digit)
    

digitsMapStr = {
    "one": 1,
    "two": 2,
    "three" : 3,
    "four": 4,
    "five": 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

digitsReversedMapStr = {}
for key in digitsMapStr:
    digitsReversedMapStr[key[::-1]] = digitsMapStr[key]

class Calibrator():
    def __init__(self) -> None:
        self.runningCount = 0
    
    def processCalibrationLine(self, calibrationLine):
        firstDigit = getFirstDigit(calibrationLine, digitsMapStr)
        lastDigit = getFirstDigit(calibrationLine[::-1], digitsReversedMapStr)
        calibrationValueStr = firstDigit + lastDigit
        
        print(calibrationValueStr)
        self.runningCount += int(calibrationValueStr)
    
    def getFinalCalibrationValue(self):
        return self.runningCount
    

x = Calibrator()

with open('Day1/Day1.txt', 'r') as file:
    for calibrationLine in file:
        print(calibrationLine)
        x.processCalibrationLine(calibrationLine)

print(x.getFinalCalibrationValue())

