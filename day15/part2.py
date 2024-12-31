def checkMove(grid, direction, robotRow, robotCol):
    if direction == '^':
        if grid[robotRow - 1][robotCol] == '#':
            return False
        elif grid[robotRow - 1][robotCol] == '.':
            return True
        elif grid[robotRow - 1][robotCol] == '[':
            return checkMove(grid, direction, robotRow - 1, robotCol) and checkMove(grid, direction, robotRow - 1, robotCol + 1)
        elif grid[robotRow - 1][robotCol] == ']':
            return checkMove(grid, direction, robotRow - 1, robotCol) and checkMove(grid, direction, robotRow - 1, robotCol - 1)
            
    if direction == 'v':
        if grid[robotRow + 1][robotCol] == '#':
            return False
        elif grid[robotRow + 1][robotCol] == '.':
            return True
        elif grid[robotRow + 1][robotCol] == '[':
            return checkMove(grid, direction, robotRow + 1, robotCol) and checkMove(grid, direction, robotRow + 1, robotCol + 1)
        elif grid[robotRow + 1][robotCol] == ']':
            return checkMove(grid, direction, robotRow + 1, robotCol) and checkMove(grid, direction, robotRow + 1, robotCol - 1)

def moveRobot(grid, direction, robotRow, robotCol):
    if direction == '^':
        if grid[robotRow - 1][robotCol] == '#':
            return (robotRow, robotCol)
        elif grid[robotRow - 1][robotCol] == '.':
            grid[robotRow - 1][robotCol], grid[robotRow][robotCol] = grid[robotRow][robotCol], grid[robotRow - 1][robotCol]
            return (robotRow - 1, robotCol)
        elif grid[robotRow - 1][robotCol] == '[':
            if not checkMove(grid, direction, robotRow, robotCol):
                return (robotRow, robotCol)
            else:
                moveRobot(grid, direction, robotRow - 1, robotCol)
                moveRobot(grid, direction, robotRow - 1, robotCol + 1)
                grid[robotRow - 1][robotCol] = grid[robotRow][robotCol]
                grid[robotRow][robotCol] = '.'
                return (robotRow - 1, robotCol)
        elif grid[robotRow - 1][robotCol] == ']':
            if not checkMove(grid, direction, robotRow, robotCol):
                return (robotRow, robotCol)
            else:
                moveRobot(grid, direction, robotRow - 1, robotCol)
                moveRobot(grid, direction, robotRow - 1, robotCol - 1)
                grid[robotRow - 1][robotCol] = grid[robotRow][robotCol]
                grid[robotRow][robotCol] = '.'
                return (robotRow - 1, robotCol)
            
    if direction == 'v':
        if grid[robotRow + 1][robotCol] == '#':
            return (robotRow, robotCol)
        elif grid[robotRow + 1][robotCol] == '.':
            grid[robotRow + 1][robotCol], grid[robotRow][robotCol] = grid[robotRow][robotCol], grid[robotRow + 1][robotCol]
            return (robotRow + 1, robotCol)
        elif grid[robotRow + 1][robotCol] == '[':
            if not checkMove(grid, direction, robotRow, robotCol):
                return (robotRow, robotCol)
            else:
                moveRobot(grid, direction, robotRow + 1, robotCol)
                moveRobot(grid, direction, robotRow + 1, robotCol + 1)
                grid[robotRow + 1][robotCol] = grid[robotRow][robotCol]
                grid[robotRow][robotCol] = '.'
                return (robotRow + 1, robotCol)
        elif grid[robotRow + 1][robotCol] == ']':
            if not checkMove(grid, direction, robotRow, robotCol):
                return (robotRow, robotCol)
            else:
                moveRobot(grid, direction, robotRow + 1, robotCol)
                moveRobot(grid, direction, robotRow + 1, robotCol - 1)
                grid[robotRow + 1][robotCol] = grid[robotRow][robotCol]
                grid[robotRow][robotCol] = '.'
                return (robotRow + 1, robotCol)
            
    if direction == '<':
        if grid[robotRow][robotCol - 1] == '#':
            return (robotRow, robotCol)
        elif grid[robotRow][robotCol - 1] == '.':
            grid[robotRow][robotCol - 1], grid[robotRow][robotCol] = grid[robotRow][robotCol], grid[robotRow][robotCol - 1]
            return (robotRow, robotCol - 1)
        elif grid[robotRow][robotCol - 1] == ']':
            if moveRobot(grid, direction, robotRow, robotCol - 2) == (robotRow, robotCol - 2):
                return (robotRow, robotCol)
            else:
                grid[robotRow][robotCol - 2], grid[robotRow][robotCol - 1], grid[robotRow][robotCol] = grid[robotRow][robotCol - 1], grid[robotRow][robotCol], grid[robotRow][robotCol - 2]
                return (robotRow, robotCol - 1)

    if direction == '>':
        if grid[robotRow][robotCol + 1] == '#':
            return (robotRow, robotCol)
        elif grid[robotRow][robotCol + 1] == '.':
            grid[robotRow][robotCol + 1], grid[robotRow][robotCol] = grid[robotRow][robotCol], grid[robotRow][robotCol + 1]
            return (robotRow, robotCol + 1)
        elif grid[robotRow][robotCol + 1] == '[':
            if moveRobot(grid, direction, robotRow, robotCol + 2) == (robotRow, robotCol + 2):
                return (robotRow, robotCol)
            else:
                grid[robotRow][robotCol + 2], grid[robotRow][robotCol + 1], grid[robotRow][robotCol] = grid[robotRow][robotCol + 1], grid[robotRow][robotCol], grid[robotRow][robotCol + 2]
                return (robotRow, robotCol + 1)


# Read the input into grid where each cell is either a wall, box, robot or empty
# Record the future moves of the robot
grid = []
moves = ''
robotRow, robotCol = (None, None)
with open('input.txt') as f:
    isGrid = True
    for i, row in enumerate(f.readlines()):
        if row == '\n':
            isGrid = False
            continue

        gridRow = []
        for j, col in enumerate(row.strip()):
            if isGrid:
                if col == '#':
                    gridRow += ['#', '#']
                elif col == '.':
                    gridRow += ['.', '.']
                elif col == 'O':
                    gridRow += ['[', ']']
                elif col == '@':
                    robotRow, robotCol = (i, 2 * j)
                    gridRow += ['@', '.']
            else:
                moves += col
        if isGrid:
            grid.append(gridRow)


# Simulate the robot's movements
for move in moves:
    robotRow, robotCol = moveRobot(grid, move, robotRow, robotCol)


# Find the GPS location of each box (100 * row + col)
gpsSum = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == '[':
            gpsSum += i * 100 + j


# Return the sum of the GPS locations
print(gpsSum)