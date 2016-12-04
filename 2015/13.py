import re, collections, itertools

change = collections.defaultdict(dict)
regexp = r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)'
with open('13.txt') as fp:
    txt = fp.read()
    for A, s, x, B in re.findall(regexp, txt):
        change[A][B] = -int(x) if s=='lose' else int(x)

# for name in list(change):
#     change[name]['me'] = 0
#     change['me'][name] = 0

arrangement = {}
for perm in itertools.permutations(change):
    arrangement[perm] = \
        sum(change[a][b]+change[b][a] for a,b in zip(perm, perm[1:]+perm[:1]))

print(max(arrangement.values()))
