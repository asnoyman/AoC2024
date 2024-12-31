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
                gridRow.append(col)
                if col == '@':
                    robotRow, robotCol = (i, j)
            else:
                moves += col
        if isGrid:
            grid.append(gridRow)
            

# Simulate the robot's movements
for move in moves:
    if move == '^':
        if grid[robotRow - 1][robotCol] == '#':
            continue
        elif grid[robotRow - 1][robotCol] == '.':
            grid[robotRow - 1][robotCol], grid[robotRow][robotCol] = grid[robotRow][robotCol], grid[robotRow - 1][robotCol]
            robotRow -= 1
        elif grid[robotRow - 1][robotCol] == 'O':
            for row in range(robotRow-2, -1, -1):
                if grid[row][robotCol] == '#':
                    break
                if grid[row][robotCol] == '.':
                    grid[robotRow][robotCol], grid[robotRow - 1][robotCol], grid[row][robotCol] = grid[row][robotCol], grid[robotRow][robotCol], grid[robotRow - 1][robotCol]
                    robotRow -= 1
                    break
    if move == 'v':
        if grid[robotRow + 1][robotCol] == '#':
            continue
        elif grid[robotRow + 1][robotCol] == '.':
            grid[robotRow + 1][robotCol], grid[robotRow][robotCol] = grid[robotRow][robotCol], grid[robotRow + 1][robotCol]
            robotRow += 1
        elif grid[robotRow + 1][robotCol] == 'O':
            for row in range(robotRow+2, len(grid)):
                if grid[row][robotCol] == '#':
                    break
                if grid[row][robotCol] == '.':
                    grid[robotRow][robotCol], grid[robotRow + 1][robotCol], grid[row][robotCol] = grid[row][robotCol], grid[robotRow][robotCol], grid[robotRow + 1][robotCol]
                    robotRow += 1
                    break
    if move == '<':
        if grid[robotRow][robotCol - 1] == '#':
            continue
        elif grid[robotRow][robotCol - 1] == '.':
            grid[robotRow][robotCol - 1], grid[robotRow][robotCol] = grid[robotRow][robotCol], grid[robotRow][robotCol - 1]
            robotCol -= 1
        elif grid[robotRow][robotCol - 1] == 'O':
            for col in range(robotCol-2, -1, -1):
                if grid[robotRow][col] == '#':
                    break
                if grid[robotRow][col] == '.':
                    grid[robotRow][robotCol], grid[robotRow][robotCol - 1], grid[robotRow][col] = grid[robotRow][col], grid[robotRow][robotCol], grid[robotRow][robotCol - 1]
                    robotCol -= 1
                    break
    if move == '>':
        if grid[robotRow][robotCol + 1] == '#':
            continue
        elif grid[robotRow][robotCol + 1] == '.':
            grid[robotRow][robotCol + 1], grid[robotRow][robotCol] = grid[robotRow][robotCol], grid[robotRow][robotCol + 1]
            robotCol += 1
        elif grid[robotRow][robotCol + 1] == 'O':
            for col in range(robotCol+2, len(grid[0])):
                if grid[robotRow][col] == '#':
                    break
                if grid[robotRow][col] == '.':
                    grid[robotRow][robotCol], grid[robotRow][robotCol + 1], grid[robotRow][col] = grid[robotRow][col], grid[robotRow][robotCol], grid[robotRow][robotCol + 1]
                    robotCol += 1
                    break


# Find the GPS location of each box (100 * row + col)
gpsSum = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == 'O':
            gpsSum += i * 100 + j


# Return the sum of the GPS locations
print(gpsSum)