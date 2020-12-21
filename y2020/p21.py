import sys


text = sys.stdin.read()
test = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''


contains = {}
for line in text.splitlines():
    food, allergens = line[:-1].split(' (contains ')
    food = frozenset(s.strip() for s in food.split(' '))
    allergens = frozenset(s.strip() for s in allergens.split(','))
    contains[food] = allergens

all_allergens = {a for b in contains.values() for a in b}
all_foods = {a for b in contains.keys() for a in b}

reverse = {}
for food in all_foods:
    reverse[food] = set(all_allergens)

for food, allergens in contains.items():
    for f2 in reverse:
        if f2 not in food:
            reverse[f2] -= allergens

clean = {k for k, v in reverse.items() if not v}
ans = 0
for v in contains.keys():
    ans += len(v & clean)
print(ans)


final = {v: k - clean for k, v in contains.items()}


def recurse(ings, known=tuple()):
    if not ings:
        yield known
    else:
        key, = min(ings, key=lambda k: len(k))
        for val in sorted(ings.pop(frozenset({key}))):
            expa = known + ((key, val),)
            lob = {k - {key}: v - {val} for k, v in ings.items()}
            yield from recurse(lob, expa)


for out in recurse(dict(final)):
    d = dict(out)
    if all(({d[e] for e in k} <= set(v)) for k, v in final.items()):
        print(','.join(v for _, v in sorted(out)))
