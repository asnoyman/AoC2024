import math

def sumTuples(a, b):
    return (a[0] + b[0], a[1] + b[1])

# Create dynamic programming table for each claw game
# Tuple consisting of deltaA, deltaB and target
claws = []
with open('input.txt') as f:
    claw = []
    for line in f.readlines():
        line = line.strip()
        if line == '':
            claws.append(claw)
            claw = []
        elif line[0] == 'B':
            parts = line.split()
            claw.append((int(parts[2].strip(',')[1:]), int(parts[3][1:])))
        else:
            parts = line.split()
            claw.append((int(parts[1].strip(',')[2:]), int(parts[2][2:])))
        
    claws.append(claw)

# Fill the grid with each option 
# Record the option that hits the target with the lowest cost
totalCost = 0
for claw in claws:
    dp = [[-1] * 101] * 101
    minCost = math.inf
    for row in range(101):
        for col in range(101):
            if row == 0 and col == 0:
                dp[row][col] = (0, 0)
            elif row == 0:
                dp[row][col] = sumTuples(claw[0], dp[row][col - 1])
            else:
                dp[row][col] = sumTuples(claw[1], dp[row - 1][col])
            
            if dp[row][col] == claw[2]:
                minCost = min(minCost, row + col * 3)

    if minCost != math.inf:
        totalCost += minCost

# Print the sum of each cost
print(totalCost)