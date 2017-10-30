import itertools, collections

with open('24.txt') as fp:
    txt = fp.read().strip()

available = set()
wanted = set()
for j, row in enumerate(txt.splitlines()):
    for i, cell in enumerate(row):
        p = i+1j*j
        if cell.isdigit():
            wanted |= {p}
        if cell == '0':
            start = p
        if cell != '#':
            available |= {p}


def shortest_path(A, B):
    reached = set()
    inner = set()
    while B not in reached:
        for p in reached:
            for n in [p+1,p-1,p+1j,p-1j]:




costs = collections.defaultdict(dict)
for A, B in itertools.combinations(wanted, 2):
    c = shortest_path(A, B)
    costs[A][B] = c
    costs[B][A] = c
