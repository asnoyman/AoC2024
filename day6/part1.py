class cell:
    def __init__(self, v, e):
        self.visited = v
        self.empty = e

    def __repr__(self):
        return f"({self.visited}, {self.empty})"
    
    def setVisisted(self, v):
        self.visited = v
    
    def getVisited(self):
        return self.visited
    
def moveGuard(map, guardX, guardY, guardDir):
    newX = guardX + dirs[guardDir][0]
    newY = guardY + dirs[guardDir][1]
    if newX < 0 or newY < 0 or newX >= len(map[0]) or newY >= len(map):
        return True, guardX, guardY, guardDir
    
    if not map[newY][newX].empty:
        guardDir += 1
        guardDir %= 4
    else:
        guardX = newX
        guardY = newY
        map[guardY][guardX].visited = True
    return False, guardX, guardY, guardDir
    
    
# Read input into 2D list
map = []
dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
guardX = None
guardY = None
guardDir = 0
with open('input.txt') as f:
    for y, line in enumerate(f.readlines()):
        row = []
        for x, char in enumerate(line):
            # Each cell will be a class with a visited bool and an empty bool
            if char == '.':
                row.append(cell(False, True))
            elif char == '#':
                row.append(cell(False, False))
            # Create a guard positions, direction and set the starting position to visisted = True
            elif char == '^':
                row.append(cell(True, True))
                guardX = x
                guardY = y
        map.append(row)

# Simulate the guard movement until it would move off the map
while True:
    offGrid, guardX, guardY, guardDir = moveGuard(map, guardX, guardY, guardDir)
    if offGrid:
        break

# Count the number of visisted = True in the map
tally = 0
for row in map:
    for pos in row:
        if pos.visited:
            tally += 1

print(tally)