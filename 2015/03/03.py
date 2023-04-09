#--- Day 3: Perfectly Spherical Houses in a Vacuum ---
with open('03.input', 'r') as elf_call:
    instructions = elf_call.read().strip()

def next_position(position: tuple, instruction: str) -> tuple:
    '''Return the position after following a given instruction'''
    x, y = position
    if instruction == '>':
        x += 1
    if instruction == '<':
        x -= 1
    if instruction == '^':
        y += 1
    if instruction == 'v':
        y -= 1
    return (x, y)

# Part 1: find houses visited by Santa
position = (0, 0)
houses = {position}
for instruction in instructions:
    position = next_position(position, instruction)
    houses.add(position)

print(len(houses))

# Part 2: find houses visited by Santa or Robo-Santa
santa_position, robo_position = (0, 0), (0, 0)
houses = {santa_position}
for turn, instruction in enumerate(instructions):
    if turn % 2 == 0:
        santa_position = next_position(santa_position, instruction)
        houses.add(santa_position)
    else:
        robo_position = next_position(robo_position, instruction)
        houses.add(robo_position)
    
print(len(houses))