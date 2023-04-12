#--- Day 6: Probably a Fire Hazard ---
with open('06.input', 'r') as mail:
    instructions = [line.split() for line in mail.readlines()]
SIZE = 1000

# Part 1: on/off lights
rows = [int('0' * SIZE, 2)] * SIZE # An array of bits to represent the state of each row of lights
for instruction in instructions:
    from_x, from_y = map(int, instruction[-3].split(','))
    to_x, to_y = map(int, instruction[-1].split(','))
    command = instruction[-4]

    mask = int('1' * (to_x - from_x + 1) + '0' * (SIZE - 1 - to_x), 2) # A mask to apply boolean logic on a full row at once

    if command == 'toggle':
        for y in range(from_y, to_y + 1):
            rows[y] ^= mask
    if command == 'on':
        for y in range(from_y, to_y + 1):
            rows[y] |= mask
    if command == 'off':
        for y in range(from_y, to_y + 1):
            rows[y] &= ~mask

print(sum([bin(row).count('1') for row in rows]))

# Part 2: individual brightness lights
brightnesses = [[0] * SIZE for _ in range(SIZE)]  # A two-dimensional array to represent each light brightness
for instruction in instructions:
    to_x, to_y = map(int, instruction[-1].split(','))
    from_x, from_y = map(int, instruction[-3].split(','))
    command = instruction[-4]
    
    if command == 'toggle':
        for x in range(from_x, to_x + 1):
            for y in range(from_y, to_y + 1):
                brightnesses[x][y] += 2
    if command == 'on':
        for x in range(from_x, to_x + 1):
            for y in range(from_y, to_y + 1):
                brightnesses[x][y] += 1
    if command == 'off':
        for x in range(from_x, to_x + 1):
            for y in range(from_y, to_y + 1):
                if brightnesses[x][y] > 0:
                    brightnesses[x][y] -= 1
    
print(sum([sum(row) for row in brightnesses]))
