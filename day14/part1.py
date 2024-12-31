import math

# Use modular arithmetic to get the location of the robots after n seconds
def moveRobotForNSeconds(robot, n, xMax, yMax):
    pos, vel = robot
    return ((pos[0] + vel[0] * n) % xMax, (pos[1] + vel[1] * n) % yMax)

# Read in the position and velocity of each robot
robots = []
# * For test1 and test2
# xMax=11
# yMax=7
# * For input
xMax = 101
yMax = 103
with open('input.txt') as f:
    for row in f.readlines():
        pos, vel = row.split()
        pos = pos[2:]
        vel = vel[2:]
        pos = tuple(int(num) for num in pos.split(','))
        vel = tuple(int(num) for num in vel.split(','))
        robot = (pos, vel)
        robots.append(robot)

movedRobotsPositions = []
for robot in robots:
    movedRobotsPositions.append(moveRobotForNSeconds(robot, 100, xMax, yMax))

# Split the grid into quadrants
# Count the number of robots in each quadrant
quadrantCounts = [0, 0, 0, 0]
for robot in movedRobotsPositions:
    if robot[0] < xMax//2 and robot[1] < yMax//2:
        quadrantCounts[0] += 1
    elif robot[0] > xMax//2 and robot[1] < yMax//2:
        quadrantCounts[1] += 1
    elif robot[0] < xMax//2 and robot[1] > yMax//2:
        quadrantCounts[2] += 1
    elif robot[0] > xMax//2 and robot[1] > yMax//2:
        quadrantCounts[3] += 1

# Return the product of the quadrantCounts
print(math.prod(quadrantCounts))
