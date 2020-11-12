# Question:
"""
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
"""
# Hint:
"""
Use for loop to iterate all possible solutions.
"""


def solve(numheads, numlegs):
    ns = 'No solutions!'
    for i in range(numberheads+1):
        j = numberheads-i
        if 2*i+4*j == numberlegs:
            return i, j
    return ns, ns


numberheads = 35
numberlegs = 94
solutions = solve(numberheads, numberlegs)
print(solutions)
