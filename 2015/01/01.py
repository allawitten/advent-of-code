# --- Day 1: Not Quite Lisp ---
with open('01.input', 'r') as directions:
    instructions = directions.read()

# Part 1: find the floor
print(instructions.count('(') - instructions.count(')'))

# Part 2: find the first basement encounter
floor = 0
for position, instruction in enumerate(instructions):
    if instruction == '(':
        floor += 1
    if instruction == ')':
        floor -= 1
    position += 1
    if floor == -1:
        print(position)
        break
