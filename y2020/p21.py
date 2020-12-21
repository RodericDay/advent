import re
import sys


def words(string):
    return frozenset(re.findall(r'\w+', string))


text = sys.stdin.read()
recipes = dict(map(words, ln.split('contains')) for ln in text.splitlines())
all_ingredients = {item for group in recipes.keys() for item in group}
all_allergens = {item for group in recipes.values() for item in group}

# any ingredient can be any allergen,
# but if the allergen *is* there, and the ingredient *isn't*
# then the ingredient *cannot* be the allergen
options = {ingredient: set(all_allergens) for ingredient in all_ingredients}
for ingredients, allergens in recipes.items():
    for f2 in all_ingredients - ingredients:
        options[f2] -= allergens

clean = {ing for ing, als in options.items() if not als}
ans = sum(len(recipe & clean) for recipe in recipes)
print(ans)


def recurse(leftover, known=[]):
    if not leftover:
        yield dict(known)
    else:
        ing, = key = min(leftover, key=len)
        for alg in leftover.pop(key):
            a1 = {k - {ing}: v - {alg} for k, v in leftover.items()}
            a2 = known + [(ing, alg)]
            yield from recurse(a1, a2)


def valid(mapping):
    return all(mapping[a] in fs for fs, als in recipes.items() for a in als)


cleaned_up = {v: k - clean for k, v in recipes.items()}
maps, = (maps for maps in recurse(cleaned_up) if valid(maps))
print(','.join(v for k, v in sorted(maps.items())))
