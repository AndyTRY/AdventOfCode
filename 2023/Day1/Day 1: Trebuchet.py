def getFirstDigit(str):
    for char in str:
        if char.isdigit():  return char

class Calibrator():
    def __init__(self) -> None:
        self.runningCount = 0
    
    def processCalibrationLine(self, calibrationLine):
        firstDigit = getFirstDigit(calibrationLine)
        lastDigit = getFirstDigit(calibrationLine[::-1])
        calibrationValueStr = firstDigit + lastDigit
        
        self.runningCount += int(calibrationValueStr)
    
    def getFinalCalibrationValue(self):
        return self.runningCount
    

x = Calibrator()

with open('Day1.txt', 'r') as file:
    for calibrationLine in file:
        x.processCalibrationLine(calibrationLine)

print(x.getFinalCalibrationValue())

