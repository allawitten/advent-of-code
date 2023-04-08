#--- Day 2: I Was Told There Would Be No Math ---
with open('02.input', 'r') as presents:
    dimensions_list=[tuple(map(int, line.strip().split('x'))) for line in presents.readlines()]

# Part 1: find the total paper needed
def required_paper(l: int, w: int, h: int) -> int:
    sides_areas = [l*w, w*h, h*l]
    return 2*sum(sides_areas) + min(sides_areas)

print(sum([required_paper(*dimensions) for dimensions in dimensions_list]))

# Part 2: find the total ribbon needed
def required_ribbon(l: int, w: int, h: int) -> int:
    perimeters = [2*(l+w), 2*(w+h), 2*(h+l)]
    return min(perimeters) + w*h*l

print(sum([required_ribbon(*dimensions) for dimensions in dimensions_list]))
