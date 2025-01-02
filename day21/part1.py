from itertools import pairwise, permutations
from math import inf

NUMBER_COORDS = {'0': (3,1), '1': (2,0), '2': (2,1), '3': (2,2), '4': (1,0), '5': (1,1), 
                '6': (1,2), '7': (0,0), '8': (0,1), '9': (0,2), 'A': (3,2), '': (3,0)}

DIR_COORDS = {'': (0,0), '<': (1,0), '>': (1,2), '^': (0,1), 'v': (1,1), 'A': (0,2)}

def testPath(keypad, path):
    pos = keypad[path[0]]
    for move in path[1:]:
        if move == '^':
            pos = (pos[0] - 1, pos[1])
        if move == 'v':
            pos = (pos[0] + 1, pos[1])
        if move == '>':
            pos = (pos[0], pos[1] + 1)
        if move == '<':
            pos = (pos[0], pos[1] - 1)
    
        if pos == keypad['']:
            return False
    return True


def paths_between(keypad, start, end):
    deltaX = keypad[end][0] - keypad[start][0]
    deltaY = keypad[end][1] - keypad[start][1]

    path = ''
    if deltaX < 0:
        path += '^' * abs(deltaX)
    else:
        path += 'v' * abs(deltaX)

    if deltaY < 0:
        path += '<' * abs(deltaY)
    else:
        path += '>' * abs(deltaY)

    return [''.join(p) + 'A' for p in set(permutations(path)) if testPath(keypad, start + ''.join(p) + 'A')]


def cost_between(keypad, start, end, links):
    minPath = inf
    for path in paths_between(keypad, start, end):
        if links != 0:
            minPath = min(minPath, cost(DIR_COORDS, path, links - 1))
        else:
            minPath = 1
    return minPath

def cost(keypad, buttons, links):
    sum = 0
    for startButton, endButton in pairwise('A' + buttons):
        sum += cost_between(keypad, startButton, endButton, links)
    return sum

def complexity(code, robots):
    return cost(NUMBER_COORDS, code, robots + 1) * int(code[:-1])

# Read input for expected codes
codes = []
with open('input.txt') as f:
    for line in f.readlines():
        codes.append(line.strip())

sum = 0
for code in codes:
    print(complexity(code, 2))
    sum += complexity(code, 2)
print(sum)