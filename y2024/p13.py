import re
from functools import partial


def solve(group, mod=0):
    a1, a2, b1, b2, c1, c2 = map(int, re.findall(r'\d+', group))

    c1 += mod
    c2 += mod

    a, b = solve_system(a1, b1, c1, a2, b2, c2)
    if round(a, 2) == a and round(b, 2) == b:
        return int(a), int(b)
    else:
        return 0, 0

# Cramer's Rule
def solve_system(a1, b1, c1, a2, b2, c2):

    # Calculate the determinant D
    D = a1 * b2 - a2 * b1

    # Check if the system has a unique solution (D != 0)
    if D == 0:
        return "The system has no unique solution (D = 0)"

    # Calculate D_x and D_y
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    # Calculate the solutions for x and y
    x = Dx / D
    y = Dy / D

    return x, y


inp = open(0).read()
print(sum(3 * a + 1 * b for a, b in map(solve, inp.split('\n\n'))))
print(sum(3 * a + 1 * b for a, b in map(partial(solve, mod=10**13), inp.split('\n\n'))))
