def is_safe(level, fails_left):
    if len(level) <= 1:
        return True
    
    # For first val in level, mark pos = True if diff is pos else false
    pos = level[1] - level[0] > 0

    # For each item in level (except the last), check if diff is between 1 and 3 and pos is consistent
    # If there is a fail, run recursively on all lists with one item removed and return if any are true
    for i in range(len(level) - 1):
        diff = level[i + 1] - level[i]

        if bool(diff > 0) != bool(pos):
            if fails_left > 0:
                sub_lists = [is_safe(level[:i] + level[i+1:], fails_left - 1) for i in range(len(level))]
                return any(sub_lists)
            return False
        
        if abs(diff) < 1 or abs(diff) > 3:
            if fails_left > 0:
                sub_lists = [is_safe(level[:i] + level[i+1:], fails_left - 1) for i in range(len(level))]
                return any(sub_lists)
            return False

    return True


# Read data by line
tally = 0
with open('input.txt') as f:
    for line in f.readlines():
        level = [int(i) for i in line.split()]

        # Increment tally if line is safe
        if is_safe(level, 1): 
            tally += 1
 
print(tally)


level.pop()