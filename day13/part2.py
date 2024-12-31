import numpy as np

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
            claw.append((int(parts[1].strip(',')[2:]) + 10000000000000, int(parts[2][2:]) + 10000000000000))
        
    claws.append(claw)

# For each claw machine, solve the linear equations that determine the single number of button presses
# of each button to get to the target and add the cost of those presses to the total
total = 0
for claw in claws:
    A = np.array([
                    [claw[0][0], claw[1][0]], 
                    [claw[0][1], claw[1][1]]
                ])
    B = np.array([claw[2][0], claw[2][1]])

    solution = np.round(np.linalg.solve(A, B), 3)

    # Only add to total if there is an integer solution to the linear equations
    if all(val == np.floor(val) for val in solution):
        total += solution[0] * 3 + solution[1]

# Print the total cost of all machines
print(total)