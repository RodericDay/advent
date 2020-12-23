import re
import sys


def solve_sudoku(string):
    known = [(i, v) for i, v in enumerate(string) if v != '0']
    solved, = map(dict, solve(X, Y, known))
    return ''.join(solved[i] for i in range(81))


def solve(X, Y, solution):
    for choice in solution:
        X = select(X, Y, choice)

    for solution in complete(X, Y, solution):
        yield solution


def select(X, Y, choice):
    fulfilled = Y[choice]
    excluded = {y for x in fulfilled for y in X[x]}
    return {x: ys - excluded for x, ys in X.items() if x not in fulfilled}


def complete(X, Y, solution):
    if not X:
        yield solution
    else:
        for choice in min(X.values(), key=len):
            yield from complete(select(X, Y, choice), Y, solution + [choice])


Y, X = {}, {}
for i in range(81):
    r = i // 9
    c = i % 9
    b = r // 3 * 3 + c // 3
    for v in '123456789':
        choice = (i, v)
        Y[choice] = {('p', i), ('r', r, v), ('c', c, v), ('b', b, v)}
        for x in Y[choice]:
            X.setdefault(x, set()).add(choice)


text = sys.stdin.read()
strings = re.split(r'Grid \d\d', text.replace('\n', ''))[1:]
print(sum(int(solve_sudoku(string)[:3]) for string in strings))
