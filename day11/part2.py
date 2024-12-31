from collections import defaultdict

# Read stones into dict
stones = defaultdict(int)
with open('input.txt') as f:
    for stone in f.read().split():
        stones[stone] += 1

# Loop through list creating a new list of stones according to the rules 75 times
for _ in range(75):
    temp_stones = defaultdict(int)
    for stone, amount in stones.items():
        if stone == '0':
            temp_stones['1'] += amount
        elif len(stone) % 2 == 0:
            newLeftStone = stone[:len(stone) // 2].lstrip('0')
            newRightStone = stone[len(stone) // 2:].lstrip('0')

            if newLeftStone == '':
                newLeftStone = '0'
            if newRightStone == '':
                newRightStone = '0'

            temp_stones[newLeftStone] += amount
            temp_stones[newRightStone] += amount
        else:
            temp_stones[str(int(stone) * 2024)] += amount
    stones = temp_stones

# Print number of stones in the dict
print(sum(stones.values()))