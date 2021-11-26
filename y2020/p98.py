import collections
import itertools
import re
import sys


txt = '''90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct
''' # 39542 is unique
txt = sys.stdin.read()


exclusions = collections.defaultdict(set)
clues = []
for string, n in re.findall(r'(\d+) ;(\d)', txt):
    choices = set(enumerate(string))
    combos = [frozenset(cs) for cs in itertools.combinations(choices, int(n))]
    for combo in combos:
        exclusions[combo] |= (choices - combo)
    if int(n):
        clues.append(combos)


for pos in range(len(string)):
    choices = {(pos, char) for char in '0123456789'}
    for choice in choices:
        exclusions[frozenset({choice})] |= (choices - {choice})


def solve(clues_left, known=frozenset()):
    if not clues_left:
        avail = {a for gr in exclusions for a in gr}
        avail -= {v for k, vs in exclusions.items() if k <= known for v in vs}
        yield ''.join(c for _, c in sorted(avail))

    else:
        choices = min(clues_left, key=len)
        for choice in choices:
            chosen = known | choice
            bads = {v for k, vs in exclusions.items() if k <= chosen for v in vs}
            mods = [[c for c in cl if not c & bads] for cl in clues_left if cl != choices]
            yield from solve(mods, chosen)


solution = next(solve(clues))
print(solution)
