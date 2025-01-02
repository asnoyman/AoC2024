from collections import defaultdict
import itertools

def pruneNumber(secret):
    return secret % 16777216

def mixNumber(secret, mixNumber):
    return secret ^ mixNumber

# Write function to evolve a serect into its next form
def transformSecret(secret):
    secret = pruneNumber(mixNumber(secret, secret * 64))
    secret = pruneNumber(mixNumber(secret, secret // 32))
    secret = pruneNumber(mixNumber(secret, secret * 2048))
    return secret

# Read in starting secrets
secrets = []
with open('input.txt') as f:
    secrets = [int(secret) for secret in f.read().split()]

# Run transformSecret 2000 times per secret. For each, record the price and price change
priceMovments = []
for secret in secrets:
    monkeyPrices = [(secret % 10, 'NA')]
    for _ in range(2001):
        secret = transformSecret(secret)
        monkeyPrices.append((secret % 10, (secret % 10) - monkeyPrices[-1][0]))
    priceMovments.append(monkeyPrices)

# For each monkeyPrice, add to that sequence's total value to the 
monkeySequences = defaultdict(int)
for monkeyPrice in priceMovments:
    sequencesFound = set()
    for i in range(4, 2001):
        seq = (monkeyPrice[i-3][1], monkeyPrice[i-2][1], monkeyPrice[i-1][1], monkeyPrice[i][1])
        if seq not in sequencesFound:
            sequencesFound.add(seq)
            monkeySequences[seq] += monkeyPrice[i][0]

print(max(monkeySequences.values()))