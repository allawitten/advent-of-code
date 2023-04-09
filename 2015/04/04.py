#--- Day 4: The Ideal Stocking Stuffer ---
from hashlib import md5

with open('04.input', 'r') as secret_key_file:
    secret_key = secret_key_file.read().strip().encode()

def mine(key: bytes, difficulty: int) -> int:
    '''Find a number that produces a hash with leading zeroes (as many as the difficulty) when concatenated to the key'''
    nonce = 0
    while True:
        hash = md5(key + str(nonce).encode()).hexdigest()
        if hash.startswith('0' * difficulty):
            return(nonce)
        nonce += 1

# Part 1: mine AdventCoins, 5 leading zeroes
print(mine(secret_key, 5))

# Part 2: mine AdventCoins, 6 leading zeroes
print(mine(secret_key, 6))
