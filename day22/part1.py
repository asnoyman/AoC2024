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

# Run transformSecret 2000 times for each secret
sum = 0
for secret in secrets:
    for _ in range(2000):
        secret = transformSecret(secret)
    sum += secret

# Sum the results
print(sum)