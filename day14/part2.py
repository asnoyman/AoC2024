import math
from copy import deepcopy

# Use modular arithmetic to get the location of the robots after n seconds
def moveRobotForNSeconds(robot, n, xMax, yMax):
    pos, vel = robot
    return ((pos[0] + vel[0] * n) % xMax, (pos[1] + vel[1] * n) % yMax)

# Read in the position and velocity of each robot
robots = []
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

images = []
for n in range(10000):
    grid = [[' '] * 101 for _ in range(103)]
    for robot in robots: 
        col, row = moveRobotForNSeconds(robot, n, xMax, yMax)
        grid[row][col] = '#'


    # Find a grid that has both a vertical and horizontal stretch of 5 drones in a row
    potentialMatch = False
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] == '#':
                if (i >= 4 and all(grid[r][j] == '#' for r in range(i-4, i+1))) and (j >= 4 and all(grid[i][c] == '#' for c in range(j-4, j+1))):
                    potentialMatch = True
                
    if potentialMatch:
        images.append([''.join(str(num) for num in row) for row in grid])
        print(n)

# ChatGPT code to display each image in terminal for one second each
import time
import os

def print_image(image):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
    print(*image, sep='\n')

# Loop through the images, printing one every second
for image in images:
    print_image(image)
    time.sleep(1)