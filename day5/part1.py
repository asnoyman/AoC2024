from collections import defaultdict

# Load rules as a dict of lists: key first then anything in the list after
rules = defaultdict(list)
updates = []
with open('input.txt') as f:
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

# For each line of updates, check if the order follows the rules above:
score = 0
for update in updates:
    length = len(update)
    
    ordered = True
    for i in range(length - 1):
        if update[i] in rules[update[i+1]]:
            ordered = False

    if ordered:
        score += int(update[length//2])

print(score)