def is_safe(level):
    if len(level) <= 1:
        return True
    
    # For first val in level, mark pos = True if diff is pos else false
    pos = level[1] - level[0] > 0

    # For each item in level (except the last), check if diff is between 1 and 3 and pos is consistent
    for i in range(len(level) - 1):
        diff = level[i + 1] - level[i]

        if bool(diff > 0) != bool(pos):
            return False
        
        if abs(diff) < 1 or abs(diff) > 3:
            return False

    return True


# Read data by line
tally = 0
with open('input.txt') as f:
    for line in f.readlines():
        level = [int(i) for i in line.split()]

        # Increment tally if line is safe
        if is_safe(level): 
            tally += 1
 
print(tally)