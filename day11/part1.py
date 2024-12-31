# Read stones into list
stones = []
with open('input.txt') as f:
    stones = f.read().split()

# Loop through list creating a new list of stones according to the rules 25 times
for _ in range(25):
    temp_stones = []
    for stone in stones:
        if stone == '0':
            temp_stones.append('1')
        elif len(stone) % 2 == 0:
            newLeftStone = stone[:len(stone) // 2].lstrip('0')
            newRightStone = stone[len(stone) // 2:].lstrip('0')

            if newLeftStone == '':
                newLeftStone = '0'
            if newRightStone == '':
                newRightStone = '0'

            temp_stones += [newLeftStone, newRightStone]
        else:
            temp_stones.append(str(int(stone) * 2024))
    stones = temp_stones

# Print length of list
print(len(stones))