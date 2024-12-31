from collections import defaultdict

# Load rules as a dict of lists: key first then anything in the list after
rules = defaultdict(list)
updates = []
with open('test1.txt') as f:
    reading_rules = True
    for line in f.readlines():
        if line == '\n':
            reading_rules = False
            continue
        if reading_rules:
            key, value = line.strip().split('|')
            rules[key].append(value)
        else:
            updates.append(line.strip().split(','))

# For each line of updates, check if there is an order that follows the rules above:
score = 0
for update in updates:
    length = len(update)
    
    ordered = True
    for i in range(length - 1):
        if update[i] in rules[update[i+1]]:
            ordered = False

    if not ordered:
        iterations = length
        # Run this n times where n is the number of pages in the update 
        for _ in range(iterations):
            for i in range(length - 1):
                if update[i] in rules[update[i+1]]:
                    # If the left one has to be after the right one, swap them
                    update[i], update[i+1] = update[i+1], update[i]
        score += int(update[length//2])

print(score)