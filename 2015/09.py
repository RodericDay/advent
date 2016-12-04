import re, collections, itertools

places = set()
leg = collections.defaultdict(dict)
with open('09.txt') as fp:
    for A, B, d in re.findall(r'(\w+) to (\w+) = (\d+)', fp.read()):
        places |= {A, B}
        leg[A][B] = int(d)
        leg[B][A] = int(d)

path = {}
for perm in itertools.permutations(places):
    path[perm] = sum(leg[a][b] for a,b in zip(perm, perm[1:]))

ans1 = min(path.values())
print(ans1)

ans2 = max(path.values())
print(ans2)

