class cell:
    def __init__(self, e, d):
        self.empty = e
        self.directions = d

    def __repr__(self):
        return f"({self.empty}, {self.directions})"
    
def moveGuard(map, guardX, guardY, guardDir):
    newX = guardX + dirs[guardDir][0]
    newY = guardY + dirs[guardDir][1]

    # Iff guard moves off grid
    if newX < 0 or newY < 0 or newX >= len(map[0]) or newY >= len(map):
        return True, False, guardX, guardY, guardDir
    
    # If guard hits obstacle
    if not map[newY][newX].empty:
        guardDir += 1
        guardDir %= 4
    # If guard moves
    else:
        guardX = newX
        guardY = newY

    # If guard is in the same position and direction as before, it is in a loop
    if guardDir in map[guardY][guardX].directions:
        return False, True, guardX, guardY, guardDir
    map[guardY][guardX].directions.add(guardDir)
    return False, False, guardX, guardY, guardDir
    
def testForLoop(map, guardX, guardY, guardDir):
    # Simulate the guard movement until it would move off the map
    while True:
        offGrid, inLoop, guardX, guardY, guardDir = moveGuard(map, guardX, guardY, guardDir)
        if inLoop:
            return True
        if offGrid:
            return False

# Read input into 2D list
map = []
dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
guardXStart = None
guardYStart = None
guardDirStart = 0
emptyCells = []
with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        row = []
        for x, char in enumerate(line):
            # Each cell will be a class with a visited bool and an empty bool
            if char == '.':
                row.append(cell(True, set()))
                emptyCells.append((y, x))
            elif char == '#':
                row.append(cell(False, set()))
            # Create a guard positions, direction and set the starting position to visisted = True
            elif char == '^':
                row.append(cell(True, set([0])))
                guardXStart = x
                guardYStart = y
        map.append(row)

# For each version of the map with an extra obstacle, test if there is a loop
# A loop occurs if a guard ever is in a position + direction that they have been in before
tally = 0
for n, pos in enumerate(emptyCells):
    # Reset map to original state
    if n != 0:
        for y, row in enumerate(map):
            for x, c in enumerate(row):
                if y == guardYStart and x == guardXStart:
                    c.directions = set([0])
                else:
                    c.directions = set()
        map[emptyCells[n-1][0]][emptyCells[n-1][1]].empty = True

    # Add temp obstacle
    map[emptyCells[n][0]][emptyCells[n][1]].empty = False
    if testForLoop(map, guardXStart, guardYStart, guardDirStart):
        tally += 1

    if n % 100 == 0:
        print(n, tally)

print(tally)