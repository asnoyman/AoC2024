from itertools import pairwise, permutations
from functools import cache
from math import inf

NUMBER_COORDS = '789456123 0A'

DIR_COORDS = ' ^A<v>'

def buttonToPos(keypad, button):
    i = keypad.index(button)
    return (i // 3, i % 3)

def testPath(keypad, path):
    pos = buttonToPos(keypad, path[0])
    posEmpty = buttonToPos(keypad, ' ')
    for move in path[1:]:
        if move == '^':
            pos = (pos[0] - 1, pos[1])
        if move == 'v':
            pos = (pos[0] + 1, pos[1])
        if move == '>':
            pos = (pos[0], pos[1] + 1)
        if move == '<':
            pos = (pos[0], pos[1] - 1)
    
        if pos == posEmpty:
            return False
    return True


def paths_between(keypad, start, end):
    deltaX = buttonToPos(keypad, end)[0] - buttonToPos(keypad, start)[0]
    deltaY = buttonToPos(keypad, end)[1] - buttonToPos(keypad, start)[1]

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


@cache
def cost_between(keypad, start, end, links):
    minPath = inf
    for path in paths_between(keypad, start, end):
        if links != 0:
            minPath = min(minPath, cost(DIR_COORDS, path, links - 1))
        else:
            minPath = 1
    return minPath

@cache
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
    sum += complexity(code, 25)
print(sum)