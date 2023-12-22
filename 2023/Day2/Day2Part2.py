class Cube():
    def __init__(self, color, count) -> None:
        self.color = color
        self.count = count


class CubeSet():
    def __init__(self, string) -> None:
        splitStr = string.split(',')
        splitStr = [x.strip() for x in splitStr]
        splitStr = [x.split(' ') for x in splitStr]
        self.cubes = [Cube(x[1], int(x[0])) for x in splitStr]

        missingColors = self.determineMissingColors()
        for color in missingColors:
            self.cubes.append(Cube(color, 0))

    def determineMissingColors(self):
        allColors = ["red", "blue", "green"]
        cubeColors = [cube.color for cube in self.cubes]
        return [color for color in allColors if color not in cubeColors]

    def isPlayableWith(self, cubeset):
        for cube in self.cubes:
            dualCube = [dcube for dcube in cubeset.cubes if dcube.color == cube.color][0]
            if (cube.count > dualCube.count): return False
        return True

    def power(self):
        val = 1
        for cube in self.cubes:
            val *= cube.count
        
        return val
            

class Game():
    def __init__(self, string) -> None:
        splitString  = string.split(':')

        self.id = int(splitString[0].split(' ')[1])

        self.cubeSets = []
        self.parseGameCubeSets(splitString[1])

    
    def parseGameCubeSets(self, string):
        cubeSetStrs = string.split(';')
        for cubeSetStr in cubeSetStrs:
            cubeSet = CubeSet(cubeSetStr)
            self.cubeSets.append(cubeSet)
    
    def isPossibeAccordingToCubeSet(self, dCubeSet):
        for cubeSet in self.cubeSets:
            if not cubeSet.isPlayableWith(dCubeSet): return False
    

    def minPossibleCubeSet(self):
        minCubeSet = CubeSet("0 red, 0 green, 0 blue")
        
        def updateMin(cubeset, minCubSet):
            for cube in minCubSet.cubes:
                dCube = [dCube for dCube in cubeset.cubes if cube.color == dCube.color][0]
                cube.count = max(cube.count, dCube.count)
            
        for cubeset in self.cubeSets:
            updateMin(cubeset, minCubeSet)


        return minCubeSet


runningCount = 0

with open('Day2/Day2.txt', 'r') as file:
    for gameLine in file:
        game = Game(gameLine)
        minPossibleCubeSet = game.minPossibleCubeSet()
        runningCount += minPossibleCubeSet.power()


print(runningCount)

    
