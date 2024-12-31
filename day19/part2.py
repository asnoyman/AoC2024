towelTypes = set()
possibleDisplays = 0
with open('input.txt') as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            for towelType in list(line.strip().split(', ')):
                towelTypes.add(towelType)
        elif i > 1:
            line = line.strip()
            print(i)
            dp = [0] * (len(line) + 1)
            for i in range(1, len(line) + 1):
                for j in range(i):
                    for towelType in towelTypes:
                        if j + len(towelType) == i and towelType == line[j:i]:
                            # If this is a base towelType, add 1 to dp[i]
                            if j == 0:
                                dp[i] += 1
                            # Otherwise add all of the ways to get to j to the ways to get to dp[i]
                            else:
                                dp[i] += dp[j]

            possibleDisplays += dp[-1]

print(possibleDisplays)