#--- Day 5: Doesn't He Have Intern-Elves For This? ---
with open('05.input', 'r') as text:
    strings = text.readlines()

# Part 1: find the quantity of nice strings
def is_nice(string: str) -> bool:
    '''Check if the string has 3+ vowels, a double and no forbidden sequence'''
    previous = ''
    vowel_count = 0
    double = False
    for char in string:
        if char in 'aeiou':
            vowel_count += 1
        if previous == char:
            double = True
        if previous + char in ['ab', 'cd', 'pq', 'xy']:
            return False
        previous = char
    return vowel_count >= 3 and double

print(sum([is_nice(string) for string in strings]))

# Part 2: find the quantity of nicer strings
def is_nicer(string: str) -> bool:
    '''Check if the string has a sandwiched letter and two twin pairs'''
    sandwich = False
    twins = False
    for index in range(1, len(string) - 1):
        if string[index - 1] == string[index + 1]:
            sandwich = True
        if string[index - 1] + string[index] in string[index + 1:]:
            twins = True
    return sandwich and twins

print(sum([is_nicer(string) for string in strings]))